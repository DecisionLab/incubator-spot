INSERT INTO spot.event
partition(p_dvc_vendor='alex', p_dvc_type='test', p_dt='2018-01-07')
(begin_time, event_time, dns_len, dst_ip4_str, src_ip4_str, dns_query, dns_class, dns_type, dns_response_code, dns_answers)
VALUES (1518806042, 1518806042, 253, '1.1.1.1', '10.1.1.1', 'google.com', '0x00000001', 1, '0', 'sample answers');

INSERT INTO spot.event
partition(p_dvc_vendor='alex', p_dvc_type='test', p_dt='2018-01-07')
(begin_time, event_time, dns_len, dst_ip4_str, src_ip4_str, dns_query, dns_class, dns_type, dns_response_code, dns_answers)
VALUES (1518806050, 1518806050, 212, '1.1.1.1', '10.1.1.2', 'google.com', '0x00000001', 1, '0', 'sample answers');

INSERT INTO spot.event
partition(p_dvc_vendor='alex', p_dvc_type='test', p_dt='2018-01-07')
(begin_time, event_time, dns_len, dst_ip4_str, src_ip4_str, dns_query, dns_class, dns_type, dns_response_code, dns_answers)
VALUES (1518806042, 1518806052, 260, '1.1.1.1', '10.1.7.22', 'cnn.com', '0x00000001', 1, '0', 'sample answers');

INSERT INTO spot.event
partition(p_dvc_vendor='alex', p_dvc_type='test', p_dt='2018-01-07')
(begin_time, event_time, dns_len, dst_ip4_str, src_ip4_str, dns_query, dns_class, dns_type, dns_response_code, dns_answers)
VALUES (1518806042, 1518806042, 243, '1.1.1.1', '10.1.32.255', 'amazon.com', '0x00000001', 1, '0', 'sample answers');

-- NOTE: SAMPLE ata pulled from spot docker
-- frame_time,frame_len,ip_dst,dns_qry_name,dns_qry_class,dns_qry_type,dns_qry_rcode,domain,subdomain,subdomain_length,num_periods,subdomain_entropy,top_domain,word,score,query_rep,hh,ip_sev,dns_sev,dns_qry_class_name,dns_qry_type_name,dns_qry_rcode_name,network_context,unix_tstamp
-- Jul  8 2016 06:58:45.765735000 UTC,253,172.16.0.167,customer.ihre-magenverkleinerung-zum-trinken.co,0x00000001,1,0,customer,None,0,3,2.0,1,1_10_7_0_1_5_1_0,1.3209783610934376E-8,gti:Medium:2::fb:UNKNOWN:-1,06,0,0,Internet (IN),A,NoError,,1467961125
-- Jul  8 2016 05:03:42.704701000 UTC,229,172.16.0.164,87-59-200-143-dynamic.dk.customer.tdc.net,0x00000001,1,0,tdc,87-59-200-143-dynamic.dk.customer,33,5,4.498939573903908,1,1_2_4_1_2_5_1_0,1.3227393260366873E-8,gti:Minimal:1::fb:UNKNOWN:-1,05,0,0,Internet (IN),A,NoError,,1467954222
-- Jul  8 2016 06:31:38.895195000 UTC,232,172.16.0.185,www.wallstreetinsightsandindictments.com,0x00000001,1,0,wallstreetinsightsandindictments,www,3,3,0.0,1,1_6_6_1_0_5_1_0,1.3227739896214263E-8,gti:Minimal:1::fb:UNKNOWN:-1,06,0,0,Internet (IN),A,NoError,,1467959498
-- Jul  8 2016 07:11:46.972041000 UTC,293,172.16.0.185,stjhnbsu1kw-047055190132.dhcp-dynamic.fibreop.nb.bellaliant.net,0x00000001,1,0,bellaliant,stjhnbsu1kw-047055190132.dhcp-dynamic.fibreop.nb,48,6,4.756328385912463,1,1_10_7_1_5_5_1_0,1.3251552085672652E-8,gti:Minimal:1::fb:UNKNOWN:-1,07,0,0,Internet (IN),A,NoError,,1467961906
-- Jul  8 2016 03:40:38.853811000 UTC,229,172.16.0.167,87-59-200-143-dynamic.dk.customer.tdc.net,0x00000001,1,0,tdc,87-59-200-143-dynamic.dk.customer,33,5,4.498939573903908,1,1_2_2_1_2_5_1_0,1.32594185306699E-8,gti:Minimal:1::fb:UNKNOWN:-1,03,0,0,Internet (IN),A,NoError,,1467949238
