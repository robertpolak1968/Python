# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#http://matplotlib.org/
#http://matplotlib.org/api/pyplot_api.html
#http://matplotlib.org/api/pyplot_api.html

print('same line1')
x = np.arange(0, 5, 0.1)
y = np.sin(x)
#plt.plot(x, y)
print('same line2')

#plt.plot([1,2,3])

#plt.plot([10, 20, 30, 40], [5, 10, 15, 20])

#arr = np.array([[1, 2, 3], [4, 5, 6]], float)
#plt.plot(arr)


# plots one line
plt.plot([10, 20, 30, 40,55], [5, 10, 15, 20,-12])
#plots a second line
#plt.plot([4, 50], [60, 35])

plt.show()

# generate a random walk time-series
np.random.seed(19)
s = pd.Series(np.random.randn(1096),index=pd.date_range('2014-01-01','2016-12-31'))
walk_ts = s.cumsum()
#walk_ts.plot();

#df = pd.DataFrame(np.random.randn(1096, 2),index=pd.date_range('2014-01-01','2014-16-31'), columns=list('AB'))
#walk_df = df.cumsum()
#walk_df.head()
#walk_df.plot()

df = pd.read_csv("C:\\Users\\R00078187\\Documents\\titanic.csv")
# filter the dataframe to only return rows
# where the passenger died
criteria = df['Survived']==0
fatalities = df[criteria]
pclassGroup = fatalities.groupby("Pclass")
# extract the Survived column from the groupby object
classSurived = pclassGroup['Survived'].count()
print (classSurived)
classSurived.plot()
plt.show()
