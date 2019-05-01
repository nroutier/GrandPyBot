import nltk
from nltk.tokenize import word_tokenize
import string
import requests

query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
# query = "Yo tu peux me trouver le 1 rue de la véga à paris"

def parse_query(query):
    # Put query in lowercase and tokenize it keeping only words
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    query = tokenizer.tokenize(query.lower())
    print(query)
    # Retrieve french stopwords
    fr_sw = requests.get('https://raw.githubusercontent.com/6/stopwords-json/master/dist/fr.json')
    sw = fr_sw.json()
    greetings = ['yo', 'hello', 'bonjour', 'salut', 'coucou', 'grandpy']
    sw.extend(greetings)
    # print(sw)
    # remove stopwords from query
    query = [word for word in query if word not in sw]
    return query

parse_query(query)