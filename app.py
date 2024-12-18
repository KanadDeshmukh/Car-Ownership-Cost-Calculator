import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("Car Ownership Cost Calculator V1.0 SVASK.inc ")

# Inputs
st.header("Enter Car Details")
car_cost = st.number_input("Car Cost (in your currency)", min_value=0.0, step=1000.0, value=0.0)
down_payment = st.number_input("Down Payment", min_value=0.0, step=500.0, value=0.0)
interest_rate = st.number_input("Loan Interest Rate (Annual %)", min_value=0.0, step=0.1, value=0.0)
fuel_cost = st.number_input("Average Monthly Fuel Cost", min_value=0.0, step=100.0, value=0.0)
parking_cost = st.number_input("Monthly Parking Cost (if any)", min_value=0.0, step=50.0, value=0.0)
toll_cost = st.number_input("Monthly Toll Cost (if any)", min_value=0.0, step=50.0, value=0.0)
service_fee = st.number_input("Annual Service Fee (if any)", min_value=0.0, step=500.0, value=0.0)
taxes = st.number_input("Annual Taxes (if any)", min_value=0.0, step=500.0, value=0.0)
insurance = st.number_input("Annual Insurance Cost", min_value=0.0, step=500.0, value=0.0)
purchase_year = st.number_input("Year of Purchase", min_value=2000, step=1, value=2024)
current_year = st.number_input("Current Year", min_value=purchase_year, step=1, value=2024)
monthly_income = st.number_input("Your Monthly Income (optional)", min_value=0.0, step=1000.0, value=0.0)

# Validate Inputs
if purchase_year > current_year:
    st.error("Purchase year cannot be greater than the current year!")
else:
    # Calculations
    loan_amount = car_cost - down_payment
    years_owned = max(1, current_year - purchase_year)  # At least 1 year to avoid zero division
    depreciation_rate = 0.15  # Example: 15% annual depreciation
    resale_value = car_cost * ((1 - depreciation_rate) ** years_owned)
    monthly_depreciation_cost = (car_cost - resale_value) / (years_owned * 12) if years_owned > 0 else 0
    monthly_loan_emi = (loan_amount * (1 + (interest_rate / 100) * years_owned)) / (years_owned * 12) if years_owned > 0 else 0
    monthly_cost = (
        monthly_loan_emi +
        (insurance / 12) +
        fuel_cost +
        parking_cost +
        toll_cost +
        (service_fee / 12) +
        (taxes / 12)
    )

    # Outputs
    st.header("Results")
    st.write(f"*Total Monthly Cost of the Car:* {monthly_cost:.2f}")
    st.write(f"*Predicted Resale Value:* {resale_value:.2f}")
    st.write(f"*Monthly Depreciation Cost:* {monthly_depreciation_cost:.2f}")

    # Efficiency Analysis
    if monthly_income > 0:
        efficiency = (monthly_cost / monthly_income) * 100
        st.write(f"*Percentage of Monthly Income Spent on Car:* {efficiency:.2f}%")
        if efficiency > 50:
            st.warning("This car might not be economical for you.")
        else:
            st.success("This car seems economical for you.")

    # Analysis Section
    if car_cost > 0 and down_payment <= car_cost and years_owned > 0:
        st.header("Analysis")

        # Pie Chart for Cost Breakdown
        labels = ['Loan EMI', 'Insurance', 'Fuel', 'Parking', 'Toll', 'Service Fee', 'Taxes']
        values = [
            monthly_loan_emi, 
            (insurance / 12), 
            fuel_cost, 
            parking_cost, 
            toll_cost, 
            (service_fee / 12), 
            (taxes / 12)
        ]
        
        # Ensure valid values for the pie chart
        if sum(values) > 0:
            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
            st.subheader("Monthly Cost Breakdown")
            st.pyplot(fig)
        else:
            st.warning("Unable to generate a pie chart: All cost components are zero or invalid.")

        # Depreciation Curve
        years = range(purchase_year, current_year + 1)
        depreciation_values = [
            car_cost * ((1 - depreciation_rate) ** (year - purchase_year)) for year in years
        ]

        # Ensure valid values for the depreciation curve
        if all(value >= 0 for value in depreciation_values):
            fig, ax = plt.subplots()
            ax.plot(years, depreciation_values, marker='o')
            ax.set_title("Depreciation Over Time")
            ax.set_xlabel("Year")
            ax.set_ylabel("Resale Value")
            st.subheader("Depreciation Curve")
            st.pyplot(fig)
        else:
            st.warning("Unable to generate the depreciation curve: Invalid values detected.")
    else:
        st.warning("Please provide valid inputs to generate analysis.")