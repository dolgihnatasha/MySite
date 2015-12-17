from bottle import route, run, template


TEMPLATE = 'main_template'
myphoto = 'https://avatars0.githubusercontent.com/u/6077501?v=3&s=460'


@route('/')
def main():
    with open('aboutme.txt') as f:
        info = f.read()
    main_content = template('index', myPhoto=myphoto, aboutMe=info)
    return template(TEMPLATE, stylesheet='index.css', content=main_content)

print()
run()
