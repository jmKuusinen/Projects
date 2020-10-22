# Program to predict stocks 
# Depenencies

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

#stockData = pd.read_csv("Ntyres_Stock.csv")
#stockData.head(6)