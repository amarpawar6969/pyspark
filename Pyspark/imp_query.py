from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.getOrCreate()
# ====================================================================================================
df1 = spark.read.format('CSV').option('header', True).option('inferSchema', True).load('employee.csv')

# ====================================================================================================
# -- find diff between highest salary and second highest salary
df2 = df1.groupBy("DEPARTMENT").agg(max("SALARY").alias('salary'))
win = Window.partitionBy("DEPARTMENT").orderBy(col('SALARY').desc())
df3 = df1.select("SALARY","DEPARTMENT",dense_rank().over(win).alias('rn')).where(col('rn') == 2)
df4 = df3.join(df2, df3.DEPARTMENT == df2.DEPARTMENT, 'inner').\
    select(df3.DEPARTMENT, (df2.salary-df3.SALARY).alias('diff')).distinct()
df4.show()

