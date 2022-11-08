import numpy as np
import pandas as pd
import gc
import time
import matplotlib.pyplot as plt
import seaborn as sns

train_df = pd.read_csv('D:/vsc_project/machinelearning_study/pubg-finish-placement-prediction/train_V2.csv')
test_df = pd.read_csv('D:/vsc_project/machinelearning_study/pubg-finish-placement-prediction/test_V2.csv')

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 200)

# nan값 확인
# print(train_df.isnull().sum())
# print(test_df.isnull().sum())
# winPlacePerc       1

# nan값 제거
train_df = train_df.dropna()
