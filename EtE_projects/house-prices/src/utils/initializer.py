# Initialize spark context and session

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

def init_spark(app: str = "Exp_session"):
    """
    Creates spark session with given app name
    
    Args:
        app (str): Name of the session
    
    Returns:
        (sparkSession object , sparkContext Object)
    
    """
    conf = SparkConf().setAppName(app).setMaster("local")
    try:
        spark_context = SparkContext(conf=conf)
        spark_session = SparkSession(sparkContext=spark_context)
    except Exception as e:
        print("unable to create spark context/session error: \n", e)
        raise Exception("Spark initialization failed.")
    return spark_session, spark_context
    