# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df)
p_b = len(df[df['purpose']== 'debt_consolidation'])/len(df)
df1 = df[df['purpose']== 'debt_consolation']
p_and_b = df[(df['fico']>700) & (df['purpose']== 'debt_consolidation')]
p_a_b = (len(p_and_b)/len(df))/p_a
print(p_a_b)
result = p_a_b == p_b
print(result)
# code ends here


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)
new_df = df[df['paid.back.loan'] == 'Yes']
p_and_b = df[(df['paid.back.loan'] == 'Yes') & (df['credit.policy'] == 'Yes')]
prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
print(prob_pd_cs)
bayes = (prob_pd_cs*prob_lp)/prob_cs
print(bayes)
# code ends here


# --------------
# code 
df1 = df[df['paid.back.loan'] == 'No']
df1['purpose'].value_counts().plot.bar()

# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
import matplotlib.pyplot as plt
plt.hist(df['installment'])
plt.hist(df['log.annual.inc'])

# code ends here


