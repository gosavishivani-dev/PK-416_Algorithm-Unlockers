import pylab
import calendar
import numpy as np
import pandas as pd
import seaborn as sn
from scipy import stats
from datetime import datetime
import matplotlib.pyplot as plt
from datetime import date ,timedelta,datetime
from selenium import webdriver
import csv

import warnings
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore", category=DeprecationWarning)
#%matplotlib inline
daily_Data= pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\SIH\\Final_data.csv")
daily_Data.head(5)
df=daily_Data.copy()
df.columns
df.head()
'''a=input("Enter commodity : ")
b=input("Enter variety : ")
#print(a)
data = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\Final_dataset.csv", index_col ="Commodity")
s=data.loc[[a]]
s.to_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv", sep=',')
data1 = pd.read_csv("C:\\Users\\rushikeshaher10\\Desktop\\try_Modal.csv", index_col ="Commodity")
'''
print(1)

today = date.today()
day = (today- timedelta(days=578))
print("Today's date:", day)
day1 = day.strftime('%d/%m/%Y')

path = r'C:\\Users\\rushikeshaher10\\Desktop\\SIH\\chromedriver'
driver = webdriver.Chrome(executable_path = path)
driver.get('https://www.krishimaratavahini.kar.nic.in/mobile/MarketWise.aspx')

driver.find_element_by_id('ContentPlaceHolder1_txtDate').send_keys('.')
js = "document.getElementById('ContentPlaceHolder1_txtDate').value = '"+day1+"';"
driver.execute_script(js)

driver.find_element_by_id('ContentPlaceHolder1_butSearch').click()
driver.implicitly_wait(10)
l = driver.find_elements_by_xpath("//*[contains(text(), 'All Market')]")
l[0].click()
l = driver.find_elements_by_xpath("//*[contains(text(), 'View Report')]")
l[0].click()

links = driver.find_elements_by_css_selector('#ContentPlaceHolder1_grdData')
df = pd.read_html(driver.page_source)[0]

df.to_csv('temp.csv' , sep=',')
dff = pd.read_csv("temp.csv")
dff.drop(dff.columns.difference(['Market','Commodity','Variety','Arrival','Min','Max','Modal']), 1, inplace=True)
dff["Date"] = day1

dff.to_csv('Final_data.csv' , mode='a' ,header =False)
driver.close()


