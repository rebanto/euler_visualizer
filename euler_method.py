import streamlit as st
from sympy import symbols, sympify, lambdify, sin, cos, tan, exp, log
import matplotlib.pyplot as plt

st.set_page_config(page_title="Euler's Method Visualizer", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1f77b4; }
    .stButton>button { background-color: #1f77b4; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Euler's Method Differential Equation Solver")
st.markdown("Visualize numerical solutions to **dy/dx = f(x, y)** using Euler's method.")

x, y = symbols('x y')
allowed_funcs = {
    'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log,
    'sqrt': lambda x: x**0.5, 'abs': abs, 'asin': lambda x: sin(x)**-1,
    'acos': lambda x: cos(x)**-1, 'atan': lambda x: tan(x)**-1
}

st.sidebar.header("🧠 Enter Equation & Parameters")
default_eq = "y - x**2"

with st.sidebar.expander("ℹ️ Allowed Functions"):
    st.markdown("""
    **You can use the following functions in your equation:**
    - `sin(x)`: Sine
    - `cos(x)`: Cosine
    - `tan(x)`: Tangent
    - `exp(x)`: Exponential
    - `log(x)`: Natural Logarithm
    - `sqrt(x)`: Square Root
    - `abs(x)`: Absolute Value
    - `asin(x)`: Inverse Sine
    - `acos(x)`: Inverse Cosine
    - `atan(x)`: Inverse Tangent
    """)

user_input = st.sidebar.text_input("dy/dx = f(x, y)", value=default_eq)

x0 = st.sidebar.number_input("Initial x (x₀)", value=0.0)
y0 = st.sidebar.number_input("Initial y (y₀)", value=0.0)
x_end = st.sidebar.number_input("Final x", value=2.0)
h = st.sidebar.number_input("Step size (h)", min_value=0.001, value=0.1, step=0.01)

valid = True
try:
    expr = sympify(user_input, locals=allowed_funcs)
    diff_eq = lambdify((x, y), expr, modules=["math"])
except Exception as e:
    st.error(f"❌ Error in parsing equation: {e}")
    valid = False

if valid and st.sidebar.button("Run Euler's Method 🚀"):
    x_vals = [x0]
    y_vals = [y0]

    while x_vals[-1] < x_end:
        curr_x = x_vals[-1]
        curr_y = y_vals[-1]
        try:
            dydx = diff_eq(curr_x, curr_y)
        except Exception as e:
            st.error(f"❌ Error during computation: {e}")
            break
        x_vals.append(curr_x + h)
        y_vals.append(curr_y + h * dydx)

    st.subheader("📍 Final Result")
    st.markdown(f"**x = {x_vals[-1]:.4f}**, **y = {y_vals[-1]:.4f}**")

    st.subheader("📊 Solution Graph")
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, marker='o', linestyle='-', color='#1f77b4')
    ax.set_title("Euler's Method Approximation")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    st.pyplot(fig)