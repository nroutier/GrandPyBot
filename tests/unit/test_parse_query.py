import pytest
from app.main.classes.Parse_query import Parse_query

def test_parse_query():
    """
    GIVEN a query
    WHEN the parse_query function is called woth the query as parameter
    THEN check the response is parsed correctly
    """
    question = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    query = Parse_query(question)
    assert query.parse_query() == 'openclassrooms'