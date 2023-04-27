import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv('archive/Mall_Customers.csv')
print(df.head())

X = df.drop(columns=['CustomerID','Genre']).values    # returns as a numpy array not dataframe
print(X)

# plt.figure(figsize = (10,6))
# plt.scatter(X[:,0], X[:,2])
# plt.show()

from sklearn.cluster import DBSCAN


for i in np.arange(10,50,0.1):
    db = DBSCAN(eps = i, min_samples=20)
    db.fit(X)
    labels = db.labels_
    # print(db.labels_[db.labels_ == -1])
    from collections import Counter
    print(Counter(labels), " ", i)

# y_pred = db.fit_predict(X)
# plt.figure(figsize=(10,6))
# plt.scatter(X[:,0], X[:,1],c=y_pred, cmap='Paired')



# plt.show()
