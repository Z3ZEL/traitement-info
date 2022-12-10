from data_reworker import Reworker
from data_regression import Regression
from sklearn import linear_model
import pandas as pd
import numpy as np
import sys

def main():
    #Take the path of the csv file as an argument
    if(len(sys.argv) < 2):
        print("Please provide the path of the csv path of the test data file")
        return
    df = pd.read_csv('res/data.csv')
    df = Reworker(df).rework();
    model = Regression(df).Train()
    df_test = pd.read_csv(sys.argv[1])
    pred = model.Predict(df_test)
    print(pred)
    if (len(sys.argv) >= 3):
        #Save numpy array pred to a csv file without exp notation
        np.set_printoptions(suppress=True)
        np.savetxt("res/saved_result/"+ sys.argv[2] + ".csv", pred, delimiter=",", fmt='%i')


if __name__ == "__main__":
    main()