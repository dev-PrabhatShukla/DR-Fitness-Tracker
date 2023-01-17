import dash
from dash import dcc, html, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import dash_player

dash.register_page(__name__, path='/', name='Home')  # '/' is home page

# page 1 data
df = pd.read_csv('fitness_tracker.csv')
#df = px.data.gapminder()



layout = html.Div(
    [html.H3('Dataset Details :'),
    html.Br(),
    html.H6('This dataset contains 610 samples with 11 attributes.There are some missing values in this dataset. Here are the columns in this dataset-:'),
    html.P("1. Brand Name: This indicates the manufacturer of the product (fitness tracker)"),
    html.P("2. Device Type: This has two categories- FitnessBand and Smartwatch"),
    html.P("3. Model Name: This indicates the variant/Product Name"),
    html.P("4. Color: This includes the color of the Strap/Body of the fitness tracker"),
    html.P("5. Selling Price: This column has the Selling Price or the Discounted Price of the fitness tracker"),
    html.P("6. Original Price: This includes the Original Price of the product from the manufacturer."),
    html.P("7. Display: This categorical variable shows the type of display for the fitness tracker. eg: AMOLED, LCD,OLED, etc."),
    html.P("8. Rating (Out of 5): Average customer ratings on a scale of 5."),
    html.P("9. Strap Material: Details of the material used for the strap of the fitness tracker."),
    html.P("10. Average Battery Life (in days): Quoted average battery life from the manufacturer based on the individual product pages. (It is not the scraped data)"),
    html.P("11. Reviews: count of product reviews received."),
    html.Br(),
        html.Div(
            [
                html.Div(
                    style={"width": "48%", "padding": "0px"},
                    children=[
                        dash_player.DashPlayer(
                            id="player",
                            url="https://youtu.be/d5pb9TgCGc0",
                            controls=True,
                            width="100%",
                            height="250px",
                        ),
                        dcc.Checklist(
                            id="bool-props-radio",
                            options=[
                                {"label": val.capitalize(), "value": val}
                                for val in [
                                    "playing",
                                    "loop",
                                    "controls",
                                    "muted",
                                ]
                            ],
                            value=["controls"],
                            inline=True,
                            style={"margin": "20px 0px"},
                        ),
                        html.Div(
                            [
                                dcc.Input(
                                    id="seekto-number-input",
                                    type="number",
                                    placeholder="seekTo value",
                                    style={"width": "calc(100% - 115px)"},
                                ),
                                html.Button(
                                    "seekTo",
                                    id="seekto-number-btn",
                                    style={"width": "105px"},
                                ),
                            ],
                            style={"margin": "20px 0px"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    id="current-time-div",
                                    style={"margin": "10px 0px"},
                                ),
                                html.Div(
                                    id="seconds-loaded-div",
                                    style={"margin": "10px 0px"},
                                ),
                                html.Div(
                                    id="duration-div",
                                    style={"margin": "10px 0px"},
                                ),
                            ],
                            style={
                                "display": "flex",
                                "flex-direction": "column",
                            },
                        ),
                    ],
                ),
                html.Div(
                    style={"width": "48%", "padding": "10px"},
                    children=[
                        html.P("Volume:", style={"marginTop": "30px"}),
                        dcc.Slider(
                            id="volume-slider",
                            min=0,
                            max=1,
                            step=0.05,
                            value=0.5,
                            updatemode="drag",
                            marks={0: "0%", 0.5: "50%", 1: "100%"},
                        ),
                        html.P("Playback Rate:", style={"marginTop": "25px"}),
                        dcc.Slider(
                            id="playback-rate-slider",
                            min=0,
                            max=2,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) + "x" for i in [0, 0.5, 1, 1.5, 2]},
                            value=1,
                        ),
                        html.P(
                            "Update Interval for Current Time:",
                            style={"marginTop": "30px"},
                        ),
                        dcc.Slider(
                            id="intervalCurrentTime-slider",
                            min=0,
                            max=1000,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) for i in [0, 250, 500, 750, 1000]},
                            value=250,
                        ),
                        html.P(
                            "Update Interval for Seconds Loaded:",
                            style={"marginTop": "30px"},
                        ),
                        dcc.Slider(
                            id="intervalSecondsLoaded-slider",
                            min=0,
                            max=1000,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) for i in [0, 250, 500, 750, 1000]},
                            value=500,
                        ),
                        html.P(
                            "Update Interval for Duration:",
                            style={"marginTop": "30px"},
                        ),
                        dcc.Slider(
                            id="intervalDuration-slider",
                            min=0,
                            max=1000,
                            step=None,
                            updatemode="drag",
                            marks={i: str(i) for i in [0, 250, 500, 750, 1000]},
                            value=500,
                        ),
                    ],
                ),
            ],
            style={
                "display": "flex",
                "flexDirection": "row",
                "justifyContent": "space-between",
            },
        ),
    ]
)


@callback(
    Output("player", "playing"),
    Output("player", "loop"),
    Output("player", "controls"),
    Output("player", "muted"),
    Input("bool-props-radio", "value"),
)
def update_bool_props(values):
    playing = "playing" in values
    loop = "loop" in values
    controls = "controls" in values
    muted = "muted" in values
    return playing, loop, controls, muted


@callback(
    Output("player", "seekTo"),
    Input("seekto-number-btn", "n_clicks"),
    Input("seekto-number-input", "value"), #Here I update Input in place of State
)
def set_prop_seekTo(n_clicks, seekto):
    return seekto


@callback(
    Output("current-time-div", "children"),
    Input("player", "currentTime"),
)
def display_currentTime(currentTime):
    return f"Current Time: {currentTime}"


@callback(
    Output("seconds-loaded-div", "children"),
    Input("player", "secondsLoaded"),
)
def display_secondsLoaded(secondsLoaded):
    return f"Second Loaded: {secondsLoaded}"


@callback(
    Output("duration-div", "children"),
    Input("player", "duration"),
)
def display_duration(duration):
    return f"Duration: {duration}"


@callback(
    Output("player", "volume"),
    Input("volume-slider", "value"),
)
def set_volume(value):
    return value


@callback(
    Output("player", "playbackRate"),
    Input("playback-rate-slider", "value"),
)
def set_playbackRate(value):
    return value


@callback(
    Output("player", "intervalCurrentTime"),
    Input("intervalCurrentTime-slider", "value"),
)
def set_intervalCurrentTime(value):
    return value


@callback(
    Output("player", "intervalSecondsLoaded"),
    Input("intervalSecondsLoaded-slider", "value"),
)
def set_intervalSecondsLoaded(value):
    return value


@callback(
    Output("player", "intervalDuration"),
    Input("intervalDuration-slider", "value"),
)
def set_intervalDuration(value):
    return value