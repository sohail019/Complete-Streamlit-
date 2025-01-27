import streamlit as st

def app():
    st.title("Shopping Cart")

    if "cart" not in st.session_state or len(st.session_state.cart) == 0:
        st.write("Your cart is empty.")
    else:
        total_price = 0
        for item in st.session_state.cart:
            st.subheader(item["title"])
            st.image(item["image"], width=100)
            st.write(f"Price: ${item['price']}")
            total_price += item["price"]

        st.markdown(f"### Total: ${total_price:.2f}")
