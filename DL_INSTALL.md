# ODM Install Guide

## spot-setup

1. run `spot-setup/hdfs_setup.sh`
2. run `spot-setup/odm/odm_setup.sh`

## Assumptions

We assume that after you setup `HDFS` and `Hive`, you have populated it with `ODM` event source data. To see the event schema created, refer to `spot-ml/spot.event.schema`. Within the schema take note of the different columns used for AD and DNS.

### Active Directory(AD) Events

1. Within `/etc/spot.conf` the location of the AD data must be defined. For example: 
```
AD_PATH=${HUSER}/odm/event/p_dvc_vendor=Microsoft_AD/p_dvc_type=McAfee_SIEM/p_dt=${YR}-${MH}-${DY}*
```

For example:
```
/user/spot/odm/event/p_dvc_vendor=Microsoft_AD/p_dvc_type=McAfee_SIEM/p_dt=2016-01-22
```

With a sample hive record:
```
hive> select user_id, type, code, src_ip4_str, dst_ip4_str, application_name, dvc_domain, category, app, action, begin_time, end_time, src_port, dst_port 
from spot.event 
where code is not null 
limit 1;

S-1-5-21-775157530-558380669-1391014627-240625	Kerberos pre-authentication failed	263047710	10.181.114.247	10.180.64.248	Domain Login	int.carlsonwagonlit.com	Domain Login	microsoft-windows-security-auditing	9	NULL	NULL	54158	0
```

### Domain Name System(DNS) Events

Since I didn't have any real DNS data, I created something to mock it. You can find it in `spot-ml/mock_dns_data.sql`. If you run that in `hive`, it will load up the data that I used for testing.

1. Within `/etc/spot.conf` the location od the DNS data must be defined. For example:
```
/user/spot/odm/event/p_dvc_vendor=alex/p_dvc_type=test/p_dt=2018-01-07
```

With a sample hive record:
```
hive> select begin_time, event_time, dns_len, dst_ip4_str, src_ip4_str, dns_query, dns_class, dns_type, dns_response_code, dns_answers 
from spot.event 
where dns_query = 'cnn.com' 
limit 25;

1518806042	1518806052	260	1.1.1.1	10.1.7.22	cnn.com	0x00000001	1	0	sample answers
``` 


## spot-ml

### Compiling and Building and Jar File
From the spot-ml directory run:

```
sbt 'set test in Test := {}' clean compile assembly
```

If you're building this locally, and plan on pushing it to your cluster remotely, then run this:
```
scp target/scala-2.11/spot-ml-assembly-1.1.jar [host]:/path/to/incubator-spot/spot-ml/target/scala-2.11/
```

### Running DNS and/or AD Analytics

Ensure that you have data for the day you supply to `ml_ops_cdh.sh` and then run it. For example:
```
spot-ml/ml_ops_cdh.sh 20180107 dns 1000
```
```
spot-ml./ml_ops_cdh.sh 20160122 ad
```

## spot-oa

`spot-oa` enriches the data that comes out of spot-ml and preps everything for the web application. 

### Assumptions

You need to have `python` installed. I tested against 2.7. You also need to pip install the requirements file.

###  Running the python enrichment
The script that does this is located at `spot-oa/oa/start_oa.py`. For DNS I used:
```
python start_oa.py -d 20180107 -t dns -l 10
```
And for AD:
```
python start_oa.py -d 20180105 -t ad -l 10
```
To learn more about the options/switches for this CLI, use the --help flag.

### Building the front-end
Go through the steps in the `spot-oa/ui/README.md` and `spot-oa/ui/INSTALL.md` to build the front-end

### Starting the web server
The web server can be started using 
```
spot-oa/runIpython.sh
```

### Using the UI
In your browser, navigate to:
```
http://[hostname]:8889/files/ui/ad/suspicious.html#date=2016-01-22
```
or
```
http://[hostname]:8889/files/ui/dns/suspicious.html#date=2018-01-07
```

Please remember to substitute the host name of the machine running your web application. In addition, change the query string parameter `date` to reflect the day you're interested in (just be sure you've processed that day already). 

