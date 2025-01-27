import streamlit as st
import requests

def app():
    st.title("Product List")

    if "cart" not in st.session_state:
        st.session_state.cart = []

    API_URL = "https://fakestoreapi.com/products"
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        products = response.json()

        for product in products:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(product["image"], width=120)
            with col2:
                st.subheader(product["title"])
                st.write(f"Price: ${product['price']}")
                st.write(product["description"])
                if st.button(f"Add {product['title']} to Cart", key=product["id"]):
                    st.session_state.cart.append(product)
                    st.success(f"Added {product['title']} to the cart!")
            st.markdown("---")

    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch products: {e}")
