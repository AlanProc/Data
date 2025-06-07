Dataframes it’s tabular format(rows & columns); supports SQL-like operations; comparable to pandas dataframe, but pandas operate on a single compute instance,
while PySpark distributes data across multiple instances = more speed and data scalability.
So Spark dataframes are designed for much larger datasets. Can do manipulation tasks like:filtering, grouping and aggregating.

Common method for loading data is using ‘spark.read.csv()’. It reads CSV files into a Spark DataFrame, allowing us to define headers and automatically infer schema types.
We can also include ‘header=True’ and ‘inferSchema=True’. E.g:
census_df = spark.read.csv(‘path/to/census.csv’, header=True, inferSchema=True)
We can create DataFrames using ‘createDataFrame()’ function, ‘spark.read.csv()’ is generally faster.

‘.printSchema()’ to view DF structure.
‘.count()’ method to count rows.
‘.groupBy()’  ‘.agg()’   ‘.filter()’ {like WHERE in SQL}   ‘select()’ {like in SQL}
‘.sort()’ for simple flexible sorting.
‘orderby()’ for complex multi-column sorting.
‘.na.drop()’: drop rows with null values either across the entire DF or in specific columns.
‘.where()’ and ‘isNotNull()’: column-specific filtering
‘.na.fill()’: replace nulls with default values using
‘.withColumn()’ create new columns.
‘.withColumnRenamed()’ rename columns.
‘.drop()’ removes columns with irrelevant data

Practice:

filtered_census_df = census_df.filter(df[‘age’] > 50).select(‘age’, ‘occupation’)
filtered_census_df.show()



