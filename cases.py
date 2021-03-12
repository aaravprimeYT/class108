import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("Project 103.csv")

caseList = df["cases"].tolist()

fig = ff.create_distplot([caseList],["Cases"],show_hist=False)
fig.show()