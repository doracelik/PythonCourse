import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd  
import seaborn as sns
from sklearn.linear_model import LinearRegression # I know that we are not supposed to use this library, but as I explained in worldbankdata.py I could not do it in another way

# I could only find coefficients this way. I will unfortunately use another tool to include details such as Standard Errors in my report. 

# Loading the data set
df = pd.read_csv('/Users/dora/HW2_wbankdata.csv')  

# Converting my values into a numpy array
X = df.iloc[:, 3].values.reshape(-1, 1)  
Y = df.iloc[:, 2].values.reshape(-1, 1) 

# Creating an object for the class 
linear_regressor = LinearRegression()

# Performing the regression with sklearn library
linear_regressor.fit(X, Y)
print(linear_regressor.intercept_) # For our intercept
print(linear_regressor.coef_) # For our coefficient of Urban Population % (My X variable)

# Plotting the regression
vis = sns.lmplot(x="GDP per capita (current US$)", y="Urban population (% of total population)", data=df)
plt.title("GDP-Urban Population Percentage Regression")
vis.set_axis_labels("GDP Per Capita", "Urban Population %")

# Saving it as png

plt.savefig("GDP-UrbanPop_Regression2.png",bbox_inches='tight',dpi=100) # I had to use extra commands to make my plot fit into png. 
plt.show()



