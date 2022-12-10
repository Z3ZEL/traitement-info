import numpy as np
import pandas as pd

def generate_backers_test():
    df = pd.DataFrame(columns=['goal ','backers ','currency ','main_category ','duration '])
    # add 1000 rows with 0 
    df = df.append(pd.DataFrame(np.zeros((5000, 5)), columns=['goal ','backers ','currency ','main_category ','duration ']))

    #fill goal with 50000
    df['goal '] = 50000
    df['currency '] = 1
    df['main_category '] = 1
    df['duration '] = 30*24*60*60

    #fill backers with increasing
    df['backers '] = np.arange(0, 5000, 1)

    print(df.head())
    return df
def generate_currency_test():
    df = pd.DataFrame(columns=['goal ','backers ','currency ','main_category ','duration '])
    # add 22 rows with 0 
    df = df.append(pd.DataFrame(np.zeros((22, 5)), columns=['goal ','backers ','currency ','main_category ','duration ']))

    #fill goal with 50000
    df['goal '] = 50000
    df['backers '] = 576
    df['main_category '] = 1
    df['duration '] = 30*24*60*60

    #fill backers with increasing
    df['currency '] = np.arange(0, 22, 1)

    print(df.head())
    return df
def generate_duration():
    df = pd.DataFrame(columns=['goal ','duration '])
    # add 30*5 rows with duration increasing by one day each row for five different goal
    df = df.append(pd.DataFrame(np.zeros((30*5, 2)), columns=['goal ','duration ']))

    #fill goal with pattern 1000, 10000, 50000, 100000, 500000
    df['goal '] = np.repeat([1000, 10000, 50000, 100000, 500000], 30)

    #fill duration with pattern  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
    df['duration '] = np.tile(np.arange(1, 31, 1), 5)*24*60*60




    return df

def generate_main_category():
    df = pd.DataFrame(columns=['goal ','backers '])
    # add 30*5 rows with duration increasing by one day each row for five different goal
    df = df.append(pd.DataFrame(np.zeros((25, 2)), columns=['goal ','backers ']))

    #fill goal with pattern 1000, 10000, 50000, 100000, 500000
    df['goal '] = np.tile([1000, 10000, 50000, 100000, 500000], 5)

    #fill backers with repeat 10 50 100 1000 5000
    df['backers '] = np.repeat([10, 50, 100, 1000, 5000], 5)

    return df

def generate_pledged():
    #generate unique column pledged from 100 to 1 000 000 with 1000 rows
    df = pd.DataFrame(columns=['pledged '])
    df = df.append(pd.DataFrame(np.zeros((1000, 1)), columns=['pledged ']))
    df['pledged '] = np.arange(100, 1000000, 1000)
    return df

def save_to_csv(df, filename):
    df.to_csv("res/test_data/"+filename+'.csv', index=False)


#save_to_csv(generate_backers_test(), "backers_test")
#save_to_csv(generate_currency_test(), "currency_test")
#save_to_csv(generate_duration(), "duration_test")
# save_to_csv(generate_main_category(), "main_category_test")

save_to_csv(generate_pledged(), "pledged_test")