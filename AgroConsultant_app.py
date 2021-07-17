import streamlit as st 
import pandas as pd
import numpy as np
import os
import pickle
import warnings


st.set_page_config(page_title="AgroConsultant Application", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:GREEN;text-align:left;"> AgroConsultant Application 🌱🌱 </h1><br>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1,col2  = st.beta_columns([2,2])
    
    with col1: 
        st.subheader(" Find out the most suitable crop to grow in your farm 👨‍🌾")
        N = st.number_input("Nitrogen in g/kg", 1,1000)
        P = st.number_input("Phosporus in g/kg", 1,1000)
        K = st.number_input("Potassium in g/kg", 1,1000)
        temp = st.number_input("Temperature in °C",0.0,100.0)
        humidity = st.number_input("Humidity in %", 0.0,100.0)
        ph = st.number_input("Ph", 0.0,50.0)
        rainfall = st.number_input("Rainfall in mm",0.0,1000.0)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('AgroConsultant.pkl')
            prediction = loaded_model.predict(single_pred)
            col1.write('''
            ## Results 🔍 
            ''')
            col1.success(f"{prediction.item().title()} are recommended by the AgroConsultant 🌾 for your farm 👨‍🌾")
      #code for html 👨‍🌾 👨‍🌾 👨‍🌾 👨‍🌾  👨‍🌾
       


    with col2:
        with st.beta_expander(" ℹ️ Information", expanded=True):
            st.write("""
            AgroConsultant - an intelligent system that would consider environmental parameters (temperature, rainfall, farm’s latitude, longitude, altitude and distance from the sea) and soil characteristics (pH value, soil type and thickness of aquifer and topsoil) before recommending the most suitable crop to the user.       
            Crop recommendation is one of the most important aspects of precision agriculture.Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues.
            However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.

            """)
        '''
        ## How does it work ❓ 
        Complete all the parameters and the machine learning model will predict the most suitable crops to grow in a particular farm based on various parameters
        '''
        
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.success("Streamlined by :- The Alpha")
    
    
   
if __name__ == '__main__':
	main()
