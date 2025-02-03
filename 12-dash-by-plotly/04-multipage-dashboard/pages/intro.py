import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction 😃", order=0)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Wine Dataset Overview"),
        "The data is the results of a chemical analysis of wines grown in the same region in Italy by three different cultivators. There are thirteen different measurements taken for different constituents found in the three types of wine.",
        html.Br(),html.Br(),
        "This is a copy of UCI ML Wine recognition datasets. (https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)",
        ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        "Number of Instances: 178",html.Br(),
        "Number of Attributes: 13 numeric, predictive attributes and the class",
        html.Br(),html.Br(),
        html.B("- Alcohol"),
        html.Br(),
        html.B("- Malic acid"),
        html.Br(),
        html.B("- Ash"),
        html.Br(),
        html.B("- Alcalinity of ash"),
        html.Br(),
        html.B("- Magnesium"),
        html.Br(),
        html.B("- Total phenols"),
        html.Br(),
        html.B("- Flavanoids"),
        html.Br(),
        html.B("- Nonflavanoid phenols"),
        html.Br(),
        html.B("- Proanthocyanins"),
        html.Br(),
        html.B("- Color intensity"),
        html.Br(),
        html.B("- Hue"),
        html.Br(),
        html.B("- OD280/OD315 of diluted wines"),
        html.Br(),
        html.B("- Proline"),
        html.Br(),html.Br(),
        html.B("Class"),
        html.Br(),html.Br(),
        html.B("- class_0"), html.Br(),
        html.B("- class_1"), html.Br(),
        html.B("- class_2"),
    ])
], className="p-4 m-2", style={"background-color": "#e3f2fd"})