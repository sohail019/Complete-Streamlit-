# * Import packages
from dash import Dash, html, dash_table
#? when creating dash apps, we always use the import statement above, for more advanced dash apps, we will import more packages
import pandas as pd

#* Connecting to Data
#? There are many ways to add data: APIs, databases, local .txt files, JSON files, and more. here we will use CSV sheet

#* Load data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

#* Initialize the Dash app
app = Dash() #? this is Dash constructor, it creates a new Dash app instance

#* App layout
app.layout = [html.Div(children='Hello Dash'),
              dash_table.DataTable(data=df.to_dict('records'), page_size=10)] #? this is the layout of the app, it is a list of components that will be rendered on the page

#* Run the app
if __name__ == '__main__':
    app.run(debug=True) #? this runs the app, the debug=True argument is optional, it is used to enable debug mode


