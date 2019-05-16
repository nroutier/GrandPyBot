import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string

# query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
query = "Yo tu peux me trouver le 1 rue de la véga à paris"

class Parse_query:
    def __init__(self, query):
        self.query = query

    def parse_query(self):
        # Put query in lowercase and tokenize it keeping only words
        tokenizer = nltk.RegexpTokenizer(r'\w+')
        query = tokenizer.tokenize(self.query.lower())
        # print(query)
        # Retrieve french stopwords
        sw = nltk.corpus.stopwords.words('french')
        greetings = ['yo', 'hello', 'bonjour', 'salut', 'coucou', 'grandpy', 'stp', 'papi', 'papy']
        sw.extend(greetings)
        location_words = ["adresse", "endroit"]
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