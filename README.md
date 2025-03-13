# Customer Data Generation Script

## Overview

This Python script generates a CSV file containing synthetic customer data. The data includes various agreements and demographic information for 500,000 customers. The script ensures that the generated data is consistent with specified rules and constraints.

## Generated Columns

The script generates the following columns for each customer:

- `sCustomerNaturalKey`: Primary key of the user.
- `mFirst_BankKonto`: First time started BankKonto agreement.
- `mFirst_BankKort`: First time started BankKort agreement.
- `mFirst_BankBolån`: First time started BankBolån agreement.
- `mFirst_BoKvar`: First time started BoKvar agreement.
- `mFirst_Pension`: First time started Pension agreement.
- `mFirst_Personbil`: First time started Personbil agreement.
- `mLastStart_BankKort`: Last time started BankKort agreement (if churned, uses random 15-20% churn rate).
- `mLastStart_BankBolån`: Last time started BankBolån agreement (if churned, uses random 20-30% churn rate).
- `mLastStart_BoKvar`: Last time started BoKvar agreement (if churned, uses random 20% churn rate).
- `mLastStart_Pension`: Last time started Pension agreement (if churned, uses random 10% churn rate).
- `mLastStart_Personbil`: Last time started Personbil agreement (if churned, uses random 40% churn rate).
- `Age`: Age of the customer, between 18 and 99.
- `Apartment`: 1 for apartment, 0 for villa/cottage.
- `Woman`: 1 for woman, 0 for man.

## Rules and Constraints

- If a customer has not churned, the first and last start dates should be the same.
- The script generates random dates for each primary key between 2000/01/01 and 2025/01/01.
- The age of the customer is between 18 and 99.
- The script ensures that the data is believable, e.g., a customer aged 18 in 2025 cannot have started a BankBolån agreement in 2000.

## How to Run the Script

1. Install the required Python libraries:
   ```bash
   pip install pandas numpy
   ```
   
2. Run the script:
   ```bash
   python randomGen.py
   ```
3. The script will generate a CSV file named `customer_data.csv` in the same directory.

## Example Usage

```bash
import pandas as pd

# Load the generated CSV file
df = pd.read_csv('customer_data.csv')

# Display the first few rows of the DataFrame
print(df.head())
```

## License
This project is licensed under the MIT License.
