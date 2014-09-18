
function area_display(arealist)
{
    selected_aid=$.cookie('aid');
    if(selected_aid==null)
    {
     selected_aid=arealist[0].id;
    }
    for(i=0;i<arealist.length;i++)
    {
        if(arealist[i]==null){continue;}
        if(arealist[i].id=selected_aid)
        {
            $("#sp_sltid").text(arealist[i].name);
        }
        var li=$('<li><a href="#"><span aid="'+area[i].id+'">'+area[i].name+'</span></a></li>');
        li.on("click", function(e){
            aid=$(e.target).attr('aid');
            $.cookie('aid',aid);
            window.location.href=window.location.href;
        });
        $("#ul_area").append(li);
    }
}
