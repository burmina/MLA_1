from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import os
import pickle


def main():
    filename = 'model.pickle'
    model = pickle.load(open(filename, 'rb'))
    dir = './test'
    df = None
    if os.path.isdir(dir):
        for i in os.listdir(dir):
            if i.find('.csv') != -1:
                df = pd.concat([df,pd.read_csv(dir+'/'+i,index_col=0)]) if df is not None else pd.read_csv(dir+'/'+i,index_col=0)
        y = df['t20']
        X = df.drop(['t20'],axis=1)
        y_pred = model.predict(X)
        print(mean_squared_error(y_pred,y))

if __name__ == "__main__":
    main()