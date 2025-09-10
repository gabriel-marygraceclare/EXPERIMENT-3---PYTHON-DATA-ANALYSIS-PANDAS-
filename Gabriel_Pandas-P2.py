#!/usr/bin/env python
# coding: utf-8

# # EXPERIMENT 3
# ## PYTHON DATA ANALYSIS (PANDAS)

# ### Name: Mary Grace Clare R. Gabriel
# ### Section: 2ECE-B
# ### Date: September 10, 2025

# In[2]:


import pandas as pd #importing the library


# In[3]:


cars = pd.read_csv('cars.csv') #load the file "cars.csv"
cars #display the contents of the file


# In[5]:


cars_oddnumbers = cars.iloc[:5, [1, 3, 5, 7, 9, 11]] #using .iloc to locate the rows and specific columns
cars_oddnumbers #to display the subset result


# In[39]:


#select the .loc[] with index of zero to display the specific row for the car model Mazda RX4
#then displaying the specific columns
mazda_rxv = cars.loc[[0], ['Model', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']] 
mazda_rxv


# In[28]:


camaro = cars[cars['Model'] == 'Camaro Z28'] #filtering the df to include only the row where the Model is Camaro Z28

cylinders = camaro['cyl'].values[0] #to extract the value of cylinders from cyl

print(f"The car model Camaro Z28 has {cylinders} cylinders.") #to print the result in a string


# In[38]:


specific_cars = cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']] #to select the specific row and column from the dataframe
specific_cars #to display the result


# In[ ]:




