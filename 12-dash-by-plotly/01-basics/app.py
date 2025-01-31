# * Import packages
from dash import Dash, html
#? when creating dash apps, we always use the import statement above, for more advanced dash apps, we will import more packages

#* Initialize the Dash app

app = Dash() #? this is Dash constructor, it creates a new Dash app instance

#* App layout
app.layout = [html.Div(children='Hello Dash')] #? this is the layout of the app, it is a list of components that will be rendered on the page

#* Run the app
if __name__ == '__main__':
    app.run(debug=True) #? this runs the app, the debug=True argument is optional, it is used to enable debug mode


