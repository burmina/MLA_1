import numpy as np
import pandas as pd
import os

def preprocess(dir,test=False):
    for i in os.listdir(dir):
        if i.find('.csv') != -1:
            df = pd.read_csv(dir+'/'+i,index_col=0)
            df['std']= df.iloc[:,:-1].apply(lambda x: np.std(x),axis=1)
            #if test:
            #    df = df.drop(['t20'],axis=1)
            df.to_csv(dir+'/'+i)

def main():
    if os.path.isdir('./test'):
        preprocess('./test',True)
    if os.path.isdir('./train'):
        preprocess('./train')

if __name__ == "__main__":
    main()