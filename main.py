import numpy as np; 
import pandas as pd
import prince
from sklearn import datasets

X, y = datasets.load_files('../res/superficie-mois.csv', encoding='utf-8', return_X_y=True)
