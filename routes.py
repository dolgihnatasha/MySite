"""
Routes and views for the bottle application.
"""

from bottle import route, view, response, request
import os

myphoto = 'https://avatars0.githubusercontent.com/u/6077501?v=3&s=460'

def check_visit():
    try:
        cookie = int(request.get_cookie("visit"))
    except (NameError, TypeError):
        response.set_cookie("visit", str(True))


@route('/')
@route('/index')
@view('index')
def home():
    """Renders the home page."""

    with open('aboutme.txt') as f:
        info = f.read()
    return dict(
        title='About Me',
        stylesheet='index.css',
        scripts='',
        myPhoto=myphoto,
        aboutMe=info
    )

@route('/gallery')
@view('gallery')
def gallery():
    """Renders the contact page."""
    pics = [f for x in os.walk('./static/RV/small/') for f in x[2]]
    return dict(
        title='Gallery',
        stylesheet='gallery.css',
        scripts='<script>',
        pictures=pics
    )

@route('/projects')
@route('/index2')
@view('projects')
def projects():
    """Renders the project page."""
    return dict(
        title='Projects',
        stylesheet='index2.css',
    )
