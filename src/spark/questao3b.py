from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, desc

spark = SparkSession.builder.appName("BiggestRevenueCategory").getOrCreate()

sales_path = "data/vendas.csv"
products_path = "data/produtos.csv"
clients_path = "data/clientes.csv"

df_sales = spark.read.csv(sales_path, header=True, inferSchema=True)
df_products = spark.read.csv(products_path, header=True, inferSchema=True)
df_clients = spark.read.csv(clients_path, header=True, inferSchema=True)

# join both dataframes in order to obey the question command (use all three tables)
df_products_sales = df_sales.join(df_products, "id_produto")
df_complete = df_products_sales.join(df_clients, "id_cliente")

revenue_by_category = (df_complete
                        .groupBy("categoria")
                        .agg(sum("valor_venda")
                        .alias("receita_total"))
                        .orderBy(desc("receita_total"))
                     )

# category with best sales
revenue_by_category.show(1)
spark.stop()