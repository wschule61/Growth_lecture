#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:17:20 2022

@author: wernerschule
"""

import numpy as np
x = np.array(2)
print(x)
import pandas as pd

URL_DATA = 'https://storage.dosm.gov.my/gdp/gdp_qtr_real_demand_sub.parquet'

df = pd.read_parquet(URL_DATA)
if 'date' in df.columns: df['date'] = pd.to_datetime(df['date'])

print(df)

URL_DATA = 'https://storage.dosm.gov.my/gdp/gdp_qtr_real_sa_demand.parquet'

df2 = pd.read_parquet(URL_DATA)
if 'date' in df2.columns: df2['date'] = pd.to_datetime(df2['date'])

print(df2)
df2.set_index('date', inplace=True)
print(df2.loc[df2.index.year <= df2.index.year.unique()[4]])
df2_sorted = df2.sort_values('date')
print(df2_sorted)
pd.set_option('display.max_rows', None)
print(df2)