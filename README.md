streamlit_House_price
=============
###### 인천광역시 서구의 개별주택 데이터와 가격예측 프로그램입니다.

현재 거주지인 인천서구의 주택데이터를 통하여 주택가격을 예측해보는 인공지능을 만들어 보았습니다.
사용한 언어는 python 이며 Google Colab 을 이용하여 코딩하고 인공지능을 학습 시켰습니다.
데이터를 시각화하기위해 Visual Studio Code 로 작업한 데이터를 streamlit에 적용 시켰습니다.


데이터 출처 : https://www.data.go.kr/data/15013512/fileData.do

데이터의 컬럼 설명
=============

1. 법정동명  :  주택이 있는곳의 지역 명칭
2. 특수지 구분 코드 : 특수지역과 일반 지역을 구분지은 코드
3. 특수지 구분 명 : EX) 산, 일반 ....
4. 본번 : 단독으로 지번을 구성할 수 있는 번호
5. 부번 : 세부적인 영역을 표시하기 위해 줄표 뒤에 쓰는 번호
6. 건축물대장 고유번호 : 건축물 단위로 대표지번까지만 정비(19자리) 1은 단독 3은 집합건물 
7. 기준년도 : 조사한 년도
8. 토지대장 면적 : 토지대장에 등록되어있는 면적 
9. 산정대지 연면적 : 하나의 건축물 각 층의 바닥면적의 합계
10. 건물전체 연면적 : 하나의 건축물 전체의 바닥면적의 합계
11. 건물산정 연면적 : 건물의 산정한 값의 면적의 합계
12. 주택 가격  : 주택가격  (원)


사용한 라이브러리 
=============

1.import streamlit as st

2.from streamlit_option_menu import option_menu

3.import pandas as pd

4.from PIL import Image

5.import numpy as np

6.import seaborn as sb


사용한 인공지능 라이브러리
=============

1.from sklearn.preprocessing import MinMaxScaler

2.from sklearn.model_selection import train_test_split

3.from sklearn.linear_model import LinearRegression



