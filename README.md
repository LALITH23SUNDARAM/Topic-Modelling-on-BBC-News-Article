
## Topic Modeling on News Articles

**Abstract:** 
Are you really wondering what is and where Topic extraction is being used? Before getting an answer to the above question, lets yourself respond to the following questions.
   
 *  what Indians are talking about their goverment over twitter?
 *  How different channels potrait news about covid?
 *  Whats are the discussions carried out in Last three years NIPS Conference?
To perform these tasks, we can manually go through some popular Twitter tweets, read popular news channel articles one by one to know about how they capture during the pandemic period or read the post-conference NIPS scripts. This is the way we are able to extract, what's all talk about. But do you think is this the efficient step to do. It consumes a heavy period and may not produce results as we expected. Here were Machines came to help us, But they are not good at computing rather than Numericals. We have to pretreat our input as machines can be understood. This project is all about what are the preprocessing steps, how to implement different tools to achieve what we care about.


![Logo](https://www.indezine.com/products/powerpoint/cool/images/word-cloud-01.jpg)

    
## Project Objective:

To extract Latent themes or keywords from BBC News Article. Corpus contains 2225 Article under Five categories. Business, Entertainment, Politics, Sports and Technology.
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Natural Language Precessing:
In 2021, 2.5 quintillion bytes of data being created every day. In that almost 80% of data are in unstructured in the form of Image, Audio and Text. Many Business documents are unstructured such as E-mails, videos, photos, web pages and audio files.  As all we know machines works well on numerical values. The process converting human language to machine understandable language is known as Natural Language Processing.
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)


## RoadMap:

* 2225 csv's to Pandas Dataframe.
* Text Pre-processing.
    * Casefolding 
    * Removing Punctuation's
    * Removing Standalone Numerical
    * Remove Stopwords
    * Normalizing inflated words
         * Lemmatization
    * Parts of speech Tagging

* Document to vector
    * Count Vectorizer
    * TF-IDF
* Model Training
    * Latent Sementic Indexing
    * Latent Dirichlet Allocation
    * Non-Negative Matrix Factorization

* Hyperparametre Tuning
* Topics Visualization
    * t-SNE 
    * pyLDAvis
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

Clone the project

```bash
  git clone https://github.com/LALITH23SUNDARAM/st_app.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt 
```

Start the server

```bash
  streamlit run app.py
  

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
## Acknowledgements

 - [Towards Data Science](https://towardsdatascience.com/topic-modeling-quora-questions-with-lda-nmf-aff8dce5e1dd)
 - [NLP Stanford Edu](https://ai.stanford.edu/blog/nlp/)
 - [Negative Matrix Factorization](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization)
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## Credits:
< Lalith M > | Avid Learner | Data Scientist | Machine Learning Engineer | Deep Learning enthusiast
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lalith-m-0103b9ab/)
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
