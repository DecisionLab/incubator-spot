/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.spot.dns

import org.apache.spark.sql.types._

/**
  * Data frame schemas and column names used in the DNS suspicious connects analysis.
  */
object DNSSchema {

  // input fields

  val TimeStamp = "begin_time"
  val TimeStampField = StructField(TimeStamp, LongType, nullable= true)

  val UnixTimeStamp = "event_time"
  val UnixTimeStampField = StructField(UnixTimeStamp, LongType, nullable= true)

  val FrameLength = "dns_len"
  val FrameLengthField = StructField(FrameLength, IntegerType, nullable= true)

  val ClientIP = "dst_ip4_str"
  val ClientIPField = StructField(ClientIP, StringType, nullable= true)

  val ServerIP = "src_ip4_str"
  val ServerIPField = StructField(ServerIP, StringType, nullable= true)

  val QueryName = "dns_query"
  val QueryNameField = StructField(QueryName, StringType, nullable= true)

  val QueryClass = "dns_class"
  val QueryClassField = StructField(QueryClass, StringType, nullable= true)

  val QueryType = "dns_type"
  val QueryTypeField = StructField(QueryType, IntegerType, nullable= true)

  val QueryResponseCode = "dns_response_code"
  val QueryResponseCodeField = StructField(QueryResponseCode, StringType, nullable= true)

  val AnswerAddress = "dns_answers"
  val AnswerAddressField = StructField(AnswerAddress, StringType, nullable= true)

  // intermediate and derived fields

  val Domain = "domain"
  val DomainField = StructField(Domain, StringType)

  val TopDomain = "top_domain"
  val TopDomainField = StructField(TopDomain, IntegerType)

  val Subdomain = "subdomain"
  val SubdomainField = StructField(Subdomain, StringType)

  val SubdomainLength = "subdomain_length"
  val SubdomainLengthField = StructField(SubdomainLength, IntegerType)

  val NumPeriods = "num_periods"
  val NumPeriodsField = StructField(NumPeriods, IntegerType)

  val SubdomainEntropy = "subdomain_entropy"
  val SubdomainEntropyField = StructField(SubdomainEntropy, DoubleType)

  // output fields

  val Word = "word"
  val WordField = StructField(Word, StringType)

  val Score = "score"
  val ScoreField = StructField(Score, DoubleType)
}
