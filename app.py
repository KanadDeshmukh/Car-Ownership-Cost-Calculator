import streamlit as st

# Function to calculate monthly vehicle cost
def calculate_monthly_cost(car_cost, downpayment, loan_interest_rate, fuel_cost, parking_cost, toll_cost, service_fee, tax, insurance_yearly):
    # Calculate loan amount and monthly loan cost
    loan_amount = car_cost - downpayment
    loan_monthly_cost = loan_amount * (loan_interest_rate / 100) / 12
    
    # Calculate yearly insurance cost
    insurance_monthly_cost = insurance_yearly / 12
    
    # Calculate total monthly cost
    total_monthly_cost = loan_monthly_cost + fuel_cost + parking_cost + toll_cost + service_fee + tax + insurance_monthly_cost
    return total_monthly_cost

# Function to predict resell value and depreciation
def resell_value_and_depreciation(car_cost, year_purchased, current_year):
    # Assuming car depreciates by 10% per year
    depreciation_rate = 0.10
    age_of_car = current_year - year_purchased
    if age_of_car >= 1:
        depreciation_cost = car_cost * depreciation_rate * age_of_car
    else:
        depreciation_cost = 0
    resell_value = car_cost - depreciation_cost
    return resell_value, depreciation_cost

# Streamlit UI
st.title('Car Ownership Cost Calculator V1.1 SVASK.inc')

# User inputs
car_cost = st.number_input('Car Cost (in currency)', min_value=0.0, value=10000.0)
downpayment = st.number_input('Downpayment (in currency)', min_value=0.0, value=1000.0)
loan_interest_rate = st.number_input('Loan Interest Rate (%)', min_value=0.0, value=5.0)
fuel_cost = st.number_input('Monthly Fuel Cost (in currency)', min_value=0.0, value=150.0)
parking_cost = st.number_input('Monthly Parking Cost (in currency)', min_value=0.0, value=50.0)
toll_cost = st.number_input('Monthly Toll Cost (in currency)', min_value=0.0, value=20.0)
service_fee = st.number_input('Monthly Service Fee (if any, in currency)', min_value=0.0, value=30.0)
tax = st.number_input('Monthly Tax (if any, in currency)', min_value=0.0, value=15.0)
insurance_yearly = st.number_input('Annual Insurance Cost (in currency)', min_value=0.0, value=300.0)

year_purchased = st.number_input('Year the Car Was Purchased', min_value=2000, max_value=2024, value=2020)
current_year = 2024  # You can dynamically get this, but we'll use a constant for simplicity

# Calculate monthly costs
monthly_cost = calculate_monthly_cost(car_cost, downpayment, loan_interest_rate, fuel_cost, parking_cost, toll_cost, service_fee, tax, insurance_yearly)

# Resell value and depreciation
resell_value, depreciation_cost = resell_value_and_depreciation(car_cost, year_purchased, current_year)

# Display results
st.subheader(f"Total Monthly Cost of Vehicle: {monthly_cost:.2f} (in currency)")
st.subheader(f"Estimated Resell Value After Depreciation: {resell_value:.2f} (in currency)")
st.subheader(f"Total Depreciation Cost: {depreciation_cost:.2f} (in currency)")

# Efficiency comment
income = st.number_input('Your Monthly Income (in currency)', min_value=0.0, value=5000.0)

if monthly_cost <= income * 0.2:
    st.write("This car is very affordable for you.")
elif monthly_cost <= income * 0.4:
    st.write("This car is somewhat affordable, but consider your budget carefully.")
else:
    st.write("This car might be too expensive for your current income.")