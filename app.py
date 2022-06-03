import streamlit as st
from app_home import run_home
from app_eda import run_eda
from app_price import run_price
from app_ml import run_ml
from app_chart import run_chart

def main() :
    st.title('주택 데이터 제공 및 가격 예측')
    menu= ['메인 페이지','주택 데이터','주택 가격 데이터','데이터 차트','주택가격 예상']
    choice = st.sidebar.selectbox('메뉴 선택',menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_price()
    elif choice == menu[3] :
        run_chart()
    elif choice == menu[4] :
        run_ml()





if __name__ == '__main__' :
    main()