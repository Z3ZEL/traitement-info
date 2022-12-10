#Visualize data with matplotlib given in a args the path of the csv file
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def main():
    #Take the path of the csv file as an argument
    if(len(sys.argv) < 2):
        print("Please provide the path of the csv path of the test data file")
        return
    df = pd.read_csv(sys.argv[1])
    #scatter plot of the data x with the index and on y the plagged amount
    plt.scatter(df.index, df)
    plt.show()
main()