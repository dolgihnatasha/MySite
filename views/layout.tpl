<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="/static/{{ stylesheet }}">
    <link rel="stylesheet" href="/static/header-footer.css">
    <link rel="stylesheet" href="/static/css/960_12_col.css">
    <script type="text/javascript" src="/static/visitsCanvas.js"></script>
    % if len({{background}}) > 0:
    <style>
        body {
            background: url(/static/RV/small/{{background}});
        }
    </style>
    %end
</head>
<body onload="draw({'visits':{{visits}}, 'unique':{{unique}}, 'today':{{today}}, 'last':'{{last}}'})">
    <div class="wrap">
        <div class="header">
            <div class="menuContainer container_12">
                <a class="menuItem grid_4" href="index"><div><p>Main</p></div></a>
                <a class="menuItem grid_4" href="gallery"><div><p>Gallery</p></div></a>
                <a class="menuItem grid_4" href="other">
                    <div><p>Other</p></div>
                </a>
            </div>
        </div>
        <div class="main container_12">
            {{ !base }}
        </div>
    </div>
    <footer>
        <div class="container_12">
            <div class="links grid_4">

                <a class="contactLink" target="_blank" href="http://urfu.ru/ru/">
                    <img class="contactLink" alt="ufu link" src="https://sts.urfu.ru/adfs/portal/logo/logo.ru.png">
                </a>
                <a class="contactLink" target="_blank" href="http://imkn.urfu.ru/">
                    <img class="contactLink" alt="mm link" src="http://cs623830.vk.me/v623830655/5f663/1QOVEtPLi9Q.jpg">
                </a>
            </div>
            <div class="grid_4">
                <a href="visits">
                    <canvas height="60px" width="300px" id="visitsCanvas">
                        По&shy;се&shy;ще&shy;ний:{{visits}}<br>Уни&shy;каль&shy;ных:{{unique}}
                    </canvas>
                </a>
            </div>
            <!--<div class="grid_4 ">-->
            <!--<div class="visits grid_2">По&shy;се&shy;ще&shy;ний:{{visits}}<br>Уни&shy;каль&shy;ных:{{unique}}-->
            <!--</div>-->
            <!--<div class="visits grid_2"><a href="visits">Ис&shy;то&shy;рия</a></div>-->
            <!--</div>-->

            <div class="mylink grid_4">

                <a class="contactLink" target="_blank" href="https://vk.com/natasha.glukhovtseva">
                    <img class="contactLink" alt="vk link" src="/static/pictures/vk.png">
                </a>
                <a class="contactLink" target="_blank" href="https://github.com/dolgihnatasha">
                    <img class="contactLink" alt="git link" src="/static/pictures/git.png">
                </a>
                <a class="contactLink" target="_blank" href="https://twitter.com/dolgih_natasha">
                    <img class="contactLink" alt="twi link" src="/static/pictures/twi.png">
                </a>
                <a class="contactLink" target="_blank" href="mailto:n.e.dolgih@yandex.ru">
                    <img class="contactLink" alt="mail link" src="/static/pictures/mail.png">
                </a>

            </div>
        </div>
    </footer>
</body>
</html>