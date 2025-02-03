import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
from sklearn.datasets import load_wine

dash.register_page(__name__, path='/relationship', name="Relationship 📈", order=3)

####################### DATASET #############################
wine = load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

####################### SCATTER CHART #############################
def create_scatter_chart(x_axis, y_axis):
    fig = px.scatter(data_frame=wine_df, x=x_axis, y=y_axis, color="WineType", height=600)
    fig.update_traces(marker={"size":15, "opacity": 0.85, "line":{"width": 2, "color": "black"}})
    fig.update_layout(paper_bgcolor="#e5ecf6", margin={"t":0})
    return fig

####################### WIDGETS #############################
x_axis = dcc.Dropdown(id="x_axis", options=wine.feature_names, value="alcohol", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=wine.feature_names, value="malic_acid", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Explore Relationship between Features", className="fw-bold text-center"),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    html.Br(),
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)

