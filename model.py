import numpy as np 
import pandas as pd
from sklearn.ensemble import IsolationForest

# data = pd.read_csv("mydata.csv") # csvcheck the format of my data
def detect_fraud(data):
    import pdb; pdb.set_trace()
    clf = IsolationForest(max_samples=1000)
    X_train = pd.get_dummies(data)
    del X_train['id']
    clf.fit(X_train)
    y_pred = clf.predict(X_train)
    #-1 fraud, 1 not fraud
    return list(zip(data['id'], y_pred))
