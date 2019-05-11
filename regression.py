from pca import score
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#total assets and perundp
score = score
code = score.index
code = pd.DataFrame(code)

basic = pd.read_csv('basic_data.csv')

tA = pd.DataFrame()
for i in code['code']:
    i = int(i)
    tA = tA.append(basic.ix[basic['code']==i])

tA.index = tA['code']
tA = tA[['code', 'totalAssets', 'perundp']]

#current assets turnover
cato = pd.read_csv('operation_data_2017.csv')
columns = cato.columns
columns = columns.drop('Unnamed: 0')
cato = cato[columns]
cO = pd.DataFrame()
for i in code['code']:
    i = int(i)
    cO = cO.append(cato.ix[cato['code']==i])
cO.index = cO['code']
cO = cO[['code', 'currentasset_turnover']]

#mbrg
mbrg = pd.read_csv('growth_data_2017.csv')
columns = mbrg.columns
columns = columns.drop('Unnamed: 0')
mbrg = mbrg[columns]
mB = pd.DataFrame()
for i in code['code']:
    i = int(i)
    mB = mB.append(mbrg.ix[mbrg['code']==i])
mB.index = mB['code']
mB = mB[['code', 'mbrg']]

#cashflow ratio
csfl = pd.read_csv('cashflow_data_2017.csv')
columns = csfl.columns
columns = columns.drop('Unnamed: 0')
csfl = csfl[columns]
cR = pd.DataFrame()
for i in code['code']:
    i = int(i)
    cR = cR.append(csfl.ix[csfl['code']==i])
cR.index = cR['code']
cR = cR[['code', 'cashflowratio']]

#current ratio
crrt = pd.read_csv('debtpaying_data_2017.csv')
columns = crrt.columns
columns = columns.drop('Unnamed: 0')
crrt = crrt[columns]
cT = pd.DataFrame()
for i in code['code']:
    i = int(i)
    cT = cT.append(crrt.ix[crrt['code']==i])
cT.index = cT['code']
cT = cT[['code', 'currentratio']]

#merged data
data = pd.merge(tA, cO)
data = pd.merge(data, mB)
data = pd.merge(data, cR)
data = pd.merge(data, cT)

#data preprocessing
data.index = data['code']
data['totalAssets'] = np.log(data['totalAssets'])

#regression
columns = data.columns
columns = columns.drop('code')
X = data[columns]
y = score['score']
reg = LinearRegression()
reg.fit(X, y)
intercept = reg.intercept_
coef = reg.coef_
Rsquare = reg.score(X, y)
