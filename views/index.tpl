% rebase('layout.tpl', title=title, stylesheet=stylesheet)

<section class="main">
    <h2>Обо мне</h2>
    <div id="myPhoto"><img src="{{ myPhoto }}"
                           alt="моя фотка"></div>
    <div id="myInfo">
        <p>
            {{ aboutMe }}
        </p>
    </div>
</section>