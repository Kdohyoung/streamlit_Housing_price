import streamlit as st
import pandas as pd
from PIL import Image


def  run_home() :
    st.subheader('인천광역시 서구 단독주택 가격 관련 데이터입니다.')
    st.text('왼쪽 사이드 바에서 원하는 항목을 선택하세요')

    
    url = 'https://cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/VOXW23JKCWW4KFBKYOKLMECNIE.jpg'
    st.image(url)
    
    url2 = 'https://blog.kakaocdn.net/dn/vkQUE/btqwAmq4AD4/0i9MoDFZ3manZfEzUOGmd0/img.jpg'
    st.image(url2)



    url3 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHcjJkMA5t25Vw4iCMThN4mYdu4cvycNvr_MFz-jpDDv0bWM9j8y1jfCQeKd8HfCCWlQ8&usqp=CAU'
    st.image(url3)