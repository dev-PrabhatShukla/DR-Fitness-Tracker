import dash
from dash import Dash, dash_table, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px

dash.register_page(__name__, name='Top Brands')
#------------------------------------------------------------------------

df = pd.read_csv('fitness_tracker.csv')

dataframe = df['Brand Name'].groupby(df['Brand Name']).count().sort_values(ascending=False).iloc[:5]  #['Brand Name'].groupby(df['Brand Name'])


fig = px.pie(df, names="Brand Name", color="Brand Name", values='Number_Of_Tracker', template='presentation', width=800, height=600, hole=0.5,
title="Players (Brands) present in the market (in percent)", color_discrete_sequence=["red","green","blue","orange", "yellow", "pink", "purple"])

dfig = px.pie(dataframe, names="Brand Name", color="Brand Name", values='Brand Name', template='presentation', width=800, height=600,
title="Top five Players (Brands) present in the market (in percent)", color_discrete_sequence=["red","green","blue","orange", "yellow"])

layout = html.Div([
    dcc.Graph(figure=fig),
    html.Br(),
    html.H6("On above we seeing that there are multiple (25) brands present who captured the market. Now we will check the top five big players (brands) among all"),
    html.Br(),
    dcc.Graph(figure=dfig),
    html.H6("By the medium of visualization above, we understand and can say that who are top five players captured the market"),
    html.H5("Brand Name  ------  Number of Trackers"),
    html.H6("FOSSIL  ------  133"),
    html.H6("GARMIN  ------  101"),
    html.H6("APPLE  ------  86"),
    html.H6("FitBit  ------  51"),
    html.H6("SAMSUNG  ------  48"),
])
