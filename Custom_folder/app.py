from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyApp").getOrCreate()

df = spark.read.option("multiline", "true").json("logs.json")
df.printSchema()
df.where("age > 21").select("name.first").show()