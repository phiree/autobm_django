selected_item_values={}
var test = [{"model": "car_service.servicedetail", "pk": 1,
         "fields": {"foil_model_sides_back": null, "car": [], "main_light_suit": null, "brand": null,
                    "glass_damage_size": null, "sound_suit": null, "price": "12", "price_preorder": "1213",
                    "foil_model_front": null, "foil_type": null, "tire_repair_type": null, "body_damage_size": null,
                    "sound_proofing_type": null,
                    "wash_type": [4, "wash_type", "\u4eba\u5de5\u6d17\u8f66", ["service", "\u670d\u52a1"]],
                    "service": 1}},
        {"model": "car_service.servicedetail", "pk": 2,
         "fields": {"foil_model_sides_back": null, "car": [], "main_light_suit": null,
                    "brand": null, "glass_damage_size": null, "sound_suit": null,
                    "price": "123", "price_preorder": "12", "foil_model_front": null,
                    "foil_type": null, "tire_repair_type": null, "body_damage_size": null,
                    "sound_proofing_type": null,
                    "wash_type": [7, "wash_type", "\u7535\u8111\u6d17\u8f66",
                                  ["service", "\u670d\u52a1"]], "service": 1}}]

// 将该商家同一种服务的不同选项展示, 根据用户选择确定价格
//对应的服务id, 通过ajax预订.
// step1
//展示所有选项

var service_list_changed=[];//经过选择之后的服务列表
var selected_item={};//已经选择的值
/*functions*/
function value_click(e)
{
    service_list_changed=[]
    alert(e.data.id);
    sp_item=$(e.target);
    dv_parent=sp_item.parent('div')[0];
    //1 将该值加入selected
    title=dv_parent.id.replace('dv_','');
    value=e.data.id;
    item_selected[title]=value;


    //3 可以供选择的服务详情.
    for (key in item_selected)
    {
        k=get_value(item_selected[key],service_list)
        m=get_value(item_selected[key],service_list_changed)
        if(k>=0&&m<0)
        {
            service_list_changed.push(_service_list[k]);
        }
    }
    service_list_changed=service_list;
    detail_layout('');
}

function get_value(value,list)
{
    for (m =0;m < list.length;m++)
    {
        for (j in list[m].fields)
        {
            item_property=list[m].fields[j]
            if (item_property!=null)
            {
                if( item_property[0]==value)
                {
                     selected_item_values.title=item_property[3][1]
                //属性值: 人工洗车/电脑洗车.
                     selected_item_values.value=item_property[2]
                    return m;
                }
            }

        }
    }
    return -1;
}
function detail_layout(selected_id){

    $('#dv_lay').empty()
    var title_added=[],item_added=[]
    for (i =0;i < service_list.length;i++)
    {
        var service_pk=service_list[i].pk;
        selected_style='';
        //初始选择的值
        if(service_pk==selected_id)
        {
            selected_style="selected";
        }
        for (j in service_list[i].fields)
        {
            //跳过不需要解析的属性.
            if(j=='car'){continue;}
            if(j=='price'||j=='price_preorder'){ continue;}
            if(j=='service'){ continue; }

            item_property=service_list[i].fields[j]
            if (item_property!=null)
            {
                //如果-selected_id 不为空 那么 需要将默认属性添加进 item_selected

                //属性名称: 如 洗车类型,品牌
                title=item_property[3][1]
                //属性值: 人工洗车/电脑洗车.
                value=item_property[2]

                if(selected_id!='')
                {
                    if(service_pk==selected_id)
                    item_selected[title]=value;
                }
                //创建html元素,
                var dv_property;
                if (title_added.indexOf(title)==-1)
                {
                    dv_property=$("<div id='dv_"+j+"' ></div>")
                    dv_property.append("<span>"+title+"</span>");
                    $('#dv_lay').append(dv_property);
                    title_added.push(title)
                }
                else
                {
                    dv_property=$('#dv_lay').find("#dv_"+j);
                }
                var sp_value;
                if (item_added.indexOf(value)==-1)
                {
                    sp_value=$("<span  class='item_value "+selected_style+"' id='"+item_property[0]+"'>"+value+"</span>");
                    sp_value.on("click",{id:item_property[0]}, value_click)
                    dv_property.append(sp_value);
                    item_added.push(value)
                }
                else
                {
                    sp_value=$('#dv_lay').find("#"+item_property[0]);
                }
                //判断该值  1 是否可以选择 2 是否已经被选择
                debugger;
                k=get_value(item_property[0],service_list_changed);
                if(k<0)
                {
                    sp_value.css('color','gray');
                }
                else
                {
                    sp_value.css('color','black');
                }
                for(p in item_selected)
                {
                    if (p.value==item_property[0])
                    {
                        sp_value.css('color','red');
                    }
                }
            }
        }
    }
}



