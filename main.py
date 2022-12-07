import numpy as np; 
import pandas as pd
import prince
from sklearn import datasets

data = pd.read_csv('res/nombre-origine.csv',encoding = 'ISO-8859-1', index_col=0)
#data = pd.DataFrame(data=data, columns=["Juridiction","Origine","Année","Qualificatifs de données","Nombre (nul)"])

#show
data.head()
