import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
from datetime import date ,timedelta,datetime

import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)
#%matplotlib inline
daily_Data= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Final_data.csv")
daily_Data.head(5)
df=daily_Data.copy()
df.columns
df.head()

#commo = [ "Garlic", "Potato","Tomato","Paddy","Rice","Maize","Green Ginger","Coconut (Per 1000)"]
commo1= input("enter commodity :")
print(commo1)
commo2=["1"]
for b in commo2:
#b=input("Enter variety : ")
    #print(a)
    data = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Final_data.csv", index_col ="Commodity")
    print(commo1)
    s=data.loc[[commo1]]
    s.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv", sep=',')
    '''
    data1 = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv", index_col ="Commodity")





    data1 = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv", index_col ="Variety")
    x=data1.loc[[b]]
    x.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\trying_Modal.csv", sep=',')

    '''
    import warnings
    import itertools
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    fields = ['Modal', 'Date']
    df= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv",skipinitialspace=True, usecols=fields)
    df.Date = pd.to_datetime(df.Date, errors='coerce')
    df=df.set_index('Date')
    df.head(10)

    data = df.copy()
    n= data

    Z = n['Modal'].resample('D').sum()
    Z.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv", sep=',')
    y= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv",)
    y= y.set_index(['Date'])
    y.index = pd.to_datetime(y.index)




    y = y['Modal'].resample('D').mean()
    #y = y['Modal'].mean()
    y = y.fillna(y.bfill())
    #ssprint(y)




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
    pred = results.get_prediction(start=pd.to_datetime('2018-9-2'), dynamic=False)
    pred_ci = pred.conf_int()
    ax = y['1990':].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)

    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.2)

    ax.set_xlabel('Date')
    ax.set_ylabel('Crop Price')
    plt.legend()

    plt.show()
    y_forecasted = pred.predicted_mean
    y_truth = y['2018-9-2':]

    #print(y_forecasted)
    #print(y_truth)
    y_forecasted.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\data41_Arrival.csv", sep=',')
    per = (abs((y_forecasted - y_truth))/y_truth).mean()
    per=(1-per)*100
    print('the accuracy in %',per)


    da = pd.read_csv('data41_Arrival.csv')

    #t=da.loc[:,['0']].mean()
    #print('the mean of max prize is')
    #


    pred_uc = results.get_forecast(steps=25)

    # Get confidence intervals of forecasts
    pred_ci = pred_uc.conf_int()
    #print(pred_ci)
    pred_ci.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv", sep=',')
    pred_ci1=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv")
    pred_ci1["Commodity"] = commo1

    pred_ci1.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv", sep=',')
    fd=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv")
    sum_column = fd["lower Modal"] + fd["upper Modal"]
    fd["Modal"] = sum_column/2
    fd.drop(["lower Modal","upper Modal"],axis=1, inplace=True)
    fd.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Modal_pred.csv",sep=',')
    print(fd)




    '''
for a in commo:
    #b=input("Enter variety : ")
    #print(a)
    data = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Final_data.csv", index_col ="Commodity")
    s=data.loc[[a]]
    s.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv", sep=',')
    '''
   
    '''
    import warnings
    import itertools
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    plt.style.use('fivethirtyeight')
    fields = ['Modal', 'Date']
    df= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv",skipinitialspace=True, usecols=fields)
    df.Date = pd.to_datetime(df.Date, errors='coerce')
    df=df.set_index('Date')
    df.head(10)

    data = df.copy()
    n= data

    Z = n['Modal'].resample('D').sum()
    Z.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv", sep=',')
    y= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\try_Modal1.csv",)
    y= y.set_index(['Date'])
    y.index = pd.to_datetime(y.index)




    y = y['Modal'].resample('Y').mean()
    #y = y['Modal'].mean()
    y = y.fillna(y.bfill())
    #ssprint(y)




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

                #print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
            except:
                continue
    pred = results.get_prediction(start=pd.to_datetime('2018-12-31'), dynamic=False)
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
    y_truth = y['2018-12-31':]

    #print(y_forecasted)
    #print(y_truth)
    y_forecasted.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\data41_Arrival.csv", sep=',')
    per = (abs((y_forecasted - y_truth))/y_truth).mean()
    per=(1-per)*100
    #print('the accuracy in %',per)


    da = pd.read_csv('data41_Arrival.csv')

    #t=da.loc[:,['0']].mean()
    #print('the mean of max prize is')
    #


    pred_uc = results.get_forecast(steps=25)

    # Get confidence intervals of forecasts
    pred_ci = pred_uc.conf_int()
    #print(pred_ci)
    pred_ci.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv", sep=',')
    pred_ci1=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv")
    pred_ci1["Commodity"] = a

    pred_ci1.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv", sep=',')
    fd=pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\temp11.csv")
    sum_column = fd["lower Modal"] + fd["upper Modal"]
    fd["Modal"] = sum_column/2
    fd.drop(["lower Modal","upper Modal"],axis=1, inplace=True)
    fd.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Modal_pred.csv",mode='a',sep=',')
    print(fd)


'''
