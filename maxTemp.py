import pyspark as sp
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,date_format,concat,substring,lit,lpad,to_timestamp,when
import  pandas as pd
import os


spark = SparkSession.builder \
    .appName("Max Temperature MapReduce") \
    .getOrCreate()


for filename in os.listdir("./dataPreprocessed"):
      
                  df = spark.read.option("header", "true").csv("./dataPreprocessed/"+filename)
                  temperature_rdd = df.rdd.map(lambda row: (dir, float(row.airtemp)))
                  max_temperature = temperature_rdd.reduceByKey(lambda x, y: max(x, y)).collect()
                  print(f"Year {filename[0:5]}: Maximum Temperature = {max_temperature[0][1]}")