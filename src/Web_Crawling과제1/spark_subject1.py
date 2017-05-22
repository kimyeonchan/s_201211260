import os
import sys 
import matplotlib.pyplot as plt

os.environ["SPARK_HOME"]="C:\Users\poqi7\Desktop\spark-2.0.0-bin-hadoop2.7"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))
import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).getOrCreate()
myRdd2=spark.sparkContext.textFile(os.path.join("data","data.txt"))
wc=myRdd2.flatMap(lambda x:x.split()).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).map(lambda x:(x[1],x[0])).sortByKey(False).take(100)
for e in wc:
    print e

    
count = map(lambda x: x[0], wc)
word = map(lambda x: x[1], wc)
plt.figure(figsize=(5, 18))
plt.barh(range(len(count)), count, color = 'grey')
plt.yticks(range(len(count)), word)
plt.show()