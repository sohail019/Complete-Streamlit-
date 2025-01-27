import streamlit as st

def app():
    st.title("Checkout")

    if "orders" not in st.session_state:
        st.session_state.orders = []

    if "cart" not in st.session_state or len(st.session_state.cart) == 0:
        st.warning("Your cart is empty. Add items to your cart before checking out.")
        return

    total_price = 0
    st.markdown("### Order Summary:")
    for item in st.session_state.cart:
        st.write(f"- {item['title']} (${item['price']})")
        total_price += item["price"]
    st.markdown(f"**Total: ${total_price:.2f}**")

    st.markdown("### Shipping Information:")
    with st.form("checkout_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        address = st.text_area("Shipping Address")
        submit = st.form_submit_button("Place Order")

        if submit:
            if name and email and address:
                order = {
                    "name": name,
                    "email": email,
                    "address": address,
                    "items": st.session_state.cart,
                    "total": total_price,
                }
                st.session_state.orders.append(order)
                st.session_state.cart.clear()
                st.success("Order placed successfully! 🎉")
            else:
                st.error("Please fill in all the details.")
