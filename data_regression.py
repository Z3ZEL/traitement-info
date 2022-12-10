import sklearn as sk
from sklearn import linear_model,cluster,svm

class Regression:
    def __init__(self, df):
        self.df = df
        self.model = linear_model.LinearRegression();

    def Train(self): 
        pledge = self.df[['pledged ']]
        self.df =  self.df.drop(['pledged '], axis=1)
        self.model = self.model.fit(self.df,pledge)
        return self
    
    def Predict(self, df_test):
        self.pred = self.model.predict(df_test[['goal ','backers ','currency ','main_category ','duration ']])
        return self.pred

