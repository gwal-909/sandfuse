# Import the necessary libraries
# Since we are using Python, import the SparkSession and related functions from the PySpark module.
import sys

from pyspark.sql import SparkSession

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: mmcount <file>', file=sys.stderr)
        sys.exit(-1)

    # Build a SparkSession using the SparkSession APIs.
    # If one does not exist, than create an instance. 
    # There can only be one SparkSession per JVM.
    spark = (SparkSession
        .builder
        .appName('PythonMnMCount')
        .getOrCreate())

    # Get the M&M data set filename from the command-line arguments
    mnm_file = sys.argv[1]
    # Read the file into a Spark dataframe using the CSV format
    # by inferring the schema and specifying that the file
    # contains a header, which provides column names for comma
    # separated fields.
    mnm_df = (spark.read.format('csv')
        .option('header', 'true')
        .option('inferSchema', 'true')
        .load(mnm_file))

    # We use the DataFrame high-level APIs. Note that we don't
    # use RDDs at all. Because soem fo Spark's functions return
    # the same object, we can chain function calls.
    # 1. Select from the DataFrame the fields 'State', 'Color', and 'Count'
    # 2. Since we want to group each state and its M&M color count, we use groupBy()
    # 3. Aggregate counts fo all colders and groupBy "State" and "Color"
    # 4. orderBy() in descending order
    count_mnm_df = (mnm_df
        .select('State', 'Color', 'Count')
        .groubBy('State', 'Color')
        .sum('Count')
        .orderBy('sum(Count)', ascending=False))
    # 
    count_mnm_df.show(n=60, truncate=False)
    print(f'Total Rows = {count_mnm_df.count()}')
    #
    #
    ca_count_mnm_df = (mnm_df
        .select('State', 'Color', 'Count')
        .where(mnm_df.State == 'CA')
        .groupBy('State', 'Color')
        .sum('Count')
        .orderBy('sum(Count)', ascending=False))
    #
    ca_count_mnm_df.show(n=10, truncate=False)
    # Stop the SparkSession
    spark.stop()
    
