from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession


class ps_connection(object):
    def __init__(self, app_name, log_level, cores):
        self._app_name = app_name
        self._log_level = log_level
        self._cores = cores
        self._conf = SparkConf().setAppName(self._app_name).setMaster(f"local[{self._cores}]")
        self.sc = SparkContext.getOrCreate(conf=self._conf)
        self.sc.setLogLevel(self._log_level)
    
    def __repr__(self):
        return f"ps_connection(app_name = '{self._app_name}', log_level = '{self._log_level}', cores= {self._cores})"