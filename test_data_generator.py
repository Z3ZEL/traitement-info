import numpy as np
import pandas as pd

def generate_backers_test():
    df = pd.DataFrame(columns=['goal ','backers ','country ','currency ','main_category ','duration '])
    # add 1000 rows with 0 
    df = df.append(pd.DataFrame(np.zeros((5000, 6)), columns=['goal ','backers ','country ','currency ','main_category ','duration ']))

    #fill goal with 50000
    df['goal '] = 50000
    df['country '] = 1
    df['currency '] = 1
    df['main_category '] = 1
    df['duration '] = 30*24*60*60

    #fill backers with increasing
    df['backers '] = np.arange(0, 5000, 1)

    print(df.head())
    return df
def generate_country_test():
    df = pd.DataFrame(columns=['goal ','backers ','country ','currency ','main_category ','duration '])
    # add 1000 rows with 0 
    df = df.append(pd.DataFrame(np.zeros((5000, 6)), columns=['goal ','backers ','country ','currency ','main_category ','duration ']))

    #fill goal with 50000
    df['goal '] = 50000
    df['backers '] = 576
    df['currency '] = 1
    df['main_category '] = 1
    df['duration '] = 30*24*60*60

    #fill backers with increasing
    df['country '] = np.arange(0, 5000, 1)

    print(df.head())
    return df



def save_to_csv(df, filename):
    df.to_csv("res/test_data/"+filename+'.csv', index=False)


#save_to_csv(generate_backers_test(), "backers_test")