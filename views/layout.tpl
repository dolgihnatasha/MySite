<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="../static/{{ stylesheet }}">
    <link rel="stylesheet" href="../static/header-footer.css">
</head>
<body>
    <header>
        <div class="menuContainer">
            <a class="menuItem" href="index"><div><p>Main</p></div></a>
            <a class="menuItem" href="gallery"><div><p>Gallery</p></div></a>
            <a class="menuItem" href="projects"><div><p>Projects</p></div></a>
        </div>
    </header>
    <main>
        {{ !base }}
    </main>
    <footer>
        <div class="links">
            <a target="_blank" href=""><img class="contactLink" alt="ufu link"
                src="https://sts.urfu.ru/adfs/portal/logo/logo.ru.png?id=C87B799C7B171E40C45B877734E33A187F073FA49E811309F93601B84A38E7CF"></a>
            <a target="_blank" href=""><img class="contactLink" alt="mm link"
                src="http://cs623830.vk.me/v623830655/5f663/1QOVEtPLi9Q.jpg"></a>
        </div>
        <div>
            <p>Посещений:{{visits['visits'}}</p>
            <p>Уникальных:{{len(visits['unique'])}}</p>
        </div>
        <div class="links">
            <a target="_blank" href="https://vk.com/natasha.glukhovtseva"><img class="contactLink" alt="vk link"
                src="static/pictures/vk.bmp"></a>
            <a target="_blank" href="https://github.com/dolgihnatasha"><img class="contactLink" alt="git link"
                src="static/pictures/git.bmp"></a>
            <a target="_blank" href="https://twitter.com/dolgih_natasha"><img class="contactLink" alt="twi link"
                src="static/pictures/twi.bmp"></a>
            <a target="_blank" href="mailto:n.e.dolgih@yandex.ru"><img class="contactLink" alt="mail link"
                src="static/pictures/mail.bmp"></a>
        </div>
    </footer>
</body>
</html>