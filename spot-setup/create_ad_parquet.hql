CREATE EXTERNAL TABLE ${var:dbname}.ad_scores (
user_id STRING,
type STRING,
code STRING,
src_ip4_str STRING,
dst_ip4_str STRING,
application_name STRING,
dvc_domain STRING,
category STRING,
app STRING,
begintime BIGINT,
endtime BIGINT,
action STRING,
src_port INT,
dst_port INT,
date_day STRING,
score INT
)
PARTITIONED BY ( 
y SMALLINT,
m TINYINT,
d TINYINT
)
STORED AS PARQUET
LOCATION '${var:huser}/ad/hive/oa/suspicious';