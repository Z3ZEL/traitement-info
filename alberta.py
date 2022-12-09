import pandas as pd
import prince

data1 = pd.read_csv("res/alberta-superficie-mois.csv")
data2 = pd.read_csv("res/alberta-ori-mois.csv")

#means of years for each month
means_superficie_per_months = data1.values[:,3:].mean(axis=1);
