import streamlit as st

# Inflation Calculator Function
def inflation_calculator(amount, inflation_rate, years):
    future_value = amount * ((1 + (inflation_rate / 100)) ** years)
    return future_value

# Dollar to Rupee Conversion Function
def dollar_to_rupee(dollars, exchange_rate=83.20):
    rupees = dollars * exchange_rate
    return rupees

# Rupee to Dollar Conversion Function
def rupee_to_dollar(rupees, exchange_rate=83.20):
    dollars = rupees / exchange_rate
    return dollars

# Streamlit Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Inflation Calculator", "Dollar to Rupee/Rupee to Dollar Converter"])

# Inflation Calculator Page
if page == "Inflation Calculator":
    st.title("Inflation Calculator")
    
    # Inputs for the inflation calculator
    amount = st.number_input("Enter the Amount (in your currency)", min_value=0.0, format="%.2f")
    inflation_rate = st.number_input("Enter the Rate of Inflation (%)", min_value=0.0, format="%.2f")
    years = st.number_input("Enter the Duration (in years)", min_value=0, format="%d")

    if st.button("Calculate Future Value"):
        future_value = inflation_calculator(amount, inflation_rate, years)
        st.write(f"The future value of {amount} at an inflation rate of {inflation_rate}% for {years} years is: {future_value:.2f}")

# Dollar to Rupee and Rupee to Dollar Converter Page
elif page == "Dollar to Rupee/Rupee to Dollar Converter":
    st.title("Currency Converter")
    
    # Input for Dollar to Rupee conversion
    st.subheader("Dollar to Rupee Conversion")
    dollars = st.number_input("Enter the Amount in USD", min_value=0.0, format="%.2f")
    if st.button("Convert to INR"):
        rupees = dollar_to_rupee(dollars)
        st.write(f"${dollars:.2f} is equivalent to ₹{rupees:.2f}")
    
    # Input for Rupee to Dollar conversion
    st.subheader("Rupee to Dollar Conversion")
    rupees_inr = st.number_input("Enter the Amount in INR", min_value=0.0, format="%.2f")
    if st.button("Convert to USD"):
        dollars_usd = rupee_to_dollar(rupees_inr)
        st.write(f"₹{rupees_inr:.2f} is equivalent to ${dollars_usd:.2f}")

# To run, execute: streamlit run your_app.py
