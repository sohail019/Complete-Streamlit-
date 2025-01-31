import streamlit as st
from streamlit_option_menu import option_menu

import about, account, home, trending, your_posts

st.set_page_config(page_title="Multi page app", page_icon=":earth_americas:", layout="wide")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:        
            app = option_menu(
                menu_title='Multipage App ',
                options=['Home','Account','Trending','Your Posts']
            )
        if app == 'Home':
            home.app()
        elif app == 'Account':
            account.app()
        elif app == 'Trending':
            trending.app()
        elif app == 'Your Posts':
            your_posts.app()

# Create an instance of MultiApp
app = MultiApp()

# Add your apps
app.add_app("Home", home.app)
app.add_app("Account", account.app)
app.add_app("Trending", trending.app)
app.add_app("Your Posts", your_posts.app)

# Run the app
app.run()