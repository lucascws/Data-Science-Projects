# Introduction

## Executive Summary

In this project, the aim is to assist a new gaming store in the setting up of the online forum for the local community by implementing a classification model for them to tag/allocate their post to either 'PS5' or 'Xbox'. To achieve this, we utilise the latest posts from reddit for the respective consoles. In addition, they need insights from the console gaming community to aid in their marketing campaign to determine the focus. From our research, PS5 seems to be have more popular and active community than Xbox. For both consoles, the trending topics are similar. Those topics are their subscription services, PS Plus and Game Pass, the top games as well as the controllers. After performing sentiments and emotions analysis on the reddit posts, games, in general, seems to garner the most positive sentiments. Thus, games could be a focus for a marketing campaign. To classify the post into PS5 and Xbox, we will use a classification model as the variable here is a binary variable. After evaluating the various models, our top three models are Logistic Regression, Light GBM and Random Forest. The Logistic Regression Model was chosen as the best model as it gave the best accuracy score.

## Problem Statement

A gaming store has been newly set up. The owners wish to build its business activities, and increase its physical and online presences.
To start off, they would like to find out which topics of the major consoles (PS5 and Xbox) are trending. At the same time, they are exploring the idea of having a forum on their website that allow discussion among gaming community, and e-commerce section to include product reviews. 
We are engaged to develop a classification model that predicts which category a post belongs to. This will be helpful for their forum moderation/upkeep while users experience better navigation of the store’s online space with the help of accurate tagging/sections allocation. 
We are also tasked to identify the recent topics of interest and the community’s sentiments towards them to aid them in their marketing campaign. This would provide them an indicative area of focus.

To address thos problem, our goal is to: 
- Identify the hottest topics from the subreddits of PS5 and Xbox Series X
- What are general sentiments and emotions of the community in general and towards the topics/products
- Develop a Classification Model to distinguish PS5 and Xbox posts
    - Our objective is to classify post without the words 'PS5' and 'Xbox' (or similar words) in them as those posts can be automatically tagged/allocated
    
### Key Questions

- Which community is more active?
- What are the trending topics for each community?
- Which products should we focus our marketing on?
- Regarding top topics, what are the community’s sentiments and emotions towards them?
- What is the best model to classify post

### Process

- Data Collection
- Data Cleaning and Exploration
- Pre-processing
- Modelling
- Model Evaluation
- Sentiments and Emotions Analysis

# Data Collection

To achieve our objective, we will extract the last 15,000 posts from the PS5 and Xbox Series X subreddit respectively to analyse.
We will Webscraped using Pushshift Reddit API for the Subreddits, PS5 (PlayStation 5) and XBox Series X. 
The time frame we will use: Before 24 Jun 2022 0000hr

14986 out of 15000 PS5 post were extracted. 
Our ps5 dataset covers posts from the period of 8 March 2022 to 24 Jun 2022
14996 out of 15000 Xbox post were extracted.
Our Xbox dataset covers posts from the period of 31 January 2022 to 24 Jun 2022

# Data Cleaning and EDA

## EDA

There are 10479 unique words in the ps5 corpus
The top occurring unigrams for both datasets contain some common words like ‘game’, ‘controller’ and their respective console specific words like
playstation and xbox 
The top bigram words for PS5 are PS Plus, games such as Elden Ring, Final Fantasy and Horizon Forbidden West and PS5 Controller
There are 10003 unique words in the Xbox corpus
The top bigram words for Xbox are Game Pass, Elden Ring, Halo Infinite, Dying Light and Series Controllera
Both Count Vectorizer (Most Frequent) and TD-IDF (Most important) returns mostly the same words

Judging by the count of post and the period of the 15,000 post for each subreddit, PS5 definitely looks like it is the more popular console
During the last few months, ps5 has more post on average. 

## Data Cleaning and Preprocessing

We will use the title, subreddit and created date for our analysis. During our cleaning of the title column, we remove noises in our data such
as the html links, symbols and any markdown language like '/n'. We also covert our emojis to text. Then, stop words are removed from the corpus.
Some custom stopwords were also included. These are words like PS5, Xbox or words similar to them. Most Documents have words less than 13 words. 
There are a small group of documetns with more than 20 words. We only kept documents with at least 2 words as single word documents do not seem 
to be useful for our modelling.

We assess both Stemming and Lemmatizing. Stemming was used as it reduced the number of features by a greater magnitude.
There are 11354 words remaining after stemming. Most of the top words remain after cleaning - with the exception of the PS5/Xbox words.


# Model

We kept 20% of the data as a holdout sample which is not exposed to any fitting from the modelling. We generate predictions against this dataset.
**Target Labels**
- PS5: 1
- Xbox: 0

Since our target variable is a binary value, this is a classification problem. We will evaluate the classification models to get the best model. 
As a baseline, we will use a Naive Bayes model after performing a Count Vectorizer. The baseline model achieve an accuracy score of 70%.

The proportion of target variables are balanced. Therefore, accuracy would be the selected metric to evaluate our models. In addition, in this 
context, the consequences of False Negative and False Positive is more or less the same. Our goal is to accurately categorise both PS5 and Xbox titles.

I will use a TF-IDF vectorizer for my model factors in the importance of the word relative to other documents in the corpus. This will reduce the effects 
of words that are frequent in both Xbox and PS5 subreddit but has no predictive power. Also, I will proceed with a unigram and bigram bag of words. As
seen from our EDA section, many of the top games and features of each console appear in our top bigram. 

## Model Evaluation

The top 3 models we will evaluate are Random Forest, Light GBM and Logistic Regression. I will tuned the hyperparameters in order to get the best results.


| Model       | Logistic Regression | Random Forest | LightGBM | Naive Bayes |
|-------------|---------------------|---------------|----------|-------------|
| Train Score | 0.7205              | 0.9493        | 0.7472   |    0.7149   |
| Test Score  | 0.7038              | 0.6896        | 0.6974   |    0.7008   |

From our results, Logistic Regression gives the best accuracy of 0.70. This means 70% of the future post are likely to be classified correctly. The other 
two models show signs of overfitting, especially for Random Forest, as the train score is significantly higher than the test score. The result is also slightly 
better than our baseline model (0.7008) in terms of accuracy. In addition, a Logistic Regression is computationally inexpensive compared to Random Forest and 
LightGBM and easy to interpret. Therefore, a Logistic Regression is the best model.

# Sentiments and Emotion analysis

Overall, the results from our sentiment and emotion analysis could be useful for problem statement. In general, the results from sentiments analysis seem
to be a better indication than the emotions analysis due to the neutral nature of most posts. Games then to be a topic that generates more positive 
sentiments for both console. On the other hand, the controller seems to be a topic that is not well-received, possibly due to complaints or issues. 
Game Pass subscription seems to be well received as compared to PS Plus as well. This are some insights that could be useful for our client's marketing 
campaign

# Conclusion and Recommendation

## Conclusion

From our research, it is indicative that PS5 is the more popular of the two. However, we should not disregard Xbox as it is still a huge community and potential market. For both consoles, the topics of interest seems to be the top games and their subscription services. The top games are generally the post that garner more positive sentiments. Xbox Game Pass also seems to be well-received. Our sentiments and emotions analysis also do indicate that most community post are neutral in nature. In order to create a solution for the tagging of posts for the local gaming forum, we will use a Logistic Regression Model that is trained on reddit post to distinguish an Xbox topic from a PS5 topic.

## Limitations

Both consoles tend to have very similar topics as well as same words that appear prominently in many of their posts as they are both very similar in nature. These words that appear commonly in both topics - such as games, controller and trailers could be factors that limit our predictions. 

Emotions analysis seem to be ineffective in giving accurate outcomes due to the neutral nature of most post on reddit and might not be effective in predicting titles that relate to questions, news and facts.  

## Recommendation

Marketing Campaign: 

- Allocate more resources to PS5 products
- Avoid focusing on the controllers for each console
- Prioritse Game Pass for Xbox over PS Plus
- The top games for each console are generall well received and could be the main focus for marketing

Forum/product review categorisation:

- A Logistic Regression Model can be implemented to help with the tagging of documents