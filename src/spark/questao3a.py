from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

spark = SparkSession.builder.appName("MeanDailySales").getOrCreate()

sales_path = "data/vendas.csv"

df_sales = spark.read.csv(sales_path, header=True, inferSchema=True)

mean_daily_sales = (df_sales.groupBy("data_venda")
        .agg(avg("valor_venda").alias("valor_medio_venda"))
        .orderBy(col("data_venda"))
    )

mean_daily_sales.show()
spark.stop()