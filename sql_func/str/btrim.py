from pyspark.sql import SparkSession
from pyspark.sql.functions import btrim, upper

# Create a SparkSession
spark = SparkSession.builder.getOrCreate()

# Create a sample DataFrame
data = [("  John  ",), ("  Alice  ",), ("  Bob  ",)]
df = spark.createDataFrame(data, ["name"])

# Apply btrim function to remove leading and trailing spaces
df = df.withColumn("trimmed_name", btrim(df.name))

# Apply upper function to convert names to uppercase
df = df.withColumn("uppercase_name", upper(df.trimmed_name))

# Show the result
df.show()
