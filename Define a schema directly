from pyspark.sql import SparkSession

# Fill in the schema with the columns we need
schema = StructType([StructField("age",IntegerType()),
                     StructField("education_num",IntegerType()),
                     StructField("marital_status",StringType()),
                     StructField("occupation",StringType()),
                     StructField("income",StringType()),
                    ])

# Read in the CSV, using the schema defined above
census_adult = spark.read.csv("adult_reduced_100.csv", sep=',' , header=False, schema=schema)

# Print out the schema
census_adult.printSchema()
