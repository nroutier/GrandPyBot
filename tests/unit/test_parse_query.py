""" Module that defines the TestParseQuery class """

import pytest
from app.main.classes.Parse_query import ParseQuery


class TestParseQuery:
    """
    GIVEN a query
    WHEN the parse_query function is called woth the query as parameter
    THEN check the response is parsed correctly
    """
    question = "Salut GrandPy ! Est-ce que tu connais l'adresse "\
        "d'OpenClassrooms ?"
    query = ParseQuery(question)

    def test_parse_query(self):
        assert self.query.parse_query() == 'openclassrooms'
