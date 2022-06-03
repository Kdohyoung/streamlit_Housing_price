import streamlit as st
import pandas as pd
from PIL import Image


def  run_home() :
    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['ê³ ìœ ë²ˆí˜¸','ë²•ì •?™ì½”ë“œ','?™ì½”ë“œ','?™ëª?','?‘œì¤?ì§??—¬ë¶?','ê¸°ì???›”','?°?´?„°ê¸°ì???¼?'],axis=1)
    st.subheader('?¸ì²œê´‘?—­?‹œ ?„œêµ? ?‹¨?…ì£¼íƒ ê°?ê²? ê´?? ¨ ?°?´?„°?…?‹ˆ?‹¤.')
    st.text('?™¼ìª? ?‚¬?´?“œ ë°”ì—?„œ ?›?•˜?Š” ?•­ëª©ì„ ?„ ?ƒ?•˜?„¸?š”')

    
    url = 'https://cloudfront-ap-northeast-1.images.arcpublishing.com/chosunbiz/VOXW23JKCWW4KFBKYOKLMECNIE.jpg'
    st.image(url)
    
    url2 = 'https://blog.kakaocdn.net/dn/vkQUE/btqwAmq4AD4/0i9MoDFZ3manZfEzUOGmd0/img.jpg'
    st.image(url2)



    url3 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHcjJkMA5t25Vw4iCMThN4mYdu4cvycNvr_MFz-jpDDv0bWM9j8y1jfCQeKd8HfCCWlQ8&usqp=CAU'
    st.image(url3)