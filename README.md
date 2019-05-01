# GrandPyBot
Python bot that show a location on google maps and tell a story retrieved from Media Wiki from an entered address or known place.

# Getting started

You have to set FLASK_APP=grandpybot.py and SECRET_KEY='secret-is-env-secret' in your environment variables (replacing 'secret-is-secret' by your own secret key and you can add a .env file with these entries, the .env file will be load by pipenv when launching the program).

You need to install Python 3.7 and pipenv to use the following commands in a terminal:

`pipenv install`

`pipenv run flask run`
