import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Science App")


# Title
st.title("Data Analysis App")
st.subheader("This is a simple data analysis app created by Sohail")

#? Load the data
df = sns.load_dataset("tips")

dataset_name = st.selectbox("Select Dataset", ["tips", "iris", "titanic", "diamonds"])

df = sns.load_dataset(dataset_name)
uploaded_file = st.file_uploader("Or upload your own dataset (CSV file)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# Display the Dataset
st.write(df)

# Display the number of rows and columns from the selected data
st.write("Number of rows: ", df.shape[0])
st.write("Number of columns: ", df.shape[1])

# Display the column names of selected data with their data type
st.write("Column Names and Data Type: ", df.dtypes)

# Display the summary statistics of the selected data
st.write("Summary Statistics: ", df.describe())

# Select the specific column for X and Y axis from the dataset and also select the plot type and plot the data
x_axis = st.selectbox("Select X Axis", df.columns)
y_axis = st.selectbox("Select Y Axis", df.columns)
plot_type = st.selectbox("Select Plot Type", ["scatter", "line", "bar", "hist", "box", "kde"])

# plot the data
if plot_type == "line":
    st.line_chart(df[[x_axis, y_axis]])
elif plot_type == "scatter":
    st.scatter_chart(df[[x_axis, y_axis]])
elif plot_type == "bar":
    if pd.api.types.is_numeric_dtype(df[x_axis]) and pd.api.types.is_numeric_dtype(df[y_axis]):
        st.bar_chart(df[[x_axis, y_axis]])
    else:
        st.error("Selected columns for bar chart must be numeric.")
elif plot_type == "hist":
    fig, ax = plt.subplots()
    df.hist(ax=ax)
    ax.set_xlabel(x_axis)
    fig, ax = plt.subplots()
    df.boxplot(ax=ax)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "kde":
    fig, ax = plt.subplots()
    sns.kdeplot(df[[x_axis, y_axis]], ax=ax)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)

# Create a pairplot of the selected data
st.subheader("Pairplot")

# Select the column to be used as hue in the pairplot
hue_column = st.selectbox("Select a column to be used as hue", df.columns)
st.pyplot(sns.pairplot(df, hue=hue_column))


# Create a heatmap
st.header("Heatmap")

# Select the column which are numeric and then create a corr_matrix
numeric_columns = df.select_dtypes(include=np.number).columns
corr_matrix = df[numeric_columns].corr()

from plotly import graph_objects as go

heatmap_fig = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                                        x=corr_matrix.values,
                                        y=corr_matrix.values,
                                        colorscale="Viridis"))

st.plotly_chart(heatmap_fig)
