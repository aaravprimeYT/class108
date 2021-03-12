import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics


df = pd.read_csv("class108.csv")

heightList = df["Height(Inches)"].tolist()

mean = statistics.mean(heightList)
median = statistics.median(heightList)
mode = statistics.mode(heightList)

print(mean,median,mode)

fig = ff.create_distplot([heightList],["Height"],show_hist=False)
fig.show()