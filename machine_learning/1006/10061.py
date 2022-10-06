import pandas as pd
import matplotlib.pyplot as plt

feature_name_df = pd.read_csv('human_activity/features.txt', sep='\s+', header=None, names=['column_index', 'column_name'])
feature_name = feature_name_df.iloc[:,1].values.tolist()
# print('전체 피처명에서 10개만 추출:', feature_name[:10])
# 전체 피처명에서 10개만 추출: ['tBodyAcc-mean()-X', 'tBodyAcc-mean()-Y', 'tBodyAcc-mean()-Z', 'tBodyAcc-std()-X', 'tBodyAcc-std()-Y', 
#                             'tBodyAcc-std()-Z', 'tBodyAcc-mad()-X', 'tBodyAcc-mad()-Y', 'tBodyAcc-mad()-Z', 'tBodyAcc-max()-X']

feature_dup_df = feature_name_df.groupby('column_name').count()
# print('데이터 세트 내 중복 피처명:', feature_dup_df[feature_dup_df['column_index'] > 1].count())
# 데이터 세트 내 중복 피처명: column_index    42
# dtype: int64

