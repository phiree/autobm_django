//屏蔽可忽略的js脚本错误
function killErr(){
	return true;
}
window.onerror=killErr;

//选项卡
var fodTime = 0;
function geto(o){ return (typeof o == "object")?o:document.getElementById(o);}
function swTabs(e){if(typeof e=="string"){e=geto(e);}var isAjax,sobject;var cls="on";var tmp=e.id.split("_");var sid=tmp[0];var snum=tmp[1];sobject=geto(sid+"_"+snum+"_Info");e.className=cls;if(!isAjax){swLabs(sobject,sid,snum)}tmp=sobject=isAjax=maxItemNum=null;}
function swLabs(sobject,sid,snum){var maxItemNum;var cls="";try{var i=1;maxItemNum=gp[sid][0];while(i<=maxItemNum){if(i!=snum){var tmp1,tmp2;tmp1=geto(sid+"_"+i);tmp2=geto(sid+"_"+i+"_Info");tmp1.className=cls;tmp2.style.display = "none";}i++}}catch(e){} sobject.style.display="block";}
function tagOver(a){clearTimeout(fodTime);fodTime=0;fodTime = setTimeout(function(){swTabs(a)},50);}
function tagOut(a){clearTimeout(fodTime);fodTime=0;}

var gp = [];
gp["AreaA"] = ["2"];
gp["AreaB"] = ["4"];

//end

//搜索
function serach_form_submit(){
    if(cksearch())
        $('#seach_form').submit();
}
function cls() {
    var val = document.getElementById("txtKey");
    if (val.value == val.defaultValue)
        val.value = "";
}
function res() {
    var val = document.getElementById("txtKey");
    if (val.value == "")
        val.value = val.defaultValue;
}
function cksearch() {
    var obj = document.getElementById("txtKey");
    if (obj.value == obj.defaultValue || obj.value == "") {
        alert("请输入要搜索的内容");
        return false;
    } else {
        return true;
    }
}

//end

//更换城市
function ddd(obj, sType) { 
var oDiv = document.getElementById(obj); 
if (sType == 'show') { oDiv.style.display = 'block';} 
if (sType == 'hide') { oDiv.style.display = 'none';} 

} 
//end

//弹出分类
function aaa(obj, sType) { 
var oDiv = document.getElementById(obj); 
if (sType == 'show') { oDiv.style.display = 'block';} 
if (sType == 'hide') { oDiv.style.display = 'none';} 

} 
//end