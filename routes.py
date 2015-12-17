"""
Routes and views for the bottle application.
"""

from bottle import route, view, response, request
import os

myphoto = 'https://avatars0.githubusercontent.com/u/6077501?v=3&s=460'

@route('/')
@route('/index')
@view('index')
def home():
    try:
        cookie = int(request.get_cookie("visit"))
    except NameError:
        response.set_cookie("visit", str(1), max_age=10)
    except TypeError:
        response.set_cookie("visit", str(1), max_age=10)
    else:
        print(cookie)
        response.set_cookie("visit", str(cookie + 1), max_age=10)
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
    try:
        cookie = int(request.get_cookie("visit"))
    except NameError:
        response.set_cookie("visit", str(1), max_age=10)
    except TypeError:
        response.set_cookie("visit", str(1), max_age=10)
    else:
        print(cookie)
        response.set_cookie("visit", str(cookie + 1), max_age=10)
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
    try:
        cookie = int(request.get_cookie("visit"))
    except NameError:
        response.set_cookie("visit", str(1), max_age=10)
    except TypeError:
        response.set_cookie("visit", str(1), max_age=10)
    else:
        print(cookie)
        response.set_cookie("visit", str(cookie + 1), max_age=10)

    return dict(
        title='Projects',
        stylesheet='index2.css',
    )
