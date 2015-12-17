/**
 * Created by Natasha on 22.11.2015.
 */
var KEYCODE = {
    UP: 38,
    DOWN: 40,
    LEFT: 37,
    RIGHT:39,
    F1:112,
    ESC: 27
};
var close = document.getElementById('close');
var fullPicPath = 'static/RV/full/';
var loadingGIF = 'http://www.novalnet.de/sites/all/themes/novalnetag/images/ajax-loader.gif';

addEvents('change', 'checkPicture', openFullPicture);

addBackContent();

function addEvents(eventType, className, eventFunction) {
    var elements = document.getElementsByClassName(className);
    for (var i = 0; i < elements.length; i++) {
        elements[i].addEventListener(eventType, eventFunction)
    }
}

function addBackContent() {
    var picContainers = document.querySelectorAll('.picContainer');
    for (var i = 0; i < picContainers.length; i++) {
        //alert(picContainers);
        var whiteBack = document.createElement('div');
        whiteBack.classList.add('whiteback');
        var loading = document.createElement('img');
        loading.src = loadingGIF;
        whiteBack.appendChild(loading);
        var picCont = picContainers[i];
        var blackOut = picCont.lastElementChild;
        blackOut.appendChild(whiteBack);
    }
}


function openFullPicture(e, curInput) {
    if (e) {
        curInput = e.target;
    }
    if (!document.querySelector('#' + curInput.id + '~ .picFull .picture')){
        var img = document.querySelector('#' + curInput.id + ' ~ .smallPic .picture');
        var imgName = img.getAttribute('data-picname');
        var fullPic = newFullPicture(imgName);
        document.querySelector('#' + curInput.id + '~ .picFull').appendChild(fullPic);
    }
}

function newFullPicture(picName) {
    var picFull = document.createElement('img');
    picFull.classList.add('picture');
    picFull.src = fullPicPath + picName;
    return picFull;
}


function nextPic() {
    var current = getCheckedInput('pictures');
    if (current && current[1] !== 0) {
        var inputs = current[0];
        var index = current[1];
        if (index !== inputs.length - 1) {
            inputs[index + 1].checked = true;
            openFullPicture(null, inputs[index + 1]);
            if (index !== inputs.length - 2) {
                openFullPicture(null, inputs[index + 2])
            }
        }
    }
}

function prevPic() {
    var current = getCheckedInput('pictures');
    if (current && current[1] !== 0) {
        var inputs = current[0];
        var index = current[1];
        if (index > 1) {
            inputs[index - 1].checked = true;
            openFullPicture(null, inputs[index - 1]);
            if (index > 2) {
                openFullPicture(null, inputs[index - 2]);
            }
        }
    }
}

function getCheckedInput(inputName) {
    var inputs = document.getElementsByName(inputName);
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            return [inputs, i];
        }
    }
}

function closePic() {
    close.checked = true;
}

document.getElementsByTagName('html').item(0).onkeydown = function(e) {
    if (e.keyCode == KEYCODE.RIGHT){
        nextPic();
    }
    if (e.keyCode == KEYCODE.LEFT){
        prevPic();
    }
    if (e.keyCode == KEYCODE.F1){
        alert('Стрелка вправо - следующая картинка,\nстрелка влево - предыдущая,\nECS - закрыть картику')
    }
    if (e.keyCode == KEYCODE.ESC) {
        closePic();
    }
};
