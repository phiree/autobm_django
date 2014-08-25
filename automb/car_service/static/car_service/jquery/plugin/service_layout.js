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
$.fn.detail_layout = function(params)
{

    var options = $.extend(
    {
        service_list: test
    },
    params
);

/*functions*/

//已经添加的属性/值
var title_added=[],item_added=[]
for (i =0;i < options.service_list.length;i++)
{
 service_pk=options.service_list[i].pk;
for (j in options.service_list[i].fields)
{


    //跳过不需要解析的属性.
    if(j=='car'){continue;}
    if(j=='price'||j=='price_preorder'){ continue;}
    if(j=='service'){ continue; }

    item_property=options.service_list[i].fields[j]
   if (item_property!=null)
   {
   //属性名称: 如 洗车类型,品牌
     title=item_property[3][1]
     //属性值: 人工洗车/电脑洗车.
     value=item_property[2]
     //创建html元素,
     var dv_property;
     if (title_added.indexOf(title)==-1)
     {
        dv_property=$("<div id='dv_"+j+"' ></div>")
        dv_property.append("<span>"+title+"</span>");
        $(this).append(dv_property);
        title_added.push(title)
     }
     else
     {
        dv_property=$(this).find("#dv_"+j);
     }
     if (item_added.indexOf(value)==-1)
     {
        dv_property.append("<span onclick='item_selected(this)' class='item_value' id='"+item_property[0]+"'>"+value+"</span>");
        item_added.push(value)
     }
   }
}
}



};


selected_item_values={}
function item_selected(s)
{
  selected_title=$(s).parent()[0].id.replace('dv_','');
  alert(selected_title);
}

