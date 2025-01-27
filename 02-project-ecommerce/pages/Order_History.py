import streamlit as st

def app():
    st.title("Order History")

    if "orders" not in st.session_state or len(st.session_state.orders) == 0:
        st.info("No orders have been placed yet.")
        return

    for i, order in enumerate(st.session_state.orders, start=1):
        st.markdown(f"### Order {i}")
        st.write(f"**Name:** {order['name']}")
        st.write(f"**Email:** {order['email']}")
        st.write(f"**Address:** {order['address']}")
        st.write("**Items:**")
        for item in order["items"]:
            st.write(f"- {item['title']} (${item['price']})")
        st.markdown(f"**Total:** ${order['total']:.2f}")
        st.markdown("---")
