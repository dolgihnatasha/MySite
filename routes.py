"""
Routes and views for the bottle application.
"""

from bottle import route, view, response, request
import os
import json

myphoto = 'https://avatars0.githubusercontent.com/u/6077501?v=3&s=460'
visit = 0

database = open('data.json')

def check_visit():
    try:
        cookie = request.get_cookie("visit")
        data = json.load(database)
        data['visit'] += 1
        json.dump(data, database)
    except (NameError, TypeError):
        response.set_cookie("visit", str(True))
        data = dict()
        data['visit'] = 1
        json.dump(data, database)



@route('/')
@route('/index')
@view('index')
def home():
    """Renders the home page."""
    check_visit()
    with open('aboutme.txt') as f:
        info = f.read()
    return dict(
        title='About Me',
        stylesheet='index.css',
        scripts='',
        myPhoto=myphoto,
        aboutMe=info,
        visits=visit
    )

@route('/gallery')
@view('gallery')
def gallery():
    """Renders the contact page."""
    check_visit()
    pics = [f for x in os.walk('./static/RV/small/') for f in x[2]]
    return dict(
        title='Gallery',
        stylesheet='gallery.css',
        scripts='<script>',
        pictures=pics,
        visits=visit
    )

@route('/projects')
@route('/index2')
@view('projects')
def projects():
    """Renders the project page."""
    check_visit()
    return dict(
        title='Projects',
        stylesheet='index2.css',
        visits=visit
    )
