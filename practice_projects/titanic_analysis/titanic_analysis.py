import pandas as pd
import numpy as np
data = pd.read_csv(r"C:\Users\Namratha Kilari\Downloads\data-analysis-roadmap\practice_projects\titanic_analysis\titanic.csv")
print(data.info())
data["Age"]=data["Age"].fillna(data["Age"].mean())

data["Sex"]=data["Sex"].map({"Male":0,"Female":1})
print(data.info())
