import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Implementation\Dataset_1.csv")
X = np.array(data)[:,0].reshape(-1,1)
x = np.array(data)[:,1].reshape(-1,1)
y = np.array(data)[:,2].reshape(-1,1)
z = np.array(data)[:,3].reshape(-1,1)

plt.title('Data Visualization for Signal Loss at No Rainfall Conditions')  
plt.xlabel('Days')  
plt.ylabel('Loss of Signal') 
plt.plot(X,x,color="red")
plt.show()