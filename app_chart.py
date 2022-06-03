import streamlit as st
import pandas as pd 
import seaborn as sb 
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def run_chart() :
    st.subheader('법정동명별 데이터 갯수')

    df = pd.read_csv('data/incheon.csv',encoding='EUC-KR')
    df = df.drop(['고유번호','법정동코드','동코드','동명','표준지여부','기준월','데이터기준일자'],axis=1)

    st.text('내림차순')
    fig = plt.figure()
    my_order = df['법정동명'].value_counts().index
    sb.countplot(data=df, x= '법정동명' ,  order=my_order)
    st.pyplot(fig)