# Decision tree
'''
entropy -> amount of randomness in the sample {no randomness = less entropy = High information gain}
gini impurity -> it is used when the computation is less because it does not use log function
* they both are used to find how pure the split is?

'''


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("Decision_Tree_ Dataset.csv")

X = data.drop('target', axis=1)
y = data['target']


# converting into numerical form but even categorical works ?
# from sklearn.preprocessing import LabelEncoder
# le = LabelEncoder()
# y = le.fit_transform(y)
# print(y)
print(X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Prediction:", y_pred)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)


# display the decision tree
from sklearn import tree
import matplotlib.pyplot as plt
tree.plot_tree(model, feature_names = X.columns, class_names = ['0', '1'], filled = True  )
plt.show()
