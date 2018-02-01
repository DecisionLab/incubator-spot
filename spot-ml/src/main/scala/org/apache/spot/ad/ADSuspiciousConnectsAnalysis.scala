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

import org.apache.log4j.Logger
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spot.SuspiciousConnects.SuspiciousConnectsAnalysisResults
import org.apache.spot.SuspiciousConnectsArgumentParser.SuspiciousConnectsConfig
import org.apache.spot.ad.ADSchema._
import org.apache.spot.utilities.data.validation.InputSchema.InputSchemaValidationResponse
import org.apache.spot.utilities.data.validation.{InputSchema, InvalidDataHandler => dataValidation}

object ADSuspiciousConnectsAnalysis {

  val InStructType = StructType(
    List(
      UserIDField,
      TypeField,
      CodeField,
      SourceIPv4Field,
      DestinationIPv4Field,
      ApplicationNameField,
      DVCDomainField,
      CategoryField,
      AppField,
      BeginTimeField,
      EndTimeField,
      ActionField,
      SourcePortField,
      DestinationPortField
    )
  )
  val InSchema = InStructType.fieldNames.map(col)
  val OutSchema = StructType(
    List(UserIDField,
      TypeField,
      CodeField,
      SourceIPv4Field,
      DestinationIPv4Field,
      BeginTimeField,
      EndTimeField)).fieldNames.map(col)

  /**
    * Run suspicious connections analysis on AD log data.
    * Saves the most suspicious connections to a CSV file on HDFS.
    *
    * @param config Object encapsulating runtime parameters and CLI options.
    * @param sparkSession
    * @param logger
    */
  def run(config: SuspiciousConnectsConfig, sparkSession: SparkSession, logger: Logger,
          inputADRecords: DataFrame): Option[SuspiciousConnectsAnalysisResults] = {


    logger.info("Starting AD suspicious connects analysis.")

    logger.info("Validating schema...")
    val InputSchemaValidationResponse(isValid, errorMessages) = validateSchema(inputADRecords)

    if (!isValid) {
      errorMessages.foreach(logger.error(_))
      None
    } else {
      val invalidADRecords = filterInvalidRecords(inputADRecords)

      val filteredADRecords = filterRecords(inputADRecords).select(InSchema: _*)
      val suspiciousADRecords = ADSimplisticAnomalyDetector.suspiciousPreAuthRecords(filteredADRecords)

      Some(SuspiciousConnectsAnalysisResults(suspiciousADRecords, invalidADRecords))
    }
  }


  /**
    *
    * @param inputADRecords raw AD records.
    * @return
    */
  def filterRecords(inputADRecords: DataFrame): DataFrame = {

    val cleanADRecordsFilter = inputADRecords(UserID).isNotNull &&
      inputADRecords(UserID).notEqual("") &&
      inputADRecords(Type).isNotNull &&
      inputADRecords(Type).notEqual("") &&
      inputADRecords(Code).isNotNull &&
      inputADRecords(Code).notEqual("") &&
      inputADRecords(BeginTime).gt(0) &&
      inputADRecords(EndTime).gt(0) &&
      inputADRecords(SourceIPv4).isNotNull &&
      inputADRecords(SourceIPv4).notEqual("") &&
      inputADRecords(DestinationIPv4).isNotNull &&
      inputADRecords(DestinationIPv4).notEqual("")

    inputADRecords
      .filter(cleanADRecordsFilter)
  }

  /**
    *
    * @param inputADRecords raw AD records.
    * @return
    */
  def filterInvalidRecords(inputADRecords: DataFrame): DataFrame = {
    val invalidFilter = inputADRecords(UserID).isNull &&
      inputADRecords(UserID) === "" &&
      inputADRecords(Type).isNull &&
      inputADRecords(Type) === "" &&
      inputADRecords(Code).isNull &&
      inputADRecords(Code) === "" &&
      inputADRecords(BeginTime).leq(0) &&
      inputADRecords(EndTime).leq(0) &&
      inputADRecords(SourceIPv4).isNull &&
      inputADRecords(SourceIPv4) === "" &&
      inputADRecords(DestinationIPv4).isNull &&
      inputADRecords(DestinationIPv4) === ""

    inputADRecords.filter(invalidFilter)
  }

  /**
    * Validates incoming data matches required schema for model training and scoring.
    *
    * @param inputADRecords incoming data frame
    * @return
    */
  def validateSchema(inputADRecords: DataFrame): InputSchemaValidationResponse = {

    InputSchema.validate(inputADRecords.schema, ADSuspiciousConnectsAnalysis.InStructType)

  }

}