% rebase('layout.tpl', title=title, stylesheet=stylesheet, visits=visits, unique=unique)

<input type="radio" name="makeTitle" class="resetTitle" id="reset" checked>
<div class="titlePicture grid_12">
    <label class="resetTitle" for="reset">Сбросить</label>
</div>

<div class="gallery container_12">
    <input type="radio" name="pictures" class="closeImg" id="close" checked>
    %i = 0
    %for numb in order:
        %pic = pictures[numb]
        %i += 1
        <div class="picContainer grid_3">
            <input type="radio" name="pictures" class="checkPicture" id="pic{{ i }}">

            <input type="radio" name="makeTitle" class="makeTitle" id="start{{ i }}">

            <label class="smallPic" for="pic{{ i }}">
                <img alt="picture {{ pic }}" class="picture" src="/static/RV/small/{{ pic }}" data-picname="{{ pic }}">
            </label>

            <div class="picFull">
                <div class="whiteback">
                    <label for="close" class="cross">
                        <img alt="close" src="https://cdn2.iconfinder.com/data/icons/flat-ui-icons-24-px/24/cross-24-512.png">
                    </label>
                    <label for="start{{ i }}" class="">Сделать стартовой</label>
                    <img alt="loading" class="loading" src="http://tobago.it/fragments/loading.gif">
                </div>
            </div>
        </div>
    %end
</div>
<script type="text/javascript" src="/static/gallery.js"></script>