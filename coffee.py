import pandas as pd
import plotly.express as px
import csv 
import numpy as np

"""df=pd.read_csv("coffee.csv")
fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
fig.show()"""

def getDataSource(data_path):
    sleep=[]
    coffee=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between coffee and sleep", correlation[0,1])

def setUp():
    data_path="coffee.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setUp()