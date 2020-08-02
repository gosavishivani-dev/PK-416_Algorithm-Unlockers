import pylab
#import calendar
#import numpy as np
import pandas as pd
#import seaborn as sn
#from scipy import stats
from datetime import datetime
#import matplotlib.pyplot as plt
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)
#%matplotlib inline

a=input("Enter commodity : ")

data = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Modal_pred.csv", index_col ="Commodity")
s=data.loc[[a]]
s.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Modal1_1.csv", sep=',')
data1 = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Modal1_1.csv")
#data1.drop(['Unnamed'])
print(data1)
