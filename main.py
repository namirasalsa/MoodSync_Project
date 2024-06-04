# import streamlit as st
# import pandas as pd
# import time
# import plotly.express as px
# import catboost
# from template.home import show_homepage
# from template.feedback import show_feedback

# # Load CatBoost model
# model = catboost.CatBoostClassifier()
# model.load_model('saved model/catboost_newModel')

# # Function to preprocess input data
# def preprocess_input(data):
#     # Menentukan nama fitur yang sesuai dengan yang diharapkan oleh model
#     feature_names = ['angry', 'fear', 'disgust', 'happy', 'nutral', 'sad', 'surprise']
#     processed_data = {feature: sum(data[feature]) for feature in feature_names}
#     processed_data = pd.DataFrame([processed_data])
#     return processed_data

# # Function to make prediction
# def make_prediction(input_data):
#     prediction = model.predict(input_data)
#     return prediction[0]

# # Define the questions dictionary outside the main function
# questions = {
#     'angry': [
#         'Seberapa sering Anda merasa kesal atau mudah marah?',
#         'Seberapa sering Anda merasa mudah tersinggung oleh hal-hal kecil?',
#         'Seberapa sering Anda merasa ingin melukai diri sendiri atau orang lain?',
#         'Seberapa sering Anda merasa ingin berteriak atau membanting barang?',
#         'Seberapa sering Anda merasa sulit untuk mengendalikan amarah Anda?'
#     ],
#     'fear': [
#         'Seberapa sering Anda merasa gugup tentang sesuatu yang buruk yang akan terjadi pada Anda atau orang yang Anda cintai?',
#         'Seberapa sering Anda menghindari tempat atau situasi karena Anda merasa itu mungkin menyebabkan Anda stres atau panik?',
#         'Seberapa sering Anda merasa tiba-tiba ketakutan, mengkhawatirkan tentang hal-hal yang tampaknya tidak dikhawatirkan oleh orang lain & tanpa alasan yang jelas?',
#         'Seberapa sering pikiran Anda dipenuhi oleh ketakutan yang Anda tahu tidak rasional?',
#         'Seberapa sering Anda mengalami gejala fisik (seperti berkeringat, gemetar) ketika Anda takut?'
#     ],
#     'disgust': [
#         'Seberapa sering Anda merasa jijik ketika memikirkan kejadian masa lalu tertentu?',
#         'Seberapa sering Anda menghindari makanan, tempat, atau pengalaman tertentu karena membuat Anda merasa mual atau jijik?',
#         'Seberapa sering Anda merasa sangat jijik atau muak terhadap sesuatu yang tampaknya tidak mengganggu orang lain?',
#         'Seberapa sering rasa jijik Anda membuat Anda ingin segera meninggalkan suatu tempat atau situasi?',
#         'Seberapa sering Anda merasakan rasa muak yang mempengaruhi suasana hati atau nafsu makan Anda?'
#     ],
#     'happy': [
#         'Seberapa sering Anda merasa bahagia dan puas?',
#         'Seberapa sering Anda merasa bersyukur atas apa yang Anda miliki?',
#         'Seberapa sering Anda merasa optimis dan bersemangat?',
#         'Seberapa sering Anda merasa tertarik pada hal-hal baru?',
#         'Seberapa sering Anda merasa memiliki tujuan hidup?'
#     ],
#     'nutral': [
#         'Seberapa sering Anda merasa datar atau tidak ada emosi?',
#         'Seberapa sering Anda merasa tidak peduli dengan apa yang terjadi di sekitar Anda?',
#         'Seberapa sering Anda merasa sulit untuk merasakan kebahagiaan atau kesedihan?',
#         'Seberapa sering Anda merasa sulit untuk membuat keputusan?',
#         'Seberapa sering Anda merasa lelah atau tidak memiliki energi?'
#     ],
#     'sad': [
#         'Seberapa sering Anda merasa sedih atau tertekan?',
#         'Seberapa sering Anda menangis atau merasa ingin menangis?',
#         'Seberapa sering Anda merasa putus asa atau tidak berdaya?',
#         'Seberapa sering Anda kehilangan minat pada hal-hal yang biasa Anda sukai?',
#         'Seberapa sering Anda merasa terpisah dari orang lain?'
#     ],
#     'surprise': [
#         'Seberapa sering Anda merasa terkejut atau kaget?',
#         'Seberapa sering Anda merasa mudah marah atau kesal?',
#         'Seberapa sering Anda merasa sulit untuk bereaksi terhadap situasi yang mengejutkan?',
#         'Seberapa sering Anda merasa cemas atau gelisah setelah mengalami sesuatu yang mengejutkan?',
#         'Seberapa sering Anda merasa mudah tersentak atau ketakutan?'
#     ]
# }

# def main():
#     if show_homepage(questions):
#         input_data = st.session_state.input_data
#         for attribute, question_list in questions.items():
#             st.subheader(attribute.capitalize())
#             options = ['Tidak Pernah', 'Sesekali', 'Sering']
#             for i, question in enumerate(question_list):
#                 answer = st.radio(question, options=options, key=f'{attribute}_{i}')
#                 weight = {'Tidak Pernah': 0, 'Sesekali': 1, 'Sering': 2}
#                 if len(input_data[attribute]) <= i:
#                     input_data[attribute].append(weight[answer])
#                 else:
#                     input_data[attribute][i] = weight[answer]

#         # Tombol untuk melakukan prediksi
#         if st.button('Cek Prediksi'):
#             with st.spinner('Sedang memuat hasilmu...'):
#                 time.sleep(1)
#                 # Preprocess input data
#                 input_df = preprocess_input(input_data)
#                 # Membuat prediksi
#                 prediction = make_prediction(input_df)

#                 # Calculate emotion scores for plotting
#                 emotion_scores = {feature: sum(scores) for feature, scores in input_data.items()}
#                 emotion_scores_df = pd.DataFrame(list(emotion_scores.items()), columns=['Emotion', 'Score']).set_index('Emotion')

#                 st.subheader('Grafik Emosi:')
#                 # Plot radar chart
#                 fig = px.line_polar(emotion_scores_df.reset_index(), r='Score', theta='Emotion', line_close=True)
#                 fig.update_traces(fill='toself')
#                 fig.update_layout(
#                     width=400,  
#                     height=400, 
#                     margin=dict(l=40, r=40, t=40, b=40) 
#                 )
#                 st.plotly_chart(fig)

#                 # Menampilkan hasil prediksi
#                 st.subheader('Hasil Prediksi:')
#                 st.write(prediction)
#                 # Menampilkan hasil prediksi dan feedback
#                 show_feedback(prediction)

# if __name__ == '__main__':
#     main()

import streamlit as st
import pandas as pd
import time
import plotly.express as px
import catboost
from template.home import show_homepage
from template.feedback import show_feedback

# Load CatBoost model
model = catboost.CatBoostClassifier()
model.load_model('saved model/catboost_newModel')

# Function to preprocess input data
def preprocess_input(data):
    # Menentukan nama fitur yang sesuai dengan yang diharapkan oleh model
    feature_names = ['angry', 'fear', 'disgust', 'happy', 'nutral', 'sad', 'surprise']
    processed_data = {feature: sum(data[feature]) for feature in feature_names}
    processed_data = pd.DataFrame([processed_data])
    return processed_data

# Function to make prediction
def make_prediction(input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# Define the questions dictionary outside the main function
questions = {
    'angry': [
        'Seberapa sering Anda merasa kesal atau mudah marah?',
        'Seberapa sering Anda merasa mudah tersinggung oleh hal-hal kecil?',
        'Seberapa sering Anda merasa ingin melukai diri sendiri atau orang lain?',
        'Seberapa sering Anda merasa ingin berteriak atau membanting barang?',
        'Seberapa sering Anda merasa sulit untuk mengendalikan amarah Anda?'
    ],
    'fear': [
        'Seberapa sering Anda merasa gugup tentang sesuatu yang buruk yang akan terjadi pada Anda atau orang yang Anda cintai?',
        'Seberapa sering Anda menghindari tempat atau situasi karena Anda merasa itu mungkin menyebabkan Anda stres atau panik?',
        'Seberapa sering Anda merasa tiba-tiba ketakutan, mengkhawatirkan tentang hal-hal yang tampaknya tidak dikhawatirkan oleh orang lain & tanpa alasan yang jelas?',
        'Seberapa sering pikiran Anda dipenuhi oleh ketakutan yang Anda tahu tidak rasional?',
        'Seberapa sering Anda mengalami gejala fisik (seperti berkeringat, gemetar) ketika Anda takut?'
    ],
    'disgust': [
        'Seberapa sering Anda merasa jijik ketika memikirkan kejadian masa lalu tertentu?',
        'Seberapa sering Anda menghindari makanan, tempat, atau pengalaman tertentu karena membuat Anda merasa mual atau jijik?',
        'Seberapa sering Anda merasa sangat jijik atau muak terhadap sesuatu yang tampaknya tidak mengganggu orang lain?',
        'Seberapa sering rasa jijik Anda membuat Anda ingin segera meninggalkan suatu tempat atau situasi?',
        'Seberapa sering Anda merasakan rasa muak yang mempengaruhi suasana hati atau nafsu makan Anda?'
    ],
    'happy': [
        'Seberapa sering Anda merasa bahagia dan puas?',
        'Seberapa sering Anda merasa bersyukur atas apa yang Anda miliki?',
        'Seberapa sering Anda merasa optimis dan bersemangat?',
        'Seberapa sering Anda merasa tertarik pada hal-hal baru?',
        'Seberapa sering Anda merasa memiliki tujuan hidup?'
    ],
    'nutral': [
        'Seberapa sering Anda merasa datar atau tidak ada emosi?',
        'Seberapa sering Anda merasa tidak peduli dengan apa yang terjadi di sekitar Anda?',
        'Seberapa sering Anda merasa sulit untuk merasakan kebahagiaan atau kesedihan?',
        'Seberapa sering Anda merasa sulit untuk membuat keputusan?',
        'Seberapa sering Anda merasa lelah atau tidak memiliki energi?'
    ],
    'sad': [
        'Seberapa sering Anda merasa sedih atau tertekan?',
        'Seberapa sering Anda menangis atau merasa ingin menangis?',
        'Seberapa sering Anda merasa putus asa atau tidak berdaya?',
        'Seberapa sering Anda kehilangan minat pada hal-hal yang biasa Anda sukai?',
        'Seberapa sering Anda merasa terpisah dari orang lain?'
    ],
    'surprise': [
        'Seberapa sering Anda merasa terkejut atau kaget?',
        'Seberapa sering Anda merasa mudah marah atau kesal?',
        'Seberapa sering Anda merasa sulit untuk bereaksi terhadap situasi yang mengejutkan?',
        'Seberapa sering Anda merasa cemas atau gelisah setelah mengalami sesuatu yang mengejutkan?',
        'Seberapa sering Anda merasa mudah tersentak atau ketakutan?'
    ]
}

def main():
    if show_homepage(questions):
        input_data = st.session_state.input_data
        for attribute, question_list in questions.items():
            st.subheader(attribute.capitalize())
            options = ['Tidak Pernah', 'Sesekali', 'Sering']
            for i, question in enumerate(question_list):
                question_text = f'{i + 1}. {question}'
                st.markdown(f'<p style="color:black;">{question_text}</p>', unsafe_allow_html=True)
                answer = st.radio("", options=options, key=f'{attribute}_{i}')
                weight = {'Tidak Pernah': 0, 'Sesekali': 1, 'Sering': 2}
                if len(input_data[attribute]) <= i:
                    input_data[attribute].append(weight[answer])
                else:
                    input_data[attribute][i] = weight[answer]

        # Tombol untuk melakukan prediksi
        if st.button('Cek Prediksi'):
            with st.spinner('Sedang memuat hasilmu...'):
                time.sleep(1)
                # Preprocess input data
                input_df = preprocess_input(input_data)
                # Membuat prediksi
                prediction = make_prediction(input_df)

                # Calculate emotion scores for plotting
                emotion_scores = {feature: sum(scores) for feature, scores in input_data.items()}
                emotion_scores_df = pd.DataFrame(list(emotion_scores.items()), columns=['Emotion', 'Score']).set_index('Emotion')

                st.subheader('Grafik Emosi:')
                # Plot radar chart
                fig = px.line_polar(emotion_scores_df.reset_index(), r='Score', theta='Emotion', line_close=True)
                fig.update_traces(fill='toself')
                fig.update_layout(
                    width=400,  
                    height=400, 
                    margin=dict(l=40, r=40, t=40, b=40) 
                )
                st.plotly_chart(fig)

                # Menampilkan hasil prediksi
                st.subheader('Hasil Prediksi:')
                st.write(prediction)
                # Menampilkan hasil prediksi dan feedback
                show_feedback(prediction)

if __name__ == '__main__':
    main()
