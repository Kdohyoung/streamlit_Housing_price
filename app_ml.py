import streamlit as st
import pandas as pd 
import joblib
import numpy as np
import sklearn
def run_ml():
    st.subheader('인천서구 집값 예측')

    print(sklearn.__version__)


    regressor = joblib.load('data/regressor (1).pkl')
    scaler_X = joblib.load('data/scaler_X1.pkl')
    scaler_y = joblib.load('data/scaler_y1.pkl')


    토지대장면적 = st.number_input('토지대장면적 입력 (m²)',0,)
    산정대지면적 = st.number_input('산정대면적 입력 (m²)',0,)
    건물전체연면적 = st.number_input('건물전체연면적 입력 (m²)',0,)
    건물산정연면적 = st.number_input('건물산정 연면적 입력 (m²)',0,)

    
    if st.button ('주택 구매 금액 예측') : 

        new_data = np.array([토지대장면적,산정대지면적,건물전체연면적,건물산정연면적])

        new_data = new_data.reshape(1,4)
        new_data=scaler_X.transform(new_data)

        y_pred = regressor.predict(new_data)

        y_pred = scaler_y.inverse_transform(y_pred)
        y_pred = round(y_pred[0,0])
        st.write('주택의 예상 가격은' + str(y_pred)+'원 입니다')

