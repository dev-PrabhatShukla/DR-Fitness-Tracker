# Number of players in the market
# Which brand has highest number of products?

import dash
from dash import Dash, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc



dash.register_page(__name__, name='Brand Demand')  

df = pd.read_csv('fitness_tracker.csv')
layout = html.Div([
    html.H1('Demand For Fitness Trackers'),
    html.H6(['This dashboard shows the demand for fitness tracker :',
            html.Br(),
            html.A('Demand For Fitness Trackers Data Source', href='https://www.statista.com/topics/4393/fitness-and-activity-tracker/#topicOverview', target='_blank')]),
    html.Br(),

    dcc.Graph(figure=px.histogram(df, x='Device Type', y='Number_Of_Tracker', color='Device Type', range_y=[0,600], color_discrete_map={'FitnessBand': 'blue', 'Smartwatch': 'red'})),
    html.H6("There are two types of devices here : There is total 533 Smart Watches & 77 Fitness Bands."),
    dcc.Graph(figure=px.histogram(df, x='Brand Name', y='Number_Of_Tracker', color='Brand Name', range_y=[0,200])),
    html.H6("533 smartwatches and 77 fitnessbands from 25 different brands indicate that there is a good demand for Fitness Trackers in the current scenario."),
    html.H6("Now let's check the top 5 brands for fitness bands and smart watches :") 
])
