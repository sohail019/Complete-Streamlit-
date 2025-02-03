import pandas as pd
import dash
from dash import html, dcc
import plotly.graph_objects as go
from sklearn.datasets import load_wine

dash.register_page(__name__, path='/dataset', name="Dataset 📋", order=1)

####################### LOAD DATASET #############################
wine = load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

def create_table():
    fig = go.Figure(data=[go.Table(
        header=dict(values=wine.feature_names + ["WineType", ], align='left'),
        cells=dict(values=wine_df.values.T, align='left'))
    ])
    fig.update_layout(paper_bgcolor="#e5ecf6", margin={"t":0, "l":0, "r":0, "b":0})
    return fig

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Dataset Explorer", className="fw-bold text-center"),
    dcc.Graph(id="dataset", figure=create_table()),
])