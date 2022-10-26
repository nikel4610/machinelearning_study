import pandas as pd

df = pd.read_excel('D:/vsc_project/machinelearning_study/default of credit card clients.xls', header=1, sheet_name='Data').iloc[0:, 1:]
# print(df.head())

df.rename(columns={'PAY_0':'PAY_1', 'default payment next month':'default'}, inplace=True)
y_target = df['default']
x_features = df.drop('default', axis=1)
# print(y_target.value_counts())