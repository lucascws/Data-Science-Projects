import streamlit as st
from pycaret.classification import *
import pandas as pd

pred_model = load_model('pred_model1')

def predict_outcome(input_data):
    prediction = predict_model(pred_model, data=input_data)
    outcome = prediction.iloc[0,-2]
    if outcome == 1:
        result = "Pet will not get adopted"
    elif outcome == 0:
        result = "Pet will get adopted"
    return result

maturity_size_options = {1: 'Small', 2: 'Medium', 3: 'Large'}
fur_length_options = {1: 'Short', 2: 'Medium', 3: 'Long'}
status_options = {1: 'Yes', 2: 'No', 3: 'Not Sure'}
health_options = {1: 'Healthy', 2: 'Minor Injury', 3: 'Serious Injury'}
mixed_breed_option = {0: 'No', 1: 'Yes'}
multi_color_option = {0: 'No', 1: 'Yes'}
fee_option = {0:'No Fee', 1: 'Small Fee (<500)', 2:'High Fee (>500)'}
photo_option = {0: 'No', 1: 'Yes'}

#### Title for Webpage ####
st.title("🐶 Pet Adoption Prediction 😺")

### Selection ####

quantity = st.slider('Number of Pets up for adoption', min_value=1, max_value=50, step=1)

cols1, cols2 = st.columns(2)

with cols1:
    
    type_pet = st.selectbox('Type of Pet?', 
                            ('dog', 'cat'))

    main_color = st.selectbox('Primary Color of Pet?', 
                              ('Black', 'Brown', 'Cream', 'Golden', 'Gray', 'White', 'Yellow'))
    
    mixed_breed = st.selectbox('Is pet a Mixed/Unknown Breed?', 
                               list(mixed_breed_option.keys()), 
                               format_func=lambda x: mixed_breed_option[x])

    age = st.slider('How old is the Pet (Months)', min_value=1, max_value=200, step=1)

    vaccinated = st.selectbox('Is Pet Vaccinated?', 
                              list(status_options.keys()), 
                              format_func=lambda x: status_options[x])

    dewormed = st.selectbox('Has Pet been Dewormed?', 
                              list(status_options.keys()), 
                              format_func=lambda x: status_options[x])
    
    photo = st.selectbox('Does Pet have a Profile Picture?', 
                         list(photo_option.keys()), 
                         format_func=lambda x: photo_option[x])
    
    state = st.selectbox('Which State is the Pet in?', 
                         ('Johor', 'Kedah', 'Kelantan', 'Kuala Lumpur', 'Labuan', 'Melaka', 'Negeri Sembilan',
                         'Pahang', 'Perak', 'Pulau Pinang', 'Sabah', 'Sarawak', 'Selangor', 'Terengganu'))

with cols2:

    gender = st.selectbox('Gender?', 
                      ('male', 'female'))

    multi_color = st.selectbox('Is pet multi-colored?', 
                               list(multi_color_option.keys()), 
                               format_func=lambda x: multi_color_option[x])

    size = st.selectbox('Size of Pet?', 
                        list(maturity_size_options.keys()), 
                        format_func=lambda x: maturity_size_options[x])

    fur_length = st.selectbox('Length of Pet\'s fur?', 
                              list(fur_length_options.keys()), 
                              format_func=lambda x: fur_length_options[x])

    health = st.selectbox('What is the health status of the Pet?', 
                          list(health_options.keys()), 
                          format_func=lambda x: health_options[x])
    
    sterilized = st.selectbox('Is Pet Sterilized?', 
                              list(status_options.keys()), 
                              format_func=lambda x: status_options[x])
    
    photoamt = st.slider('Number of Photos in profile', min_value=0, max_value=25, step=1)
    
    fee = st.selectbox('Fee Amount?', 
                       list(fee_option.keys()), 
                       format_func=lambda x: fee_option[x])

if st.button("Predict Pet Adoption Outcome"):
    input_data = {'Type': type_pet,
             'Age': age,
             'Gender': gender,
             'Color1' : main_color,
             'MaturitySize' : size,
             'FurLength' : fur_length,
             'Vaccinated' : vaccinated,
             'Dewormed' : dewormed,
             'Sterilized' : sterilized,
             'Health' : health,
             'Quantity' : quantity,
             'State' : state,
             'PhotoAmt' : photoamt,
             'mixed_breed' : mixed_breed,
             'multi_color' : multi_color,
             'FeeAsked' : fee,
             'photo' : photo}
    input_data = pd.DataFrame.from_dict(input_data, orient='index').T
    outcome = predict_outcome(input_data)
    
    # Write out the result to the frontend
    st.write(outcome)