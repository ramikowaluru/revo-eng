
# coding: utf-8

# In[154]:

import pandas as pd
import numpy as np

household = pd.read_csv("C:/D_drive/isb/Capstone Project/Data_Sets/Household_Demographic.csv",header=0,encoding='utf-8')
print household.dtypes
print(household.head())
print(household.shape)


# In[155]:

household['AGE_DESC']=household['AGE_DESC'].astype('category')
household['MARITAL_STATUS_CODE']=household['MARITAL_STATUS_CODE'].astype('category')
household['INCOME_DESC']=household['INCOME_DESC'].astype('category')
household['HOMEOWNER_DESC']=household['HOMEOWNER_DESC'].astype('category')
household['HH_COMP_DESC']=household['HH_COMP_DESC'].astype('category')
household['HOUSEHOLD_SIZE_DESC']=household['HOUSEHOLD_SIZE_DESC'].astype('category')
household['KID_CATEGORY_DESC']=household['KID_CATEGORY_DESC'].astype('category')
household['HOUSEHOLD_KEY']=household['HOUSEHOLD_KEY'].astype(np.int16)
print household.dtypes

