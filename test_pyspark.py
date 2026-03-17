import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("PySparkScriptTest") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

print("Python:", sys.executable)

data = [
    ("2024-01-01", 72000, 100000),
    ("2024-01-02", 73000, 120000),
    ("2024-01-03", 71000, 90000),
]

columns = ["date", "close", "volume"]

df = spark.createDataFrame(data, columns)
df.show()

spark.stop()