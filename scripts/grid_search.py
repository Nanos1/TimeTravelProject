# Importing Libraries
import os
import pandas as pd
import numpy as np
#from pandas.plotting import scatter_matrix
import datetime
from collections import OrderedDict
from operator import itemgetter
from itertools import islice
import shutil
from datetime import datetime
from create_stocks import clean_stocks
from time_travel import make_money
import warnings
warnings.filterwarnings('ignore')

T_list = list(range(10, 100)) # the days we are looking ahead to make our next move
N_max = 1000 # max moves

best_T = 0
money_max = 0
n = 8
T= 94
clean_stocks(n)

# for T in T_list:
#     print(T)
#     money = make_money(n, T, N_max)
# #    if T%50 == 0: print ('-------I am still here dude in number:', T)
#     if money > money_max:
#         money_max = money
#         best_T = T
# print('### My money is {} out of n: {} stocks and T: {} days' .format(money_max, n, best_T))

money = make_money(n, T, N_max)
print('### My money is {} out of n: {} stocks and T: {} days' .format(money, n, T))

