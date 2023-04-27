import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score

df = pd.read_csv('Iris.csv')
print(df.head(5))

X = df.drop('Species', axis=1)
y = df['Species']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf = RandomForestClassifier(n_estimators=50)
rf.fit(X_train,y_train)
ypred = rf.predict(X_test)
accuracy = accuracy_score(y_test,ypred)
cm = confusion_matrix(y_test, ypred)

precision = precision_score(y_test, ypred, average='macro')
recall = recall_score(y_test, ypred, average='macro')

print("Accuracy of the Model: ",accuracy)
print("Confusion matrix:", cm)
print("Precision Score: ", precision)
print("Recall Score: ",recall)


