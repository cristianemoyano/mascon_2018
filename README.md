# mascon_2018
Creando tu primer chatbot con Dialogflow

# chatbot
[![Build Status](https://travis-ci.org/cristianemoyano/mascon_2018.svg?branch=master)](https://travis-ci.org/cristianemoyano/mascon_2018)

[![Coverage Status](https://coveralls.io/repos/github/cristianemoyano/mascon_2018/badge.svg?branch=master)](https://coveralls.io/github/cristianemoyano/mascon_2018?branch=master)

App that communicates with the apiV2 of a bot in [DialogFlow](https://dialogflow.com/)


## Environment

> we recommend
```sh
$ cd ..
$ virtualenv env
$ source env/bin/activate
```

> set environment
```python
(env) $ export DEBUG=bool
(env) $ export EB_ACCESS_TOKEN=secret
(env) $ export FB_MESSENGER_ACCESS_TOKEN=secret
(env) $ export OPENWEATHERMAP_KEY=secret
```
or create a file: .env in /chatbot


## Running Locally

```sh
$ https://github.com/cristianemoyano/mascon_2018.git # or clone your own fork
$ pip install -r requirements.txt
$ python server.py
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Testing

#### Doc
[Pytest Doc](https://docs.pytest.org/en/latest/)

#### Run suite
```
$ python test_suite.py test
```

#### Run specific test cases
```
$ pytest tests/<folder>/test_xxxx.py::TestClass
```

#### Debugging
```
import ipdb;ipdb.set_trace()
```
turn off capture output:
```
$ pytest -s test_case_01.py
```

## Heroku

#### deploying to Heroku in a new app

Make sure you have [Heroku CLI](https://cli.heroku.com/) installed.

```
$ heroku create <name>
$ git push heroku master
$ heroku open
```

##### View heroku logs
`heroku logs`

##### deploy a new version
You must have the correct credentials
```sh
$ git push heroku master
```

##### heroku app
[Heroku app](https://weather-webhook-bot-app.herokuapp.com/)


## New git release
[Git Basics - Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
```sh
$ gco master
$ git pull origin master
$ git tag -a v1.4 -m "my version 1.4"
$ git push origin v1.4
```

## Makefile

For new releases:
```sh
$ make new_release:
```

To deploy on Heroku:
```sh
$ make deploy
```

Run all test:
```sh
$ make test_suite
```

Run app:
```
$ make run
```
