import streamlit as st
import pandas as pd 
import seaborn as sb 
import matplotlib.pyplot as plt
from PIL import Image


def  run_price() :
    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['������ȣ','�������ڵ�','���ڵ�','����','ǥ��������','���ؿ�','�����ͱ�������'],axis=1)
    df2 = df.drop(['Ư���������ڵ�','����','�ι�','���๰���������ȣ','���س⵵'],axis=1)
    st.subheader('���� ���� �÷��� ������')
    column_list = df2.columns
    choice_list = st.multiselect('�÷��� �����ϼ���',column_list)
    st.dataframe(df[choice_list])

    st.subheader('���� ��� ���� ������')
    best = df.loc[df['���ð���']==df['���ð���'].max(),]
    st.dataframe(best)

    st.subheader('���� �� ���� ������')
    worst = df.loc[df['���ð���']== 2440000 ]
    st.dataframe(worst)


    
    st.subheader('������ ���� ��հ��� top 5 ')
    df_mean = df.groupby('��������')['���ð���'].mean().to_frame()
    df_mean = df_mean.sort_values('���ð���',ascending=False).round()
    df_mean = df_mean['���ð���'].astype(int)
    st.dataframe(df_mean.head(5))


    st.subheader('����������� �� ���ð���')
    df_mean3 = df.groupby('�����������')['���ð���'].mean().to_frame()
    df_mean3 = df_mean3['���ð���'].astype(int)
    st.dataframe(df_mean3)


    st.subheader('����������� �� ���ð���')
    df_mean4 = df.groupby('�ǹ���ü������')['���ð���'].mean().to_frame()
    df_mean4 = df_mean4['���ð���'].astype(int)
    st.dataframe(df_mean4)

    st.subheader('����������� �� ���ð���')
    df_mean5 = df.groupby('�ǹ�����������')['���ð���'].mean().to_frame()
    df_mean5 = df_mean5['���ð���'].astype(int)
    st.dataframe(df_mean5)



   