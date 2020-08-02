import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)
#%matplotlib inline
daily_Data= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\2_year_Final.csv")
daily_Data.head(5)
df=daily_Data.copy()
df.columns
df.head()
b=input("Enter Market : ")

a=input("Enter commodity : ")

#print(a)
data = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\2_year_Final.csv", index_col ="Market")
s=data.loc[[b]]
s.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\trying_Modal.csv", sep=',')
data1 = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\trying_Modal.csv", index_col ="Commodity")
x=data1.loc[[a]]
x.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv", sep=',')
import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
fields = ['Modal', 'Date']
df= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv",skipinitialspace=True, usecols=fields)
df.Date = pd.to_datetime(df.Date, errors='coerce')
df=df.set_index('Date')
df.head(10)
'''
data = df.copy()
n= data

Z = n['Modal'].resample('D').sum()
Z.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv", sep=',')
y= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv",)
y= y.set_index(['Date'])
y.index = pd.to_datetime(y.index)
'''
data = df.copy()
y = data
y
y = y['Modal'].resample('D').mean()
#y = y['Modal'].mean()
y = y.fillna(y.bfill())
#print(y)

'''
y = y['Modal'].resample('W').mean()
#y = y['Modal'].mean()
y = y.fillna(y.bfill())
print(y)

'''


#y.plot(figsize=(15, 6))
#plt.show()
p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
#print('Examples of parameter combinations for Seasonal ARIMA...')
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
#print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
#print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
#print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

warnings.filterwarnings("ignore") # specify to ignore warning messages

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue
pred = results.get_prediction(start=pd.to_datetime('2018-09-3'), dynamic=False)
pred_ci = pred.conf_int()
ax = y['1990':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('Crop Price')
#plt.legend()

#plt.show()
y_forecasted = pred.predicted_mean
y_truth = y['2018-09-3':]
'''y_forecasted.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\Temp_Forcast_Modal.csv", sep=',')
y_truth.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\Temp_truth_Modal.csv", sep=',')
yy = pd.merge(y_truth, y_forecasted, on = ['Date'])
print(yy)
'''
#print(y_forecasted)
#print(y_truth)
y_forecasted.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\data4_Modal.csv", sep=',')
per = (abs((y_forecasted - y_truth))/y_truth).mean()
per=(1-per)*100
print('the accuracy in %',per)


da = pd.read_csv('data4_Modal.csv')


pred_uc = results.get_forecast(steps=60)

# Get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()
#print(pred_ci)

pred_ci.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\temp.csv", sep=',')
pred_ci1=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\temp.csv")
pred_ci1["Commodity"] = a

pred_ci1.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\Modal_pred22.csv", sep=',')


fd=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\Modal_pred22.csv")
sum_column = fd["lower Modal"] + fd["upper Modal"]
fd["Modal"] = sum_column/2

fd.drop(fd.columns.difference(['Modal','Unnamed: 0.1','Commodity']), 1, inplace=True)

#fd.drop(["lower Modal","upper Modal"],axis=1, inplace=True)
fd.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\Modal_pred.csv", mode='a',sep=',')
print(fd)

'''

Modal_mean=fd.loc[:,['Modal']].mean()
Modal_min=fd['Modal'].min()
Modal_max=fd['Modal'].max()
#print(Modal_min)
#print(Modal_max)
print("min value with out PSF")
print(Modal_min)
print("max value with out PSF")
print(Modal_max)

Modal_min_exp_R=int(input("Enter Expected minimun Price"))
h=Modal_min_exp_R - Modal_min
Modal_min_exp=Modal_min + h
fd['Modal']=Modal_min_exp - fd['Modal']
fd.rename(columns={'Unnamed: 0': 'Date'})
fd.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\Modal_operation.csv", sep=',')

Arri=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\Arrival_pred.csv")
Mod=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\Modal_operation.csv")

df3 = pd.merge(Arri, Mod, on = ['Unnamed: 0','Commodity'])
df3.set_index('Unnamed: 0', inplace = True)
df3.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\prize_try.csv", sep=',')
df4 = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\prize_try.csv")
num = df4._get_numeric_data()
num[num<0]=0

num.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\prize_try.csv", sep=',')
fd3=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\prize_try.csv")
P_S_amount = fd3["Arrival"] * fd3["Modal"]*7
fd3["Amount"] = P_S_amount
Price_S_Fund=fd3['Amount'].sum()
fd3.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\prize_try.csv",mode='a', sep=',')


print("price Stabalizaion Fund Required")
print(Price_S_Fund,"Rs")
print("min value with PSF")
print(Modal_min_exp)
print("max value with  PSF")
print(Modal_max-10)

'''
