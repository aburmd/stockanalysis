import csv
#filename input_val.csv and file format as date,type,price,qty for cal
#dictionary = {key: value for vars in iterable}

import csv
import pandas as pd
import numpy as np
from pandas.core import strings
arr=[]
head=['date','type','price','qty']
with open('/Users/abuhura/Desktop/input_val.csv','r',encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    for row in reader:
        arr.append(dict(zip(head,row)))

df=pd.DataFrame(arr)

df['price'] = df['price'].astype(float, errors = 'raise')
df['qty'] = df['qty'].astype(float, errors = 'raise')
df['type'] = df['type'].astype(str, errors = 'raise')
df['total_price']=df['price']*df['qty']
df['total_price']=df['total_price'].where(df['type'].isin(['S']),other=(-1)*df['total_price'])
df_buy_only=df[df['type'].isin(['B'])]
df_sell_only=df[df['type'].isin(['S'])]
df_buy_only_per_day=df_buy_only.groupby(["date","type"]).sum()
df_buy_only_per_day.rename(columns = {'price':'price_per_day','qty':'qty_per_day','total_price':'total_price_per_day'}, inplace = True)
df_buy_only_per_day['price_per_day']=df_buy_only_per_day['total_price_per_day']/df_buy_only_per_day['qty_per_day']
df_sell_only_per_day=df_sell_only.groupby(["date","type"]).sum()
df_sell_only_per_day.rename(columns = {'price':'price_per_day','qty':'qty_per_day','total_price':'total_price_per_day'}, inplace = True)
df_sell_only_per_day['price_per_day']=df_sell_only_per_day['total_price_per_day']/df_sell_only_per_day['qty_per_day']
df_res=pd.merge(df_buy_only_per_day,df_sell_only_per_day,on=['date'],suffixes=("_buy","_sell"),how="outer",sort=True)
df_res['price_per_day_buy']=df_res['price_per_day_buy'].fillna(0)
df_res['qty_per_day_buy']=df_res['qty_per_day_buy'].fillna(0)
df_res['total_price_per_day_buy']=df_res['total_price_per_day_buy'].fillna(0)
df_res['price_per_day_sell']=df_res['price_per_day_sell'].fillna(0)
df_res['qty_per_day_sell']=df_res['qty_per_day_sell'].fillna(0)
df_res['total_price_per_day_sell']=df_res['total_price_per_day_sell'].fillna(0)
df_res['profit_or_loss']=df_res['total_price_per_day_buy']+df_res['total_price_per_day_sell']
df_res['cum_profit_loss']=df_res['profit_or_loss'].expanding(2).sum().fillna(0)
df_res['bal_qty']=df_res['qty_per_day_buy']-df_res['qty_per_day_sell']
df_res['bal_qty']=df_res['bal_qty'].expanding(2).sum().fillna(0)
df_res['cum_buy_qty']=df_res['qty_per_day_buy'].expanding(2).sum().fillna(0)
df_res['cum_total_buy_price']=df_res['total_price_per_day_buy'].expanding(2).sum().fillna(0)
df_res['cum_sell_qty']=df_res['qty_per_day_sell'].expanding(2).sum().fillna(0)
df_res['cum_total_sell_price']=df_res['total_price_per_day_sell'].expanding(2).sum().fillna(0)
df_res['profit_or_loss']= df_res['cum_total_sell_price']+df_res['cum_sell_qty']*(df_res['cum_total_buy_price']/df_res['cum_buy_qty']).fillna(0)
df_res.columns

df_result=df_res[['cum_buy_qty','cum_total_buy_price', 'cum_sell_qty', 'cum_total_sell_price','bal_qty','profit_or_loss']]
df_result['cum_average_buy_price']=df_result['cum_total_buy_price']/df_result['cum_buy_qty']
df_result['cum_average_sell_price']=df_result['cum_total_sell_price']/df_result['cum_sell_qty']


print(root)

import binarytree
from binarytree import build


