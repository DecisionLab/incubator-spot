INSERT INTO spot.event
partition(p_dvc_vendor='alex', p_dvc_type='test', p_dt='2018-01-05')
(begin_time, event_time, dns_len, dst_ip4_str, src_ip4_str, dns_query, dns_class, dns_type, dns_response_code, dns_answers)
VALUES (1518806042, 1518806042, 3, '1.1.1.1', '2.2.2.2', 'a fake query', 'a fake class', 7, 200, 'sample answers');