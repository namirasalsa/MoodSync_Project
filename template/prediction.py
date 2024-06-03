import streamlit as st

def show_prediction_form(questions):
    input_data = {}
    for attribute, question in questions.items():
        st.subheader(question)
        options = ['a', 'b', 'c']
        for i in range(5):
            answer = st.radio(f'{attribute} - Question {i+1}', options=options, key=f'{attribute}_{i}')
            weight = {'a': 2, 'b': 1, 'c': 0}
            input_data[f'{attribute}_{i}'] = weight[answer]
    return input_data
