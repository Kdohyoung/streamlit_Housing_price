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
    st.subheader('�������� ������ ����')

    df = pd.read_csv('data/incheon.csv',encoding='EUC-KR')
    df = df.drop(['������ȣ','�������ڵ�','���ڵ�','����','ǥ��������','���ؿ�','�����ͱ�������'],axis=1)

    st.text('��������')
    fig = plt.figure()
    my_order = df['��������'].value_counts().index
    sb.countplot(data=df, x= '��������' ,  order=my_order)
    st.pyplot(fig)