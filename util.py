import json
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def get_estimated_price(total_sqft,bath,bhk,location):

    if total_sqft//bhk >= bhk*17 and (bath <= 3*bhk+4 or bhk <= 3*bath+4):
        with open(r'\Python_project\Real_Estate_Model/server/artifacts/banglore_home_price_model.pickle','rb') as f:
            __model = pickle.load(f)

        with open(r'\Python_project\Real_Estate_Model\server\artifacts/columns.json','r') as f:
            __data_columns = json.load(f)['data_columns']
            __data_columns = [i.split('_')[1] if len(i) > 5 else i for i in __data_columns]
            __location = __data_columns[3:]

        if location in __data_columns:
            try:
                iloc_index = __data_columns.index(location.lower())
            except:
                -1
            
            x = np.zeros(len(__data_columns))
            x[0] = total_sqft
            x[1] = bhk
            x[2] = bath
            if iloc_index >= 0:
                x[iloc_index] = 1
            return round(__model.predict([x])[0])
        else:
            return "not valid loaction"

def location():

    global __location
    global __data_columns
    with open(r'\Python_project\Real_Estate_Model\server\artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __data_columns = [i.split('_')[1] if len(i) > 5 else i for i in __data_columns]
        __location = __data_columns[3:]
    return __location