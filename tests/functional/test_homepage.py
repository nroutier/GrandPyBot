""" Module that test the app routes """


def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert 'GrandPy Bot' in response.get_data().decode('utf-8')
    assert 'Un papi qui en sait long en '\
        'géographie !' in response.get_data().decode('utf-8')


def test_query_route(test_client):
    """
    GIVEN a Flask application
    WHEN the '/query/' page is requested (POST)
    THEN check the response is valid
    """
    query = {
        "query": "Salut GrandPy ! Est-ce que tu connais l'adresse "
        "d'OpenClassrooms ?"
        }

    response = test_client.post('/query/', data=query)
    assert response.status_code == 200
