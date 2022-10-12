import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import pandas as pd

df = pd.read_csv('data-master\pima-indians-diabetes3.csv')

df.drop(['pressure', 'thickness'], axis=1, inplace=True)
df.head()
