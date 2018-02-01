package org.apache.spot.ad

import java.util.Date

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions.{count, udf, desc, col, lit}

object ADSimplisticAnomalyDetector {

  def suspiciousPreAuthRecords(inputRecords: DataFrame): DataFrame = {
    inputRecords.filter(col(ADSchema.UserID).isNotNull)
      .select(ADSchema.Code, ADSchema.Type, ADSchema.UserID, ADSchema.BeginTime)
      .withColumn(ADSchema.BeginTime, udfUppercase(inputRecords(ADSchema.BeginTime)))
      .groupBy(ADSchema.BeginTime, ADSchema.UserID)
      .agg(count("*").alias("total"))
      .where(col("total") >= 50)
      .orderBy(desc("total"))
      .withColumn("score", lit(1.0))
  }

  def udfUppercase:UserDefinedFunction = udf((timestamp: Long) => convert(timestamp))

  private def convert(time: Long) : String = {
    val sdf = new java.text.SimpleDateFormat("yyyy-MM-dd")
    sdf.format(new Date(time * 1000))
  }


}
