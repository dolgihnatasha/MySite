"""
Routes and views for the bottle application.
"""

from bottle import route, view, response, request, error
import os
import json
import random
from datetime import datetime as dt
from datetime import timedelta

myphoto = 'https://avatars0.githubusercontent.com/u/6077501?v=3&s=460'


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
        data['unique'] = dict()
    if 'visit' not in data.keys():
        data['visit'] = 0
    if change:
        data['visit'] += 1
        ip = request.get('REMOTE_ADDR')
        if ip not in data['unique'].keys():
            data['unique'][ip] = [dt.ctime(dt.now())]
        else:
            data['unique'][ip].append(dt.ctime(dt.now()))
    # date fromm string to datetime: dt.strptime(time, "%a %b %d %X %Y")
    print(request.get('REMOTE_ADDR'), data)
    write_visits(data)
    return data


def check_visit():
    cookie = request.get_cookie("visit")
    print(cookie)
    if cookie:
        return add_visits(False)
    else:
        response.set_cookie("visit", str(1))
        return add_visits(True)



@route('/')
@route('/index')
@view('index')
def home():
    """Renders the home page."""
    v = check_visit()
    with open('aboutme.txt') as f:
        info = f.read()
    return dict(
        title='About Me',
        stylesheet='index.css',
        scripts='',
        myPhoto=myphoto,
        aboutMe=info,
        visits=v['visit'],
        unique=len(v['unique'])
    )

@route('/gallery')
@view('gallery')
def gallery():
    """Renders the contact page."""
    v = check_visit()
    pics = [f for x in os.walk('./static/RV/small/') for f in x[2]]
    return dict(
        title='Gallery',
        stylesheet='gallery.css',
        order=random.sample(range(0, 10), 10),
        pictures=pics,
        visits=v['visit'],
        unique=len(v['unique'])
    )

@route('/other')
@view('projects')
def projects():
    """Renders the project page."""
    v = check_visit()
    return dict(
        title='Other',
        stylesheet='index2.css',
        visits=v['visit'],
        unique=len(v['unique'])
    )

@route('/visits')
@view('visits')
def projects():
    """Renders the visits page."""
    v = check_visit()
    visitsTable = []
    for ip in v['unique']:
        print(ip)
        for t in v['unique'][ip]:
            time = dt.strptime(t, "%a %b %d %X %Y")
            time += timedelta(hours=5)
            t = dt.ctime(time)
            visitsTable.append((t, ip))
    visitsTable = sorted(visitsTable, key=lambda x:dt.strptime(x[0], "%a %b %d %X %Y"))
    return dict(
        title='Visits',
        stylesheet='visits.css',
        visits=v['visit'],
        unique=len(v['unique']),
        visitsTable=visitsTable
    )



@error(404)
@view('error')
def error404(err):
    """Renders the error page."""
    v = check_visit()
    return dict(
        title='Error',
        stylesheet='index2.css',
        visits=v['visit'],
        unique=len(v['unique'])
    )
