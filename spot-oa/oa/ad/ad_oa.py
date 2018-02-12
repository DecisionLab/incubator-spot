#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
import os
import json
import shutil
import sys
import datetime
import csv, math
from collections import OrderedDict
from utils import Util
from components.data.data import Data
from components.iana.iana_transform import IanaTransform
from components.nc.network_context import NetworkContext

import api.resources.hdfs_client as HDFSClient
import api.resources.impala_engine as impala
from multiprocessing import Process
import pandas as pd
from impala.util import as_pandas

import time
import md5


class OA(object):

    def __init__(self, date, limit=500, logger=None):

        self._initialize_members(date, limit, logger)

    def _initialize_members(self, date, limit, logger):

        # get logger if exists. if not, create new instance.
        self._logger = logging.getLogger('OA.AD') if logger else Util.get_logger('OA.AD', create_file=False)

        # initialize required parameters.
        self._scrtip_path = os.path.dirname(os.path.abspath(__file__))
        self._date = date
        self._table_name = "ad"
        self._ad_results = []
        self._limit = limit
        self._data_path = None
        self._ipynb_path = None
        self._ingest_summary_path = None
        self._ad_scores = []
        self._ad_scores_headers = []
        self._ad_extra_columns = []
        self._results_delimiter = '\t'

        # get app configuration.
        self._spot_conf = Util.get_spot_conf()

        # get scores fields conf
        conf_file = "{0}/ad_conf.json".format(self._scrtip_path)
        self._conf = json.loads(open(conf_file).read(), object_pairs_hook=OrderedDict)

        # initialize data engine
        self._db = self._spot_conf.get('conf', 'DBNAME').replace("'", "").replace('"', '')

    def start(self):

        ####################
        start = time.time()
        ####################

        self._create_folder_structure()
        self._clear_previous_executions()
        self._add_ipynb()
        self._get_ad_results()
        self._create_ad_scores_csv()
        # self._get_oa_details()
        # self._ingest_summary()

        ##################
        end = time.time()
        print(end - start)
        ##################

    def _create_folder_structure(self):

        # create date folder structure if it does not exist.
        self._logger.info("Creating folder structure for OA (data and ipynb)")
        self._data_path, self._ingest_summary_path, self._ipynb_path = Util.create_oa_folders("ad", self._date)

    def _clear_previous_executions(self):

        self._logger.info("Cleaning data from previous executions for the day")
        yr = self._date[:4]
        mn = self._date[4:6]
        dy = self._date[6:]
        table_schema = []
        HUSER = self._spot_conf.get('conf', 'HUSER').replace("'", "").replace('"', '')
        table_schema = ['suspicious', 'edge', 'threat_investigation', 'timeline', 'storyboard', 'summary']

        for path in table_schema:
            HDFSClient.delete_folder(
                "{0}/{1}/hive/oa/{2}/y={3}/m={4}/d={5}".format(HUSER, self._table_name, path, yr, int(mn), int(dy)),
                user="impala")
        impala.execute_query("invalidate metadata")

        # removes Feedback file
        HDFSClient.delete_folder(
            "{0}/{1}/scored_results/{2}{3}{4}/feedback/ml_feedback.csv".format(HUSER, self._table_name, yr, mn, dy))
        # removes json files from the storyboard
        HDFSClient.delete_folder("{0}/{1}/oa/{2}/{3}/{4}/{5}".format(HUSER, self._table_name, "storyboard", yr, mn, dy))

    def _add_ipynb(self):

        if os.path.isdir(self._ipynb_path):

            self._logger.info("Adding advanced mode IPython Notebook")
            shutil.copy("{0}/ipynb_templates/Advanced_Mode_master.ipynb".format(self._scrtip_path),
                        "{0}/Advanced_Mode.ipynb".format(self._ipynb_path))

            self._logger.info("Adding threat investigation IPython Notebook")
            shutil.copy("{0}/ipynb_templates/Threat_Investigation_master.ipynb".format(self._scrtip_path),
                        "{0}/Threat_Investigation.ipynb".format(self._ipynb_path))

        else:
            self._logger.error("There was a problem adding the IPython Notebooks, please check the directory exists.")

    def _get_ad_results(self):

        self._logger.info("Getting {0} Machine Learning Results from HDFS".format(self._date))
        ad_results = "{0}/ad_results.csv".format(self._data_path)

        # get hdfs path from conf file.
        HUSER = self._spot_conf.get('conf', 'HUSER').replace("'", "").replace('"', '')
        hdfs_path = "{0}/ad/scored_results/{1}/scores/ad_results.csv".format(HUSER, self._date)

        # get results file from hdfs.
        get_command = Util.get_ml_results_form_hdfs(hdfs_path, self._data_path)
        self._logger.info("{0}".format(get_command))

        # valdiate files exists
        if os.path.isfile(ad_results):

            # read number of results based in the limit specified.
            self._logger.info("Reading {0} ad results file: {1}".format(self._date, ad_results))
            self._ad_results = Util.read_results(ad_results, self._limit, self._results_delimiter)[:]
            if len(self._ad_results) == 0:
                self._logger.error("There are not ad results.")
                sys.exit(1)
        else:
            self._logger.error("There was an error getting ML results from HDFS")
            sys.exit(1)

        self._ad_scores = self._ad_results[:]

    def _create_ad_scores_csv(self):
        # get date parameters.
        yr = self._date[:4]
        mn = self._date[4:6]
        dy = self._date[6:]
        value_string = ""

        for row in self._ad_scores:
            for item in row:
                cells = map(lambda cell: Util.cast_val(cell), item.split(","))
                cells[2] = str(cells[2])    # manual cast from int to string
                cells[11] = str(cells[11])  # manual cast from int to string
                value_string += str(tuple(cells)) + ","

        load_into_impala = ("""
             INSERT INTO {0}.ad_scores partition(y={2}, m={3}, d={4}) VALUES {1}
        """).format(self._db, value_string[:-1], yr, mn, dy)
        impala.execute_query(load_into_impala)

    def _get_oa_details(self):

        self._logger.info("Getting OA Proxy suspicious details")
        # start suspicious connects details process.
        p_sp = Process(target=self._get_suspicious_details)
        p_sp.start()

    def _get_suspicious_details(self):
        uri_list = []
        iana_conf_file = "{0}/components/iana/iana_config.json".format(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        if os.path.isfile(iana_conf_file):
            iana_config = json.loads(open(iana_conf_file).read())
            ad_iana = IanaTransform(iana_config["IANA"])

        for conn in self._ad_scores:
            clientip = conn[self._conf["ad_score_fields"]["clientip"]]
            fulluri = conn[self._conf["ad_score_fields"]["fulluri"]]
            date = conn[self._conf["ad_score_fields"]["p_date"]].split('-')
            if len(date) == 3:
                year = date[0]
                month = date[1].zfill(2)
                day = date[2].zfill(2)
                hh = (conn[self._conf["ad_score_fields"]["p_time"]].split(":"))[0]
                self._get_ad_details(fulluri, clientip, year, month, day, hh, ad_iana)

    def _get_ad_details(self, fulluri, clientip, year, month, day, hh, ad_iana):
        limit = 250
        value_string = ""

        query_to_load = ("""
            SELECT p_date, p_time, clientip, host, webcat, respcode, reqmethod, useragent, resconttype,
            referer, uriport, serverip, scbytes, csbytes, fulluri, {5} as hh
            FROM {0}.{1} WHERE y='{2}' AND m='{3}' AND d='{4}' AND
            h='{5}' AND fulluri='{6}' AND clientip='{7}' LIMIT {8};
        """).format(self._db, self._table_name, year, month, day, hh, fulluri.replace("'", "\\'"), clientip, limit)

        detail_results = impala.execute_query(query_to_load)

        if ad_iana:
            # add IANA to results.
            self._logger.info("Adding IANA translation to details results")

            updated_rows = [conn + (ad_iana.get_name(conn[5], "ad_http_rcode"),) for conn in detail_results]
            updated_rows = filter(None, updated_rows)
        else:
            updated_rows = [conn + ("") for conn in detail_results]

        for row in updated_rows:
            value_string += str(tuple(item for item in row)) + ","

        if value_string != "":
            query_to_insert = ("""
                INSERT INTO {0}.ad_edge PARTITION (y={1}, m={2}, d={3}) VALUES ({4});
            """).format(self._db, year, month, day, value_string[:-1])

            impala.execute_query(query_to_insert)

    def _ingest_summary(self):
        # get date parameters.
        yr = self._date[:4]
        mn = self._date[4:6]
        dy = self._date[6:]

        self._logger.info("Getting ingest summary data for the day")

        ingest_summary_cols = ["date", "total"]
        result_rows = []
        df_filtered = pd.DataFrame()

        # get ingest summary.

        query_to_load = ("""
                SELECT p_date, p_time, COUNT(*) as total
                FROM {0}.{1} WHERE y='{2}' AND m='{3}' AND d='{4}'
                AND p_date IS NOT NULL AND p_time IS NOT NULL
                AND clientip IS NOT NULL AND p_time != ''
                AND host IS NOT NULL AND fulluri IS NOT NULL
                GROUP BY p_date, p_time;
        """).format(self._db, self._table_name, yr, mn, dy)

        results = impala.execute_query(query_to_load)

        if results:
            df_results = as_pandas(results)
            # Forms a new dataframe splitting the minutes from the time column/
            df_new = pd.DataFrame([["{0} {1}:{2}".format(val['p_date'], val['p_time'].split(":")[0].zfill(2),
                                                         val['p_time'].split(":")[1].zfill(2)),
                                    int(val['total']) if not math.isnan(val['total']) else 0] for key, val in
                                   df_results.iterrows()], columns=ingest_summary_cols)
            value_string = ''
            # Groups the data by minute
            sf = df_new.groupby(by=['date'])['total'].sum()
            df_per_min = pd.DataFrame({'date': sf.index, 'total': sf.values})

            df_final = df_filtered.append(df_per_min, ignore_index=True).to_records(False, False)
            if len(df_final) > 0:
                query_to_insert = ("""
                    INSERT INTO {0}.ad_ingest_summary PARTITION (y={1}, m={2}, d={3}) VALUES {4};
                """).format(self._db, yr, mn, dy, tuple(df_final))

                impala.execute_query(query_to_insert)

        else:
            self._logger.info("No data found for the ingest summary")
