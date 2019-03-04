# https://stackoverflow.com/questions/21405274/this-app-would-like-to-have-offline-access-when-access-type-online
# https://myaccount.google.com/permissions
import functools
import os
import sqlite3
conn = sqlite3.connect('DHS_PTM.db')
c = conn.cursor()
from flask import Flask, render_template, make_response, session, redirect, request, url_for
from search import student_subjects
from display import display_DB
from manipulate import manipulate
from remove import remove
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

ACCESS_TOKEN_URI = "https://www.googleapis.com/oauth2/v4/token"
AUTHORIZATION_URL = "https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=consent"

AUTHORIZATION_SCOPE = "email"

AUTH_REDIRECT_URI = os.environ.get('FN_AUTH_REDIRECT_URI')
BASE_URI = os.environ.get('FN_BASE_URI')
CLIENT_ID = os.environ.get('FN_CLIENT_ID')
CLIENT_SECRET = os.environ.get('FN_CLIENT_SECRET')

AUTH_TOKEN_KEY = "auth_token"
AUTH_STATE_KEY = "auth_state"
USER_INFO_KEY = "user_info"

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = os.environ.get('FN_FLASK_SECRET_KEY')

@app.route('/')
def welcome():
    if is_logged_in():
        return redirect(url_for('index'))
    else:
        return render_template('welcome.html')

@app.route('/dashboard', methods = ['POST', 'GET'])
def index():
    if is_logged_in():
        user_info = get_user_info()
        email = user_info['email']
        name = user_info['family_name']
        inTeachers, inSubj = student_subjects(email)
        outTeachers = []
        outSubj = []
        CTs = inTeachers[::-1][:2]
        for i in range(len(inTeachers)):
            if inTeachers[i] in outTeachers:
                pass
            else:
                outTeachers.append(inTeachers[i])
                outSubj.append(inSubj[i])
        slots = []
        for i in range(len(outTeachers)):
            slots.append(display_DB(outTeachers[i]))
        if request.method == 'GET':
            return render_template('index.html', email = email, name = name, teachers = outTeachers, CTs = CTs, subjects = outSubj, slots = slots)

        elif request.method == 'POST':
            DB_in_slot = request.form['Bookings']
            DB_in_slot = manipulate(DB_in_slot) #2D Array
            remove(DB_in_slot, email, outTeachers)
            return redirect(url_for('index'))

    return redirect(url_for('login'))

def no_cache(view):
    @functools.wraps(view)
    def no_cache_impl(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        return response

    return functools.update_wrapper(no_cache_impl, view)

@app.route('/google/login')
@no_cache
def login():
    OAuth_session = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope=AUTHORIZATION_SCOPE, redirect_uri=AUTH_REDIRECT_URI)
    uri, state = OAuth_session.authorization_url(AUTHORIZATION_URL) # session.authorization_url(AUTHORIZATION_URL)
    session[AUTH_STATE_KEY] = state
    session.permanent = True
    return redirect(uri, code=302)


@app.route('/google/auth')
@no_cache
def google_auth_redirect():
    state = request.args.get('state', default=None, type=None)

    OAuth_session = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope=AUTHORIZATION_SCOPE, state=state, redirect_uri=AUTH_REDIRECT_URI)
    oauth2_tokens = OAuth_session.fetch_access_token(ACCESS_TOKEN_URI, authorization_response=request.url)
    session[AUTH_TOKEN_KEY] = oauth2_tokens

    return redirect(url_for('index'), code=302)

@app.route('/google/logout')
@no_cache
def logout():
    session.pop(AUTH_TOKEN_KEY, None)
    session.pop(AUTH_STATE_KEY, None)
    session.pop(USER_INFO_KEY, None)

    return redirect(BASE_URI, code=302)

def is_logged_in():
    return True if AUTH_TOKEN_KEY in session else False

def build_credentials():
    if not is_logged_in():
        raise Exception('User must be logged in')

    oauth2_tokens = session[AUTH_TOKEN_KEY]
    return google.oauth2.credentials.Credentials(
        oauth2_tokens['access_token'],
        refresh_token=oauth2_tokens['refresh_token'],
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        token_uri=ACCESS_TOKEN_URI)

def get_user_info():
    credentials = build_credentials()
    oauth2_client = googleapiclient.discovery.build('oauth2', 'v2', credentials=credentials)
    return oauth2_client.userinfo().get().execute()

@app.route('/about')
def about():
    if is_logged_in():
        user_info = get_user_info()
        email = user_info['email']
        return render_template('about.html', email = email)
    else:
        return render_template('about.html')

#Updating database is ok
#Cancelling is buggy