import random
import plotly.express as px
import plotly.figure_factory as ff 
import pandas as pd
import csv

df = pd.read_csv('data.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()],['Average Rating'],show_hist = False)
fig.show()
