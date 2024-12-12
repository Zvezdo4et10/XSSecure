import streamlit as st

from src.sanitize import clean_html

st.title("XSSecure")
st.title("HTML Ввод и Очистка")
html_input = st.text_area("Введите ваш HTML код:")


if st.button("Очистить HTML"):
    if html_input:
        cleaned_html = clean_html(html_input)
        st.subheader("Очищенный HTML код:")
        st.code(cleaned_html, language='html')
    else:
        st.warning("Пожалуйста, введите HTML код.")