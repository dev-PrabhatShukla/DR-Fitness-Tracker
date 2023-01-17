import dash
from dash import Dash, dash_table, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px

dash.register_page(__name__, name='Color & Strap')

df = pd.read_csv('fitness_tracker.csv')
'''
list = ["Black","Blue","Silver ","Grey","Gold"]
series = df["Color"].isin(list)
df_f = df[series]
'''
fig = px.histogram(df, x="Color", y="Number_Of_Tracker",color="Device Type", hover_name="Brand Name", title="Most Common Colors Available For The Trackers")

fig1 = px.pie(df, names="Strap Material", color="Brand Name", values='Number_Of_Tracker', template='presentation', width=800, height=600, hole=0.5,
title="Most Common Available Strap Material For Trackers", color_discrete_sequence=["red","green","blue","orange", "yellow", "pink", "purple"])

layout = html.Div([
    html.Br(),
    html.H5("Let's see the most commonly colors available for trackers :"),
    html.Br(),
    dcc.Graph(figure=fig),
    html.Br(),
    html.H6("Here we see above that red seems to be the most offered color in both Smart watches and fitness bands."),
    html.Br(),
    html.H5("Let's also see the most commonly available strap material for trackers :"),
    html.Br(),
    dcc.Graph(figure=fig1),
    html.Br(),
    html.H6("Silicone and Elastomer seem to be the most common choices for Fitness Bands while Silicone, Stainless Steel, Leather and Aluminium seem to be the top choices for Smart Watches.")
])