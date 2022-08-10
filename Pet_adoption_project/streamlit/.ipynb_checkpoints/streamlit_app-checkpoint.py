import streamlit as st
from pycaret.classification import *
import pandas as pd
import numpy as np
import cv2
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input, EfficientNetV2B3
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import AveragePooling1D, Lambda, Input, MaxPooling2D, GlobalMaxPooling2D
import tensorflow.keras.backend as K
from tensorflow.keras.models import load_model as tf_load_model
from sentence_transformers import SentenceTransformer
import re
import emoji
from PIL import Image

image_model = tf_load_model('../models/image_embeddings.h5')
text_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
pred_model = load_model('../models/pred_model2')

def resize_image(im, img_size=300):
    # Get original size of image in height and width
    original_size = im.shape[:2]
    ratio = float(img_size)/max(original_size)
    # resize both length and width with the same ratio so image will not be distorted
    new_size = tuple([int(measurements*ratio) for measurements in original_size])
    im = cv2.resize(im, (new_size[1], new_size[0]))
    # find empty spaces area the shorter size
    delta_w = img_size - new_size[1]
    delta_h = img_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    # padding with black color
    color = [0, 0, 0]
    # copy image into the middle and fill sides/top/bottom empty spaces with black color
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,value=color)
    return new_im

def process_image(img_file):
    # create blank canvas image
    processed_img = np.zeros((1,300,300,3))
    # read image
    try:
        img = Image.open(img_file)
        img = img.save("img.jpg")
        image = cv2.imread('img.jpg')
        image = resize_image(image)
        image = preprocess_input(image)
        processed_img[0] = image
    except:
        pass
    img_embeddings = image_model.predict(processed_img)
    img_embeddings = img_embeddings[0]
    img_embedding_dict = {}
    for i in range(len(img_embeddings)):
        img_embedding_dict[f'image_{i}'] = img_embeddings[i]
    return img_embedding_dict

def clean_text(description):
    clean_description = re.sub(r"http\S+", '', description)
    clean_description = emoji.demojize(clean_description)
    clean_description = re.sub(r"\b([-'])\b|[\W_]", ' ', clean_description)
    clean_description = re.sub(r' +', ' ', clean_description)
    return clean_description

def get_text_embeddings(cleaned_text):
    text_embedding = text_model.encode(cleaned_text)
    text_embedding_dict = {}
    for i in range(len(text_embedding)):
        text_embedding_dict[f'text_{i}'] = text_embedding[i]
    return text_embedding_dict

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


with st.form("my_form"):
    
    #### Title for Webpage ####
    st.title("🐶 Pet Adoption Prediction 😺")

    ### Selection ####

    uploaded_img = st.file_uploader("Choose an image file")

    description = st.text_input('Pet Description', ' ')

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
        
    submitted = st.form_submit_button("Predict Outcome")
    
    if submitted:
        img_embedding_dict = process_image(uploaded_img)
        cleaned_description = clean_text(description)
        description_len = len(cleaned_description)
        description_wc = len(cleaned_description.split())
        text_embedding_dict = get_text_embeddings(cleaned_description)

        tab_data = {'Type': type_pet,
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
                 'photo' : photo,
                 'desc_length': description_len,
                 'desc_word_count': description_wc}
        tab_data = pd.DataFrame.from_dict(tab_data, orient='index').T
        text_data = pd.DataFrame.from_dict(text_embedding_dict, orient='index').T
        image_data = pd.DataFrame.from_dict(img_embedding_dict, orient='index').T
        input_data = pd.concat([tab_data, text_data, image_data], axis=1)

        outcome = predict_outcome(input_data)

        # Write out the result to the frontend
        st.write(outcome)
