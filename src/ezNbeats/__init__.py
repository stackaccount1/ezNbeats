import datetime as dt
import pandas as pd
import numpy as np
import logging
import sklearn
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize']=20,10
from nbeats_forecast import NBeats
from scipy import stats
from sklearn.preprocessing import MinMaxScaler


def process_data_return_prediction(ethdata, period):
    data = pd.read_csv(ethdata)   
    data = data.values        #univariate time series data of shape nx1 (numpy array)
    print("Data size is:", len(data))
    assert len(data) >= 50, 'Data set must be over 50'
    assert (period/len(data)) <= .25, 'Prediction period must be less than 25% of the data set'
    data_for_chart = data.tolist()
    data_for_chart = [val for sublist in data_for_chart for val in sublist]
    model = NBeats(data=data, period_to_forecast=period)
    model.fit()
    forecast = model.predict()
    return forecast, data, data_for_chart

def makexvalueforlist(data):
    x_list = []
    j = 0
    for i in range(len(data)):
        j += 1
        x_list.append(j)
    return x_list

def makexvalueforpredictionvalues(list1, array_predicted):
    #x_list = makexvalueforlist(list1)
    x_pred_list = []
    j = makexvalueforlist(list1)[-1]
    #print(j)
    for i in range(len(array_predicted)):
        j += 1
        x_pred_list.append(j)
    #print(x_pred_list)
    return x_pred_list

def run_prediction_and_plot(ethdata, period):
    forecast, data, data_for_chart = process_data_return_prediction(ethdata, period)
    x_list = makexvalueforlist(data)
    x_pred_list = makexvalueforpredictionvalues(data, forecast)
    forecast = forecast.reshape(len(forecast))
    df = pd.DataFrame({'Price' : data_for_chart, 'Day': x_list})
    df.head()
    dr = pd.DataFrame({'Price_Prediction': forecast, 'Date': x_pred_list})
    dr.head()
    plt.plot(df["Price"],label='Price History')
    plt.plot(dr["Date"], dr["Price_Prediction"])

def return_prediction(ethdata, period):
    forecast, data, data_for_chart = process_data_return_prediction(ethdata, period)
    return forecast