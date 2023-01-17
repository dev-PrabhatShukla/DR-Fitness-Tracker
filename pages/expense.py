import dash
from dash import Dash, dash_table, dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
#import plotly.graph_objs as go

dash.register_page(__name__, name='Expensiveness')
#------------------------------------------------------------------------

df = pd.read_csv('fitness_tracker.csv')

list = ["APPLE","OnePlus","FOSSIL ","SAMSUNG","Honor","FitBit","Xiaomi","Huawei","huami","realme"]
series = df["Brand Name"].isin(list)
df_f = df[series]

fig = px.scatter(df_f, x="Rating (Out of 5)", y="Selling Price",
                 size="Number_Of_Tracker", color="Brand Name", hover_name="Brand Name",
                 log_x=True, size_max=60)


data={"Brand Name":["GARMIN","huami","Oppo","Xiaomi","SAMSUNG","Honor","Huawei","realme","OnePlus","boAt","Noise","GOQii","LAVA","FitBit","LCARE","Fastrack","FOSSIL","Noise","Infinix","APPLE"],
      "Avg Battery Life":[17.0,16.0,14.0,12.0,12.0,12.0,11.0,10.0,9.0,8.0,7.0,7.0,7.0,7.0,6.0,6.0,5.0,5.0,4.0,1.0]}
df_batt=pd.DataFrame(data)
fig1 = px.scatter(df_batt, x="Brand Name", y="Avg Battery Life", color='Brand Name')

#Most expensive brand
fig2 = px.scatter(df, x="Brand Name", y="Selling Price", color='Brand Name')


layout = html.Div([
    html.Br(),
    html.H5("Let's analyse the cost of fitness tracker in different-different cases :"),
    html.Br(),
    html.H6("Let's check first, Are fitness trackers with higher ratings more expensive?"),
    dcc.Graph(id='life-exp-vs-gdp', figure=fig),
    html.H6("As we seeing above expensive brands seem to enjoy a higher rating."),
    html.Br(),
    html.H6("Now let's see that do expensive fitness trackers have a better battery performance"),
    dcc.Graph(figure=fig1),
    html.Br(),
    html.Br(),
    html.H6("Garmin seems to provide the best battery life in days as an expensive brand. Samsung on the other hand gives around 12 days of battery life, a week lesser than Garmin. Most Apple products provide only a 1-2 days battery life. Similarly, Fossil even though expensive brand but offers a very low battery life of lesser than a week."),
    html.Br(),
    html.Br(),
    html.P("Both Garmin and Fossil brands are expensive but do not have comparable battery life. Hence, expensive does not always equal to better battery life for the fitness tracker."),
    html.Br(),
    html.H6("Now let's check the most expensive brand among all other brands"),
    html.Br(),
    dcc.Graph(figure=fig2),
    html.Br(),
    html.H6("1. Average Price of tracker from Apple is around 50K INR while average price for Garmin trackers is around 35K INR. Fitness Trackers from Samsung are priced at an average of 22K INR."),
    html.H6("2. Products from Apple are the most expensive while FitBit seems to offering the maximum number of mid price range products.")
])