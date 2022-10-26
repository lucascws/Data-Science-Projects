# Capstone Project - Predicting Pet Adoption Outcome 

# Introduction

## Executive Summary

The purpose of this project is to use data science to help animal shelters get more pets adopted in a bid to tackle shelter overcrowding and reduce euthanasia rate for shelter animals. There are three goals for the project. Firstly, it is to identify the factors or characteristics that influences pet adoption outcomes. Secondly, it is to build a classifier model to predict a pet’s adoption outcome. Lastly, I will also create an image search function to allow potential adopters to search for similar looking pets. The analysis of the variables indicates that age and the number of photos has a strong correlation with the pets adoption outcome. Pure-breed pets and pets that have rarer characteristics tend to be adopted more quickly too (longer fur and golden/cream color). Using Sentence BERT and EfficientNet models, features were extracted in the form of text and image embeddings to use for modeling. The final best model, an LightGBM model taking in all features, produced a precision score of 0.616 and AUC-ROC of 0.767 on the test set, which was a significant improvement on the baseline model. Image search was finalized using JINA Now to create a web-app for a image-to-image neural search.

[Presentation Link](https://docs.google.com/presentation/d/1__w8mf5US1aJ_Otg_dlM6X6e4mj7NIAvRq7aNizzQss/edit?usp=sharing)

## Problem Statement

Animal Shelters face the issue of shelter overcrowding and limited resources. The longer a pet remains in a shelter, the higher the risk of the pet being euthanized. The aim of this project is to help more pets get adopted. In order to do so, I will firstly examine what are some traits that influences pet adoption outcomes. Next, a classifier model will be created to predict whether pets will be adopted within a 100 days to help animal shelters identify the pets to allocate resources to. Lastly, an image search model will be developed to help adopters search for similar looking pets in the adoption listing.

## Goals

1. Findings on what influences pet adoption outcomes
- What are some features that make a pet more desirable and vice versa

2. Adoption Outcome Prediction
- Build a classifier model to predict pet adoption outcome for incoming pets

3. Image Search for pets
- Build an Image Search App to allow the searching of similar pets from the listing

## Background 

"Dogs and cats are domesticated animals who depend on humans to meet their needs for food, water, veterinary care, shelter, and safety and cannot survive for long on their own." [(source)](https://www.peta.org/issues/animal-companion-issues/overpopulation/)
Shelter overpopulation is a critical issue. The longer pets are housed in an animal shelter, the more likely they will be euthanized.  This problem has been excabated during the lockdowns over the world during the covid 19 pandemic. For instance, in Malaysia, the nationwide implementation of the Movement Control Order (MCO) heavily impacted adoption rates. [(source)](https://www.nst.com.my/news/nation/2020/04/582694/animal-shelters-running-out-space-food) 
In the US alone, over 6 million pets are put into animal shelters every year, of which roughly 3 million are cats and the other 3 million are dogs. Of these animals, approximately 1 million of them are euthanized every year. [(statistics)](https://www.aspca.org/helping-people-pets/shelter-intake-and-surrender/pet-statistics) 

The goal of this project is to identify some ways we can use Data Science or other technologies to help tackle this issue that occcurs all over the world. Digitisation has proven to be an effective way to help animal shelters. In one animal shelter in the USA, they managed to cut their operation cost \\$262,570 by successfully digitizing, reducing staffing requirements and streamline many processes. [(source)](https://tdwi.org/articles/2016/09/09/analytics-digital-records-pet-shelters.aspx) Throughout this project, we will analyse three specific methods that might be able to help animal shelters increase their adoption rate. Firstly, we can identify what influences adoption outcome to analyse if there are ways we can enhance a pet's profile to boost adoption. Animal shelters have limited resources and space.[(source)](https://www.sittingforacause.com/blog/adopt-dont-shop/3-problems-facing-animal-shelters/) These resources are usually derived from donations and volunteerism. The second task from this project is to develop a classification model to help predict if a pet will be adopted within a 100 days based on their characteristics and profile. Doing so will help animal shelters identify the pets that would require more resources in the form of marketing and adoption drive to increase their chances of adoption. This will hopefully result in animal shelters being able to manage their resources more effectively. The last component of the project will be to develop an image search function to allow for the searching of similar looking pets in the listing to help adopters search for similar looking pets in the adoption listing.

## Dataset
For this project, I will be using a dataset comprising of pets from animal shelters all over Malaysia. The dataset comes from a pet adoption platfrom 'PetFinder Malaysia'. While the dataset here is localized to Malaysia, the results of this project would be transferrable to dataset for other countries with minor tweaking. The dataset contains information for the pet listed. This includes their profile picture, description summary as well as the pet's health, status and features.

[Petfinder Dataset Source](https://www.kaggle.com/competitions/petfinder-adoption-prediction/data)

# Summary of EDA

- The features that have a higher correlation to the target variable are age, number of photos and presence of profile picture
- 27% of the pets do not get adopted (4197)
- Cats have a higher adoption rate as compared to dogs. About 30% of dogs are not adopted within a 100 days
- Most listed pets are very young, younger pets have a much higher rate of adoption
- Most Breeds are mixed breed(dogs) and domestic (cats) 
- Pure breed pets are more likely to get adopted
- Male have a slightly higher adoption rate than female
- Majority of the pets are black or brown in color
- Colors that are less common seem to have a higher adoption rate
- Multi-colored pets also seem to have a slightly better adoption rate (27% not adopted) compared to single colored pets (30% adopted)
- Medium size pets have the worst adoption rate (29% not adopted) while small pets have the best (25% not adopted)
- Most pets have short hair. Very few pets have long fur
- Pets with long fur have the highest adoption rate (16% not adopted) while pets with shorter fur have the lowest adoption rate (30% not adopted)
- Rarer traits seem to positively impact adoption outcome
- For Vaccination, Dewormed and sterilization, adopters tend to prefer pets that have not undergone any of the procedure - perhaps they want to do it themselves
- Not having information about these negatively impacts adoption outcome
- Adoption rates becomes worse as health deteriorates. Healthy pets have 28% unadopted while for pets with serious injury, 41% are not adopted
- When there is a high fee, pets are adopted faster, perhaps people are more inclined to pay for a more ‘desirable’ pet
- A small fee tends to make the pet less desirable
- Pets with no photo have a worse adoption rate (62% not adopted)
- A higher number of photos tend to lead to better adoption rate
- Most frequent words for adopted and non adopted profile does not seem to differ much
- Pets with longer Description in their profile have a slightly better adoption chance

# Feature Engineering

## Text and Image Embeddings

Text and Image features are extracted using pre-trained Neural Network models. For the description of each profile, a Sentence BERT model was used to obtain a fixed size vector for all the rows in the dataset. A BERT model was chosen to capture the contextual meaning of the sentence. For the image, a CNN model was used. CNN models are are a class of Neural Network models that are specialized in processing image data. 

## Image Search

An image search was performed using the embeddings extracted from the images. I took the K-Nearest-Neighbour after generating the cosine similarity from the images in the dataset. However, using KNN for an image search is limited in terms of scalability. I finally constructed the image search using JINA Now, which uses Approximate Nearest Neighbour instead. JINA Now also creates the embedding for the images automatically and productionizes the web-app on their cloud server. 

## Modelling

For the modelling section, I have constructed three separate models:
1. Baseline Model - I will firstly create a baseline model to compare the modelling results against
2. Model with tabular features - I will create a model with just the tabular dataset
3. Model with all features - I will create a model with all the data, including the image and text embeddings

**Metrics**

To understand which metrics to choose, we have to understand the context of the problem. In this case, the target audience are Animal Shelters. Animal Shelters are constraint by limited financial resources and manpower. The purpose of the prediction is to identify the animals that the shelters can allocate the limited resources to, in the hopes of increasing their adoption chance. Therefore, I have chosen these metrics to look at.

1. The main metric I will be considering is the Precision score. Precision explains how many of the correctly predicted cases actually turned out to be positive. Precision is useful when False Positive is of a higher concern than False Negatives. Here, I prioritise reducing False Positives due to the limited resources of the Animal Shelters. While this might mean more pets that are likely not to get adopted will get misclassified by the model, the shelters are already constraint by their resources and they might not be able to allocate resources to all these pets. 
2. A secondary metric I will consider is the AUC-ROC score, which is a measure of the ability of a classifier to distinguish between the target classes.  The AUC-ROC curve plots the TPR(True Positive Rate) against the FPR(False Positive Rate) at various threshold values This means it is an indication of how good the model is at distinguishing the Adopted and not adopted pets. 
3. Lastly, I will also consider the computational time taken for the model. 

**Method**

The dataset here is not balanced. We have 72% of the data for pets that are adopted and 28% with pets that are not adopted after a 100 days. Thus, there are too little information of the minority class for a model to effectively distinguish between the two.

- To address the imbalanced dataset, I will firstly use the SMOTE (Synthetic Minority Oversampling Technique) method. SMOTE synthesises new data from the minority class. It does this by using information from randomly selected sample from minority class and one of its k nearest neighbors, creating new synthetic data. 
- I will also stratify the data to ensure the proportion of each classes remain when splitting the dataset


## Adoption Outcome Prediction Model

| Metric    | Baseline | LightGBM with tabular data | LightGBM with all data |
|-----------|----------|----------------------------|------------------------|
| Precision | 0.436    | 0.574                      | 0.616                  |
| AUC-ROC   | 0.708    | 0.741                      | 0.767                  |

Based on the modelling results, the lightGBM model that takes in the tabular data and the text and image embeddings gives the best results. However, it also takes substantially longer to run as compared to the LightGBM model with only the tabular data as features. Depending on the computational constraints, one of the two models can be used

# Conclusion

## Analysis of what influences pet adoption outcome

Based on the dataset explored, I have compiled some of the key factors that influences the adoption outcome of the pets. 

1. One strong influencer is the age of a pet. The older the pet, the less likely it is to get adopted.
2. Pets that are of pure breed are also more favourable to adopters
3. Pets that have rarer traits are more likely to get adopted - such as being of a less common color (cream/golden) and having long fur
4. Healthy pets are more likely to get adopted
5. Pets that are not vaccinated/dewormed/sterilized are more likely to get adopted than those that are. Having no information about this also negatively impacts adoption outcome
6. Having more pets in a single listing also reduces adoption chances
7. Having more photos seem to help with adoption outcome
8. Longer summary and description seems to increase adoption chance

## Limitations

1. While we can analyse the characteristics that can be obtained in the form of data, there are many intrinsic factors that we cannot account for in predicting adoption. For instance, there is no information on how friendly a pet is or other behavioral characteristics that can deeply influence a pet. Moreover, there is also the connection between the potential adopters and each of the pet, which cannot be quantified. 
2. Since this is a Malaysian dataset, there could be other factors (political/social) that might influence adoption and we are not able to account for this. Moreover, to use the models from this project for other countries, we might have to tweak/re-train the model to account for some features such as the State location. We would also need to include more breeds of dogs that might not be prevalent in Malaysia to ensure the model have information on those.

## Recommendation

**Improve Pet Profile**

While most of the factors/characteristics of the pet cannot be changed, there are still some way animal shelters can help improve the chances of adoption. They can firstly, take a profile picture for pets that do not have one already and include more pictures for pets. When there are multiple pets, the shelters can separate each pet listing profile so that each pet have one single profile, instead of putting multiple pets in the same profile. Shelters can also provide a longer and more meaningful description for the pet that is up for adoption. Lastly, shelters can consider putting in some resources to identifying the vaccination/deworming/sterilisation status of the pets that are not already known. An area that needs more analysis is whether shelters should consider not vaccinating/deworming/sterilizing the pets. While it seems to boost adoption chances, there is also the health and safety factor of the pets to consider. Alternatively, providing more information on these, such as which vaccination and the vet responsible, can be provided to potential adopters.

**Prediction Model** 

Shelters can make use of the predictions from the LightGBM model to better allocate resources to the pets that are likely not to be adopted. This can come in the form of volunteers, marketing campaigns and adoption drive for the unadopted pets.

**Image Search**

Shelters can consider collaborating and implementing the image search using the photos of all the pets they have in their database. This could allow potential adopters to search for similar looking pets from an image of a pet they have (possibly a pet that resembles their old pet that has passed on) across all the shelters that have uploaded their pet's profile picture. 
