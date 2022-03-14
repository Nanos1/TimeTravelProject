import pandas as pd
import os
from collections import OrderedDict
from operator import itemgetter 
from itertools import islice
import shutil

def clean_stocks(n):
    os.chdir('Stocks')

    filenames = [x for x in os.listdir() if x.endswith('.txt') and os.path.getsize(x) > 0] # all files in Stocks

    myScoreDict = {} 
    for filename in filenames:
        df = pd.read_csv(filename, sep=',')  
        myScore = df.iloc[df['High'].idxmax()]['Close'] / df.iloc[0]['Close']
        myScoreDict[filename] = myScore

    myScoreDict = OrderedDict(sorted(myScoreDict.items(), key = itemgetter(1), reverse = True)) 
    myStocks = list(islice(myScoreDict, n))  

    files = os.listdir()

    dest = '../cleanStocks'

    if (os.path.isdir(dest)): shutil.rmtree(dest)
    os.makedirs(dest)
    for file in files:
        if file in myStocks:
            full_file_name = os.path.join('', file)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, '../cleanStocks')

    os.chdir('./../cleanStocks')
        
    filenames = [x for x in os.listdir() if x.endswith('.txt') and os.path.getsize(x) > 0]
    list_with_df = []
    for file in filenames:
        df = pd.read_csv(file, sep=',')
        df = df.drop(labels='OpenInt', axis=1)
        df['Stock'] = file.split('.')[0]
        df['Volume'] = df['Volume'] * 0.1
        df = df.astype({'Volume': 'int64'})
        list_with_df.append(df)
        

    result = pd.concat(list_with_df)
    result = result.sort_values(by =['Date'])
    os.chdir('..')
    result.to_csv('mystock.txt',sep=',')
 
        
    