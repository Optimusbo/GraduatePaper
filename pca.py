from dataforpandastest import data,columns
import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

data = data
columns = columns

for column in columns:
    data[column] = (data[column]-np.mean(data[column]))/np.std(data[column])

pca = PCA()
pca.fit(data)
n_components = pca.components_
explained_variance = pca.explained_variance_
A = np.diag(explained_variance)
explained_variance_ratio = pca.explained_variance_ratio_
U = n_components
for i in range(0, 5):
    explained_variance[i] = explained_variance[i]**(1.0/2.0)
A = np.diag(explained_variance)
FLM = np.dot(U, A)
#explained_variance_ratio = pd.DataFrame(explained_variance_ratio)
#explained_variance = pd.DataFrame(explained_variance)
#explained_variance_ratio.to_excel('explained_variance_ratio.xls')
#explained_variance.to_excel('explained_variance.xls')

explained_variance = pca.explained_variance_
for i in range(0, 5):
    explained_variance[i] = 1.0/(explained_variance[i]**(1.0/2.0))
A = np.diag(explained_variance)

SM = np.dot(np.dot(data, U), A)
score = (0.55740*SM[:, 0]+0.27992*SM[:, 1])/(0.55740+0.27992)
score = score.T
score = pd.DataFrame(score)
score.index = data.index
score.columns = ['score']
score = score.sort_values(by=['score'], ascending=False)
#score.to_excel('score.xls')
#FLM = pd.DataFrame(FLM)
#FLM.to_excel('flm.xls')
