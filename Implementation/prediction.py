import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data=pd.read_csv("Implementation\Dataset_1.csv")

X = np.array(data)[:,0].reshape(-1,1)
x = np.array(data)[:,1].reshape(-1,1)
y = np.array(data)[:,2].reshape(-1,1)
z = np.array(data)[:,3].reshape(-1,1)

#for No Rain
to_predict_X= [31,32,33]
to_predict_X= np.array(to_predict_X).reshape(-1,1)
regsr=LinearRegression()
regsr.fit(X,x)
predicted_x= regsr.predict(to_predict_X)
m= regsr.coef_
c= regsr.intercept_
print("For No Rain")
print("Predicted x:\n",predicted_x)
print("slope (m): ",m)
print("y-intercept (c): ",c)
print("\n")

#for Light Rain
to_predict_Y= [31,32,33]
to_predict_Y= np.array(to_predict_Y).reshape(-1,1)
regsr=LinearRegression()
regsr.fit(X,y)
predicted_y= regsr.predict(to_predict_Y)
m= regsr.coef_
c= regsr.intercept_
print("For Light Rain")
print("Predicted x:\n",predicted_y)
print("slope (m): ",m)
print("y-intercept (c): ",c)
print("\n")

#for Heavy Rain
to_predict_Z= [31,32,33]
to_predict_Z= np.array(to_predict_Z).reshape(-1,1)
regsr=LinearRegression()
regsr.fit(X,z)
predicted_z= regsr.predict(to_predict_Z)
m= regsr.coef_
c= regsr.intercept_
print("For Heavy Rain")
print("Predicted x:\n",predicted_z)
print("slope (m): ",m)
print("y-intercept (c): ",c)
