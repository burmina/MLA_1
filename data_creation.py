import numpy as np
import pandas as pd
import random
import os

def get_df(n=60):
    t = {}
    for j in range(6):
        t[f't{j*4}'] = []
    df = pd.DataFrame(columns=t)
    for i in range(n):
        min = random.randint(5,10)
        max = random.randint(12,30)
        for j in range(6):
            t[f't{j*4}'].append((np.concatenate([np.linspace(min,max+random.random()*3,3),np.linspace(max,min+random.random()*8,3)])+np.random.random(6)*3)[j])
    return pd.DataFrame(t)
def main():
    if not(os.path.isdir('./test')):
        os.mkdir('./test')
    if not(os.path.isdir('./train')):
        os.mkdir('./train')
    get_df().to_csv('./test/df.csv')
    get_df().to_csv('./train/df1.csv')
    get_df().to_csv('./train/df2.csv')

if __name__ == "__main__":
    main()