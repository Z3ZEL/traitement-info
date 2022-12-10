from pickle import LONG
from data_reworker import Reworker
from data_regression import Regression
from sklearn import linear_model
import pandas as pd
import numpy as np
import sys


def get_means(df):
    #Get the mean of each column
    df = df.astype(LONG)
    means = df.mean(skipna=True)
    
    #Convert the series to a dictionary
    means = means.to_dict()
    return means

def main():
    #Take the path of the csv file as an argument
    if(len(sys.argv) < 2):
        print("Please provide the path of the csv path of the test data file")
        return

    df = pd.read_csv('res/data.csv')
    df = Reworker(df).rework();
    # #Select only GBP and Art
    # df = df[df['currency '] == 1]
    # df = df[df['main_category '] == 7]

    
    df = df[df['currency '] == 5]
    df = df[df['main_category '] == 6]

    #df = df[df['pledged '] >= df['goal ']]

    print(len(df))

    means = get_means(df)
    print(df.head())

    print(means)

#    df_reworked['main_category '] = df_reworked['main_category '].map({'Film & Video': 1, 'Music': 2, 'Publishing': 3, 'Games': 4, 'Technology': 5, 'Design': 6, 'Art': 7, 'Food': 8, 'Fashion': 9, 'Theater': 10, 'Comics': 11, 'Photography': 12, 'Crafts': 13, 'Journalism': 14, 'Dance': 15})

    # for i in range(0,16):
    #     df_temp = df[df['main_category '] == i]
    #     if(len(df_temp) == 0):
    #         continue

    #     df_temp.drop(['duration ','currency ','main_category '], axis=1, inplace=True)
    #     model = Regression(df_temp).Train()
    #     df_test = pd.read_csv(sys.argv[1])
    #     pred = model.Predict(df_test)
    #     if (len(sys.argv) >= 3):
    #         #Save numpy array pred to a csv file without exp notation
    #         np.set_printoptions(suppress=True)
    #         np.savetxt("res/saved_result/"+ sys.argv[2]+str(i)+ ".csv", pred, delimiter=",", fmt='%i')

    # df_temp = df[['goal ','pledged ','backers ']]
    # model = Regression(df_temp).TrainToPredict()
    # df_test = pd.read_csv(sys.argv[1])
    # pred = model.Predict(df_test)
    # #Save numpy array pred to a csv file without exp notation
    # np.set_printoptions(suppress=True)
    # np.savetxt("res/saved_result/"+ sys.argv[2]+".csv", pred, delimiter=",", fmt='%i')


if __name__ == "__main__":
    main()