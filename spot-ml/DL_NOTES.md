# ml_ops_cdh.sh

ml_ops_cdh.sh is a customized version of the ml_ops.sh script that operates on the ODM formatted data. This is the operator used in this project, and the original has been retained for use if non-ODM data is ingested.

# Run the previous day's data
Proxy:
DATE=`date +%Y%m%d -d "yesterday" `; cd /opt/spot/incubator-spot/spot-ml; /opt/spot/incubator-spot/spot-ml/ml_ops_cdh.sh $DATE proxy
AD:
DATE=`date +%Y%m%d -d "yesterday" `; cd /opt/spot/incubator-spot/spot-ml; /opt/spot/incubator-spot/spot-ml/ml_ops_cdh.sh $DATE ad

# Sample Data
https://issues.apache.org/jira/browse/SPOT-135?jql=project%20%3D%20SPOT
