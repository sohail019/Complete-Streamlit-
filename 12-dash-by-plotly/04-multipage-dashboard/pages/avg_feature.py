import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sklearn.datasets import load_wine

dash.register_page(__name__, path='/avg-feature', name="Avg Feature 📊", order=4)

####################### DATASET #############################
wine = load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

####################### BAR CHART #############################
def create_bar_chart(col_name):
    fig =  px.histogram(data_frame=wine_df, y=col_name, x="WineType", color="WineType",
                        histfunc="avg", height=600)
    fig.update_traces(marker={"line":{"width": 2, "color": "black"}})
    fig = fig.update_layout(bargap=0.7, paper_bgcolor="#e5ecf6", margin={"t":0})
    return fig

####################### WIDGETS ################################
dd = dcc.Dropdown(id="sel_col", options=wine.feature_names, value="malic_acid", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Explore Avg Feature Values per Wine Type", className="fw-bold text-center"),
    dd, 
    html.Br(),
    dcc.Graph(id="bar_chart")
])

####################### CALLBACKS ################################
@callback(Output("bar_chart", "figure"), [Input("sel_col", "value"), ])
def update_bar_chart(sel_col):
    return create_bar_chart(sel_col)

