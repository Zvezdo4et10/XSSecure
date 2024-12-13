import streamlit as st
from style import container_style
from src.sanitize import clean_html

st.markdown(container_style, unsafe_allow_html=True)
st.title("XSSecure")
st.title("HTML Ввод и Очистка")
html_input = st.text_area("Введите ваш HTML код:")


if st.button("Очистить HTML"):
    if html_input:
        cleaned_html = clean_html(html_input)
        st.subheader("Очищенный HTML код:")
        st.code(cleaned_html, language='html')
        st.subheader("Рендер HTML")
        with st.container() as container1:
            container1.markdown("<div class='container1'>", unsafe_allow_html=True)
            st.markdown(cleaned_html, unsafe_allow_html=True)
    else:
        st.warning("Пожалуйста, введите HTML код.")