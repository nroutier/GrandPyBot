""" Module that defines the ParseQuery class """

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


class ParseQuery:
    """ Class used to parse a query and keep the useful words """

    def __init__(self, query):
        """ Function that instantiate an object ParseQuery """
        self.query = query

    def parse_query(self):
        """ Function that parse, format and keep only the useful words """
        # Put query in lowercase and tokenize it keeping only words
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        query = tokenizer.tokenize(self.query.lower())
        # Retrieve french stopwords
        sw = nltk.corpus.stopwords.words('french')
        greetings = ['yo', 'hello', 'hey', 'bonjour', 'salut', 'coucou', 'grandpy', 'stp', 'papi', 'papy']
        sw.extend(greetings)
        location_words = ["adresse", "endroit", "quoi"]
        sw.extend(location_words)
        # remove stopwords from query
        query = [word for word in query if word not in sw]
        # Stemm query words and keep only those that doesn't match stem_verbs list
        stemmer = SnowballStemmer("french")
        stem_verbs = ["con", "trouv", "situ", "montr", "peux", "sais"]
        stem_process = []
        stem_process += [word for word in query if not stemmer.stem(word) in stem_verbs]
        query = " ".join(stem_process)
        return query
