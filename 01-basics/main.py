import streamlit as st
import pandas as pd
import time as time
from matplotlib import pyplot as plt
table_data = pd.DataFrame({
    'Name': ['Sohail', 'Sohrab', 'Aniket', 'Ajay', 'Bhumi', 'Suraj', 'Akash', 'Darshan', 'Surya', 'Shivani'],
    'Age': [22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
})

# Basic Text Elements
st.title('Hello Streamlit!') # Title 
st.header('This is a header') # Header 
st.subheader('This is a subheading') # Subheading
st.text('This is a text') # Text -> p tag

# Markdown
st.markdown("**Hello** in bold")
st.markdown("*Hello* in Italic")

st.markdown("# This is a H1 heading")
st.markdown("## This is a H2 heading")
st.markdown("### This is a H3 heading")
st.markdown("#### This is a H4 heading")
st.markdown("##### This is a H5 heading")
st.markdown("###### This is a H6 heading")

st.markdown("> This is a blockquote")
st.markdown("```print('Hello Streamlit') ```")

st.markdown("[Streamlit Doc](https://www.streamlit.io/)") # Markdown with link
st.markdown("---") # Markdown with horizontal line
st.markdown("![Streamlit Logo](https://www.streamlit.io/images/brand/streamlit-mark-color.png)") # Markdown with image
st.markdown("---") 

st.caption("This is a caption") # Caption

# Mathematical Equations
st.header("Mathematical Equations")

st.text("Integral of the function ( f(x) ) from ( a ) to ( b )")
st.latex(r'\int_a^b f(x) dx') 

st.text("Derivative of the function ( f(x) ) with respect to ( x )")
st.latex(r'\frac{df}{dx}')

st.text("Quadratic Equation")
st.latex(r'ax^2 + bx + c = 0') 

st.text("Pythagorean Theorem")
st.latex(r'a^2 + b^2 = c^2')

st.text("Fraction with a as the numerator and b as the denominator")
st.latex(r'\frac{a}{b}') 

st.text("Square root of the sum of squares of a and b")
st.latex(r'\sqrt{a^2 + b^2}') 

st.text("Round Matrix with 3 rows and 3 columns")
st.latex(r'\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}') 

st.text("Square Matrix with 3 rows and 3 columns")
st.latex(r'\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}')

st.text("Determinant of a 3x3 matrix")
st.latex(r'\def\arraystretch{1.5}\begin{array}{c:c:c} a & b & c \\ \hline d & e & f \\\hdashline g & h & i\end{array}')

st.text("Equation with a curly brace")
st.latex(r'\begin{CD} A @>a>> B \\ @VbVV @AAcA \\ C @= D \end{CD}')


# JSON
st.header("JSON Function")
json_code = {"name": "Sohail", "age": 22, "company": "Digital Salt", "location": "Ghatkopar", "city": "Mumbai", "country": "India", "position": "Full Stack Developer", "skills": ["Python", "JavaScript", "React", "Node.js", "MongoDB", "Express.js", "Django", "HTML", "CSS", "NextJS"]}
st.json(json_code)

# Code Block
st.header("Code Block")
python_code = '''def hello_streamlit():
    print('Hello Streamlit')'''

st.code(python_code, language='python')

js_code = '''function hello_streamlit() {
    console.log('Hello Streamlit')
}'''
st.code(js_code, language='javascript')


# Metrics
st.header("Metrics Function")
st.metric(label="Revenue", value="₹100,000", delta="10%")
st.metric(label="Profit", value="₹50,000", delta="20%")
st.metric(label="Loss", value="₹10,000", delta="-20%", delta_color="normal")
st.metric(label="Sales", value="1000", delta="50%")

st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")


# Tables
st.header("Table")
st.table(table_data)

# DataFrames
st.header("DataFrame")
st.dataframe(table_data)

# DataFrames with Styling
st.header("Styled DataFrame")
st.dataframe(table_data.style.highlight_max(axis=0))


# Media Files
st.header("Media Files")
st.text("Image")
st.image("squid-game.jpg", caption="Red Light, Green Light")

st.text("Video")
st.video("https://youtu.be/SbAKYgfYET8?si=5ouyqtoN8N0ilZVm")

st.text("Mingle Audio File")
st.audio("mingle.mp3")

# Basic Interactive Widget

# Checkbox
st.header("Checkbox")
if st.checkbox("Show/Hide"):
    st.write("You have checked the checkbox")

# Radio Button
st.header("Radio Button")
radio_button = st.radio("Gender", ["Male", "Female", "Other"])
if radio_button:
    st.write(f"You have selected: {radio_button}")

# Selectbox
st.header("Selectbox")
selectbox = st.selectbox("Select a Country", ["India", "USA", "UK", "Australia", "Canada"])
if selectbox:
    st.write(f"You have selected: {selectbox}")

# Multiselect
st.header("Multiselect")
multiselect = st.multiselect("Select a Country", ["India", "USA", "UK", "Australia", "Canada"])
if multiselect:
    st.write("You have selected the following countries:")
    for country in multiselect:
        st.write(f"- {country}")

# Slider
st.header("Slider")
slider = st.slider("Select a Number", min_value=1, max_value=100, value=50)
if slider is not None:
    st.write(f"**You have selected: {slider}**")


# Text Input
st.header("Text Input")
text_input = st.text_input("Enter your name")
if text_input:
    st.write(f"Hello {text_input}")

# Text Area
st.header("Text Area")
text_area = st.text_area("Enter your message")
if text_area:
    st.write(f"Your message: {text_area}")

# Number Input
st.header("Number Input")
number_input = st.number_input("Enter your age", min_value=1, max_value=100, value=18)
if number_input:
    st.write(f"Your age is: {number_input}")

# Date Input
st.header("Date Input")
date_input = st.date_input("Select a date")
if date_input:
    st.write(f"Selected date: {date_input}")

# Time Input
st.header("Time Input")
time_input = st.time_input("Select a time")
if time_input:
    st.write(f"Selected time: {time_input}")


# File Uploader
st.header("File Uploader")
file_uploader = st.file_uploader("Upload a file", type=["csv", "txt", "pdf", "jpg", "jpeg", "png", "mp4", "mp3"])
if file_uploader:
    st.write(f"File name: {file_uploader.name}")
    st.write(f"File type: {file_uploader.type}")
    st.write(f"File size: {file_uploader.size} bytes")

# Color Picker
st.header("Color Picker")
color_picker = st.color_picker("Pick a color", "#00FF00")
if color_picker:
    st.write(f"You have selected: {color_picker}")

# Progress Bar
# st.header("Progress Bar")

# progress_bar = st.progress(0)
# for i in range(101):
#     progress_bar.progress(i)
#     time.sleep(0.1)

# Spinner
# st.header("Spinner")
# with st.spinner("Wait for it..."):
#     time.sleep(5)
#     st.success("Done!")

# Forms
st.header("Form")
with st.form(key="my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=1, max_value=100, value=18)
    email = st.text_input("Enter your email")
    feedback = st.text_area("Enter your feedback")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        st.write(f"Feedback: {feedback}")


st.markdown("---")

st.markdown("<h4 style='text-align: center;'>User Registration Form</h1>", unsafe_allow_html=True)
with st.form(key="user_registration_form"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name")
    last_name = col2.text_input("Last Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit_button = st.form_submit_button("Register")
    if submit_button:
        if password == confirm_password:
            st.success("Registration Successful!")
            full_name = f"{first_name} {last_name}"
            st.write(f"Name: {full_name}")
            st.write(f"Email: {email}")
        else:
            st.error("Passwords do not match!")


# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png")
st.sidebar.header("Navigation")
st.sidebar.markdown("[Home](#hello-streamlit)", unsafe_allow_html=True)
st.sidebar.markdown("[About](#this-is-a-header)", unsafe_allow_html=True)
st.sidebar.markdown("[Contact](#this-is-a-subheading)", unsafe_allow_html=True)


fig = plt.figure()
plt.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
st.pyplot(fig)

st.markdown("---")
# More Complex Figure
st.header("More Complex Figure")

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# First subplot
axs[0, 0].plot([1, 2, 3, 4], [10, 20, 25, 30], label='Line 1')
axs[0, 0].plot([1, 2, 3, 4], [30, 25, 20, 15], label='Line 2')
axs[0, 0].set_title('Subplot 1')
axs[0, 0].legend()

# Second subplot
axs[0, 1].bar([1, 2, 3, 4], [10, 20, 25, 30])
axs[0, 1].set_title('Subplot 2')

# Third subplot
axs[1, 0].scatter([1, 2, 3, 4], [10, 20, 25, 30])
axs[1, 0].set_title('Subplot 3')

# Fourth subplot
axs[1, 1].hist([10, 20, 25, 30, 30, 25, 20, 10], bins=5)
axs[1, 1].set_title('Subplot 4')

plt.tight_layout()
st.pyplot(fig)

# Add 3 graphs with the radio selection of the user
st.markdown("---")
st.header("Graphs with Radio Button")
graph_option = st.radio("Select a Graph", ["Line Plot", "Bar Plot", "Scatter Plot", "Pie Chart"])

fig, ax = plt.subplots()
if graph_option == "Line Plot":
    ax.plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
elif graph_option == "Bar Plot":
    ax.bar([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
elif graph_option == "Scatter Plot":
    ax.scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
else:
    ax.pie([1, 4, 9, 16, 25], labels=['A', 'B', 'C', 'D', 'E'], autopct='%1.1f%%')

st.pyplot(fig)

st.markdown("### Thank You! 😊")