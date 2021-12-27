import pandas as pd

# data input
data = pd.read_csv("data_frame.csv", delimiter=";").iloc[ : , 0:2 ]

# variable name
name_index = "index_date"
name_variable = "variable1"

#rename columns
data.columns=[name_index, name_variable]

data.to_csv("data_frame2.csv", index=False, sep =",")
