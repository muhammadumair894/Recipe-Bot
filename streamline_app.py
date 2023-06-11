import openai
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

st.set_page_config(page_title="ChatBot")

# Sidebar contents
with st.sidebar:
    st.title('Diet Recommendation')

st.markdown("""
          <style>
          footer {visibility: hidden;}
          </style>""", unsafe_allow_html=True)

with st.sidebar:
    openAPIkey = st.text_input('Your OpenAI API KEY', type="password")

# Generate empty lists for generated and past.
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Please fill the following questions."]
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# Questionnaire
with st.form(key='questionnaire'):
    user_AGE = st.text_input("What is your age?")
    user_TP = st.text_input("How long have you been trying to get pregnant?")
    user_MW = st.text_input("What week of your menstrual cycle will this be for?")
    user_PI = st.text_input("Do you have PCOS/Insulin resistance? (Yes/No)")
    user_E = st.text_input("Do you have Endometriosis? (Yes/No)")
    user_H = st.text_input("Do have Hasimotos? (Yes/No)")
    user_AO = st.text_input("Do your basal body temperatures stay above 98 after ovulation? (Yes/No)")
    user_BO = st.text_input("Are your basal body temperatures above 97.6 before ovulation (on average)? (Yes/No)")
    user_MS = st.text_input("How many days of menstrual bleeding do you have? (3 or less, 4, more than 4)")
    user_DR = st.text_input("Do you have any dietary restrictions or aversions?")
    submit_button = st.form_submit_button(label='Submit')

# Response output
def generate_response():
    #openai.api_key = "sk"
    openai.api_key = openAPIkey
    role = f"""
     ...
    The user is {user_AGE} years old and has been trying to get pregnant for {user_TP}.
    The user is in week {user_MW} of their menstrual cycle.
    The user has PCOS/Insulin resistance: {user_PI}.
    The user has Endometriosis: {user_E}.
    The user has Hasimotos: {user_H}.
    The user's basal body temperatures stay above 98 after ovulation: {user_AO}.
    The user's basal body temperatures are above 97.6 before ovulation (on average): {user_BO}.
    The user has {user_MS} days of menstrual bleeding.
    The user's dietary restrictions or aversions are: {user_DR}.
    """
    prompt = "Generate Diet Plan"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": role},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

with response_container:
   
