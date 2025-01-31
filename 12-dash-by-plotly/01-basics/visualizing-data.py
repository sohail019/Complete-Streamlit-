
#* The plotly graphing library has more than 50 chart types. we will use histogram chart

from dash import Dash, html, dash_table, dcc
#? import dcc (Dash core components) module, it includes a Graph component called dcc.Graph, which is used to render graphs 
import pandas as pd
import plotly.express as px #? to build interactive graphs

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the Dash app
app = Dash()

# App layout
app.layout = [html.Div(children="Visualize the Data and a Graph"),
              dash_table.DataTable(data=df.to_dict('records'), page_size=10),
              dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc='avg'))]

# Run the app
if __name__ == "__main__":
    app.run(debug=True)