#Necessary imports
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from textblob import TextBlob
from nltk.tokenize import sent_tokenize
from gensim.summarization.summarizer import summarize 
from gensim.summarization import keywords
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()


#Headings for Web Application
st.title("NLP App")
st.subheader("Pillih Jenis NLP")

#Picking what NLP task you want to do
option = st.selectbox('NLP Service',('Sentiment Analysis', 'Summarization')) #option is stored in this variable

#Textbox for text user is entering
st.subheader("Input Text untuk dianalisis atau input 5 paragraf kalimat untuk Summary.")
text = st.text_input('Enter text') #text is stored in this variable

#Display results of the NLP task
st.header("Results")

#Function to take in dictionary of entities, type of entity, and returns specific entities of specific type
def entRecognizer(entDict, typeEnt):
    entList = [ent for ent in entDict if entDict[ent] == typeEnt]
    return entList


#Sentiment Analysis
if option == 'Sentiment Analysis':

    #Creating graph for sentiment across each sentence in the text inputted
    sents = sent_tokenize(text)
    entireText = TextBlob(text)
    sentScores = []
    for sent in sents:
        text = TextBlob(sent)
        score = text.sentiment[0]
        sentScores.append(score)

    #Plotting sentiment scores per sentencein line graph
  

    #Polarity and Subjectivity of the entire text inputted
    sentimentTotal = entireText.sentiment
    st.write("The sentiment of the overall text below.")
    st.write(sentimentTotal)

#Named Entity Recognition
else:
    
    #Getting Entity and type of Entity
    summWords = summarize(text)
    st.subheader("Summary")
    st.write(summWords)
#Text Summarization

   