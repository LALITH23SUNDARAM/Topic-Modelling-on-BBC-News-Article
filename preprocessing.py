import nltk
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

def length(sub):
  ''''
  function returns number of words 
  '''
  # split the documents with defined delimiter
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  # count the words
  length_ = len(tokenizer.tokenize(sub))
  return length_

# function lowers the characters
def lowercase(strings_):
  return strings_.lower()

def remove_punctuations(sub):
  # punctuations list from nltk library
  default_punctuations = [punc for punc in string.punctuation]
  # create tokenizer instance with different delimiters
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  # list to store tokens
  non_stop_msg = []
  # tokens to final string of tokens
  final_str = ' '
  # loop through tokens
  for char in tokenizer.tokenize(sub):
    # conditionl statement 
    if char not in default_punctuations:
      non_stop_msg.append(char)
  return final_str.join(non_stop_msg)

nltk.download('stopwords')

def removing_stopwords(sub):
  '''
  functions takes string and return string without stopwords
  '''
  # returns list of strings
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  # to store tokens which not in stopwords
  msg = []
  # null string to retun final string
  final2       = ' '  
  # loop through list of tokens
  for elem in tokenizer.tokenize(sub):
    # condition to remove stopwords
    if elem.lower() not in stopwords.words('english'):
      msg.append(elem)
  return final2.join(msg)

def removing_numericals(doc):
  '''
  retunrs string that without having stand alone numerics.
  '''
  # returns list of strings
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  # stores non numeric tokens
  msg1 = []
  # list to strings
  final3       = ' '  
  # loop through list of tokens
  for token in tokenizer.tokenize(doc):
    # boolean condition
    if token.isdigit() == False:
      msg1.append(token)
  return final3.join(msg1)


nltk.download('wordnet')

def get_lemma2(sub):
  '''
  function returns root word from the inflated ones
  '''
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  msg2 = []
  final3       = ' '  
  for elem in tokenizer.tokenize(sub):
    msg2.append(WordNetLemmatizer().lemmatize(elem))
  return final3.join(msg2)

def remove_tokens(sub):
  '''
  fubction takes list of list tokens and returns list of tokens whose length greater or equals to 3
  '''
  # returns list of strings
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  # to store tokens
  msg2 = []
  # convert list of strings to single string
  final3       = ' '  
  # loop through list of tokens
  for elem in tokenizer.tokenize(sub):
    # conditional statement
    if len(elem) >= 3:
      msg2.append(elem)
  return final3.join(msg2)

# tokenizing strings
def tokenizer(doc):
  tokenizer = RegexpTokenizer("\w+|\$[\d\.]+|\S+|\,'+|\'+|\-")
  tokenized_doc = tokenizer.tokenize(doc)
  return tokenized_doc



