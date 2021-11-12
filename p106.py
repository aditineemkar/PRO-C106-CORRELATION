import plotly_express as px
import csv
import numpy as np

data = open("Days_Marks.csv")
df = csv.DictReader(data)
p = px.scatter(df, x="Days Present", y="Marks In Percentage")
p.show()
def get_data_source(data_path):
    Days_Present =[]
    Percentage=[]

    with open(data_path) as f:
        data = csv.DictReader(f)
        for i in data:
            Days_Present.append(float(i["Days Present"]))
            Percentage.append(float(i["Marks In Percentage"]))
        
        return {"x":Days_Present, "y": Percentage}

def correlation(dataSource):
    correlation_data = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation_data[0, 1])

def setup():
    data_path="Days_Marks.csv"
    data_source = get_data_source(data_path)
    correlation(data_source)

setup()
