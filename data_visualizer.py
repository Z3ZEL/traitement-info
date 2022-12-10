#Visualize data with matplotlib multiple data sets in args with csv path 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def backer_comparison():
    #Take all the path of the csv file as an argument
    if(len(sys.argv) < 2):
        print("Please provide the path of the csv path of the test data file")
        return
    #Create a list of dataframes
    dfs = []
    for i in range(1, int(sys.argv[2])):
        dfs.append(pd.read_csv("res/saved_result/"+sys.argv[1] + str(i) + ".csv"))

    #Display data on the same graph with df index as x axis and df value as y axis
    for df in dfs:
        plt.plot(df.index, df)
    #D{'USD': 1, 'GBP': 2, 'CAD': 3, 'AUD': 4, 'EUR': 5, 'SEK': 6, 'MXN': 7, 'NZD': 8, 'DKK': 9, 'NOK': 10, 'CHF': 11, 'HKD': 12, 'SGD': 13, 'JPY': 14})

    legends = ['USD', 'GBP', 'CAD', 'AUD', 'EUR', 'SEK', 'MXN', 'NZD', 'DKK', 'NOK', 'CHF', 'HKD', 'SGD', 'JPY']
    plt.legend(legends)
    plt.xlabel('Backer number')
    plt.ylabel('Pledged amount')

    plt.show()

# backer_comparison()


def duration_comparison():
    #take duration_test.csv and duration_result.csv as arguments and display the result in function of the duration and the color depending on the goal
    result = pd.read_csv("res/saved_result/duration_result.csv")
    test = pd.read_csv("res/test_data/duration_test.csv")
    print(result.shape)
    print(test.shape)
    #Display data on the same graph with duration as x axis and pledged as y axis and color depending on the goal
    plt.scatter(test.values[1:,1], result, c=test.values[1:,0], cmap='viridis')

    plt.xlabel('Duration')
    plt.ylabel('Pledged amount')

    plt.show()

def main_category_comparison():
#Take all the path of the csv file as an argument
    if(len(sys.argv) < 2):
        print("Please provide the path of the csv path of the test data file")
        return
    #Create a list of dataframes
    test = pd.read_csv("res/test_data/main_category_test.csv")
    dfs = []
    for i in range(1, int(sys.argv[2])):
        dfs.append(pd.read_csv("res/saved_result/"+sys.argv[1] + str(i) + ".csv"))

    #Display data on the same graph with df index as x axis and df value as y axis
    for df in dfs:
        plt.plot(test.values[1:,1], df)
#df_reworked['main_category '] = df_reworked['main_category '].map({'Film & Video': 1, 'Music': 2, 'Publishing': 3, 'Games': 4, 'Technology': 5, 'Design': 6, 'Art': 7, 'Food': 8, 'Fashion': 9, 'Theater': 10, 'Comics': 11, 'Photography': 12, 'Crafts': 13, 'Journalism': 14, 'Dance': 15})

    legends = ['Film & Video', 'Music', 'Publishing', 'Games', 'Technology', 'Design', 'Art', 'Food', 'Fashion', 'Theater', 'Comics', 'Photography', 'Crafts', 'Journalism', 'Dance']
    plt.legend(legends)
    plt.xlabel('Backers number')
    plt.ylabel('Pledged amount')

    plt.show()


def pledged_comparison():
    #show the backers needed in function of the goal
    df = pd.read_csv("res/saved_result/pledged_result.csv")

    plt.plot(df.values[:,1], df.values[:,0])
    plt.xlabel('Goal number')
    plt.ylabel('Backers number')

    plt.show()



#duration_comparison()
#main_category_comparison()
pledged_comparison()