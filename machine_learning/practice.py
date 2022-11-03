import numpy as np
import pandas as pd
import gc
import time
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier, plot_importance

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 300)
pd.set_option('display.max_colwidth', 30)

app_train = pd.read_csv('D:/vsc_project/machinelearning_study/home-credit-default-risk/application_train.csv')
app_test = pd.read_csv('D:/vsc_project/machinelearning_study/home-credit-default-risk/application_test.csv')
