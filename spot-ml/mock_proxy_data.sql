INSERT INTO spot.event
partition(p_dvc_vendor='dl', p_dvc_type='testproxy', p_dt='2018-01-08')
(event_time, src_ip4_str, prx_host, prx_method, prx_browser, prx_type, duration, user_name, prx_filter_result, prx_category, prx_referrer, prx_code, prx_action, prx_query, in_bytes, out_bytes, http_request_uri)
VALUES (1518806042, '10.1.2.3', 'hsn.mpl.miisolutions.net', 'POST', 'Firefox', 'sample type', 2345, 'DL', 'sample filter result', 'Technology/Internet', 'sample referrer', '200', 'sample action', 'sample query', 10, 20, 'http://google.com?q=test');

-- N/A	  event_time	src_ip4_str	prx_host	prx_method	prx_browser	prx_type	  duration	user_name	N/A         N/A	          prx_filter_result	prx_category	prx_referrer	prx_code	prx_action	N/A	  		N/A     N/A     prx_query N/A           N/A       in_bytes  out_bytes N/A     N/A       N/A       http_request_uri
-- p_date	p_time	    clientip	  host	    reqmethod	  useragent	  resconttype	duration	username  authgroup   exceptionid   filterresult      webcat        referer       respcode  action      urischeme uriport uripath uriquery  uriextension  serverip  scbytes   csbytes   virusid bcappname bcappoper fulluri

-- p_date	    p_time	  clientip	      host	                    reqmethod	  useragent	                                                                resconttype	duration	user_name	webcat	      referer	      respcode	    uriport	  uripath	  uriquery	  serverip	scbytes	  csbytes	fulluri	word	      score	        uri_rep	uri_sev	respcode_name	network_context	hash
-- 2016-07-08	7:11:11	  10.254.75.186	  hsn.mpl.miisolutions.net	POST	      Shockwave Flash	-	2047	-	Content Servers	http://www.hsn.com/arcade/lights-camera-subtraction/10	503	1935	/send/1294067758/3	-	10.7.210.157	962	471	hsn.mpl.miisolutions.net/send/1294067758/3	1_2_POST_2_2_5	6.66E-11	gti:Minimal:1:Computing/Internet|Information Technology	0	Service Unavailable		bd6d293e133a9680c200d447c44363de7
-- 2016-07-08	16:15:11	10.254.107.195	api.rollbar.com	          POST	      Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.115 Safari/537.36	application/json;%20charset=utf-8	292	-	Technology/Internet	http://seekingalpha.com/account/portfolio/news	429	80	/api/1/item/	-	10.7.210.157	662	5139	api.rollbar.com/api/1/item/	1_5_POST_1_3_4	7.73E-11	gti:Unverified:-1:Business|Business/Services;Computing/Internet|Information Technology	0	Too Many Requests		bf6e76e454ff1b91ce19e6ec38f748d616
-- 2016-07-08	20:48:55	10.34.132.70	  10.7.210.157	            TUNNEL	    Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)	-	6	-	none	-	0	911	/	-	10.7.210.157	0	341	10.7.210.157	0_8_TUNNEL_0_1_0	1.23E-10	gti:Unverified:-1:Business|Business/Services;Computing/Internet|Information Technology	0	0		5ec46c8780aeb0a3e2616a998d30cac020
-- 2016-07-08	20:48:55	10.34.132.70	  10.7.210.157	            TUNNEL	    Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)	-	1	-	none	-	0	911	/	-	10.7.210.157	0	341	10.7.210.157	0_8_TUNNEL_0_1_0	1.23E-10	gti:Unverified:-1:Business|Business/Services;Computing/Internet|Information Technology	0	0		5ec46c8780aeb0a3e2616a998d30cac020