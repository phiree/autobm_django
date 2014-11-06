var sctimer;
var tempwidth = 0, tempheight = 0, temppate = 1, speedrate = 24, interval_id = 0;
var isautosrc = false;
var isopen = false;
var newiframe = document.createElement("iframe");
var newdiv = document.createElement("div");
var sdiv = document.createElement("div");
var contentdiv = document.createElement("div");
var docbody = (document.documentElement || document.body);
var ie6 = ! -[1,] && !window.XMLHttpRequest;
var Globle_width = 0, //宽度
Globle_height = 0, //高度
Globle_src = '', //对象元素
Globle_title = '', //标题
Globle_Str = '', //
Globle_width_p = 0,
Globle_height_div = 0;

document.writeln('<style type="text/css">body{ margin:0px !ipmortant; padding:0px  !ipmortant;}#blackbg{position:fixed;_position:absolute;}');
document.writeln('#contentouter{zoom:1; position:fixed!important;position:absolute;left:50%;top:15%;_top:expression((document.documentElement.scrollTop || document.body.scrollTop) + Math.round(15 * (document.documentElement.offsetHeight || document.body.clientHeight) / 100));}</style>');

//hassrc 是否是url还是div
//hashead 是否有头
//hastitle是否有Title
//hasclose是否有关闭按钮

function Covert(ptitle, pwidth, pheight, psrc, hassrc, hashead, hasclose, hasback, hcolor) {

    var issrc = true, ishead = true, istitle = true, isclose = true, isback = true, bgcolor = "#ff6600";

    if (typeof (hassrc) != "undefined" && !hassrc) {
        issrc = false;
    }
    if (typeof (hashead) != "undefined" && !hashead) {
        ishead = false;
    }
    if (typeof (hasclose) != "undefined" && !hasclose) {
        isclose = false;
    }
    if (typeof (hasback) != "undefined" && !hasback) {
        isback = false;
    }
    if (typeof (hcolor) != "undefined" && hcolor != "") {
        bgcolor = hcolor;
    }

    docbody.style.overflow = "hidden";

    isopen = true;
    window.scoll = false;
    isautosrc = issrc; //初始化是否是链接
    AutoBoxInitData(); //初始化遮罩层

    Globle_title = ptitle;
    Globle_width = pwidth;
    Globle_height = pheight;
    Globle_src = psrc;
    Globle_width_p = pwidth - 20;
    Globle_height_div = pheight + 30;
    Globle_Str = "";

    Globle_Str += '<div style=" position:relative">';
    Globle_Str += '<div ' + (isback ? 'id="mboxback"' : "") + ' style="display:none;width:' + Globle_width + 'px; height:38px;padding:8px;background:#000;filter:alpha(opacity=40); -moz-opacity:0.4; -kHTML-opacity: 0.4; opacity: 0.4; position:absolute; top:0; left:0; z-index:1"></div>';
    Globle_Str += '<div  id="mboxitem"  style=" width:' + Globle_width + 'px;position:absolute;border:solid 1px ' + bgcolor + ';background-color:#fff; top:8px; left:8px;z-index:1000;min-height:10px; height:auto !important; height:auto; overflow:hidden !important; overflow: visible;">';
    Globle_Str += '<div ' + (ishead ? 'id="mboxhead"' : "") + ' style=" display:none; width:' + Globle_width_p + 'px; height:30px;background:' + bgcolor + '; line-height:32px; padding:0 10px; border-bottom:none; font-size:14px; font-weight:bold; color:#fff;margin:0;">';
    Globle_Str += (isclose ? '<div style="float:right;position:absolute;top:8px; right:10px; width:15px; height:15px;background:url(http://x.autoimg.cn/y/site/img/bg.png) -66px -285px no-repeat;cursor:pointer;" onclick="AutoBoxClose();"></div>' : '');
    Globle_Str += '<div style="float:left;width:' + (Globle_width - 40) + 'px;">' + Globle_title + '</div></div>';
    Globle_Str += (issrc ? '<iframe id="BContainer"  scrolling="no" src="' + Globle_src + '" frameborder="0" height="' + Globle_height + '"  width="' + Globle_width + '"></iframe>' : '<div id="BContainer" style="width:' + Globle_width + 'px;">') + '</div>';
    Globle_Str += '</div></div>';

    AutoBoxEffect();
}


function AutoBoxResize() {
    try {
        var bcontainer = document.getElementById("BContainer");
        var bboxback = document.getElementById("mboxback");
        var bboxhead = document.getElementById("mboxhead");
        var bboxitem = document.getElementById("mboxitem");

        contentdiv.style.width = Globle_width + "px";
        contentdiv.style.height = Globle_height + "px";
        contentdiv.style.margin = "0px 0px 0px -" + Globle_width / 2 + "px";

        bcontainer.width = Globle_width;
        bcontainer.height = Globle_height;

        if (bboxhead != null && bboxhead != undefined) {
            bboxhead.style.display = "inline-block";
        }

        if (bboxback != null && bboxback != undefined) {
            bboxback.style.height = ((isautosrc) ? (Globle_height_div + 2) : bboxitem.offsetHeight) + "px";
            bboxback.style.display = "block";
        }

    } catch (e1) { }
}

function AutoBoxInitData() {
    newdiv.id = "blackbg";
    newdiv.style.display = "none";
    newdiv.style.zIndex = '99990';
    newdiv.style.backgroundColor = "#000000";
    newdiv.style.filter = "alpha(opacity=30)";
    newdiv.style.opacity = 0.3;
    newdiv.style.display = "block";
    newdiv.style.top = "0px";
    newdiv.style.left = "0px";
    newdiv.style.width = "100%";
    newdiv.style.height = AutoBoxGetHeight() + "px";
    contentdiv.id = "contentouter";
    contentdiv.style.display = "none";
    contentdiv.style.zIndex = '99991';
    contentdiv.style.width = '10px';
    contentdiv.style.height = '10px';
    contentdiv.style.margin = '-5px 0px 0px -5px';
    contentdiv.style.backgroundColor = "";
    document.body.appendChild(newdiv);
    document.body.appendChild(contentdiv);
    if (ie6) {
        newiframe.id = "iframeForIe6";
        newiframe.style.zIndex = '99989';
        newiframe.style.position = 'absolute';
        newiframe.style.display = 'block';
        newiframe.style.filter = "alpha(opacity=0)";
        newiframe.style.top = "0px";
        newiframe.style.left = "0px";
        newiframe.style.width = "100%";
        newiframe.style.height = AutoBoxGetHeight() + "px";
        document.body.appendChild(newiframe);
    }
}

function AutoBoxScrool() {
    tempwidth = Globle_width;
    tempheight = Globle_height;
    contentdiv.innerHTML = Globle_Str;
    contentdiv.style.width = tempwidth + "px";
    contentdiv.style.height = tempheight + "px";
    contentdiv.style.margin = "0px 0px 0px -" + tempwidth / 2 + "px";
    contentdiv.style.display = "block";

    var bcontainer = document.getElementById("BContainer");
    bcontainer.src = Globle_src;
    contentdiv.style.top = ResetHeight(bcontainer.offsetHeight);
    AutoBoxResize();
}



function AutoBoxMoveInto() {
    
    tempwidth = Globle_width;
    tempheight = Globle_height;
    contentdiv.innerHTML = Globle_Str;
    contentdiv.style.width = tempwidth + "px";
    contentdiv.style.height = tempheight + "px";
    contentdiv.style.margin = "0px 0px 0px -" + tempwidth / 2 + "px";
    contentdiv.style.display = "block";

    var bcontainer = document.getElementById("BContainer");
    var g_src = document.getElementById(Globle_src);
    g_src.style.display = "block";
    g_src.style.position = "absolute";
    bcontainer.appendChild(g_src);
    g_src.style.position = "relative";
    contentdiv.style.top = ResetHeight(bcontainer.offsetHeight);

    AutoBoxResize();
}

function AutoBoxMonveOut() {
    var g_src = document.getElementById(Globle_src);
    if (g_src != undefined) {
        g_src.style.display = "none";
        g_src.style.position = "absolute";
        document.body.appendChild(g_src);
        g_src.style.position = "relative";
    }
}

function AutoBoxClose() {
    isopen = false;
    if (!isautosrc) {
        AutoBoxMonveOut();
    }
    contentdiv.style.width = '10px';
    contentdiv.style.height = '10px';
    contentdiv.innerHTML = "";
    Globle_width = 0,
        Globle_height = 0,
        Globle_src = '',
        Globle_title = '',
        Globle_Str = '';
    tempwidth = 0,
        tempheight = 0,
        temppate = 1,
        contentdiv.style.display = "none";
    newdiv.style.display = "none";
    if(ie6){
    newiframe.style.display = "none";
}
    docbody.style.overflow = "auto";
}

function AutoBoxEffect() {
    if (isautosrc) {
        AutoBoxScrool();
    }
    else {
        AutoBoxMoveInto();
    }
}

function AutoBoxGetCopy() {
    var bro = navigator.userAgent.toLowerCase();
    if (/msie/.test(bro)) return bro.match(/msie ([\d.]*);/)[1]
}

function AutoBoxGetHeight() {
    var a = document.body.scrollHeight;
    var b = window.screen.height;
    return a > b ? a : b;
}

function AutoBoxAutoBoxSetHeight(input) {
    if (document.all) {
        if (AutoBoxGetCopy() < 7.0) return input + 3;
    }
    return input;
}

function ResetHeight(iheight) {
    if (AutoBoxGetCopy() < 7.0) {
        var scrolltop = (document.documentElement.offsetHeight || document.body.clientHeight) - iheight;
        return (document.documentElement.scrollTop || document.body.scrollTop) + scrolltop / 2;
    }
    else {
        if (iheight < 100) { return "43%"; }
        else if (iheight < 200) { return "33%"; }
        else if (iheight < 300) { return "23%"; }
        else if (iheight < 400) { return "18%"; }
        else if (iheight < 500) { return "8%"; }
        else if (iheight < 600) { return "2%"; }
        else { return "1%"; }
    }
}
