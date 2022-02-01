import pandas as pd
import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    days_present=[]
    marks=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x":days_present,"y":marks}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between marks and days_present", correlation[0,1])

def setUp():
    data_path="student.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setUp()