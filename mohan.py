import streamlit as st
st.title('Hello World')

if st.sidebar.button('text elements'):
    st.markdown("this is markdown")
    st.title("title")
    st.header("header")
    st.subheader("sub header")
    st.caption("caption")
    st.text("ascs")
    st.latex("latex-----(a+b)^2=a^2bv")
    st.title('Hello World')