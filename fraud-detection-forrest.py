
# coding: utf-8

# In[120]:


import numpy as np 
import pandas as pd
from sklearn.ensemble import IsolationForest


# In[121]:


raw_data = pd.read_csv("mydata.csv")


# In[122]:


X_train = raw_data
X_train.head()


# In[124]:


clf = IsolationForest(max_samples=1000)
X_train_with_dumies = pd.get_dummies(X_train)
X_train_with_dumies.head()


# In[125]:


clf.fit(X_train_dumies)


# In[130]:


y_pred_train = clf.predict(X_train_dumies)
list(zip(X_train['amount'], y_pred_train))

