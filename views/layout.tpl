<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="/static/{{ stylesheet }}">
    <link rel="stylesheet" href="/static/header-footer.css">
    <link rel="stylesheet" href="/static/css/960_12_col.css">
</head>
<body>
    <div class="wrap">
        <header>
            <div class="menuContainer container_12">
                <a class="menuItem grid_4" href="index"><div><p>Main</p></div></a>
                <a class="menuItem grid_4" href="gallery"><div><p>Gallery</p></div></a>
                <a class="menuItem grid_4" href="projects"><div><p>Projects</p></div></a>
            </div>
        </header>
        <div class="main container_12">
            {{ !base }}
        </div>
    </div>
    <footer>
        <div class="container_12">
            <div class="links grid_4">
                <a target="_blank" href=""><img class="contactLink" alt="ufu link"
                                                src="https://sts.urfu.ru/adfs/portal/logo/logo.ru.png?id=C87B799C7B171E40C45B877734E33A187F073FA49E811309F93601B84A38E7CF"></a>
                <a target="_blank" href=""><img class="contactLink" alt="mm link" src="http://cs623830.vk.me/v623830655/5f663/1QOVEtPLi9Q.jpg"></a>
            </div>
            <div class="visits grid_4">
                <div class="grid_2">Посещений:{{visits}}</div>
                <div class="grid_2">Уникальных:{{unique}}</div>
            </div>
            <div class="mylinks grid_4">
                <a target="_blank" href="https://vk.com/natasha.glukhovtseva"><img class="contactLink" alt="vk link"
                                                                                   src="/static/pictures/vk.png"></a>
                <a target="_blank" href="https://github.com/dolgihnatasha"><img class="contactLink" alt="git link"
                                                                                src="/static/pictures/git.png"></a>
                <a target="_blank" href="https://twitter.com/dolgih_natasha"><img class="contactLink" alt="twi link"
                                                                                  src="/static/pictures/twi.png"></a>
                <a target="_blank" href="mailto:n.e.dolgih@yandex.ru"><img class="contactLink" alt="mail link"
                                                                           src="/static/pictures/mail.png"></a>
            </div>
        </div>
    </footer>
</body>
</html>