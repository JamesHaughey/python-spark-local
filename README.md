[java-8-link]: https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
[spark-link]:  https://spark.apache.org/downloads.html
[win-utils-link]: https://github.com/jleetutorial/sparkTutorial/blob/winutils/winutils.exe


# python-spark-local 


## Installation & Requirements
- Java 8 from [Oracle Java Downloads][java-8-link] - follow installation instructions
- Apache Spark from [Apache Spark Downloads][spark-link] - unzip into `C:\spark\`
- winutils.exe from [jLeeTutorial Github][win-utils-link] - save into `C:\hadoop\bin\`
- add `SPARK_HOME` & `HADOOP_HOME` as env vars with values of `C:\spark\` & `C:\hadoop\` respectively
- add `%SPARK_HOME%\bin` & `%HADOOP_HOME%\bin` to the path
- create a new folder `C:\tmp\hive`
- Open a new terminal and exectute `winutils chmod 777 C:\tmp\hive` so that hadoop has access to this folder
- add `PYSPARK_DRIVER_PYTHON` : `jupyter` & `PYSPARK_DRIVER_PYTHON_OPTS` : `lab` as environment vars
- run pyspark in the terminal to test
---

Optional - turn down log message level to ERROR only to reduce log noise.

- go to `%SPARK_HOME%/conf`, take a copy of `log4j.properties.template` and rename it to just `log4j.properties`
- edit `log4j.properties` change `log4j.rootCategory=INFO, console` to `log4j.rootCategory=ERROR, console`




