import pandas as pd
data = pd.read_csv("res/nombre-origine.csv",encoding = 'utf-8', index_col=0)
print(data.head())