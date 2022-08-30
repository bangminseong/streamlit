import streamlit as st

menu = st.sidebar.selectbox('MENU',options=['회원가입','로그인'])

if menu == '회원가입':
    #회원가입 아이디, 비밀번호, 비밀번호 확인, 나이, 성별, 전화번호
    #회원가입

    ID = st.text_input('아이디')
    PassWord = st.text_input('비밀번호')
    Repeat = st.text_input('비밀번호 재확인')
    Good = st.text_input('주민등록번호')
    Age = st.text_input('나이')
    Gender1 =st.radio('성별을 선택해 주세요',('남','여'))
    Number = st.text_input('전화번호')
    st.button('회원가입')
if menu == '로그인':
    login_id = st.sidebar.text_input('아이디')
    login_pw = st.sidebar.text_input('비밀번호', type='password')
    login_btn = st.sidebar.button('로그인')
    if login_btn:
        st.sidebar.write(login_id)
        st.sidebar.write(login_pw)

