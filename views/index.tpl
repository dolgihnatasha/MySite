% rebase('layout.tpl', title=title, stylesheet=stylesheet, visits=visits, unique=unique)

<section class="main container_12">
    <h1 class="grid_12">Обо мне</h1>
    <div class="grid_4 myPhoto"><img src="{{ myPhoto }}"
                           alt="моя фотка"></div>
    <div class="grid_6 myInfo">
        <p>
            {{ aboutMe }}
        </p>
    </div>
</section>