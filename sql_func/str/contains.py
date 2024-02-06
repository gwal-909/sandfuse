from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create a sample DataFrame
data = [("John Doe", 25), ("Jane Smith", 30), ("Bob Johnson", 35)]
df = spark.createDataFrame(data, ["name", "age"])

# Use the contains function to filter rows
filtered_df = df.filter(col("name").contains("John"))

# Show the filtered DataFrame
filtered_df.show()