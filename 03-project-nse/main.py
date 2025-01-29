import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import re

# Set page configuration
st.set_page_config(page_title="NSE Cogencies", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
/* Header container */
.header {
    border-bottom: 1px solid #ddd;
    background-color: #fff;
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

.section-title{
    font-size: 1.5rem;
    font-weight: 600;
    color: #363F72;
    margin: 1rem 0;
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

.stTabs [data-baseweb="tab-list"] {
        gap: 8px;
}
.stTabs [data-baseweb="tab"] {
        height: 32px;
        padding: 0px 16px;
        background-color: #EEF2FF;
        color: #4B5563;
        border-radius: 4px;
}
.stTabs [aria-selected="true"] {
        background-color: #1E3A8A !important;
        color: white !important;
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
            <div class="search-bar" style="margin-right: 1rem; position: relative;">
                <img src="https://img.icons8.com/ios-filled/50/000000/search.png" alt="Search" style="position: absolute; right: 10px; top: 50%; transform: translateY(-50%); height: 16px;">
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
    'ETF': [200, 160, 155, 170, 180, 175, 190, 200, 210],
    'Index Fund': [100, 110, 105, 120, 130, 125, 140, 145, 150],
    'Equity': [200, 220, 210, 230, 250, 240, 260, 270, 300],
    'Debt': [100, 110, 105, 120, 115, 130, 140, 145, 150],
    'Commodity': [50, 55, 53, 60, 58, 62, 65, 70, 75],
})

st.markdown("<div class='section-title'>Passive Fund Trends</div>", unsafe_allow_html=True)
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
        # plot_bgcolor="white",
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
    st.markdown("###### Fund Type")
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
    st.markdown("###### Asset Type")
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



col1, col2 = st.columns([3, 1]) 

# NET INFLOWS SECTION
col1.markdown("<hr>", unsafe_allow_html=True)
net_inflows_data = {
    'Month': ['Jan 23', 'Feb 23', 'Mar 23', 'Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23'],
    'ETF': [1.2, 1.3, 1.2, 1.8, 1.4, 1.5, 1.6, 2.0, 2.2],
    'Index Fund': [1.0, 1.1, 1.0, 1.5, 1.2, 1.3, 1.4, 1.8, 2.0]
}
net_inflows_data_df = pd.DataFrame(net_inflows_data)

left_col, right_col = col1.columns([1, 4]) 

# Left column - Metrics
with left_col:
    st.metric(label="Net Inflows", value="₹ 12,446 cr", delta="as on Sep 2024")
    
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
            Index Fund: <span style='float: right'>₹ 48,627 cr</span>
        </div>
    """, unsafe_allow_html=True)
    

# Right column - Double Stack Bar Chart
with right_col:
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=net_inflows_data_df['Month'],
        y=net_inflows_data_df['Index Fund'], 
        name='Index Fund',
        marker_color='#3364A9'
    ))
    
    # Add ETF bars (top)
    fig.add_trace(go.Bar(
        x=net_inflows_data_df['Month'],
        y=net_inflows_data_df['ETF'],
        name='ETF',
        marker_color='#FEB273'
    ))
    

    fig.update_layout(
        barmode='stack',
        # plot_bgcolor='white',
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
            range=[0, 6] 
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    

# Aggregate ADV Section
col1.markdown("<hr>", unsafe_allow_html=True)
# Sample Data for different time periods
data_1d = {
    'Equity': [2.0, 2.1, 2.0, 2.3, 2.2],
    'Debt': [1.0, 1.1, 1.0, 1.3, 1.2],
    'Commodity': [0.5, 0.6, 0.5, 0.8, 0.7]
}

data_1w = {
    'Equity': [3.2, 3.0, 2.8, 2.6, 2.4, 2.6, 2.8],
    'Debt': [1.6, 1.5, 1.4, 1.3, 1.2, 1.3, 1.4],
    'Commodity': [1.1, 1.0, 0.9, 0.8, 0.7, 0.8, 0.9]
}

data_1m = {
    'Equity': [2.0, 2.5, 1.8, 3.0, 2.2, 3.5, 2.8, 3.2, 2.6, 3.8, 2.4],
    'Debt': [1.0, 1.4, 0.9, 1.5, 1.1, 1.6, 1.3, 1.7, 1.2, 1.8, 1.0],
    'Commodity': [0.5, 0.8, 0.4, 0.9, 0.6, 1.0, 0.7, 1.1, 0.5, 1.2, 0.6]
}

data_1y = {
    'Equity': [2.0, 2.5, 2.2, 2.8, 2.4, 3.0, 2.6, 3.2, 2.8, 3.4, 3.0, 3.6],
    'Debt': [1.0, 1.2, 1.1, 1.3, 1.2, 1.4, 1.3, 1.5, 1.4, 1.6, 1.5, 1.7],
    'Commodity': [0.5, 0.7, 0.6, 0.8, 0.7, 0.9, 0.8, 1.0, 0.9, 1.1, 1.0, 1.2]
}

#? Function to get data based on selected time period
def get_data_for_period(period):
    if period == '1D':
        return data_1d
    elif period == '1W':
        return data_1w
    elif period == '1M':
        return data_1m
    elif period == '1Y':
        return data_1y
    return None  

left_col, right_col = col1.columns([1, 4])

# Left column - Metrics
with left_col:
    st.metric(label="Aggregate Adv", value="₹ 56,846 cr", delta="as on Sep 2024", delta_color="inverse", help="Average Daily Volume")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Metrics with colored dots
    metrics = [
        ("Equity", "45,124", "#E9D5FF"),
        ("Debt", "12,564", "#7C3AED"),
        ("Commodity", "8,497", "#A78BFA")
    ]
    
    for label, value, color in metrics:
        st.markdown(f"""
            <div class='metric-row'>
                <span style='display: inline-block; width: 12px; height: 12px; background-color: {color}; border-radius: 50%; margin-right: 8px;'></span>
                {label}: <span style='float: right'>₹ {value} cr</span>
            </div>
        """, unsafe_allow_html=True)

# Right column - Chart and Time Period selector
with right_col:

    period = st.selectbox("Select Time Period", options=["1D", "1W", "1M", "1Y"])
    
    data = get_data_for_period(period)
    
    if data:  
        # Create the filled line chart (area chart)
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=list(range(len(data['Commodity']))),  
            y=data['Commodity'],
            name='Commodity',
            mode='lines',
            fill='tozeroy',  
            line=dict(color='rgba(167, 139, 250, 0.8)', width=3)
        ))

        fig.add_trace(go.Scatter(
            x=list(range(len(data['Debt']))),
            y=[d + c for d, c in zip(data['Debt'], data['Commodity'])],
            name='Debt',
            mode='lines',
            fill='tonexty',  
            line=dict(color='rgba(124, 58, 237, 0.8)', width=3)
        ))

        fig.add_trace(go.Scatter(
            x=list(range(len(data['Equity']))),
            y=[e + d + c for e, d, c in zip(data['Equity'], data['Debt'], data['Commodity'])],
            name='Equity',
            mode='lines',
            fill='tonexty',  
            line=dict(color='rgba(233, 213, 255, 0.8)', width=3)
        ))

        # Update layout
        fig.update_layout(
            title='Asset Performance Over Time',
            showlegend=True,
            # plot_bgcolor='white',
            height=400,
            margin=dict(l=40, r=40, t=40, b=40),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            ),
            xaxis=dict(
                title='Time Period',
                showgrid=True,
                showline=True,
                linecolor='#E5E7EB'
            ),
            yaxis=dict(
                title='Value',
                showgrid=True,
                gridcolor='#E5E7EB',
                zeroline=False,
                tickformat='.1f'
            )
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("No data available for this time period.")


# Number of Folios
col1.markdown("<hr>", unsafe_allow_html=True)

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Sample data
months = ['Feb, 23', 'Mar, 23', 'Apr, 23', 'May, 23', 'Jun, 23', 
          'Jul, 23', 'Aug, 23', 'Sep, 23', 'Oct, 23']

data = {
    'Month': months * 5,
    'Type': (
        ['Corporate'] * len(months) +
        ['Bank/FIs'] * len(months) +
        ['FIIs'] * len(months) +
        ['HNI'] * len(months) +
        ['Retail'] * len(months)
    ),
    'Value': [
        # Corporate values
        0.2, 0.25, 0.22, 0.28, 0.26, 0.30, 0.27, 0.32, 0.29,
        # Bank/FIs values
        0.3, 0.35, 0.32, 0.38, 0.36, 0.40, 0.37, 0.42, 0.39,
        # FIIs values
        0.4, 0.45, 0.42, 0.48, 0.46, 0.50, 0.47, 0.52, 0.49,
        # HNI values
        0.5, 0.8, 0.6, 0.9, 0.7, 1.0, 0.8, 1.1, 0.9,
        # Retail values
        0.6, 1.65, 0.7, 0.75, 1, 1.25, 1.5, 1.3, 1.4
    ]
}

df = pd.DataFrame(data)

# Layout
left_col, right_col = col1.columns([1, 4])

# Left column - Metrics
with left_col:
    st.metric(label="Number of Folios", value="1,53,19,983", delta="as on 31 Mar 2024")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Metrics with values
    metrics = [
        ("Corporate", "84,198", "#FF9800"),
        ("Bank/FIs", "1,39,597", "#2196F3"),
        ("FIIs", "5,64,198", "#4CAF50"),
        ("HNI", "32,55,785", "#9C27B0"),
        ("Retail", "1,06,55,785", "#F44336")
    ]
    
    for label, value, color in metrics:
        st.markdown(f"""
            <div class='metric-row'>
                <span style='display: inline-block; width: 12px; height: 12px; background-color: {color}; border-radius: 50%; margin-right: 8px;'></span>
                {label}: <span style='float: right'>{value}</span>
            </div>
        """, unsafe_allow_html=True)

# Right column - Chart and Investor Type selector
with right_col:
    # Investor Type tabs
    tabs = st.tabs(["All", "Corporate", "Banks/FIs", "FIIs", "HNI", "Retail"])
    
    with tabs[0]:  # All investor types
        fig = go.Figure()
        
        # Color mapping
        colors = {
            'Corporate': '#FDDCAB',
            'Bank/FIs': '#FEB273',
            'FIIs': '#FD853A',
            'HNI': '#3364A9',
            'Retail': '#002558'
        }
        
        # Add bars for each type
        for investor_type in ['Corporate', 'Bank/FIs', 'FIIs', 'HNI', 'Retail']:
            type_data = df[df['Type'] == investor_type]
            
            fig.add_trace(go.Bar(
                name=investor_type,
                x=type_data['Month'],
                y=type_data['Value'],
                marker_color=colors[investor_type],
                width=0.15  # Make bars thinner
            ))
        
        # Update layout
        fig.update_layout(
            title= 'Investor Type-wise Folio Distribution',
            barmode='group',
            showlegend=True,
            # plot_bgcolor='white',
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
                title='Month',
                showgrid=True,
                showline=True,
                linecolor='#E5E7EB',
                tickangle=0  
            ),
            yaxis=dict(
                title='Value (in Cr)',
                showgrid=True,
                gridcolor='#E5E7EB',
                zeroline=False,
                range=[0, 1.6],
                tickformat='.1f'
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # For each investor type tab
    for i, investor_type in enumerate(['Corporate', 'Bank/FIs', 'FIIs', 'HNI', 'Retail'], start=1):
        with tabs[i]:
            type_data = df[df['Type'] == investor_type]
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                name=investor_type,
                x=type_data['Month'],
                y=type_data['Value'],
                marker_color=colors[investor_type],
                width=0.15
            ))
            
            fig.update_layout(
                barmode='group',
                showlegend=True,
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
                    title='Month',
                    showgrid=True,
                    showline=True,
                    linecolor='#E5E7EB',
                    tickangle=45
                ),
                yaxis=dict(
                    title='Value (in Cr)',
                    showgrid=True,
                    gridcolor='#E5E7EB',
                    zeroline=False,
                    range=[0, 1.6],
                    tickformat='.1f'
                )
            )
            
            st.plotly_chart(fig, use_container_width=True)

# col2.header("Passive Fund Statistics",)
col2.markdown("<div class='section-title'>Passive Fund Statistics</div>", unsafe_allow_html=True)

# First Row - Donut Chart and Metrics
row1_col1, row1_col2 = col2.columns(2)

with row1_col1:
    st.metric(label="PASSIVE FUNDS AS % OF MUTUAL FUNDS", value="32%", delta="of total MFs")

with row1_col2:
    fig_donut = go.Figure()
    fig_donut.add_trace(go.Pie(
        values=[32, 68],
        labels=['Passive Funds', 'Other Funds'],
        hole=0.7,
        direction='clockwise',
        rotation=90,
        showlegend=False,
        textinfo='none',
        marker_colors=['#2563EB', '#FCD9BD']
    ))
    
    # Update layout for half donut
    fig_donut.update_layout(
        width=300,
        height=200,
        margin=dict(t=0, b=0, l=0, r=0),
        annotations=[dict(text='32%', x=0.5, y=0.5, font_size=24, showarrow=False)]
    )
    
    # Clip to show only top half
    fig_donut.update_layout(
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_donut)

# Second Row - NFO Trends
col2.markdown("<div class='section-title'>NFO TRENDS</div>", unsafe_allow_html=True)

# Sample NFO data
nfo_data = pd.DataFrame({
    'Month': ['Apr 23', 'May 23', 'Jun 23', 'Jul 23', 'Aug 23', 'Sep 23'],
    'Number of NFOs': [15, 35, 25, 20, 30, 32]
})

fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    x=nfo_data['Month'],
    y=nfo_data['Number of NFOs'],
    mode='lines+markers',
    line=dict(color='#2563EB', width=2),
    marker=dict(size=8, color='#2563EB'),
    name='Number of NFOs'
))

fig_line.update_layout(
    # plot_bgcolor='white',
    height=300,
    margin=dict(l=40, r=40, t=20, b=40),
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='#E5E7EB'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#E5E7EB',
        zeroline=False,
        range=[0, 50]
    )
)

col2.plotly_chart(fig_line, use_container_width=True)

# Third Row - Number of Indices Tracked
col2.markdown("<div class='section-title'>NUMBER OF INDICES TRACKED</div>", unsafe_allow_html=True)
col2.markdown("<div class='metric-date'>as on Sep 2023</div>", unsafe_allow_html=True)

# Create horizontal bar chart
indices_data = pd.DataFrame({
    'Type': ['by ETF', 'by Index Funds'],
    'Count': [127, 89],
    'Color': ['#FCD9BD', '#2563EB']
})

fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    y=['Indices'],
    x=[127],
    name='ETF',
    orientation='h',
    marker_color='#FCD9BD',
    text=['127'],
    textposition='auto',
))

fig_bar.add_trace(go.Bar(
    y=['Indices'],
    x=[89],
    name='Index Funds',
    orientation='h',
    marker_color='#2563EB',
    text=['89'],
    textposition='auto',
))

fig_bar.update_layout(
    barmode='stack',
    plot_bgcolor='white',
    height=100,
    margin=dict(l=40, r=40, t=20, b=20),
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False
    )
)

col2.plotly_chart(fig_bar, use_container_width=True)

# Fourth Row - Number of ETFs and Index Funds
col2.markdown("<div class='section-title'>NUMBER OF ETFs AND INDEX FUNDS</div>", unsafe_allow_html=True)
col2.markdown("<div class='metric-date'>as on Sep 2023</div>", unsafe_allow_html=True)

# Create horizontal bar chart
etf_index_data = pd.DataFrame({
    'Type': ['ETFs', 'Index Funds'],
    'Count': [65, 45],
    'Color': ['#FCD9BD', '#2563EB']
})

fig_bar = go.Figure()
fig_bar.add_trace(go.Bar(
    y=['Funds'],
    x=[65],
    name='ETFs',
    orientation='h',
    marker_color='#2563EB',
    text=['65'],
    textposition='auto',
))

fig_bar.add_trace(go.Bar(
    y=['Funds'],

    x=[45],
    name='Index Funds',
    orientation='h',
    marker_color='#FCD9BD',
    text=['45'],
    textposition='auto',
))

fig_bar.update_layout(
    barmode='stack',
    plot_bgcolor='white',
    height=100,
    margin=dict(l=40, r=40, t=20, b=20),
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False
    )
)

col2.plotly_chart(fig_bar, use_container_width=True)
# Feedback Form
col2.markdown("<div class='section-title'>Feedback Form</div>", unsafe_allow_html=True)

with col2.form(key='feedback_form'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback = st.text_area("Feedback")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.success("Thank you for your feedback!")

row1_col1, row1_col2 = col2.columns(2)

# with row1_col1:
#     st.metric(label="NIFTY 50", value="19,776.05", delta="+5.10 (0.05%)")

# with row1_col2:
#     fig_donut = go.Figure()
#     fig_donut.add_trace(go.Pie(
#         values=[20, 30, 10, 40],
#         labels=['Advances', 'Declines', 'Unchanged', 'Not Traded'],
#         hole=0.7,
#         direction='clockwise',
#         rotation=90,
#         showlegend=False,
#         textinfo='none',
#         marker_colors=['#34D399', '#F87171', '#FDBA74', '#93C5FD']
#     ))
    
#     # Update layout for half donut
#     fig_donut.update_layout(
#         width=300,
#         height=200,
#         margin=dict(t=0, b=0, l=0, r=0),
#         annotations=[dict(text='66%', x=0.5, y=0.5, font_size=24, showarrow=False)]
#     )
    
#     # Clip to show only top half
#     fig_donut.update_layout(
#         showlegend=False,
#         paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)'
#     )
    
#     st.plotly_chart(fig_donut)

# Data for the table
nse_gainers_data = {
    "Name": ["Nifty 50", "Nifty Next 50", "Nifty Bank 50", "Nifty IT 50", "COMP"],
    "LTP": [201.15, 202.30, 203.45, 204.60, 205.75],
    "%CHNG": [0.52, 0.65, 0.78, 0.91, 1.04],
}

nse_losers_data = {
    "Name": ["Nifty 50", "Nifty Next 50", "Nifty Bank 50", "Nifty IT 50", "COMP"],
    "LTP": [200.00, 199.50, 198.75, 198.00, 197.25],
    "%CHNG": [-0.52, -0.75, -0.88, -1.01, -1.14],
}

etf_gainers_data = {
    "Name": ["Nifty BeES", "ICICI Prudential Nifty ETF", "HDFC Nifty ETF", "Reliance ETF Nifty BeES", "Kotak Nifty ETF"],
    "LTP": [202.50, 203.75, 205.00, 206.25, 207.50],
    "%CHNG": [0.75, 0.85, 0.95, 1.05, 1.15],
}

etf_losers_data = {
    "Name": ["Nifty BeES", "ICICI Prudential Nifty ETF", "HDFC Nifty ETF", "Reliance ETF Nifty BeES", "Kotak Nifty ETF"],
    "LTP": [200.00, 199.25, 198.50, 197.75, 197.00],
    "%CHNG": [-0.75, -0.85, -0.95, -1.05, -1.15],
}

# Creating DataFrames
nse_gainers_df = pd.DataFrame(nse_gainers_data)
nse_losers_df = pd.DataFrame(nse_losers_data)
etf_gainers_df = pd.DataFrame(etf_gainers_data)
etf_losers_df = pd.DataFrame(etf_losers_data)

col1, col2, col3 = st.columns([1, 1, 1])

#  NSE Indices
col1.markdown("<div class='section-title'>NSE Indices</div>", unsafe_allow_html=True)

# Tabs for switching between Top Gainers and Top Losers
tab1, tab2 = col1.tabs(["Top Gainers", "Top Losers"])

with tab1:
    st.dataframe(nse_gainers_df.style.applymap(lambda v: 'color: green' if isinstance(v, (int, float)) and v > 0 else '', subset=["%CHNG"]))
    st.markdown("[View All >](#)")

with tab2:
    st.dataframe(nse_losers_df.style.applymap(lambda v: 'color: red' if isinstance(v, (int, float)) and v < 0 else '', subset=["%CHNG"]))
    st.markdown("[View All >](#)")

col2.markdown("<div class='section-title'>ETFs</div>", unsafe_allow_html=True)

tab1, tab2 = col2.tabs(["Top Gainers", "Top Losers"])

with tab1:
    st.dataframe(etf_gainers_df.style.applymap(lambda v: 'color: green' if isinstance(v, (int, float)) and v > 0 else '', subset=["%CHNG"]))
    st.markdown("[View All >](#)")

with tab2:
    st.dataframe(etf_losers_df.style.applymap(lambda v: 'color: red' if isinstance(v, (int, float)) and v < 0 else '', subset=["%CHNG"]))
    st.markdown("[View All >](#)")

col3.markdown("<div class='section-title'>News</div>", unsafe_allow_html=True)


news_data = [
    {
        "headline": "Interview: Shaktikanta Das good at short-term fixes, says ex-finance Minister of Sta...",
        "subheadline": "Nifty Bank ETF +18.00 (13.45%)",
        "source": "BQ Prime",
        "date": "Oct 6, 2023 ; 12:30 pm"
    },
    {
        "headline": "Market Update: Sensex hits all-time high, driven by IT and banking stocks",
        "subheadline": "Sensex +500.00 (1.25%)",
        "source": "Economic Times",
        "date": "Oct 6, 2023 ; 11:00 am"
    },
]

# Display news cards
for news in news_data:
    col3.markdown(f"""
    <div style="border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
        <div style="font-size: 1.2rem; font-weight: normal;">{news['headline']}</div>
        <div style="color: #4B5563; margin-bottom: 0.5rem;">{news['subheadline']}</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="color: #003D93">{news['source']}</div>
                <div style="color: #6B7280;">{news['date']}</div>
            </div>
            <button style="background-color: #003176; color: #363F72; border: none; padding: 0.5rem 1rem; border-radius: 4px;">
                <img src="https://img.icons8.com/ios-filled/50/ffffff/arrow.png" alt="Arrow" style="height: 16px; width: 16px;">
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sample news fund offer data
news_fund_offer_data = [
    {
        "status": "Open",
        "headline": "Edelweiss New Equity Fund Launched",
        "details": "Equity | Open Ended | High Risk",
        "icon": "https://companieslogo.com/img/orig/EDELWEISS.NS-32a7f779.png?t=1720244491",
        "amount": "₹ 500",
        "opening_date": "04 Oct, 2024",
        "closing_date": "18 Oct, 2024"
    },
    {
        "status": "Open",
        "headline": "Aditya Birla New Debt Fund Launched",
        "details": "Debt | Open Ended | Low Risk",
        "icon": "https://companieslogo.com/img/orig/ABCAPITAL.NS-69fa632a.png?",
        "amount": "₹ 1000",
        "opening_date": "05 Oct, 2024",
        "closing_date": "19 Oct, 2024"
    },
    {
        "status": "Closed",
        "headline": "BOB Commodity Fund ",
        "details": "Commodity | Open Ended | Medium Risk",
        "icon": "https://companieslogo.com/img/orig/BANKBARODA.NS-6790b239.png",
        "amount": "₹ 1500",
        "opening_date": "06 Oct, 2024",
        "closing_date": "20 Oct, 2024"
    },
    {
        "status": "Open",
        "headline": "TCS New Balanced Fund Launched",
        "details": "Balanced | Open Ended | Medium Risk",
        "icon": "https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png",
        "amount": "₹ 2000",
        "opening_date": "07 Oct, 2024",
        "closing_date": "21 Oct, 2024"
    },
    {
        "status": "Closed",
        "headline": "HDFC New Index Fund Launched",
        "details": "Index | Open Ended | Low Risk",
        "icon": "https://companieslogo.com/img/orig/HDB-bb6241fe.png?t=1720244492",
        "amount": "₹ 2500",
        "opening_date": "08 Oct, 2024",
        "closing_date": "22 Oct, 2024"
    },
    {
        "status": "Open",
        "headline": "Bajaj Finserv New International Fund Launched",
        "details": "International | Open Ended | High Risk",
        "icon": "https://companieslogo.com/img/orig/BAJAJFINSV.NS-69a58fe4.png?t=1720244490",
        "amount": "₹ 3000",
        "opening_date": "09 Oct, 2024",
        "closing_date": "23 Oct, 2024"
    },
]

col1, col2 = st.columns([2, 1])
col1.markdown("<div class='section-title'>News Fund Offer</div>", unsafe_allow_html=True)

# Display news fund offer cards in a 3x3 grid
for i in range(0, len(news_fund_offer_data), 3):
    cols = col1.columns(3)
    for col, news_fund in zip(cols, news_fund_offer_data[i:i+3]):
        col.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="background-color: {'#34D399' if news_fund['status'] == 'Open' else '#F87171'}; color: white; padding: 0.25rem 0.5rem; border-radius: 4px;">{news_fund['status']}</span>
            <img src="{news_fund['icon']}" alt="Icon" style="height: 24px; width: 24px;">
            </div>
            <div style="font-size: 1.2rem; font-weight: normal; margin-top: 0.5rem;">{news_fund['headline']}</div>
            <div style="color: #4B5563; margin-bottom: 0.5rem;">{news_fund['details']}</div>
            <div style="color: #6B7280; margin-bottom: 0.5rem;">Min. Subscription Amt. <br><span style="font-size: 1.5rem;">{news_fund['amount']}</span></div>
            <div style="display: flex; justify-content: space-between; color: #6B7280;">
            <span>Opening Date <br><b>{news_fund['opening_date']}</b></span>
            <span>Closing Date <br><b>{news_fund['closing_date']}</b></span>
            </div>
            </div>
        """, unsafe_allow_html=True)


        # Additional Form for NSE Cogencies
# col2.markdown("<div class='section-title'>NSE Cogencies Form</div>", unsafe_allow_html=True)

# with col2.form(key='nse_cogencies_form'):
#         name = st.text_input("Name")
#         email = st.text_input("Email")
#         age = st.number_input("Age", min_value=18, max_value=100, step=1)
#         gender = st.radio("Gender", options=["Male", "Female", "Other"])
#         investment_experience = st.selectbox("Investment Experience", options=["Beginner", "Intermediate", "Expert"])
#         feedback = st.text_area("Feedback")
#         submit_button = st.form_submit_button(label='Submit')

#         if submit_button:
#             st.success("Thank you for your submission!")

col2.markdown("<div class='section-title'>NSE Cogencies</div>", unsafe_allow_html=True)

with col2.form(key='nse-cogrencies'):
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
    gender = st.radio("Gender", options=["Male", "Female", "Other"], horizontal=True)
    investment_experience = st.selectbox("Investment Experience", options=["Beginner", "Intermediate", "Expert"])
    feedback = st.text_area("Feedback", height=70)
    submit_button = st.form_submit_button(label='Submit')


    error_messages = []

    if submit_button:
        if not name.strip():
            error_messages.append("⚠️ Name is required.")

        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not email.strip():
            error_messages.append("⚠️ Email is required.")
        elif not re.match(email_pattern, email):
            error_messages.append("⚠️ Please enter a valid email address.")

        if not gender:
            error_messages.append("⚠️ Please select a gender.")

        if not investment_experience:
            error_messages.append("⚠️ Please select your investment experience level.")

        if len(feedback.strip()) < 10:
            error_messages.append("⚠️ Feedback must be at least 10 characters long.")

        if error_messages:
            for error in error_messages:
                st.error(error)
        else:
            st.success("Thank you for your feedback!")
        

#  Footer
# Footer
st.markdown("""
<div style="background-color: #f8f9fa; padding: 2rem 0; margin-top: 2rem;">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between;">
        <!-- First Column - NSE Logo and Description -->
        <div style="flex: 1; padding: 0 1rem;">
            <img src="https://dipam.gov.in/resources/images/new/useful-links/nse-logo.png" alt="NSE Logo" style="height: 50px; width: auto;">
            <p style="color: #6c757d; margin-top: 1rem;">The National Stock Exchange of India Limited (NSE) is the leading stock exchange of India, located in Mumbai.</p>
        </div>
        <!-- Second Column - NSE ETF Menu Links -->
        <div style="flex: 1; padding: 0 1rem;">
            <h4 style="color: #343a40;">NSE ETF</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="/" style="color: #007bff; text-decoration: none;">About Us</a></li>
                <li><a href="/screener" style="color: #007bff; text-decoration: none;">Screener</a></li>
                <li><a href="/compare" style="color: #007bff; text-decoration: none;">Compare</a></li>
                <li><a href="/resources" style="color: #007bff; text-decoration: none;">Resources</a></li>
            </ul>
        </div>
        <!-- Third Column - Quick Links -->
        <div style="flex: 1; padding: 0 1rem;">
            <h4 style="color: #343a40;">Quick Links</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="https://www.nseindia.com" style="color: #007bff; text-decoration: none;">nseindia.com</a></li>
                <li><a href="https://www.sebi.gov.in" style="color: #007bff; text-decoration: none;">sebi.gov.in</a></li>
                <li><a href="https://www.amfiindia.com" style="color: #007bff; text-decoration: none;">amfiindia.com</a></li>
                <li><a href="https://www.niftyindices.com" style="color: #007bff; text-decoration: none;">niftyindices.com</a></li>
            </ul>
        </div>
        <!-- Fourth Column - Socials -->
        <div style="flex: 1; padding: 0 1rem;">
            <h4 style="color: #343a40;">Socials</h4>
            <ul style="list-style: none; padding: 0;">
                <li><a href="https://twitter.com/NSEIndia" target="_blank" style="color: #007bff; text-decoration: none;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/twitter.png" alt="Twitter" style="height: 24px; width: 24px;"> Twitter</a></li>
                <li><a href="https://www.facebook.com/NSEIndia" target="_blank" style="color: #007bff; text-decoration: none;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/facebook.png" alt="Facebook" style="height: 24px; width: 24px;"> Facebook</a></li>
                <li><a href="https://www.linkedin.com/company/national-stock-exchange-of-india-limited" target="_blank" style="color: #007bff; text-decoration: none;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/linkedin.png" alt="LinkedIn" style="height: 24px; width: 24px;"> LinkedIn</a></li>
                <li><a href="https://www.youtube.com/user/nseindia" target="_blank" style="color: #007bff; text-decoration: none;">
                    <img src="https://img.icons8.com/ios-filled/50/000000/youtube.png" alt="YouTube" style="height: 24px; width: 24px;"> YouTube</a></li>
                                </ul>
                            </div>
                        </div>
                        <div style="background-color: #f8f9fa; padding: 1rem 0; text-align: center; margin-top: 2rem;">
                <p style="color: #6c757d; margin: 0;">&copy; 2024 National Stock Exchange of India Limited. All rights reserved. Sohail Shaikh</p>
            </div>
                    </div>
                    
                    
                    """, unsafe_allow_html=True)