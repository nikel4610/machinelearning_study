from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()

columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
df = pd.DataFrame(iris.data, columns=columns)
df['target'] = iris.target

markers = ['^', 's', 'o']

for i, marker in enumerate(markers):
    x_axis_data = df[df['target'] == i]['sepal_length']
    y_axis_data = df[df['target'] == i]['sepal_width']
    plt.scatter(x_axis_data, y_axis_data, marker=marker, label=iris.target_names[i])

plt.legend()
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

# 정규화
iris_scaled = StandardScaler().fit_transform(df)

# fit() 과 transform() 을 호출하여 PCA 변환 데이터 반환
pca = PCA(n_components=2)
pca.fit(iris_scaled)
iris_pca = pca.transform(iris_scaled)

pca_col = ['pca_component_1', 'pca_component_2']
df_pca = pd.DataFrame(iris_pca, columns=pca_col)
df_pca['target'] = iris.target

markers = ['^', 's', 'o']
for i, marker in enumerate(markers):
    x_axis_data = df_pca[df_pca['target'] == i]['pca_component_1']
    y_axis_data = df_pca[df_pca['target'] == i]['pca_component_2']
    plt.scatter(x_axis_data, y_axis_data, marker=marker, label=iris.target_names[i])

plt.legend()
plt.xlabel('pca_component_1')
plt.ylabel('pca_component_2')
plt.show()

rcf = RandomForestClassifier(random_state=156)

scores = cross_val_score(rcf, iris.data, iris.target, scoring='accuracy', cv=3)
# pca 로 차원 축소
pca_x = df_pca[['pca_component_1', 'pca_component_2']]
scores_pca = cross_val_score(rcf, pca_x, iris.target, scoring='accuracy', cv=3)

print(scores)
print(np.mean(scores))
# [0.98 0.94 0.96]
# 0.96

print(scores_pca)
print(np.mean(scores_pca))
# [0.98 0.98 1.  ]
# 0.9866666666666667