import streamlit as st
import pandas as pd 
import joblib
import numpy as np
import sklearn
def run_ml():
    st.subheader('��õ���� ���� ����')

    print(sklearn.__version__)


    regressor = joblib.load('data/regressor (1).pkl')
    scaler_X = joblib.load('data/scaler_X1.pkl')
    scaler_y = joblib.load('data/scaler_y1.pkl')


    ����������� = st.number_input('����������� �Է� (m��)',0,)
    ������������ = st.number_input('��������� �Է� (m��)',0,)
    �ǹ���ü������ = st.number_input('�ǹ���ü������ �Է� (m��)',0,)
    �ǹ����������� = st.number_input('�ǹ����� ������ �Է� (m��)',0,)

    
    if st.button ('���� ���� �ݾ� ����') : 

        new_data = np.array([�����������,������������,�ǹ���ü������,�ǹ�����������])

        new_data = new_data.reshape(1,4)
        new_data=scaler_X.transform(new_data)

        y_pred = regressor.predict(new_data)

        y_pred = scaler_y.inverse_transform(y_pred)
        y_pred = round(y_pred[0,0])
        st.write('������ ���� ������' + str(y_pred)+'�� �Դϴ�')

