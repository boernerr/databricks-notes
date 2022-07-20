"""Apache Spark programming- Structured Streaming

Stream processing - is contiusouly adding data and computing some metric i.e. running sum, avg, etc. Gives multi outputs
Batch processing - Only computes result once. Run on static dataset.

* Streaming Concepts *
Allows lower latency, efficient updates because it can incrementally re-load data
micro-batch model -
"""

# Setup a dataframe for streaming:
df = (spark.readstream.__loading_from_whatever_file_type__)

# Start streaming the dataframe:
df.isStreaming

df_transformed = (df.filter(__filter_logic__).select(__columns_to_select__))
df_transformed.isStreaming

