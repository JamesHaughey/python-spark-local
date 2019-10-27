import os
from connections import connect

if __name__ == "__main__":
    context = connect.ps_connection("word count", "ERROR", 3)
    
    file_path = f"{os.environ['PROJECT_HOME']}/python-spark-tutorial/in/word_count.text"
    print(file_path)
    lines = context.sc.textFile(file_path)
    
    words = lines.flatMap(lambda line: line.split(" "))
    
    wordCounts = words.countByValue()
    
    for word, count in wordCounts.items():
        print("{} : {}".format(word, count))