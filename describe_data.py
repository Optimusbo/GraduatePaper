import pandas as pd
import numpy as np


data = pd.read_csv('finacial_data_2017.csv')
columns = data.columns
columns = columns.drop('Unnamed: 0')
data = data[columns]
data = data.drop([36, 91, 132], axis=0)
data.index = data['code']
columns = data.columns
columns = columns.drop('code')
describe = data.describe()
describe.to_excel('describe.xls')

#load data
data_2017 = pd.read_csv('finacial_data_2017.csv')
columns = data_2017.columns
columns = columns.drop('Unnamed: 0')
data_2017 = data_2017[columns]
data_2017.index = data_2017['code']
data_2016 = pd.read_csv('finacial_data_2016.csv')
columns = data_2016.columns
columns = columns.drop('Unnamed: 0')
data_2016 = data_2016[columns]
data_2016.index = data_2016['code']
data_2015 = pd.read_csv('finacial_data_2015.csv')
columns = data_2015.columns
columns = columns.drop('Unnamed: 0')
data_2015 = data_2015[columns]
data_2015.index = data_2015['code']
#merge data
data_2017 = data_2017.drop([2198, 300142, 2693, 600645], axis=0)
data_2016 = data_2016.drop([2198, 300142, 2693], axis=0)
data_2015 = data_2015.drop([2198, 300142, 2693, 597, 606, 600671, 518, 790], axis=0)
frames = [data_2017, data_2016, data_2015]
table = pd.concat(frames)
#describe data
describe_2017 = data_2017.describe()
describe_2016 = data_2016.describe()
describe_2015 = data_2015.describe()
table_describe = table.describe()
#corr
columns = columns.drop(['code'])
data = data[columns]
corr = data.corr()
# get code

