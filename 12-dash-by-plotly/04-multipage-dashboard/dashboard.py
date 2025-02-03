from dash import Dash, html, dcc
import dash

external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

app = Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css)

img_tag = html.Img(src="assets/cc.png", width=27, className="m-1")
brand_link = dcc.Link([img_tag, "  CoderzColumn "], href="#", className="navbar-brand")
pages_links = [dcc.Link(page['name'], href=page["relative_path"], className="nav-link")\
	         for page in dash.page_registry.values()]

app.layout = html.Div([
	### Navbar
    html.Nav(children=[
	    html.Div([
			    html.Div([brand_link, ] + pages_links, className="navbar-nav")
        ], className="container-fluid"),
    ], className="navbar navbar-expand-lg bg-dark", **{"data-bs-theme": "dark"}),
    #### Main Page
    html.Div([
	    html.Br(),
	    html.P('Multi-Page Dash-Plotly Web App', className="text-dark text-center fw-bold fs-1"),
	    dash.page_container
	], className="col-6 mx-auto")
], style={"height": "100vh", "background-color": "#e3f2fd"})

if __name__ == '__main__':
	app.run(debug=True)
	