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

package org.apache.spot.ad

import org.apache.spark.sql.types._

/**
  * Data frame schemas and column names used in the AD suspicious connects analysis.
  */
object ADSchema {

  // input fields

  val UserID = "user_id"
  val UserIDField = StructField(UserID, StringType, nullable = true)

  val Type = "type"
  val TypeField = StructField(Type, StringType, nullable= true)

  val Code = "code"
  val CodeField = StructField(Code, StringType, nullable= true)

  val SourceIPv4 = "src_ip4_str"
  val SourceIPv4Field = StructField(SourceIPv4, StringType, nullable= true)

  val DestinationIPv4 = "dst_ip4_str"
  val DestinationIPv4Field = StructField(DestinationIPv4, StringType, nullable= true)

  val ApplicationName = "application_name"
  val ApplicationNameField = StructField(ApplicationName, StringType, nullable = true)

  val DVCDomain = "dvc_domain"
  val DVCDomainField = StructField(DVCDomain, StringType, nullable= true)

  val Category = "category"
  val CategoryField = StructField(Category, StringType, nullable= true)

  val App = "app"
  val AppField = StructField(App, StringType, nullable= true)

  val Action = "action"
  val ActionField = StructField(Action, StringType, nullable= true)


  val BeginTime = "begintime"
  val BeginTimeField = StructField(BeginTime, LongType, nullable= true)

  val EndTime = "endtime"
  val EndTimeField = StructField(EndTime, LongType, nullable= true)


  val SourcePort = "src_port"
  val SourcePortField = StructField(SourcePort, IntegerType, nullable= true)

  val DestinationPort = "dst_port"
  val DestinationPortField = StructField(DestinationPort, IntegerType, nullable = true)

}
