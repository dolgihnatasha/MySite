"""
Routes and views for the bottle application.
"""

from bottle import route, view, response, request, error
import os
import json
import random
from datetime import datetime as dt
from datetime import timedelta
from collections import Counter
from copy import deepcopy


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
        browser_agent = request.get('HTTP_USER_AGENT')
        data['visit'] += 1
        ip = request.get('REMOTE_ADDR')
        if ip not in data['unique'].keys():
            data['unique'][ip] = list()
        data['unique'][ip].append([dt.ctime(dt.now() + timedelta(hours=5)), browser_agent])
        # else:
        #     data['unique'][ip][dt.ctime(dt.now() + timedelta(hours=5))].append(browser_agent)
    # date fromm string to datetime: dt.strptime(time, "%a %b %d %X %Y")
    # print(request.get('REMOTE_ADDR'), data)
    write_visits(data)
    return data


def check_visit():
    cookie = request.get_cookie("visit")
    if cookie:
        return add_visits(False)
    else:
        response.set_cookie("visit", str(1))
        return add_visits(True)


def get_visits_info():

    v = check_visit()
    print(v)
    ip = request.get('REMOTE_ADDR')
    last = v['unique'][ip][-1][0]
    today = 0
    todayDate = dt.now().date()
    for i in v['unique']:
        for visit in v['unique'][i]:
            d = dt.strptime(visit[0], "%a %b %d %X %Y")
            if d.date() == todayDate:
                today += 1
    return dict(
        today=today,
        visits=v['visit'],
        unique=len(v['unique']),
        last=last
    )

def join_dict(a, b):
    result = deepcopy(a)
    for x, y in b.items():
        result[x] = y
    # print(result)
    return result





@route('/')
@route('/index')
@view('index')
def home():
    """Renders the home page."""
    v = get_visits_info()
    with open('aboutme.txt') as f:
        info = f.read()
    result = dict(
        title='About Me',
        stylesheet='index.css',
        scripts='',
        myPhoto=myphoto,
        aboutMe=info
    )
    return join_dict(v, result)

@route('/gallery')
@view('gallery')
def gallery():
    """Renders the contact page."""
    v = get_visits_info()
    pics = [f for x in os.walk('./static/RV/small/') for f in x[2]]
    result = dict(
        title='Gallery',
        stylesheet='gallery.css',
        order=random.sample(range(0, 10), 10),
        pictures=pics
    )
    return join_dict(v, result)

@route('/other')
@view('projects')
def projects():
    """Renders the project page."""
    v = get_visits_info()
    result = dict(
        title='Other',
        stylesheet='index2.css'
    )
    return join_dict(v, result)

@route('/visits')
@view('visits')
def projects():
    """Renders the visits page."""
    v = check_visit()
    #print(v)
    visitsTable = []
    for ip in v['unique']:
        #print(ip)
        for t in v['unique'][ip]:
            # time = dt.strptime(t, "%a %b %d %X %Y")

            # t = dt.ctime(time)
            visitsTable.append((t, ip))
    visitsTable = sorted(visitsTable, key=lambda x:dt.strptime(x[0], "%a %b %d %X %Y"))
    v = get_visits_info()
    result = dict(
        title='Visits',
        stylesheet='visits.css',
        visitsTable=visitsTable
    )
    return join_dict(v, result)



@error(404)
@view('error')
def error404(err):
    """Renders the error page."""
    v = get_visits_info()
    result = dict(
        title='Error',
        stylesheet='index2.css'
    )
    return join_dict(v, result)

