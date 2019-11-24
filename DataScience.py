import math

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib inline
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({'a':[1,2,3,4,5,6,7],
'b':[1,4,9,16,25,36,49]})
df.plot()