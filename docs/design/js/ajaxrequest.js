function CreateXMLHttp() {
    if (window.XMLHttpRequest) {
        return new XMLHttpRequest();
    } else if (window.ActiveXObject) {
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
    throw new Error("XMLHttp object could be created.");
}


function SendRequest(url, type, data, func, isxml, isasync) {
    var xhr = CreateXMLHttp();
    type = type.toUpperCase();
    if (type != "POST") type = "GET";
    if (!data) data = null;
    if (!isasync && GetOject() == "Firefox" && (GetBete().split(".")[0] < 4)) { isasync = true; }

    xhr.open(type ? "POST" : "GET", url, isasync ? true : false);

    if (type) {
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    }
    if (func) {
        xhr.onreadystatechange = function () {
            if ((xhr.readyState == 4) && (xhr.status == 200)) {
                func(isxml && xhr.responseXML ? xhr.responseXML : xhr.responseText)
            }
        }
    }

    xhr.send(data)
}

function GetOject() {
    if (navigator.userAgent.indexOf("MSIE") > 0) {
        return "MSIE";       //IE浏览器
    }
    if (isFirefox = navigator.userAgent.indexOf("Firefox") > 0) {
        return "Firefox";     //Firefox浏览器
    }
    if (isSafari = navigator.userAgent.indexOf("Safari") > 0) {
        return "Safari";      //Safan浏览器
    }
    if (isCamino = navigator.userAgent.indexOf("Camino") > 0) {
        return "Camino";   //Camino浏览器
    }
    if (isMozilla = navigator.userAgent.indexOf("Gecko/") > 0) {
        return "Gecko";    //Gecko浏览器
    }
}

function GetBete() {
    var Sys = {};
    var ua = navigator.userAgent.toLowerCase();
    var s;
    (s = ua.match(/msie ([\d.]+)/)) ? Sys.ie = s[1] :
    (s = ua.match(/firefox\/([\d.]+)/)) ? Sys.firefox = s[1] :
    (s = ua.match(/chrome\/([\d.]+)/)) ? Sys.chrome = s[1] :
    (s = ua.match(/opera.([\d.]+)/)) ? Sys.opera = s[1] :
    (s = ua.match(/version\/([\d.]+).*safari/)) ? Sys.safari = s[1] : 0;
    if (Sys.ie) {
        if (Sys.ie != 7.0) {
            return Sys.ie;
        }
    }
    else if (Sys.firefox) {
        return Sys.firefox;
    }
    else if (Sys.chrome) {
        return Sys.chrome;
    }
    else if (Sys.opera) {
        return Sys.opera;
    }
    else if (Sys.safari) {
        return Sys.safari;
    }
    else {
        return 0;
    }
}