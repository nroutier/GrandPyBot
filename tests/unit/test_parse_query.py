import pytest
from app.main.parse_query import parse_query

def test_parse_query():
    """
    GIVEN a query
    WHEN the parse_query function is called woth the query as parameter
    THEN check the response is parsed correctly
    """
    query = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    query = parse_query(query)
    assert query == 'openclassrooms'