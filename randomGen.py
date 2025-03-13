import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Function to generate random dates within a specified range
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Function to generate churn dates based on a given churn rate
def churn_date(start_date, churn_rate):
    if np.random.rand() < churn_rate:
        churn_days = random.randint(0, int((datetime(2025, 1, 1) - start_date).days * churn_rate))
        return start_date + timedelta(days=churn_days)
    else:
        return start_date

# Create an empty list to store data
data = []

# Define start and end dates for the date range
start_date = datetime(2000, 1, 1)
end_date = datetime(2025, 1, 1)

# Generate data for 100,000 rows
for i in range(100000):
    sCustomerNaturalKey = i + 1
    age = random.randint(18, 99)
    apartment = random.randint(0, 1)
    woman = random.randint(0, 1)
    
    # Generate first start dates for each agreement
    mFirst_BankKonto = random_date(start_date, end_date)
    mFirst_BankKort = random_date(start_date, end_date)
    mFirst_BankBolån = random_date(start_date, end_date)
    mFirst_BoKvar = random_date(start_date, end_date)
    mFirst_Pension = random_date(start_date, end_date)
    mFirst_Personbil = random_date(start_date, end_date)
    
    # Generate last start dates based on churn rate
    mLastStart_BankKort = churn_date(mFirst_BankKort, random.uniform(0.15, 0.20))
    mLastStart_BankBolån = churn_date(mFirst_BankBolån, random.uniform(0.20, 0.30))
    mLastStart_BoKvar = churn_date(mFirst_BoKvar, 0.20)
    mLastStart_Pension = churn_date(mFirst_Pension, 0.10)
    mLastStart_Personbil = churn_date(mFirst_Personbil, 0.40)
    
    # Add noise to the dates to make them less linear
    noise_days = random.randint(-365, 365)
    mFirst_BankKonto += timedelta(days=noise_days)
    mFirst_BankKort += timedelta(days=noise_days)
    mFirst_BankBolån += timedelta(days=noise_days)
    mFirst_BoKvar += timedelta(days=noise_days)
    mFirst_Pension += timedelta(days=noise_days)
    mFirst_Personbil += timedelta(days=noise_days)
    
    # Add data to the list
    data.append([
        sCustomerNaturalKey,
        mFirst_BankKonto,
        mFirst_BankKort,
        mFirst_BankBolån,
        mFirst_BoKvar,
        mFirst_Pension,
        mFirst_Personbil,
        mLastStart_BankKort,
        mLastStart_BankBolån,
        mLastStart_BoKvar,
        mLastStart_Pension,
        mLastStart_Personbil,
        age,
        apartment,
        woman
    ])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=[
    'sCustomerNaturalKey',
    'mFirst_BankKonto',
    'mFirst_BankKort',
    'mFirst_BankBolån',
    'mFirst_BoKvar',
    'mFirst_Pension',
    'mFirst_Personbil',
    'mLastStart_BankKort',
    'mLastStart_BankBolån',
    'mLastStart_BoKvar',
    'mLastStart_Pension',
    'mLastStart_Personbil',
    'Age',
    'Apartment',
    'Woman'
])

# Save the DataFrame to a CSV file
df.to_csv('customer_data.csv', index=False)