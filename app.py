import os
from pathlib import Path
import streamlit as st
from preprocessing import length,lowercase,remove_punctuations,removing_stopwords,removing_numericals,get_lemma2,remove_tokens,tokenizer
import pandas as pd
import gensim
from gensim.corpora import Dictionary
from gensim import models
from nltk.tokenize import RegexpTokenizer

st.title("Topic Modelling")
st.subheader("Lets find what the documents talks about")

# preprocessing
filenames = os.listdir('.\\testcase')
selected_filename = st.selectbox('Select a file', filenames)    

if selected_filename != '':
    try:
        article = Path('.\\testcase\\' + selected_filename).read_text().replace('\n','')
    except FileNotFoundError:
        st.error('File not found.')

if st.checkbox('preprocessing'):
    st.subheader('lets do it..!')
    if st.button('process'):
        article = lowercase(article)
        article = remove_punctuations(article)
        article = removing_stopwords(article)
        article = removing_numericals(article)
        article = remove_tokens(article)
        article = get_lemma2(article)
        st.write(article)
algorithm = st.radio( 'model', ('LDA','NMF'))
if algorithm == 'LDA':
    if st.button('extract'):
        LDA_model = models.LdaModel.load('lda_test.model')
        loaded_dct = Dictionary.load_from_text('Doc_2_Bow')
        article = tokenizer(article)
        bow_test_doc = loaded_dct.doc2bow(article)
        topics_list =  LDA_model.get_document_topics(bow_test_doc)
        df = pd.DataFrame(topics_list,columns=['topics','weightage'])
        st.write(df)

    if st.button('Show training topics'):
        # Training important words
        num_of_words = st.slider('Select Top Important words per Topic', 0, 15, 5)
        def words_per_topic(num_of_words):
            '''
            function returns list of tuples, in tuples pair of topic number and topwords in topics along with weightage
            '''
            LDA_model = models.LdaModel.load('lda_test.model')
            topics = LDA_model.print_topics(num_words=num_of_words)
            for topic in topics:
                return topics

        # applying function
        words_per_topic = words_per_topic(num_of_words)

        # break the tuple and returns texts along with weightage
        words_topic_list = [tuples[1] for tuples in words_per_topic]

        def topic_word_df(dist):

            '''
            function takes texts along with weightage and returns dataframe  of important texts
            '''

            #split the string with given delimiters
            tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-+|\*+|\"")
            d = tokenizer.tokenize(dist)

            # returns list of string not having given delimiter
            d = [x for x in d if x != '0']
            d = [x for x in d if x != '+']

        # returns dataframe with important words
            text = []
            final = ','
            for elem in d:
                text.append(elem[5:])
                string = final.join(text)
            return pd.DataFrame(string.split(','))


        df_ = pd.DataFrame()
        for i in range(len(words_topic_list)):
            df = topic_word_df(words_topic_list[i])
            df = df.rename(columns={0:'topic_' + str(i)})
            df_['topic_' + str(i)] = df
    
        st.write(df_)