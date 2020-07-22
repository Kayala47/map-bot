import string
import nltk
import re

# nltk.download()

stopword = nltk.corpus.stopwords.words('english')

def remove_stopwords(tokenized_list):
    text = [word for word in tokenized_list if word not in stopword]
    return text

def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens

def process_paragraph(paragraph):
    # print(paragraph)
    processed = ""

    tokenized = tokenize(paragraph)

    unstopped = remove_stopwords(tokenized)

    processed = " ".join(unstopped)

    return processed


#this is where I can experiment
paragraph = "Draw a tiny red road in the bottom right corner. Draw a tiny orange forest in the top left corner. Draw a small green forest in the center. Draw a tiny pink lake in the top left corner."

processed_text = process_paragraph(paragraph)

# print(processed_text)