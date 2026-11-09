# Fabric PySpark Notebook: Financial Tick Data Transformation
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, current_timestamp

spark = SparkSession.builder.appName("FinancialLakehouse").getOrCreate()

bronze_path = "abfss://<workspace_id>@onelake.dfs.fabric.microsoft.com/<lakehouse_id>/Files/bronze/market_ticks/"
df_raw = spark.read.format("csv").option("header", "true").load(bronze_path)

df_silver = df_raw.select(
    col("Symbol").alias("ticker"),
    to_timestamp(col("TradeTime")).alias("trade_timestamp"),
    col("Price").cast("decimal(10,4)").alias("price")
).filter(col("price").isNotNull())

silver_path = "abfss://<workspace_id>@onelake.dfs.fabric.microsoft.com/<lakehouse_id>/Tables/silver_market_ticks"
df_silver.write.format("delta").mode("append").save(silver_path)
