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

# nan값 제거
train_df = train_df.dropna()

# rankpoint 제거
train_df = train_df.drop(['rankPoints', 'numGroups', 'groupId', 'matchId'], axis=1)
test_df = test_df.drop(['rankPoints', 'numGroups', 'groupId', 'matchId'], axis=1)

# walkDistance = 0 and weaponsAcquired >= 3 데이터 지우기
train_df = train_df.drop(train_df[(train_df['walkDistance'] == 0) & (train_df['weaponsAcquired'] >= 3)].index)

# 전체 이동한 거리 구하기
train_df['distance'] = train_df['rideDistance'] + train_df['swimDistance'] + train_df['walkDistance']
train_df = train_df.drop(['rideDistance', 'swimDistance', 'walkDistance'], axis=1)

# 전체 처치 수 구하기
train_df['Kills_and_headshotKills'] = train_df['kills'] + train_df['headshotKills'] + train_df['roadKills']
train_df = train_df.drop(['kills', 'headshotKills', 'roadKills'], axis=1)

# winPlacePerc와 상관관계가 낮은 데이터 지우기
train_df = train_df.drop(['assists', 'DBNOs', 'killPlace', 'killPoints', 'matchDuration', 'revives',
                          'teamKills', 'vehicleDestroys', 'winPoints'], axis=1)

print(train_df.info())

# solo, duo, squad, solo-fpp, duo-fpp, squad-fpp 나누기
solo_train = train_df[train_df['matchType'] == 'solo'] # 6
duo_train = train_df[train_df['matchType'] == 'duo'] # 5
squad_train = train_df[train_df['matchType'] == 'squad'] # 3
solo_fpp_train = train_df[train_df['matchType'] == 'solo-fpp'] # 4
duo_fpp_train = train_df[train_df['matchType'] == 'duo-fpp'] # 2
squad_fpp_train = train_df[train_df['matchType'] == 'squad-fpp'] # 1

solo_train = solo_train.drop(['matchType'], axis=1)
duo_train = duo_train.drop(['matchType'], axis=1)
squad_train = squad_train.drop(['matchType'], axis=1)
solo_fpp_train = solo_fpp_train.drop(['matchType'], axis=1)
duo_fpp_train = duo_fpp_train.drop(['matchType'], axis=1)
squad_fpp_train = squad_fpp_train.drop(['matchType'], axis=1)


