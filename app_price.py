import streamlit as st
import pandas as pd 
import seaborn as sb 
import matplotlib.pyplot as plt
from PIL import Image


def  run_price() :
    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['고유번호','법정동코드','동코드','동명','표준지여부','기준월','데이터기준일자'],axis=1)
   
    st.subheader('법정동명별 데이터')
    sentence = st.text_input(' **동 검색')
    if st.button('검색'):
        houes_info = df.loc [df['법정동명'].str.lower().str.contains(sentence.lower()) , ]
        st.write(houes_info)

   
   
   
    st.subheader('가장 비싼 주택 데이터')
    best = df.loc[df['주택가격']==df['주택가격'].max(),]
    st.dataframe(best)

    st.subheader('가장 싼 주택 데이터')
    worst = df.loc[df['주택가격']== 2440000 ]
    st.dataframe(worst)


    
    st.subheader('지역별 주택 평균가격 top 5 ')
    df_mean = df.groupby('법정동명')['주택가격'].mean().to_frame()
    df_mean = df_mean.sort_values('주택가격',ascending=False).round()
    df_mean = df_mean['주택가격'].astype(int)
    st.dataframe(df_mean.head(5))


    st.subheader('토지대장면적 별 주택가격')
    df_mean3 = df.groupby('토지대장면적')['주택가격'].mean().to_frame()
    df_mean3 = df_mean3['주택가격'].astype(int)
    st.dataframe(df_mean3)


    st.subheader('건물전체 연면적 별 주택가격')
    df_mean4 = df.groupby('건물전체연면적')['주택가격'].mean().to_frame()
    df_mean4 = df_mean4['주택가격'].astype(int)
    st.dataframe(df_mean4)

    st.subheader('건물산정 연면적 별 주택가격')
    df_mean5 = df.groupby('건물산정연면적')['주택가격'].mean().to_frame()
    df_mean5 = df_mean5['주택가격'].astype(int)
    st.dataframe(df_mean5)
   