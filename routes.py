"""
Routes and views for the bottle application.
"""

from bottle import route, view, response, request
import os
import json

myphoto = 'https://avatars0.githubusercontent.com/u/6077501?v=3&s=460'
visit = 0


def write_visits(data):
    with open('data.json', 'w') as d:
        json.dump(data, d)


def read_visits():
    with open('data.json', 'r') as d:
        data = json.load(d)
    return data


def add_visits(change):
    data = read_visits()
    if 'unique' not in data.keys():
        data['unique'] = list()
    if change:
        data['visit'] += 1
        if request.get('REMOTE_ADDR') not in data['unique']:
            data['unique'].append(request.get('REMOTE_ADDR'))
    print(request.get('REMOTE_ADDR'), data)
    write_visits(data)
    return data


def get_visits():
    data = read_visits()
    return data


def check_visit():
    try:
        cookie = request.get_cookie("count")
        return add_visits(True)
    except NameError:
        response.set_cookie("count", str(True))
        return add_visits(True)



@route('/')
@route('/index')
@view('index')
def home():
    """Renders the home page."""
    v = len(check_visit()['unique'])
    with open('aboutme.txt') as f:
        info = f.read()
    return dict(
        title='About Me',
        stylesheet='index.css',
        scripts='',
        myPhoto=myphoto,
        aboutMe=info,
        visits=v
    )

@route('/gallery')
@view('gallery')
def gallery():
    """Renders the contact page."""
    v = len(check_visit()['unique'])
    pics = [f for x in os.walk('./static/RV/small/') for f in x[2]]
    return dict(
        title='Gallery',
        stylesheet='gallery.css',
        scripts='',
        pictures=pics,
        visits=v
    )

@route('/projects')
@route('/index2')
@view('projects')
def projects():
    """Renders the project page."""
    v = len(check_visit()['unique'])
    return dict(
        title='Projects',
        stylesheet='index2.css',
        visits=v
    )
