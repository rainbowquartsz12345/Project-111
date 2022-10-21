import pandas as pd
import plotly.figure_factory as ff
import statistics as st

df = pd.read_csv("article_data.csv")
article = df["reading_time"].tolist()

fig = ff.create_distplot([article], ["Reading Time"], show_hist = False)
fig.show()