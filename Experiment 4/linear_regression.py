
# OLS is also used for linear regression just like sklearn but OLS provides more detailed statistical summaries of the model


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

file = pd.read_csv("salary.csv")
print(file.head(5))

x = file['Years Of Experience'] 
X = sm.add_constant(x)
y = file['Salary']

result = sm.OLS(y,X).fit()
print(result.summary())
y_pred = result.predict(X)

intercept = result.params["const"]
print("INTERCEPT :", intercept)
gradient = result.params["Years Of Experience"]
print("GRADIENT", gradient)

plt.scatter(x,y, color = 'r')
plt.scatter(x,gradient * x + intercept, color= 'g')
plt.plot(x,y_pred, color = 'b')
plt.show()