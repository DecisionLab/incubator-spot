package org.apache.spot.ad

import java.util.Date

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions.{count, udf, desc, col}

object ADSimplisticAnomalyDetector {

  val KERBERBOS_PRE_AUTH_FAILURE_CODE = "263047710"

  def suspiciousPreAuthRecords(inputRecords: DataFrame): DataFrame = {
    val pre_auth_records = inputRecords.filter(col(ADSchema.UserID).isNotNull)
      .filter(col(ADSchema.Code) === KERBERBOS_PRE_AUTH_FAILURE_CODE)

    val scores = pre_auth_records.select(ADSchema.Code, ADSchema.Type, ADSchema.UserID, ADSchema.BeginTime)
      .withColumn("date_day", udfUppercase(inputRecords(ADSchema.BeginTime)))
      .groupBy("date_day", ADSchema.UserID)
      .agg(count("*").alias("score"))     // treat the total as a score value
      .where(col("score") >= 3)
      .orderBy(desc("score"))

    pre_auth_records.join(scores, ADSchema.UserID)
  }

  def udfUppercase:UserDefinedFunction = udf((timestamp: Long) => convert(timestamp))

  private def convert(time: Long) : String = {
    val sdf = new java.text.SimpleDateFormat("yyyy-MM-dd")
    sdf.format(new Date(time * 1000))
  }


}
