# GrandPyBot

GrandPyBot is a responsive web app that acts as a grand father to whcich the user is able to ask for the location of a known place or address.
GrandPy will answer the user with the formatted address of the place, a map with a marker on the place's location and a short summury about the street where the place is located.

!(https://github.com/nroutier/GrandPyBot/blob/master/example.png)

# Specifications

This responsive web app has been built with using [Python 3.7](https://docs.python.org/3.7/) and the Python microframework [Flask](http://flask.pocoo.org/) and a [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) approach.

It uses [pipenv](https://docs.pipenv.org/en/latest/) to create and manage the python virtual environment.

It uses AJAX for interaction beetween the index page and the web server.

[Bootstrap](https://getbootstrap.com/) is used to create the responsive interface.

[NLTK](http://www.nltk.org/) is used to help parsing the questions that the users may ask to GrandPy.

[Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/start) is used to find the location of the searched place.

[Google Maps Javascript API](https://developers.google.com/maps/documentation/javascript/tutorial) is used to display the map with a marker on the location of the searched place.

[Wikipedia python Api](https://pypi.org/project/wikipedia/) is used to get some information about the street where the searched place is located.

# Getting started

After cloning this repository in your local folder, 

To set up your virtual envirnment and install all the required modules, from the program folder in the terminal type :

`pip3 install pipenv`
`pipenv install`

Then you have to define the required environment variables, you can do so either manually or renaming the `_env` file to `.env` then adapting the values to yours.

You are now able to launch the web app on your local machine with the following command:

`pipenv run flask run`

## Production deployment

If you would like to deploy your app on a [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python), you will have to set up the envirnoment variables on the Heroku console, the Procfile is already set up to use a [gunicorn](https://gunicorn.org/) WSGI HTTP server.
