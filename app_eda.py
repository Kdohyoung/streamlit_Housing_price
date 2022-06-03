import streamlit as st
import pandas as pd 
import seaborn as sb 
import matplotlib.pyplot as plt
from PIL import Image

def run_eda() :
    st.subheader('개별 주택 데이터')
    df = pd.read_csv('data/incheon.csv',encoding='cp949')
    df = df.drop(['고유번호','법정동코드','동코드','동명','표준지여부','기준월','데이터기준일자'],axis=1)
    if st.checkbox('전체 데이터 보기'):
        st.dataframe(df)
    else : 
        st.text('체크박스룰 눌러주세요.')

    st.subheader('각 컬럼별 데이터')
    df2 = df.drop(['특수지구분코드','본번','부번','건축물대장고유번호','기준년도'],axis=1)
    st.subheader('주택 정보 컬럼별 데이터')
    column_list = df2.columns
    choice_list = st.multiselect('컬럼을 선택하세요',column_list)
    st.dataframe(df[choice_list])



    st.subheader('각 데이터별 최대값 , 최소값')
    col_list = df.columns[7 : ]
    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택',col_list)

    df_max =df.loc[df[selected_col]==df[selected_col].max(), ]
    df_min =df.loc[df[selected_col]==df[selected_col].min(), ]

    st.text('{} 컬럼의 최대값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_max)
    st.text('{} 컬럼의 최소값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_min)


    st.subheader('인천 서구 지도 데이터')
    my_order = df['법정동명'].unique()
    status = st.radio('정렬방법 선택',my_order)
    if status == my_order[0]:
        url5 = 'https://www.google.com/maps/vt/data=lzomduDPLs2ACmGgnHEReg86hUCy068kJWzX5Ggk4JARNpHnTNA_Q4oONb9gGZgwXDDEmDf20pgLLV6TCvAKZf4o-jJNj_m7k6FoTaK1kMqki_ZTTkICc475OMOwHPKwZ8T_EFU9f1tovgugQo0ovBF9nEfNSsInVC_CwupRyqEuccLA6X1Rhk7g91aLFOYvFpWLE94mEWXr0DnpQD5PEFnGc6XpDhSSyifiBADq8JJg5avcPTma'
        st.image(url5)
    elif status == my_order[1] :
        url6 ='https://www.google.com/maps/vt/data=Ur4xhcAC4Ur0_ysJoQLbS69E78Bftd4Hh6r1hH9gO6SR3PT2cQK3acA0yAjZdM3svBueHj6zSjyut5Uirprcw7tnVmQlJ8JrbpKi_xlfbUuj9Bx7rr0cJRqX-lvdfCSY0_Zb27WHt6zVtOGkG6mA66W2HKq6-JAxFuejKsWCtKWZ6Kh28wgR2hTrvvrBVpT5S7xPYNLxuB5h2LAb46UDf_pkYbP17Uy0HYIqjJYvUG3Gl0QKmaD1'
        st.image(url6)
    elif status == my_order[2] :
        url7 = 'https://www.google.com/maps/vt/data=PD6ZJIlHFk8KUcfeIsIul4LZm3DLwgOfrjBsKoGyO8Y_qHZE6YXRmc_RG-RMPk865glOYXLm_sqSjy4MuAkIg82HxX5U4DS0QC71-8rw3lSk7NKAkkeYQwXTQVyOqgN5oKRzjGQ0NAVgLC-V1L203pGstlJE8389uC12FmA5i-ToT_xKiBkjkIvnlX2wcxQ9z9437rHbhEmcRa6TLgIY6Roz6RpjC-vJfxqMD84m7ftNOScaQ0Wh'
        st.image(url7)
    elif status == my_order[3] :
        url8 ='https://www.google.com/maps/vt/data=Ntw2e5Pk0Q82NHOCt2_6oJZ9rVcjTdXy-Tu-foyq5wbJsTYpT4c-WLSpqrcftNwyzeVYvPhUcUCgOEnJp-k4Ws-stVR-M_31I3BWeSxEIYM-pA-ZYGoPAI9Zt3N5HkRvQ3cCd6sVfEsDdeEAg4UJrhsUzsKWVZYKO-ErZKX-lf9zbQHPBU-S5X2tHwsmyw6t6rZ_0Ubqa4_0xuHwPj3c921c20-spT3jUBsdx9IOrTP2JVeVBstN'
        st.image(url8)
    elif status == my_order[4] :
        url9 = 'https://www.google.com/maps/vt/data=xGHS6dG0gSEbM0lVSYb6BRypCyta5PHP37nb0P_RAGa0PweJVNM6U2KOu1tV1oPR1krEfzAcX6NX1niB1QHdEhTOrLg6drJYyeTM2NTX3ElEhSp2m4JkDoH8UnX6CbxM8ajx_znm--HMqoJLXm5g2Rcm9wJX_ot3U0NqDTR8uWzds7Zglvq13N3ZlEU9nd_4cDpoKOQ9URLMXbNVPe3tDFGZAEOIOg8F_q6rZNMxnE75wNuzrJj_'
        st.image(url9)
    elif status == my_order[5] :
        url10 = 'https://www.google.com/maps/vt/data=7e1vvt0Acv24Kp9z0CQoHlYOXc7FsABaPiecjKxZPBMd9lV9IibF5RlwykL9zpTwHZyYwyti0Myp-8pGGaM7JPixQz4OchSnPZm467V-dPm-S9PCtO5jrYipfXV1cp_YmbJeNsrGB8hIhKFuJZx8kvGzBdAEP0ZQbdLMsCRJYBSIWyvA1_J9UH1GSW80XZRabr0Q6UYUIYycy0pt7TfD7r1jIUXd_FvTUrGEOaXdSX7DfaaQ4_za'
        st.image(url10)
    elif status == my_order[6] :
        url11 ='https://www.google.com/maps/vt/data=BxzZWLw2976z7_i7ZQGOQzOzQsgaIEN1zMQy1Ha2-OoxcS2tyDf9bhijq_tGopU46Aj91U-jPS0KzrWS7ydFZ4CVCJ5BIGwpmQUSayHo4-Iwsz-fZ9bSiN0haq9BBn-V9EEUghZ63O8B9asvl1GDXlJhbkFWbYboB56QQdpechSAokxzn_eHDp61kixERxALDhJyufeZIyS2OF6cUWvhMfzUc1Gz1SnQFERLUXwnHgyb20sJZKJO'
        st.image(url11)
    elif status == my_order[7] :
        url12 = 'https://www.google.com/maps/vt/data=qS8uWhtnOBLVRvMnQRvpyc1f7kvLTX6NHREgA7rqTR9ANXmrFc3mYiVutQFCSg0JjsdvipibadpCI5WvoD9uA6rntsy8EZRYKCHzbDrUMh0xTK0m7WvNdcILeZdRvn0hBkelFNwh3MQbaAmh7IX1o0HuYP-uUbFA-rLlU_BlF8aTbqh4i-T9dHbHFJtgu2Fml5ROk-DC_fiWhqxzYTnj-Lg7psjhn8EMXqNWTiATpyrrXT5nt7FZ'
        st.image(url12)
    elif status == my_order[8] :
        url13 = 'https://www.google.com/maps/vt/data=yFnG2PwFBDaC20hi_GzFCTu_LiPQWgdenFjA_KnhtWnH4UtE7c5Mq7Gt7-iWUtXIfh6bCGSjlUYaR8EsetlV_NTMyg_xSDlN4dfFPYOoWsWKa6NhrBx7RN0E5QW7ZXr9ZqO_8i77QkQF4QUmTHtdg2DcX2R1HzizhdOJGmV-MYtnDuZ-bSy66jDdv8ugn-1r_PDyKsJSjqnlZ2tuLbyY4fiPBRTtGFPjHVUst8U32Mzmdi6MHxL7'
        st.image(url13)
    elif status == my_order[9] :
        url14 = 'https://www.google.com/maps/vt/data=1hkdnHjgaF2qClxV3csJI_bKUOhE0yXA3KLsSzckXx9562ZOjq76qmER5cM7QdJRqOSvBOWjnl6-MCJtlTiafVHXzwSDqNCMerCNGX0nX3y6rUzu9MuTPi75w4syYJXR0jqAzfmiuZLCFtBM9YQf3u4kBxvISNW6ninaIqurS4Wb2EhlXBiFomBB8GoxKtINNi5zVZs1eT4injfTsgtvHuzMbBEPtJO0P4K5Sl3q8TKi8GnzD771'
        st.image(url14)
    elif status == my_order[10] :
        url15 = 'https://www.google.com/maps/vt/data=aHPM1ZHDNjt91HR30e3t0Nbduf_8l7BkPmVKefC01SbmXpS0PqN0s8clOOfAWfY-BQyjt_e2tbv1g-w0bBaqtSiqEm4Ful5fs4Xs3MuJofUC-Lflvk1xFMDoDxrPnx8ykSh4_u8FqAq4kZJqKFgOOZjmQS2vYR09tOS0aYDe4JhaAvStBEj6HxjCtYQzjdGnfNLAZgkyaaNy5DG57Yv8iZYfsk3e2ad1IqCY9k95WQAl8jUXgpO3'
        st.image(url15)
    elif status == my_order[11] :
        url16 ='https://www.google.com/maps/vt/data=bYnKXmk4hnWyaadUVygZaI1oqr9rqHYL-IgdFxsL3Q3D0fvAl73RUA_YdA_z6xGRlFOOPZeEDwjhD5OgbAzkoLeMkC0QgI6OMsWZL7WIs3ZP9IosRhaJCOCaJmt8cdUY5F27m4Fjpy9byFHlySVr7X9FdmmO5kM0ghufjLRmRSNu26ZKrkwzoAL9JRYLMXKzgzPMw4uAhN-t2oWEy8oCBfpjXF3eKR5q8me-SM3F2gUP7wABf3qQ'
        st.image(url16)
    elif status == my_order[12] :
        url17 ='https://www.google.com/maps/vt/data=Ffku8Kd-MvmEHbsyLm9OxjeqgIyv6WIpTj-GnuvbfEy3QPqX-CXKP2Umv4D88scZsnkxlhLCR3_U_5zBD4Re7PKCqJabimd2dbL5fXrAW1K8DtMf9QB8TvMkdU2O0lDLfUZGFG_nl5uSdM1DaMd8NbPlSsE1thEX7fLC3yzcCow4zJJMvsUC6VX4cahHIpIBa9jOBjLbj_mnMZj-3K9jVNpcXKriEus31nYVfjyFUOBUidR2F-hb'
        st.image(url17)
    elif status == my_order[13] :
        url18 = 'https://www.google.com/maps/vt/data=Qrj2kecS4FAUWBs-kKcmvdsijOgjk9zP52i1My3-iPLIFkaWkhK3vuJWkiDlNJBcPNRmbihpKRtDFLMb4X7814EULOnII1LEN-v5TLtWu_lWykiNyA6sVjThsvuE-18hQVB0iAlbpZM6biLDn0VQbZq4h83zPYDbqzUP12jUli9iVshTBtel0FGb9yJPo3_iT2nP_cF3_6ngR076SQTBB8Bq6OaqAiR1eVuFlj71qzYPivJUFp0G'
        st.image(url18)
    elif status == my_order[14] :
        url19 ='https://www.google.com/maps/vt/data=KHr9okEVACSB9fkN-HCWsgrwTfuePlctXvo16ji5FB7B4kQTQOnVeMQXTg229-vvhPe1wdrTaXBadDpgZPakd35eB5gWMBZIGpZ1h5i7de3xxGqpiFuB4PDvAr9HKsqQK4b4Dg0vpwbMmhcTnC7TEIrnFIxug25s5gm4SFt5AmqSnVfuA54ZDY6tL-ZxjLan1CqpNOAgitkY2Zl-cpC9qPnDSw97ib3uhHMnZ6y-mIq2c2d1MQg1'
        st.image(url19)
    elif status == my_order[15] :
        url20 = 'https://www.google.com/maps/vt/data=Dccecu-c_A2f5pP9PqFuVfdEwBa1j8g13fnk1TQiIFb4sBdB4hnrTsYj10M4w2z3ZNOroPXj55xPL4f-s5-oCK8_4au0zjF_EK9xXIVJABx-d-o6TbPcQoZDGF8MsfMjFHBNDCMFnwXLmA_sfVczfYXriPoiQGhIu3K5ivlXOJh8naBv2dKfzzqQSZWNaxAictNKmbgLFGkIdKy9FC8bKMgWPdTkKyCql_IyNSQlkwbHblGsrArW'
        st.image(url20)
    elif status == my_order[16] :
        url21 = 'https://www.google.com/maps/vt/data=8jaXl5JoKo_ua-ZVKNNVWEPVnFJ1O_v9HwowDDQ_2uxuRyrSIyzJMX1Qs1qxSbL8GqR0FDJ9lEaa9vzpdjkBqcHniC4eZiQgb4PX0un3ElI-TUevWY1CN6pm2h9Tm5CL0KBZaefndpa3in2hmR9gs_bRBs-22_bP6nFpcU_hkTo6jhAf7ozEtz0rDH0qAzoIz3CR0kCQ2C3qbYCVyzpF1iL0__qEhXhvfid0rxhl_XSDSPddDVJT'
        st.image(url21)
    elif status == my_order[17] :
        url22 = 'https://www.google.com/maps/vt/data=7DzPaYGaSQYSTmHS_GEHUdbt8ji0JmvlIRsAXK8Vw1kTTVZWDZ4VaW50uKMjn9tupEc4YoyyaH2QT_yQRFKeShlVgiZkf7K7oLqUi0-eTj-B0gHNwsUSBbeNs92IY8CAQELbPPh2A7oY6otBJD9DBcoj8ToKen9k-OrBQwtq62TEF6BNFOTB9d1VYFnnhQdrFgxt56z7GiAVFam-3uJRZXcm-qzzcYMHJoWey-s9kJQXEM4YVL1D'
        st.image(url22)
    elif status == my_order[18] :
        url23 ='https://www.google.com/maps/vt/data=uxPq5osoMCBzoER47oZDAwEp-sicjqZsqXb3BaYfRqIn5yFoYj952gMTzvKyxwf06FeZPgQTbTIBnJ-FFG-WhKay-jobfaXMwTElhlMw3Nn2k1eS5FVwpbOo_GTOXXnlnNyltf4GOFObfbiOCN4bb6W2YJ-zVMcQtjPczOiQRDArJH8ZicMulKOHJIGzxhSrKbweHp7_CPhN-61bQ6GsIkcnn3h41rbYm1v9r06ECuxf71ajwqYB'
        st.image(url23)
    

    st.subheader('주택 데이터가 가장 많은 지역 top 5')
    df_mean2 = df.groupby('법정동명').size()
    df_count=df_mean2.to_frame()
    df_count.columns= ['count']
    df_count=df_count.sort_values('count',ascending=False)
    st.dataframe(df_count.head(5))