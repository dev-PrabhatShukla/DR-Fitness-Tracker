import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import dash_player as dp
#from pymongo import MongoClient
#import pymongo
import csv
'''
client = pymongo.MongoClient("mongodb+srv://Pracoderma:<lkoprabhat>@cluster0.fat7khj.mongodb.net/?retryWrites=true&w=majority")
db = client["Fitness_Tracker"]
#print(db)
#exit()
header = ["Brand Name", "Device Type", "Model Name","Color","Selling Price","Original Price","Display","Rating (Out of 5)","Strap Material","Average Battery Life (in days)","Reviews","Number_Of_Tracker","Most_Used_In_Countries"]
collect_record = db["fitness_trackers"]

record = pd.read_csv('fitness_tracker.csv')
reader = csv.DictReader(record)

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
        
    print(row)
    collect_record.insert(row)

collect_record.insert_one(reader)
'''

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("DR Fitness Tracker Visualization Report",
                         style={'fontSize':50, 'textAlign':'center'}))
    ]),

    # html.Hr(),

    dbc.Row(
        [
        dbc.Col([
            dbc.Carousel(
                items=[
                    {"key": "1", "src": "/assets/2.jfif", "caption":"DR Fitness Tracker Data Visualization", "img_style":{"max-height":"350px"}},
                    {"key": "1", "src": "/assets/4.jpg", "caption":"DR Fitness Tracker Data Visualization", "img_style":{"max-height":"350px"}},
                    {"key": "1", "src": "/assets/3.jpg", "caption":"DR Fitness Tracker Data Visualization", "img_style":{"max-height":"350px"}},
                ],
                controls=True,
                indicators=True,
                interval=2000,
                ride="carousel",
#                 className="carousel-fade"
            )
        ], width=8)
    ], justify="center"),
    html.Br(),

    dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        dash.page_container
                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ], fluid=True)
    

if __name__ == "__main__":
    app.run(debug=True)