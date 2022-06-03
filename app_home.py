import streamlit as st
import pandas as pd
from PIL import Image


def  run_home() :
    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['고유번호','법정?��코드','?��코드','?���?','?���?�??���?','기�???��','?��?��?��기�???��?��'],axis=1)
    st.subheader('?��천광?��?�� ?���? ?��?��주택 �?�? �??�� ?��?��?��?��?��?��.')
    st.text('?���? ?��?��?�� 바에?�� ?��?��?�� ?��목을 ?��?��?��?��?��')

    
    url = 'https://cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/VOXW23JKCWW4KFBKYOKLMECNIE.jpg'
    st.image(url)
    
    url2 = 'https://blog.kakaocdn.net/dn/vkQUE/btqwAmq4AD4/0i9MoDFZ3manZfEzUOGmd0/img.jpg'
    st.image(url2)



    url3 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHcjJkMA5t25Vw4iCMThN4mYdu4cvycNvr_MFz-jpDDv0bWM9j8y1jfCQeKd8HfCCWlQ8&usqp=CAU'
    st.image(url3)