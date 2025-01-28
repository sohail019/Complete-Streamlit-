import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="NSE Cogencies", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
/* Header container */
.header {
    border-bottom: 1px solid #ddd;
    # background-color: #fff;
    padding: 0.5rem 1rem;
}

/* Flex container */
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

/* Logo section */
.header-logo img {
    height: 32px;
    width: auto;
}

/* Navbar */
.nav-links {
    display: flex;
    gap: 1.5rem;
}

.nav-links a {
    text-decoration: none;
    font-weight: 500;
    color: #ff7f00; /* Orange for Home */
}

.nav-links a:hover {
    color: #555; /* Hover color */
}

.nav-links a:not(:first-child) {
    color: #666; /* Default gray for other links */
}

/* Search bar */
.search-bar {
    position: relative;
    width: 256px;
}

.search-bar input {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.market-info {
    text-align: right;
    margin-left: 1rem;
}

.market-info .price {
    font-size: 1.1rem;
    font-weight: bold;
}

.market-info .change {
    font-size: 0.9rem;
    color: green;
}

.stButton > button {
        background-color: #EEF2FF;
        color: #4B5563;
        border: none;
        padding: 0.375rem 1rem;
        border-radius: 0.375rem;
}
.stButton > button:hover {
        background-color: #DBEAFE;
}
.stButton > button:focus {
        background-color: #1E3A8A;
        color: white;
}

.metric-value {
        font-size: 2rem;
        font-weight: 600;
        color: #fffff;
}
.metric-label {
        font-size: 0.875rem;
        color: #6B7280;
}
.metric-date {
        font-size: 0.75rem;
        color: #fffff;
}
.metric-row {
        font-size: 0.875rem;
        color: #ffffff;
        margin: 0.5rem 0;
}

</style>
""", unsafe_allow_html=True)

# Header content
st.markdown("""
<div class="header">
    <div class="header-container">
        <!-- Logo -->
        <div class="header-logo">
            <a href="/">
                <img src="https://dipam.gov.in/resources/images/new/useful-links/nse-logo.png" alt="NSE Logo">
            </a>
        </div>
        <!-- Navbar -->
        <nav class="nav-links">
            <a href="/">Home</a>
            <a href="/screener">Screener</a>
            <a href="/compare">Compare</a>
            <a href="/learn">Learn about ETFs</a>
        </nav>
        <!-- Search and Market Info -->
        <div class="flex" style="display: flex; align-items: center;">
            <div class="search-bar" style="margin-right: 1rem;">
                <input type="text" placeholder="Type Issuer name or Symbol">
            </div>
            <div class="market-info">
                <div class="price">19,776.05</div>
                <div class="change">+5.10 (0.05%)</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sample data for Asset Types
months = ['Jan 24', 'Feb 24', 'Mar 24', 'Apr 24', 'May 24', 'Jun 24', 'Jul 24', 'Aug 24', 'Sep 24']
df = pd.DataFrame({
    'Month': months,
    'ETF': [150, 160, 155, 170, 180, 175, 190, 200, 210],
    'Index Fund': [100, 110, 105, 120, 130, 125, 140, 145, 150],
    'Equity': [200, 220, 210, 230, 250, 240, 260, 270, 300],
    'Debt': [100, 110, 105, 120, 115, 130, 140, 145, 150],
    'Commodity': [50, 55, 53, 60, 58, 62, 65, 70, 75],
})

st.header("Passive Funds Trends")

# Three-column layout
col1, col2, col3 = st.columns([2, 3, 4]) 

# First Column - Left Metrics
with col1:
    st.metric(label="Overall AUM", value="₹ 1,24,737.46 cr", delta="as on Sep 2024")

    st.markdown("##### Fund Type")
    c1, c2 = st.columns(2)
    c1.markdown("ETF:")
    c2.markdown("₹ 54,454 cr")
    c1.markdown("Index Fund:")
    c2.markdown("₹ 48,627 cr")
    

    st.markdown("##### Asset Type")
    c1, c2 = st.columns(2)
    c1.markdown("Equity:")
    c2.markdown("₹ 45,124 cr")
    c1.markdown("Debt:")
    c2.markdown("₹ 12,564 cr")
    c1.markdown("Commodity:")
    c2.markdown("₹ 8,497 cr")

    st.metric(label="Number of Funds", value="328", delta="as on Sep 2024")

# Helper function to create bar charts
def create_bar_chart(x, y, title, color):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x,
        y=y,
        marker_color=color,
        name=title
    ))
    fig.update_layout(
        title=title,
        plot_bgcolor="white",
        xaxis_title="Month",
        yaxis_title="Value",
        showlegend=False,
        height=400    
    )
    return fig

def create_pie_chart(labels, values, title):
    fig = px.pie(
        names=labels,
        values=values,
        title=title,
        hole=0.4
    )
    return fig

# Second Column - Fund Type Tabs
with col2:
    st.markdown("### Fund Type Trends")
    fund_type_tab = st.tabs(["All", "ETF", "Index Fund"])

    with fund_type_tab[0]:  
        col1, col2 = st.columns(2)
        with col1:
            fig_etf = create_bar_chart(df['Month'], df['ETF'], "ETF", "#34D399")
            st.plotly_chart(fig_etf, use_container_width=True, key="all_etf")
        # fig_etf = create_bar_chart(df['Month'], df['ETF'], "ETF", "#34D399")
        # st.plotly_chart(fig_etf, use_container_width=True, key="all_etf")

        with col2:
            fig_index = create_bar_chart(df['Month'], df['Index Fund'], "Index Fund", "#4F46E5")
            st.plotly_chart(fig_index, use_container_width=True, key="all_index")

        # fig_index = create_bar_chart(df['Month'], df['Index Fund'], "Index Fund", "#4F46E5")
        # st.plotly_chart(fig_index, use_container_width=True, key="all_index")

    with fund_type_tab[1]:  # ETF Tab
        fig_etf = create_bar_chart(df['Month'], df['ETF'], "ETF", "#34D399")
        st.plotly_chart(fig_etf, use_container_width=True, key="etf")

    with fund_type_tab[2]:  # Index Fund Tab
        fig_index = create_bar_chart(df['Month'], df['Index Fund'], "Index Fund", "#4F46E5")
        st.plotly_chart(fig_index, use_container_width=True, key="index_fund")

# Third Column - Asset Type Tabs
with col3:
    st.markdown("### Asset Type Trends")
    asset_type_tab = st.tabs(["All", "Equity", "Debt", "Commodity"])

    with asset_type_tab[0]:  # All Tab
        col1, col2, col3 = st.columns(3)
        with col1:
            fig_equity = create_bar_chart(df['Month'], df['Equity'], "Equity", "#34D399")
            st.plotly_chart(fig_equity, use_container_width=True, key="all_equity")
        with col2:
            fig_debt = create_bar_chart(df['Month'], df['Debt'], "Debt", "#4F46E5")
            st.plotly_chart(fig_debt, use_container_width=True, key="all_debt")
        with col3:
            fig_commodity = create_bar_chart(df['Month'], df['Commodity'], "Commodity", "#F59E0B")
            st.plotly_chart(fig_commodity, use_container_width=True, key="all_commodity")

    with asset_type_tab[1]:  # Equity Ta
        fig_equity = create_bar_chart(df['Month'], df['Equity'], "Equity", "#34D399")
        st.plotly_chart(fig_equity, use_container_width=True, key="equity")

    with asset_type_tab[2]:  # Debt Tab
        fig_debt = create_bar_chart(df['Month'], df['Debt'], "Debt", "#4F46E5")
        st.plotly_chart(fig_debt, use_container_width=True, key="debt")

    with asset_type_tab[3]:  # Commodity Tab
        fig_commodity = create_bar_chart(df['Month'], df['Commodity'], "Commodity", "#F59E0B")
        st.plotly_chart(fig_commodity, use_container_width=True, key="commodity")



# NET INFLOWS SECTION
st.markdown("<hr>", unsafe_allow_html=True)
net_inflows_data = {
    'Month': ['Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23'],
    'ETF': [1.2, 1.3, 1.2, 1.8, 1.4, 1.5, 1.6, 2.0, 2.2],
    'Index Fund': [1.0, 1.1, 1.0, 1.5, 1.2, 1.3, 1.4, 1.8, 2.0]
}
net_inflows_data_df = pd.DataFrame(net_inflows_data)

left_col, right_col = st.columns([1, 4])  # 1st column small, 2nd column large

# Left column - Metrics
with left_col:
    # st.markdown("### NET INFLOWS:")
    st.metric(label="Net Inflows", value="₹ 1,24,737.46 cr", delta="as on Sep 2023")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ETF and Index Fund metrics
    st.markdown("""
        <div class='metric-row'>
            <span style='display: inline-block; width: 12px; height: 12px; background-color: #FCD9BD; border-radius: 50%; margin-right: 8px;'></span>
            ETF: <span style='float: right'>₹ 54,454 cr</span>
        </div>
    """, unsafe_allow_html=True)
    
    
    st.markdown("""
        <div class='metric-row'>
            <span style='display: inline-block; width: 12px; height: 12px; background-color: #2563EB; border-radius: 50%; margin-right: 8px;'></span>
            Index Fund: <span style='float: right'>₹ 54,454 cr</span>
        </div>
    """, unsafe_allow_html=True)
    

# Right column - Double Stack Bar Chart
with right_col:
    fig = go.Figure()
    
    # Add Index Fund bars (bottom)
    fig.add_trace(go.Bar(
        x=net_inflows_data_df['Month'],
        y=net_inflows_data_df['Index Fund'],  # Ensure this column name is correct
        name='Index Fund',
        marker_color='#2563EB'
    ))
    
    # Add ETF bars (top)
    fig.add_trace(go.Bar(
        x=net_inflows_data_df['Month'],
        y=net_inflows_data_df['ETF'],
        name='ETF',
        marker_color='#FCD9BD'
    ))
    
    # Update layout
    fig.update_layout(
        barmode='stack',
        plot_bgcolor='white',
        height=400,
        margin=dict(l=40, r=40, t=20, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor='#E5E7EB'
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='#E5E7EB',
            zeroline=False,
            range=[0, 6]  # Set y-axis range from 0 to 6
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)