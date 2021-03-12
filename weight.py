import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics

df = pd.read_csv("class108.csv")

weightList = df["Weight(Pounds)"].tolist()

mean = statistics.mean(weightList)
median = statistics.median(weightList)
mode = statistics.mode(weightList)

print(mean,median,mode)

fig = ff.create_distplot([weightList],["Weight"],show_hist=False)
fig.show()