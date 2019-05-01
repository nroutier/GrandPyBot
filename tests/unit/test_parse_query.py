import pytest
from app.main.parse_query import parse_query

def test_parse_query():
    query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    # query = "Salut GrandPy, Openclassrooms"
    query = parse_query(query)
    assert query == ['openclassrooms']