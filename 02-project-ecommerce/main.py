# import streamlit as st
# from pages.Home import app as home_app
# from pages.Product_List import app as product_list_app
# from pages.Cart import app as cart_app
# from pages.Checkout import app as checkout_app
# from pages.Order_History import app as order_history_app

# pages = {
#     "home": home_app,
#     "product_list": product_list_app,
#     "cart": cart_app,
#     "checkout": checkout_app,
#     "order_history": order_history_app,
# }

# query_params = st.query_params

# current_page = query_params.get("page", "home")

# if current_page not in pages:
#     st.error("Page not found!")
#     st.stop()

# pages[current_page]()

# st.sidebar.title("Navigation")

# st.sidebar.markdown("[Home](?page=home)")
# st.sidebar.markdown("[Product List](?page=product_list)")
# st.sidebar.markdown("[Cart](?page=cart)")
# st.sidebar.markdown("[Checkout](?page=checkout)")
# st.sidebar.markdown("[Order History](?page=order_history)")

# st.markdown("---")
# st.markdown(
#     "<div style='text-align: center; color: #888; font-size: 12px;'>"
#     "Built with ❤️ by Sohail</div>",
#     unsafe_allow_html=True,
# )


import streamlit as st

# Import page modules
from pages.Home import app as home_app
from pages.Product_List import app as product_list_app
from pages.Cart import app as cart_app
from pages.Checkout import app as checkout_app
from pages.Order_History import app as order_history_app

# Page selection
pages = {
    "Home": home_app,
    "Product List": product_list_app,
    "Cart": cart_app,
    "Checkout": checkout_app,
    "Order History": order_history_app,
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
pages[selection]()

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 12px;'>"
    "Built with ❤️ by Sohail</div>",
    unsafe_allow_html=True,
)