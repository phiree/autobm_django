/*
tab切换插件:切换结果是将对应的元素提到第一个显示, 不隐藏其他元素
结构需求:
<div id='tab_container'>
    <ul>
        <li></li>
        <li></li>
        <li></li>
    </ul>
    <div>content1</div>
    <div>content2</div>
    <div>content3</div>
<div/>
使用方法:$('#tab_container').tab_switch({'highlight_css':'on'})
*/
$.fn.tab_switch=function(params){
    var options=$.extend(
        {
            highlight_css:'on'
        },
        paras
    );
    $(this).find('ul li').each(function(e){
        alert(e);
    });

}