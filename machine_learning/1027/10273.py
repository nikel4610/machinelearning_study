# iris 실루엣 계수 계산
from sklearn.preprocessing import scale
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris = load_iris()

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df = pd.DataFrame(iris.data, columns=features)

# K-Means clustering
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=0).fit(df)
# 데이터당 클러스터 할당
df['cluster'] = kmeans.labels_

# 모든 개별 데이터에 실루엣 계수를 구함
score_samples = silhouette_samples(iris.data, df['cluster'])
df['silhouette_coeff'] = score_samples
average_score = silhouette_score(iris.data, df['cluster'])
# print('silhouette analysis score: {0:.3f}'.format(average_score))
# silhouette analysis score: 0.553

# print(df.groupby('cluster')['silhouette_coeff'].mean())
# cluster
# 0    0.417320
# 1    0.798140 -> 군집화가 가장 잘 됨
# 2    0.451105
# Name: silhouette_coeff, dtype: float64

# https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html?highlight=silhouette