# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/spoorthy/Documents/Excelr/Project/fmodel.sav', 'rb'))


# creating a function for Prediction

def Telecom_Churn_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The customer is not Churned'
    else:
      return 'The customer is Churned'
  
    
  
def main():
    
    
    # giving a title
    st.title('Telecom Churn Prediction Web App')
    
    
    # getting the input data from the user
    
    
    account_length  = st.text_input('account.length')
    voice_plan = st.text_input('voice.plan')
    voice_messages  = st.text_input('voice.messages')
    intl_plan = st.text_input('intl.plan')
    intl_mins = st.text_input('intl.mins')
    intl_calls = st.text_input('intl.calls')
    intl_charge = st.text_input('intl.charge')
    day_mins = st.text_input('day.mins')
    day_calls = st.text_input('day.calls')
    day_charge = st.text_input('day.charge')
    eve_mins = st.text_input('eve.mins')
    eve_calls = st.text_input('eve.calls')
    eve_charge = st.text_input('eve.charge')
    night_mins = st.text_input('night.mins')
    night_calls = st.text_input('night.calls')
    night_charge = st.text_input('night.charge')
    customer_calls = st.text_input('customer.calls')
    
    
    # code for Prediction
    churned = ''
    
    # creating a button for Prediction
    
    if st.button('Customer churn Result'):
        churned = Telecom_Churn_prediction([account_length, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins,
                                     day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls,
                                     night_charge, customer_calls])
        
        
    st.success(churned)
    
    
    
    
    
if __name__ == '__main__':
    main()