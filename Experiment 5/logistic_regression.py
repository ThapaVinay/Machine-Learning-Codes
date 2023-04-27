import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = pd.read_csv("Iris.csv")
print(iris.head(4))
print(iris.shape)         # dimensions of the dataset
print(iris.isnull().sum())      # to check any null values 


X = iris.drop("Species", axis = 1)
print(X)
y = iris["Species"]
print(y)



# assigning index to the categorical target 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y) 


# fitting the model 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

model = LogisticRegression(max_iter=1000)   # add max iteration to remove the error 
model.fit(X_train, y_train)

# making the predictions
predictions = model.predict(X_test)
print("Predictions :",predictions)

# checking the accuracy of the model
from sklearn.metrics import accuracy_score
print("Accuracy :", accuracy_score(y_test, predictions))

# plotting the residuals
residuals = y_test - predictions
plt.scatter(np.arange(len(residuals)), residuals)
plt.ylabel('Residual')
plt.title('Residual Plot')
plt.show()
