import streamlit as st
import pandas as pd 
import seaborn as sb 
import matplotlib.pyplot as plt
import platform
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_chart() :
    st.subheader('법정동명별 데이터 갯수')

    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['고유번호','법정동코드','동코드','동명','표준지여부','기준월','데이터기준일자'],axis=1)

   

    st.text('내림차순')
    fig = plt.figure()
    my_order = df['법정동명'].value_counts().index
    sb.countplot(data=df, y= '법정동명' ,  order=my_order)
    st.pyplot(fig)


    st.text('내림차순')
    fig3 = plt.figure()
    my_order = df['특수지구분명'].value_counts().index
    sb.countplot(data=df, y= '특수지구분명' ,  order=my_order)
    st.pyplot(fig3)

    
    
    
    
    st.subheader('컬럼간 상관계수')
    col_list = df.columns
    selected_list = st.multiselect('컬럼들 선택',col_list)
    if len(selected_list) > 1 :
        fig1 = sb.pairplot(data=df[selected_list])
        st.pyplot(fig1)
        st.text('선택하신 컬럼끼리의 상관계수 입니다.')    
        st.dataframe(df[selected_list].corr())

        fig2 = plt.figure()
        sb.heatmap(data=df[selected_list].corr(),annot=True,fmt='.2%',vmin=-1,vmax=1,cmap='coolwarm',linewidths=0.5 )
        st.pyplot(fig2)