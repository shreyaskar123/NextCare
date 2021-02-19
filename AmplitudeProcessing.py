import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math
import numpy as np
meanAcc = df['accX'].mean()
meanTime = df['time'].mean()
varTime = df['time'].to_numpy()
df['accX'].replace(np.nan,meanAcc,inplace = True)
df['accY'].replace(np.nan,meanAcc,inplace = True)
df['accZ'].replace(np.nan,meanAcc,inplace = True)
xAcc = df['accX'].to_numpy()
yAcc = df['accY'].to_numpy()
zAcc = df['accZ'].to_numpy()
df['time'].replace(np.nan,meanTime,inplace = True)
print(varTime[0:20])

    
   
