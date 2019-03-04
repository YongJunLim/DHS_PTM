# DHS PTM Booking System

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)
![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)

* 2019 H2 Computing Project
* What a booking system for Dunman High School's parent-teacher meetings should be
* Designed & created by Lim Yong Jun & Chiang Yu Hsuan from 19Y6C33

## Getting Started

### Prerequisites

```
authlib
flask
google-api-python-client
google-auth
```

Specify environment variables in WSGI. It can be done in this format:
```
import os

os.environ['FN_AUTH_REDIRECT_URI'] = 'https://<BASE_URI>/google/auth'
os.environ['FN_BASE_URI'] = '<BASE_URI>'
os.environ['FN_CLIENT_ID'] = '<CLIENT_ID>'
os.environ['FN_CLIENT_SECRET'] = '<CLIENT_SECRET>'
os.environ['FN_FLASK_SECRET_KEY'] = '<SECRET_KEY>'
```

### Installing

On PythonAnywhere, ensure the corresponding Python version used is specified and '--user' appears before the module name when installing with pip

Example: When using Python 3.7
```
pip3.7 install --user google-auth
```

## Built With

* [Flask](http://flask.pocoo.org/) - Web framework used
* [Bulma](https://bulma.io/) - CSS framework used
* [Authlib](https://docs.authlib.org/en/latest/client/oauth2.html) - Getting an OAuth 2.0 access token
* [Google-Auth](https://google-auth.readthedocs.io/en/latest/) - Authentication with Google
* [Google API Python Client](https://github.com/googleapis/google-api-python-client) - Constructing a Resource object for interacting with [Google Sign-In API](https://developers.google.com/identity/protocols/googlescopes)

## Authors

* **Lim Yong Jun** - Flask & Frontend
* **Chiang Yu Hsuan** - Flask & SQLite

## Acknowledgments

* [Matt Button](https://www.mattbutton.com/2019/01/05/google-authentication-with-python-and-flask/) - Google authentication with Python and Flask
* [Cilan](https://stackoverflow.com/questions/21033368/javascript-onclick-event-html-table) - Select table cells with JS
* [Felix Kling](https://stackoverflow.com/questions/3400628/how-can-i-get-the-position-of-a-cell-in-a-table-using-javascript) - Get specific timeslot booked by finding table cell position
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - Template for README
* [MDN](https://developer.mozilla.org/en-US/docs/Web/API#Interfaces) - Find suitable APIs to get booking information from table
* [Gi Soong Chee](https://github.com/dhsgisc) - Computing teacher