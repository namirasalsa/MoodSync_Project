import time
import streamlit as st

def show_homepage(questions):
    st.image("assets/poto1.png")
    st.image("assets/poto2.png")
    st.image("assets/poto3.png")
    st.image("assets/poto4.png")
    if st.button('Coba Sekarang'):
        with st.spinner('Tunggu sebentar🏃‍♂️💨'):
            time.sleep(1)
            st.session_state.start = True
            st.session_state.input_data = {feature: [] for feature in questions.keys()}
            st.experimental_rerun()
        
    return 'start' in st.session_state and st.session_state.start
