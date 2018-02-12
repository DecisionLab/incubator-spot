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
from datetime import date
from graphql import (
    GraphQLObjectType,
    GraphQLArgument,
    GraphQLNonNull,
    GraphQLField,
    GraphQLString,
    GraphQLInt,
    GraphQLList
)

from api.graphql.common import SpotDateType, SpotDatetimeType, SpotIpType, IngestSummaryType
import api.resources.ad as AD

SuspiciousType = GraphQLObjectType(
    name='ADSuspiciousType',
    fields={
        'beginTime': GraphQLField(
            type=GraphQLInt,
            description='Start time of the request',
            resolver=lambda root, *_: root.get('begintime')
        ),
        'endTime': GraphQLField(
            type=GraphQLInt,
            description='End time of the request',
            resolver=lambda root, *_: root.get('endtime')
        ),
        'score': GraphQLField(
            type=GraphQLInt,
            description='Row Score - Higher is more suspicious',
            resolver=lambda root, *_: root.get('score') or 0
        ),
        'srcPort': GraphQLField(
            type=GraphQLInt,
            description='The Source Port',
            resolver=lambda root, *_: root.get('src_port')
        ),
        'dstPort': GraphQLField(
            type=GraphQLInt,
            description='The Destination Port',
            resolver=lambda root, *_: root.get('dst_port')
        ),
        'userId': GraphQLField(
            type=GraphQLString,
            description='The User ID',
            resolver=lambda root, *_: root.get('user_id')
        ),
        'code': GraphQLField(
            type=GraphQLString,
            description='The AD Code',
            resolver=lambda root, *_: root.get('code')
        ),
        'type': GraphQLField(
            type=GraphQLString,
            description='The human readable type',
            resolver=lambda root, *_: root.get('type')
        ),
        'srcIPV4': GraphQLField(
            type=GraphQLString,
            description='The Source IP',
            resolver=lambda root, *_: root.get('src_ipv4_str')
        ),
        'dstIPV4': GraphQLField(
            type=GraphQLString,
            description='The Destination IP',
            resolver=lambda root, *_: root.get('dst_ipv4_str')
        ),
        'applicationName': GraphQLField(
            type=GraphQLString,
            description='The Application Name',
            resolver=lambda root, *_: root.get('application_name')
        ),
        'dvcDomain': GraphQLField(
            type=GraphQLString,
            description='The DVC Domain',
            resolver=lambda root, *_: root.get('dvc_domain')
        ),
        'category': GraphQLField(
            type=GraphQLString,
            description='The Category',
            resolver=lambda root, *_: root.get('category')
        ),
        'app': GraphQLField(
            type=GraphQLString,
            description='The App',
            resolver=lambda root, *_: root.get('app')
        ),
        'dateDay': GraphQLField(
            type=GraphQLString,
            description='The Begin Day',
            resolver=lambda root, *_: root.get('date_day')
        ),
        'action': GraphQLField(
            type=GraphQLString,
            description='The Action',
            resolver=lambda root, *_: root.get('action')
        )
    }
)

EdgeDetailsType = GraphQLObjectType(
    name='ADEdgeDetailsType',
    fields={
        'datetime': GraphQLField(
            type=GraphQLString,
            description='Start time of the request',
            resolver=lambda root, *_: '{} {}'.format(root.get('tdate') or '1970-01-01', root.get('time') or '00:00:00')
        ),
        'clientIp': GraphQLField(
            type=SpotIpType,
            description='Client\'s IP address',
            resolver=lambda root, *_: root.get('clientip')
        ),
        'host': GraphQLField(
            type=GraphQLString,
            description='Host name from the client request URL',
            resolver=lambda root, *_: root.get('host')
        ),
        'webCategory': GraphQLField(
            type=GraphQLString,
            description='Web content categories',
            resolver=lambda root, *_: root.get('webcat')
        ),
        'responseCode': GraphQLField(
            type=GraphQLInt,
            description='HTTP response code',
            resolver=lambda root, *_: root.get('respcode') or 0
        ),
        'responseCodeLabel': GraphQLField(
            type=GraphQLString,
            description='HTTP response code name',
            resolver=lambda root, *_: root.get('respcode_name')
        ),
        'requestMethod': GraphQLField(
            type=GraphQLString,
            description='HTTP request method',
            resolver=lambda root, *_: root.get('reqmethod')
        ),
        'userAgent': GraphQLField(
            type=GraphQLString,
            description='Client\'s user agent',
            resolver=lambda root, *_: root.get('useragent')
        ),
        'responseContentType': GraphQLField(
            type=GraphQLString,
            description='HTTP response content type (MIME)',
            resolver=lambda root, *_: root.get('resconttype')
        ),
        'referer': GraphQLField(
            type=GraphQLString,
            description='The address of the webpage that linked to the resource being requested',
            resolver=lambda root, *_: root.get('referer')
        ),
        'uriPort': GraphQLField(
            type=GraphQLInt,
            description='URI port',
            resolver=lambda root, *_: root.get('uriport')
        ),
        'serverIp': GraphQLField(
            type=SpotIpType,
            description='Server/Proxy IP',
            resolver=lambda root, *_: root.get('serverip')
        ),
        'serverToClientBytes': GraphQLField(
            type=GraphQLInt,
            description='Number of bytes sent from appliance to client',
            resolver=lambda root, *_: root.get('scbytes')
        ),
        'clientToServerBytes': GraphQLField(
            type=GraphQLInt,
            description='Number of bytes sent from client to appliance',
            resolver=lambda root, *_: root.get('csbytes')
        ),
        'uri': GraphQLField(
            type=GraphQLString,
            description='The original URI requested',
            resolver=lambda root, *_: root.get('fulluri')
        )
    }
)

ScoredRequestType = GraphQLObjectType(
    name='ADScoredRequestType',
    fields={
        'datetime': GraphQLField(
            type=SpotDateType,
            description='Date and time of user score',
            resolver=lambda root, *_: root.get('tdate') or '1970-01-01'
        ),
        'uri': GraphQLField(
            type=SpotIpType,
            description='Requested URI',
            resolver=lambda root, *_: root.get('fulluri')
        ),
        'score': GraphQLField(
            type=GraphQLInt,
            description='URI risk score value. 1->High, 2->Medium, 3->Low',
            resolver=lambda root, *_: root.get('uri_sev') or 0
        )
    }
)

CommentType = GraphQLObjectType(
    name='ADCommentType',
    fields={
        'uri': GraphQLField(
            type=GraphQLString,
            description='High risk URI',
            resolver=lambda root, *_: root.get('p_threat')
        ),
        'title': GraphQLField(
            type=GraphQLString,
            description='Threat title',
            resolver=lambda root, *_: root.get('title')
        ),
        'text': GraphQLField(
            type=GraphQLString,
            description='Threat description',
            resolver=lambda root, *_: root.get('text')
        )
    }
)

ThreatsInformationType = GraphQLObjectType(
    name='ADThreatsType',
    fields={
        'list': GraphQLField(
            type=GraphQLList(ScoredRequestType),
            description='List of URIs that have been scored',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference to retrieve the list of scored URI. Defaults to today'
                )
            },
            resolver=lambda root, args, *_: AD.get_scored_requests(date=args.get('date', date.today()))
        ),
        'comments': GraphQLField(
            type=GraphQLList(CommentType),
            description='A list of comments about threats',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference to retrieve the list of high risk comments. Defaults to today'
                )
            },
            resolver=lambda root, args, *_: AD.story_board(date=args.get('date', date.today()))
        )
    }
)

ThreatDetailsType = GraphQLObjectType(
    name='ADThreatDetailsType',
    fields={
        'datetime': GraphQLField(
            type=SpotDatetimeType,
            description='Start time of the request',
            resolver=lambda root, *_: '{} {}'.format(root.get('p_date') or '1970-01-01', root.get('p_time') or '00:00:00')
        ),
        'clientIp': GraphQLField(
            type=SpotIpType,
            description='Client\'s IP address',
            resolver=lambda root, *_: root.get('clientip')
        ),
        'username': GraphQLField(
            type=GraphQLString,
            description='Username used for authetication',
            resolver=lambda root, *_: root.get('username')
        ),
        'duration': GraphQLField(
            type=GraphQLInt,
            description='Connection duration',
            resolver=lambda root, *_: root.get('duration')
        ),
        'uri': GraphQLField(
            type=GraphQLString,
            description='The original URI requested',
            resolver=lambda root, *_: root.get('fulluri')
        ),
        'webCategory': GraphQLField(
            type=GraphQLString,
            description='Web content categories',
            resolver=lambda root, *_: root.get('webcat')
        ),
        'responseCode': GraphQLField(
            type=GraphQLInt,
            description='HTTP response code',
            resolver=lambda root, *_: root.get('respcode')
        ),
        'requestMethod': GraphQLField(
            type=GraphQLString,
            description='HTTP request method',
            resolver=lambda root, *_: root.get('reqmethod')
        ),
        'userAgent': GraphQLField(
            type=GraphQLString,
            description='Client\'s user agent',
            resolver=lambda root, *_: root.get('useragent')
        ),
        'responseContentType': GraphQLField(
            type=GraphQLString,
            description='HTTP response content type (MIME)',
            resolver=lambda root, *_: root.get('resconttype')
        ),
        'referer': GraphQLField(
            type=GraphQLString,
            description='The address of the webpage that linked to the resource being requested',
            resolver=lambda root, *_: root.get('referer')
        ),
        'uriPort': GraphQLField(
            type=GraphQLInt,
            description='URI port',
            resolver=lambda root, *_: root.get('uriport')
        ),
        'serverIp': GraphQLField(
            type=SpotIpType,
            description='The address of the webpage that linked to the resource being requested',
            resolver=lambda root, *_: root.get('serverip')
        ),
        'serverToClientBytes': GraphQLField(
            type=GraphQLInt,
            description='Number of bytes sent from appliance to client',
            resolver=lambda root, *_: root.get('scbytes')
        ),
        'clientToServerBytes': GraphQLField(
            type=GraphQLInt,
            description='Number of bytes sent from client to appliance',
            resolver=lambda root, *_: root.get('csbytes')
        )
    }
)

IncidentProgressionRequestType = GraphQLObjectType(
    name='ADIncidentProgressionRequestType',
    fields={
        'clientIp': GraphQLField(
            type=SpotIpType,
            description='Client\'s IP',
            resolver=lambda root, *_: root.get('clientip')
        ),
        'referer': GraphQLField(
            type=GraphQLString,
            description='The address of the webpage that linked to the resource being requested',
            resolver=lambda root, *_: root.get('referer')
        ),
        'requestMethod': GraphQLField(
            type=GraphQLString,
            description='HTTP Request Method',
            resolver=lambda root, *_: root.get('reqmethod')
        ),
        'responseContentType': GraphQLField(
            type=GraphQLString,
            description='HTTP response content type (MIME)',
            resolver=lambda root, *_: root.get('resconttype')
        )
    }
)

IncidentProgressionType = GraphQLObjectType(
    name='ADIncidentProgressionType',
    fields={
        'uri': GraphQLField(
            type=GraphQLString,
            description='Threat URI',
            resolver=lambda root, *_: root.get('fulluri')
        ),
        'refererFor': GraphQLField(
            type=GraphQLList(GraphQLString),
            description='A list of URI who whose referer is the threat\'s URI',
            resolver=lambda root, *_: root.get('referer_for')
        ),
        'requests': GraphQLField(
            type=GraphQLList(IncidentProgressionRequestType),
            description='A list of requests made to Threat\'s URI',
            resolver=lambda root, *_: root.get('requests')
        )
    }
)

TimelineType = GraphQLObjectType(
    name='ADTimelineType',
    fields={
        'startDatetime': GraphQLField(
            type=SpotDatetimeType,
            description='Connection\'s start time',
            resolver=lambda root, *_: root.get('tstart') or '1970-01-01 00:00:00'
        ),
        'endDatetime': GraphQLField(
            type=SpotDatetimeType,
            description='Connection\'s end time',
            resolver=lambda root, *_: root.get('tend') or '1970-01-01 00:00:00'
        ),
        'duration': GraphQLField(
            type=GraphQLInt,
            description='Connection duration',
            resolver=lambda root, *_: root.get('duration')
        ),
        'clientIp': GraphQLField(
            type=SpotIpType,
            description='Client\'s IP address',
            resolver=lambda root, *_: root.get('clientip')
        ),
        'responseCode': GraphQLField(
            type=GraphQLInt,
            description='HTTP response code',
            resolver=lambda root, *_: root.get('respcode')
        ),
        'responseCodeLabel': GraphQLField(
            type=GraphQLString,
            description='HTTP response code name',
            resolver=lambda root, *_: root.get('respcode_name')
        )
    }
)

ThreatInformationType = GraphQLObjectType(
    name='ADThreatInformation',
    fields={
        'details': GraphQLField(
            type=GraphQLList(ThreatDetailsType),
            description='Detailed information about a high risk threat',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference for detailed information. Defaults to today'
                ),
                'uri': GraphQLArgument(
                    type=GraphQLNonNull(GraphQLString),
                    description='Threat\'s URI'
                )
            },
            resolver=lambda root, args, *_: AD.expanded_search(date=args.get('date', date.today()), uri=args.get('uri'))
        ),
        'incidentProgression': GraphQLField(
            type=IncidentProgressionType,
            description='Details the type of connections that conform the activity related to the threat',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference for incident progression information. Defaults to today'
                ),
                'uri': GraphQLArgument(
                    type=GraphQLNonNull(GraphQLString),
                    description='Threat URI'
                )
            },
            resolver=lambda root, args, *_: AD.incident_progression(date=args.get('date', date.today()), uri=args.get('uri'))
        ),
        'timeline': GraphQLField(
            type=GraphQLList(TimelineType),
            description='Lists \'clusters\' of inbound connections to the IP, grouped by time; showing an overall idea of the times during the day with the most activity',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference for time line information. Defaults to today'
                ),
                'uri': GraphQLArgument(
                    type=GraphQLNonNull(GraphQLString),
                    description='Threat URI'
                )
            },
            resolver=lambda root, args, *_: AD.time_line(date=args.get('date', date.today()), uri=args.get('uri'))
        )
    }
)

QueryType = GraphQLObjectType(
    name='ADQueryType',
    fields={
        'suspicious': GraphQLField(
            type=GraphQLList(SuspiciousType),
            description='Proxy suspicious requests',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference to retrieve the list of suspicious requests. Defaults to today'
                ),
                'clientIp': GraphQLArgument(
                    type=SpotIpType,
                    description='Client\'s ip'
                )
            },
            resolver=lambda root, args, *_: AD.suspicious_requests(date=args.get('date', date.today()), ip=args.get('clientIp'))
        ),
        'edgeDetails': GraphQLField(
            type=GraphQLList(EdgeDetailsType),
            description='HTTP requests to a particular URI',
            args={
                'date': GraphQLArgument(
                    type=SpotDateType,
                    description='A date to use as reference to retrieve the list of requests made by client. Defaults to today'
                ),
                'uri': GraphQLArgument(
                    type=GraphQLNonNull(GraphQLString),
                    description='URI of interest'
                ),
                'clientIp': GraphQLArgument(
                    type=GraphQLNonNull(SpotIpType),
                    description='Client\'s IP'
                )
            },
            resolver=lambda root, args, *_: AD.details(date=args.get('date', date.today()), uri=args.get('uri'), ip=args.get('clientIp'))
        ),
        'threats': GraphQLField(
            type=ThreatsInformationType,
            description='Advanced inforamtion about threats',
            resolver=lambda *_ : {}
        ),
        'threat': GraphQLField(
            type=ThreatInformationType,
            description='Advanced inforamtion about a single threat',
            resolver=lambda *_:{}
        ),
        'ingestSummary': GraphQLField(
            type=GraphQLList(IngestSummaryType),
            description='Summary of ingested proxy records in range',
            args={
                'startDate': GraphQLArgument(
                    type=GraphQLNonNull(SpotDateType),
                    description='Start date'
                ),
                'endDate': GraphQLArgument(
                    type=GraphQLNonNull(SpotDateType),
                    description='End date'
                )
            },
            resolver=lambda root, args, *_: AD.ingest_summary(start_date=args.get('startDate'), end_date=args.get('endDate'))
        )
    }
)

TYPES = []
