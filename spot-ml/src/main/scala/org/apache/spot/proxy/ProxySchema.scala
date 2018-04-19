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

package org.apache.spot.proxy

import org.apache.spark.sql.types._

/**
  * Data frame column names used in the proxy suspicious connects analysis.
  */
object ProxySchema {

  // fields from the input

//  val Date = "p_date"
//  val DateField = StructField(Date, StringType, nullable = true)

  val Time = "event_insert_time"
  val TimeField = StructField(Time, LongType, nullable = true)

  val ClientIP = "src_ip4_str"
  val ClientIPField = StructField(ClientIP, StringType, nullable = true)

  val Host = "prx_host"
  val HostField = StructField(Host, StringType, nullable = true)

  val ReqMethod = "prx_method"
  val ReqMethodField = StructField(ReqMethod, StringType, nullable = true)

  val UserAgent = "prx_browser"
  val UserAgentField = StructField(UserAgent, StringType, nullable = true)

  val ResponseContentType = "prx_type"
  val ResponseContentTypeField = StructField(ResponseContentType, StringType, nullable = true)

  val Duration = "duration"
  val DurationField = StructField(Duration, IntegerType, nullable = true)

  val UserName = "user_name"
  val UserNameField = StructField(UserName, StringType, nullable = true)

//  val AuthGroup = "authgroup"

//  val ExceptionId = "exceptionid"

  val FilterResult = "prx_filter_result"

  val WebCat = "prx_category"
  val WebCatField = StructField(WebCat, StringType, nullable = true)

  val Referer = "prx_referrer"
  val RefererField = StructField(Referer, StringType, nullable = true)

  val RespCode = "prx_code"
  val RespCodeField = StructField(RespCode, StringType, nullable = true)

  val Action = "prx_action"

//  val URIScheme = "urischeme"

//  val URIPort = "uriport"
//  val URIPortField = StructField(URIPort, StringType, nullable = true)

//  val URIPath = "uripath"
//  val URIPathField = StructField(URIPath, StringType, nullable = true)

  val URIQuery = "prx_query"
  val URIQueryField = StructField(URIQuery, StringType, nullable = true)

//  val URIExtension = "uriextension"

//  val ServerIP = "serverip"
//  val ServerIPField = StructField(ServerIP, StringType, nullable = true)

  val SCBytes = "in_bytes"
  val SCBytesField = StructField(SCBytes, IntegerType, nullable = true)

  val CSBytes = "out_bytes"
  val CSBytesField = StructField(CSBytes, IntegerType, nullable = true)

//  val VirusID = "virusid"
//  val BcappName = "bcappname"
//  val BcappOper = "bcappoper"

  val FullURI = "http_request_uri"
  val FullURIField = StructField(FullURI, StringType, nullable = true)

  // output fields

  val Word = "word"
  val WordField = StructField(Word, StringType, nullable = true)

  val Score = "score"
  val ScoreField = StructField(Score, DoubleType, nullable = true)
}
