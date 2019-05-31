# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.DataFrame(pd.read_csv(path))
#print(bank)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)


numerical_var =  bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here


#code ends here
banks = bank.drop('Loan_ID',axis=1)
#print(banks)

print(banks.isnull().sum())

bank_mode = banks.mode


banks = banks.fillna(bank_mode)
print(banks.isnull().sum())



# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index = ['Gender', 'Married', 'Self_Employed'], values='LoanAmount')


print(avg_loan_amount)
# code ends here
#convert_dict = {'LoanAmount': float}
  
#banks = banks.astype(convert_dict) 

#banks['LoanAmount'] = pd.to_numeric(banks['LoanAmount'] , errors='coerce')print(banks.dtypes)



# --------------
# code starts here



# code ends here
loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)

loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)

percentage_se = (loan_approved_se/614)*100
print(percentage_se)
percentage_nse = (loan_approved_nse/614)*100
print(percentage_nse)


# --------------
# code starts here

#print( banks['Loan_Amount_Term'].isnull().sum())
#print( 'Nan' in banks['Loan_Amount_Term'])
#banks['Loan_Amount_Term']= banks['Loan_Amount_Term'].str.split().astype(str).astype(float)
#print(banks.dtypes)
#banks['Loan_Amount_Term'].unique()
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12)
big_loan_term = len(banks[loan_term>=25])
print(big_loan_term)
# code ends here



# --------------
# code starts here

loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()

print(mean_values)
# code ends here


