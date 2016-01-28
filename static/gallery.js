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
addEvents('change', 'makeTitle', setBackgroundPicture);



function addEvents(eventType, className, eventFunction) {
    console.log('add events');
    console.log('');
    var elements = document.querySelectorAll("." + className);
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].addEventListener) {
        elements[i].addEventListener(eventType, eventFunction)
        } else {
            elements[i].attachEvent("on" + eventType, eventFunction);
        }
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

function setBackgroundPicture(e, curInput) {
    console.log('set background picture');
    if (e) {
        curInput = e.target;
    }
    var img = document.querySelector('#' + curInput.id + '~ .picFull .whiteback .picture');
    var imgName = img.getAttribute('data-picname');
    //document.cookie = "background=" + imgName + '; path=/;';

    //if (!document.querySelector('.titlePicture .picture')) {
    //    document.querySelector('.titlePicture').appendChild(img.cloneNode(false));
    //} else {
    //    document.querySelector('.titlePicture').replaceChild(img.cloneNode(false), document.querySelector('.titlePicture .picture'));
    //}
}


function openFullPicture(e, curInput) {
    console.log('open full picture');
    if (e) {
        curInput = e.target;
    }
    if (!document.querySelector('#' + curInput.id + '~ .picFull .whiteback .picture')){
        var img = document.querySelector('#' + curInput.id + ' ~ .smallPic .picture');
        var imgName = img.getAttribute('data-picname');
        var fullPic = newFullPicture(imgName);
        document.querySelector('#' + curInput.id + '~ .picFull .whiteback').appendChild(fullPic);
    }
}

function newFullPicture(picName) {
    console.log('get full picture');
    var picFull = document.createElement('img');
    picFull.classList.add('picture');
    picFull.src = fullPicPath + picName;
    picFull.setAttribute('data-picname', picName);
    return picFull;
}


function nextPic() {
    console.log('next pic');
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
    console.log('prev pic');
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
    console.log('checked inputs');
    var inputs = document.getElementsByName(inputName);
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            return [inputs, i];
        }
    }
}

function closePic() {
    console.log('close');
    close.checked = true;
}

document.getElementsByTagName('html').item(0).onkeydown = function(event) {
    console.log('key pressed');
    if (event.keyCode == KEYCODE.RIGHT){
        nextPic();
    }
    if (event.keyCode == KEYCODE.LEFT){
        prevPic();
    }
    if (event.keyCode == KEYCODE.F1){
        alert('Стрелка вправо - следующая картинка,\nстрелка влево - предыдущая,\nECS - закрыть картику')
    }
    if (event.keyCode == KEYCODE.ESC) {
        closePic();
    }
    if (event.preventDefault) {
        event.preventDefault()
    } else {
        event.returnValue = false;
    }
};
