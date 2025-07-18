import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt
data=pd.read_csv("train.csv")
print(data.columns)
#sbn.pairplot(data)
#plt.show()
data=data.drop(["Row ID","Order ID","Customer ID","Product ID"],axis=1)
print(data.columns)
print(data.isnull().count())

