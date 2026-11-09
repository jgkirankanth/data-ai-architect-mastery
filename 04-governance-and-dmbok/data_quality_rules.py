import great_expectations as ge

# Example: Enforcing Data Quality in the Silver Layer
df = ge.read_parquet("abfss://workspace@onelake.dfs.fabric.microsoft.com/lakehouse/Tables/silver_market_ticks")

# Define DMBOK-aligned quality rules
df.expect_column_values_to_not_be_null("price")
df.expect_column_values_to_be_between("volume", min_value=0, max_value=10000000)

validation_results = df.validate()
if not validation_results["success"]:
    raise ValueError("Data Quality checks failed. Halting pipeline.")
