import streamlit as st
from style import container_style
from src.xssecure.sanitize import clean_html

st.markdown(container_style, unsafe_allow_html=True)
st.title("XSSecure")
st.title("HTML Ввод и Очистка")
html_input = st.text_area("Введите ваш HTML код:")


if st.button("Очистить HTML"):
    if html_input:
        cleaned_html = clean_html(html_input)
        st.subheader("Очищенный HTML код:")
        st.code(cleaned_html, language='html')