from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors
import pandas as pd
import pyspark
from pyspark.SQL import SQLContext
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)
if __name__ == "__main__":
    print("Success!")

