import streamlit as st

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


