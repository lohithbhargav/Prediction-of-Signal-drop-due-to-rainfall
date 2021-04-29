import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("Implementation\Dataset_1.csv")
X = np.array(data)[:,0].reshape(-1,1)
x = np.array(data)[:,1].reshape(-1,1)
y = np.array(data)[:,2].reshape(-1,1)
z = np.array(data)[:,3].reshape(-1,1)

plt.title('Data Visualization for Signal Loss at Heavy Rainfall Conditions')  
plt.xlabel('Loss of Signal')  
plt.ylabel('Days') 
plt.plot(X,z,color="red")
plt.show()