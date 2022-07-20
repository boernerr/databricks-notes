"""Databricks-apache Spark programming - Dataframes """

# Run sql statment in DB:
%sql
create table if not exists events using parquet options(path 'path/to/file.parquet');

# Query table:
%sql
SELECT * from events;

# UDFs:
# Can't use the internal catalyst optimizer
# To serialize your own functions: __name_of_function = udf(function)
# Can decorate a udf with:
@udf('__output_type__')
your_function()
