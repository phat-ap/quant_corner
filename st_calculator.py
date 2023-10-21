import streamlit as st

# Set the title and description of the app
st.title("Simple Calculator")
st.write("Perform basic calculations")

# Create input fields for user to enter numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Create a dropdown to select the operation
operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Function to perform the selected operation
def calculate(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    return result

# Calculate and display the result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")