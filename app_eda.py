import streamlit as st
import pandas as pd 
import seaborn as sb 
import matplotlib.pyplot as plt

def run_eda() :
    st.subheader('개별 주택 데이터')
    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['고유번호','법정동코드','동코드','동명','표준지여부','기준월','데이터기준일자'],axis=1)
    st.dataframe(df)


    col_list = df.columns[7 : ]
    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택',col_list)

    df_max =df.loc[df[selected_col]==df[selected_col].max(), ]
    df_min =df.loc[df[selected_col]==df[selected_col].min(), ]

    st.text('{} 컬럼의 최대값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_max)
    st.text('{} 컬럼의 최소값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_min)
