# AD

AD sub-module will extract and transform AD data already ranked by spot-ml and will load it into impala tables for the presentation layer.

## AD Components

### ad_oa.py

AD spot-oa main script executes the following steps:

		1. Creates the right folder structure to store the data and the ipython notebooks. This is: 
		
			data: data/ad/<date>/
			ipython Notebooks: ipynb/ad/<date>/
		
		2. Creates a copy of the notebooks templates into the ipython Notebooks path and renames them removing the "_master" part from the name.
		
		3. Gets the ad_results.csv from the HDFS location according to the selected date, and copies it back to the corresponding data path.
		 
		4. Reads a given number of rows from the results file.
		
		5. Saves the data in the _ad_\scores_ table. 
		
**Dependencies**

- [Python 2.7](https://www.python.org/download/releases/2.7/) should be installed in the node running AD OA. 

**Prerequisites**

Before running AD OA, users need to configure components for the first time. It is important to mention that configuring these components make them work for other data sources as Flow and DNS.  

- Configure database engine
- Generate ML results for AD

**Output**

- AD suspicious connections. _ad\_scores_ table.

Main results file for AD OA. The data stored in this table is limited by the number of rows the user selected when running [oa/start_oa.py](/spot-oa/oa/INSTALL.md#usage).
 
        0.user_id STRING
        1.type STRING
        2.code STRING
        3.src_ip4_str STRING
        4.dst_ip4_str STRING
        5.application_name STRING
        6.dvc_domain STRING
        7.category STRING
        8.app STRING
        9.begintime BIGINT
        10.endtime BIGINT
        11.action STRING
        12.src_port INT
        13.dst_port INT
        14.date_day STRING
        15.score INT

### ipynb_templates
After OA process completes, a copy of each iPython notebook is going to be copied to the ipynb/\<pipeline>/\<date> path. 
With these iPython notebooks user will be able to perform further analysis and score connections. User can also
experiment adding or modifying the code. 
If a new functionality is required for the ipython notebook, the templates need to be modified to include the functionality for new executions.
For further reference on how to work with these notebooks, you can read:   
[Threat_Investigation.ipynb](/spot-oa/oa/ad/ipynb_templates/ThreatInvestigation.md)


### Reset scored connections
To reset all scored connections for a day, a specific cell with a preloaded function is included in the Advanced Mode Notebook. The cell is commented to avoid accidental executions, but is properly labeled.
