% rebase('layout.tpl', title=title, stylesheet=stylesheet, visits=visits, unique=unique)

<section class="gallery container_12">
    <input type="radio" name="pictures" class="closeImg" id="close" checked>
    %i = 0
    %for pic in pictures:
        %i += 1
        <div class="picContainer grid_3">
            <input type="radio" name="pictures" class="checkPicture" id="pic{{ i }}">
            <div class="picFull">
                <div class="whiteback">
                    <label for="close" class="cross">
                        <img src="https://cdn2.iconfinder.com/data/icons/flat-ui-icons-24-px/24/cross-24-512.png">
                    </label>
                    <img class="loading"
                         src="http://www.novalnet.de/sites/all/themes/novalnetag/images/ajax-loader.gif">
                </div>
            </div>
            <label class="smallPic" for="pic{{ i }}">
                <img class="picture" src="/static/RV/small/{{ pic }}" data-picname="{{ pic }}">
            </label>

        </div>
    %end
</section>
<script type="text/javascript" src="/static/gallery.js"></script>