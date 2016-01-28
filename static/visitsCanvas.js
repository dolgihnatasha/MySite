if (!Object.keys) {
    Object.keys = function (obj) {
        var keys = [];
        for (var i in obj) {
            if (obj.hasOwnProperty(i)) {
                keys.push(i);
            }
        }
        return keys;
    };
}

function isIE(version, comparison) {
    var cc = 'IE',
        b = document.createElement('B'),
        docElem = document.documentElement,
        isIE;
    if (version) {
        cc += ' ' + version;
        if (comparison) {
            cc = comparison + ' ' + cc;
        }
    }
    b.innerHTML = '<!--[if ' + cc + ']><b id="iecctest"></b><![endif]-->';
    docElem.appendChild(b);
    isIE = !!document.getElementById('iecctest');
    docElem.removeChild(b);
    return isIE;
}


function draw(data) {
    if (!isIE(8) && checkInput(data)) {
        var canvas = document.getElementById("visitsCanvas");
        var context = canvas.getContext('2d');
        context.height = "60px";
        context.width = "300px";
        context.fillStyle = "#fff5e8";
        context.fillRect(0, 0, canvas.width, canvas.height);
        context.strokeRect(0, 0, canvas.width, canvas.height);
        context.textAlign = "left";
        context.textBaseline = "top";
        context.fillStyle = "#000";
        context.strokeStyle = "#555";
        context.lineWidth = 1;
        context.font = "bold 16px monospace";
        context.fillText("Total: " + data.visits, 5, 10);
        context.textAlign = "right";
        context.fillText("Today: " + data.today, canvas.width - 5, 10);
        context.textAlign = "center";
        context.fillText("Unique: " + data.unique, 150, 10);
        context.fillText("Last: " + data.last, 150, 30);
    }
}

function checkInput(data) {
    return (data instanceof Object && Object.keys(data).length === 4 &&
        hasOwnProperties(data, ['visits', 'unique', 'last', 'today']) &&
        typeof data.visits == 'number' && typeof data.unique == 'number' &&
        typeof data.today == 'number' && checkDate(data.last)
    )
}

function hasOwnProperties(obj, props) {
    for (var i = 0; i < props.length; i++) {
        if (!obj.hasOwnProperty(props[i])) {
            return false;
        }
    }
    return true;
}

function checkDate(date) {
    return !isNaN(Date.parse(date));
}