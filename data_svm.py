from pickle import LONG
from data_reworker import Reworker
from data_regression import Regression
from sklearn import linear_model
import pandas as pd
import numpy as np
import sys
import sklearn as sk
import matplotlib.pyplot as plt


df = pd.read_csv('res/data.csv')
df = Reworker(df).rework();
df.drop(['duration '], axis=1, inplace=True)

#Select only GBP and Art
df = df[df['currency '] == 1]
df = df[df['main_category '] == 7]

#erase rows with 0 backers or 0 pledged
df = df[df['backers '] != 0]
df = df[df['pledged '] != 0]

#erase rows with pledged > 250 000 and backers > 2000 goal > 100 000
df = df[df['pledged '] < 250000]
df = df[df['backers '] < 2000]
df = df[df['goal '] < 100000]

#erase all rows with pledged < goal

df = df[df['pledged '] >= df['goal ']]


#erase rows with inf or nan
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

print('data cleaned')







#plot in 3-D graph pledged vs backers vs goal
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(df['backers '], df['goal '], df['pledged '], c='r', marker='o')
# ax.set_xlabel('backers')
# ax.set_ylabel('goal')
# ax.set_zlabel('pledged')
# plt.show()



test = pd.DataFrame(columns=['backers ','goal '])
#add 100 rows
test = test.append(pd.DataFrame(np.zeros((1000, 2)), columns=['backers ','goal ']))
test['backers '] = 46
test['goal '] = np.arange(0,250000,250)

model = sk.svm.SVR(kernel="linear",verbose=True)
model.fit(df[['backers ','goal ']], df['pledged '])


pred = model.predict(test)
print(pred)

#save
np.savetxt("res/saved_result/"+ sys.argv[1]+".csv", pred, delimiter=",", fmt='%i')



