# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
import streamlit as st
def calculator_body():
        """
        Renders a calculator interface in a Streamlit app, allowing users to input two numbers and select an arithmetic operation.
        Displays the result or an error message for invalid operations (e.g., division by zero).

        UI Elements:
            - Number input for the first number
            - Number input for the second number
            - Selectbox for choosing the operation (Addition, Subtraction, Multiplication, Division)
            - Button to trigger calculation

        Calls:
            - calculate_function(num1, num2, operation): Performs the selected calculation and displays the result.

        Error Handling:
            - Displays an error message if division by zero is attempted.
        """
        st.write("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            num1 = st.number_input(label='Enter first number', step=1)
        with col2:
            num2 = st.number_input(label='Enter second number', step=1)
        with col3:
            operation = st.selectbox(label='Select operation', 
                                     options=['Addition', 'Subtraction', 'Multiplication', 'Division'])
        if st.button('Click to Calculate'):
            if num2==0 and operation=='Division':
                st.error('Error: Division by zero is not allowed.')
            else:
                 calculate_function(num1, num2, operation) 

def calculate_function(num1, num2, operation):
    if operation == 'Addition':
        result = num1 + num2
        st.success(f'The result of {num1} + {num2} is **{result}**')
    elif operation == 'Subtraction':
        result = num1 - num2
        st.success(f'The result of {num1} - {num2} is **{result}**')
    elif operation == 'Multiplication':
        result = num1 * num2
        st.success(f'The result of {num1} * {num2} is **{result}**')
    elif operation == 'Division':
        result = num1 / num2
        st.success(f'The result of {num1} / {num2} is **{result}**')
    else:
        st.error('Invalid operation selected.')