# TODO
1. clean up the ml ops cdh
2. clean up or remove the cdh spot.conf file
3. consider making he input reader support both parquet and avro, so existing spot functionality still works

# DEPLOYMENT
1. when running /opt/spot/incubator-spot/spot-oa/runIpython.sh it errors due to lacking env var ACCESS_CONTROL_ALLOW_ORIGIN
   Export manually (set to '*') since we have no clue why it's not there... sadface
