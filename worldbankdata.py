import pandas as pd
import numpy as np
import wbdata
import datetime
import linear_regression

# I will add 10 random countries for my model. First one will be Turkey. 
countries = ["TR", "JPN", "USA", "SAU", "CHN", "DEU", "FRA", "ARE", "GBR", "CHE"]

# I actually wanted to use three different indicators as GDP per capita (NY.GDP.PCAP.CD), Public Expenditure on Education (SE.XPD.EDUC.ZS)
# and Poverty Rate (SI.POV.NAPR.ZS); however, for some reason I could not use these indicators as WorldBank data had all zeros in it.
# Therefore I will use a dataset in which two of my friends have used (urban population %). 

indicators = {"NY.GDP.PCAP.CD": "GDP per capita (current US$)", 
             "SP.URB.TOTL.IN.ZS": "Urban population (% of total population)"}             

# I want to take data from 1995 to 2018.

dates = (datetime.datetime(1995, 1, 1), datetime.datetime(2018, 1, 1))

# Creating a dataframe from my indicators and the dates that I have chosen.

df = wbdata.get_dataframe(indicators, country=countries, data_date=dates)  
print(df)          

df.dropna(inplace=True) #There were some NaN values (in USA at least), therefore I dropped them.

df.to_csv('HW2_wbankdata.csv') #Writing it into a csv.

# Now I'll try to build the regression model. 
# As I am trying to conduct a regression, I will assign which columns are my independent and dependent variables. 

y = df.iloc[:,0]
x = df.iloc[:,1:] 

# Executing the linear regression model

linear_regress.linear_regress(y, x) 

# To be honest, I could not execute the model; I tried to do it both by hand and by using this object. 
# I checked the object attributes by dir(), but still could not find what I want. 
# I will write my report with the results that I obtained from an external tool. 





