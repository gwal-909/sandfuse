from pyspark.sql import SparkSession
from pyspark.sql.functions import lcase

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create a DataFrame
data = [("John", 25), ("Alice", 30), ("Bob", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Apply lcase function to convert Name column to lowercase
df = df.withColumn("LowercaseName", lcase(df["Name"]))

# Show the result
df.show()