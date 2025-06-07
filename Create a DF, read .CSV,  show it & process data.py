from pyspark.sql import SparkSession

# Load the CSV file into a DataFrame
salaries_df = spark.read.csv("salaries.csv", header=True, inferSchema=True)

# Show the DataFrame
anamefordf.show()

# Count the total number of rows
row_count = salaries_df.count()
print(f"Total rows: {row_count}")

# Group by company size and calculate the average of salaries
salaries_df.groupBy("company_size").agg({"salary_in_usd": "avg"}).show()
salaries_df.show()

# Average salary for entry level in Canada
CA_jobs = ca_salaries_df.filter(ca_salaries_df["company_location"] == "CA").filter(ca_salaries_df['experience_level']
 == "EN").groupBy().avg("salary_in_usd")

# Show the result
CA_jobs.show()
