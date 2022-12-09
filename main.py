import pandas as pd
from sklearn import linear_model

df = pd.read_csv('res/data.csv')
df = df.drop(['ID ','name ','category ','main_category ','state ','deadline ','launched ','usd pledged ','Unnamed: 13','Unnamed: 14', 'Unnamed: 15','Unnamed: 16'], axis=1)

#Erase all rows with NaN values
df = df.dropna()

df_reworked= df[['goal ','pledged ','backers ']]

#Clean all none numeric values
df_reworked = df_reworked[df_reworked['goal '].str.isnumeric()]
df_reworked = df_reworked[df_reworked['pledged '].str.isnumeric()]
df_reworked = df_reworked[df_reworked['backers '].str.isnumeric()]


model = linear_model.LinearRegression();
model.fit(df_reworked[['goal ','backers ']], df_reworked['pledged '])

df_test = pd.read_csv('res/test.csv')
pred = model.predict(df_test[['goal ','backers ']])
print(pred)
