# 🧮 Euler's Method Visualizer

### A sleek, interactive Streamlit app for solving first-order differential equations using Euler’s Method.

![Badge](https://img.shields.io/badge/Built%20With-Python%20%7C%20Streamlit%20%7C%20SymPy%20%7C%20Matplotlib-blue)

---

## 📖 About the Project

While reviewing for the **AP Calculus** exam, I was practicing **Euler’s Method** by hand — calculating tangent slopes, plugging into formulas, and repeating. That’s when I thought:

> _“Why not let a program do this for me instead?”_

So I built this app — a clean, visual, and math-aware tool that not only solves differential equations with Euler’s Method, but also **graphs the solution live**, supports **real math functions** like `sin(x)`, `exp(x)`, and `log(y)`, and gives an instant preview of how your solution behaves.

This tool is perfect for students, teachers, or anyone wanting to **see numerical approximation in action** — no manual computation required.

---

## ⚙️ Features

- 🧠 **Type any differential equation** using `x`, `y`, `sin`, `cos`, `exp`, `log`, etc.
- 🎯 **Customizable initial conditions** and **step size**
- 📈 **Live plot** of the approximated solution using Matplotlib
- ✅ **No `eval`** used — safe, symbolic parsing with SymPy
- 🎨 Streamlit-based UI with smooth, modern layout

---

## 🚀 Run the App using `pip install streamlit sympy matplotlib` and then `streamlit run euler_method.py`
