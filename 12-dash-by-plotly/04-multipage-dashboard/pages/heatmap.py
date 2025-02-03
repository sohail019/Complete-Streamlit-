import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from sklearn.datasets import load_wine

dash.register_page(__name__, path='/heatmap', name="Correlation 📊", order=5)

####################### DATASET #############################
wine = load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df["WineType"] = [wine.target_names[t] for t in wine.target]

####################### BAR CHART #############################
def create_heatmap():
    wine_corr = wine_df.corr(numeric_only=True)
    fig =  px.imshow(wine_corr, height=600, color_continuous_scale="RdBu")
    fig = fig.update_layout(paper_bgcolor="#e5ecf6", margin={"t":0})
    return fig

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("Features Correlation Heatmap", className="fw-bold text-center"),
    dcc.Graph(id="heatmap", figure=create_heatmap())
])

