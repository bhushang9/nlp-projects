# pip install -U streamlit
# (streamlit run app.py) or (python -m streamlit run app.py)

import streamlit as st
import pickle

# loading the model
model = pickle.load(open('sentiment_analysis.pkl', 'rb'))

# create the title
st.title('IMDB Sentiment Analysis Model')

review = st.text_input('Enter your review:')

submit = st.button('Predict')

if submit:
    prediction = model.predict([review])

    # print(prediction)
    # st.write(prediction)

    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')