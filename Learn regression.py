import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
import pandas as pd

df=pd.read_csv('Housing.csv')
X=df['lotsize']
Y=df['price']
X=X.values.reshape(len(X),1)
Y=Y.values.reshape(len(Y),1)
X_train=X[:-100]
Y_train=Y[:-100]
X_test=X[-100:]
Y_test=Y[-100:]

plt.scatter(X_test, Y_test, color='green')
plt.title('Test Data')
plt.xlabel('Size')
plt.ylabel('Price')
plt.xticks(())
plt.yticks(())

# Create Linear Regression Object
regr=linear_model.LinearRegression()

# Train the model using the training set and find (coefficienct of array and intercept)
regr.fit(X_train,Y_train)
#print(regr.coef_)
plt.plot(X_test, regr.predict(X_test), color='red', linewidth=3)
##plt.show()
print(str(round(regr.predict([5000]))))


