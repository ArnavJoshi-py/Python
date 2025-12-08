import streamlit as st

st.title("🧮 Simple Calculator")

st.write("Enter two numbers to perform basic arithmetic operations.")

# Inputs with validation
num1 = st.text_input("Enter first number:")
num2 = st.text_input("Enter second number:")

def is_number(value):
    try:
        float(value)   # supports integers & decimals
        return True
    except ValueError:
        return False

# Button to calculate
if st.button("Calculate"):
    if not is_number(num1) or not is_number(num2):
        st.error("❌ Please enter valid numbers only.")
    else:
        num1 = float(num1)
        num2 = float(num2)

        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Handle division by zero
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Undefined (cannot divide by zero)"

        # Output results
        st.success("✔️ Calculation Completed")

        st.write("### Results:")
        st.write(f"**Addition:** {addition}")
        st.write(f"**Subtraction:** {subtraction}")
        st.write(f"**Multiplication:** {multiplication}")
        st.write(f"**Division:** {division}")
