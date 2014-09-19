    drop table car_service_carinfo;
    drop table car_service_areainfo;
    drop table car_service_servicetype;
    drop table car_service_serviceproperty;
    drop table car_service_servicepropertyvalue;
    drop table car_service_service2;
    drop table car_service_servicevalue;
    drop table car_service_carinfo;



--car
insert into  car_service_carinfo values(1,'本田',null,'brand',null);
insert into  car_service_carinfo values(2,'飞渡',null,'series',1);
insert into  car_service_carinfo values(3,'飞渡2014款','type','small',2);

--areainfo
insert into  car_service_areainfo values(1,'广州','519000',null);
--service
insert into  car_service_servicetype values(1,'汽车美容',null);
insert into  car_service_servicetype values(2,'洗车',1);
insert into car_service_servicetype values(3,'打蜡',1);
insert into car_service_servicetype values(4,'封釉',1);
insert into car_service_servicetype values(5,'镀膜',1);
insert into car_service_servicetype values(6,'内饰清洗',1);
insert into car_service_servicetype values(7,'空调清洗',1);
insert into car_service_servicetype values(8,'真皮座椅保养',1);
insert into car_service_servicetype values(9,'发动机舱清洗',1);
insert into car_service_servicetype values(10,'前风挡镀膜',1);
insert into  car_service_serviceproperty values(1,'洗车方式',2);
insert into  car_service_servicepropertyvalue values(1,1,'人工洗车');
insert into  car_service_servicepropertyvalue values(2,1,'电脑洗车');

insert into  car_service_serviceproperty values(2,'品牌',3);
insert into  car_service_servicepropertyvalue values(1,2,'3M');
insert into  car_service_servicepropertyvalue values(2,2,'美光');

insert into  car_service_serviceproperty values(3,'型号',3);
insert into  car_service_servicepropertyvalue values(3,3,'3M');
insert into  car_service_servicepropertyvalue values(4,3,'美光');



--供应商
insert into  car_service_supplier values(1,'佛山美丽天使汽车养护店','1','门店地址门店地址门店地址门店地址',12,12,null,'1342333333','08:00:00','18:00:00','门店简介门店简介门店简介门店简介',1);
/***********TREE****************/
--车型
insert into car_service_tree(id,tree_type,car_type,name,parent_id)
                      values(1, 'car',     '',      '本田', null);
insert into car_service_tree(id,tree_type,car_type,name,parent_id)
                      values(2, 'car',     '',      '飞渡', 1);
insert into car_service_tree(id,tree_type,car_type,name,parent_id)
                      values(3, 'car',     'small',      '飞渡2013款手动', 2);
--服务类型

insert into car_service_tree(id,tree_type,name,parent_id)
                    values(4,'service','汽车美容',null);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(5,'service','洗车',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(6,'service','打蜡',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(7,'service','封釉',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(8,'service','镀膜',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(9,'service','内饰清洗',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(10,'service','空调清洗',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(11,'service','真皮座椅保养',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(12,'service','发动机舱清洗',4);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(13,'service','前风挡镀膜',4);


insert into car_service_tree(id,tree_type,name,parent_id)
                    values(14,'service','汽车装饰',null);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(15,'service','玻璃贴膜',14);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(16,'service','底盘装甲',14);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(17,'service','座椅包真皮',14);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(18,'service','汽车隔音',14);

insert into car_service_tree(id,tree_type,name,parent_id)
                    values(19,'service','汽车维修',null);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(20,'service','四轮定位',19);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(21,'service','四轮动平衡',19);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(22,'service','油路清洗',19);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(23,'service','节气门清洗',19);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(24,'service','补胎',19);

insert into car_service_tree(id,tree_type,name,parent_id)
                    values(25,'service','汽车改装',null);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(26,'service','音响改装',25);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(27,'service','车身改色贴膜',25);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(28,'service','DVD导航一体机',25);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(29,'service','疝气大灯改装',25);

--区域
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(30,'area','广州',null);
--品牌
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(31,'brand','3M',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(32,'brand','金刚',15);
--洗车方式
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(33,'wash_type','人工洗车',5);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(34,'wash_type','电脑洗车',5);
--隔音方式
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(33,'sound_proofing_type','包含隔音',26);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(34,'sound_proofing_type','不包含隔音',26);
--贴膜类型
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(35,'foil_type','前挡',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(36,'foil_type','侧后挡',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(37,'foil_type','整车',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(38,'foil_type','自选',15);

--前挡类型
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(35,'foil_model_front','风光系列 璀璨风光前挡',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(36,'foil_model_front','风光系列 田园风光前挡',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(37,'foil_model_front','晶锐 70前挡',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(38,'foil_model_front','恒色系列 恒色风光',15);

--侧后挡类型
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(39,'foil_model_sides_back','恒色系列 黑衣骑士',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(40,'foil_model_sides_back','恒色系列 魅力沙龙',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(41,'foil_model_sides_back','经典系列 蓝色魔力',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(42,'foil_model_sides_back','经典系列 魔幻大师',15);

--侧后挡类型
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(39,'glass_damage_size','10CM',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(40,'glass_damage_size','恒色系列 魅力沙龙',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(41,'glass_damage_size','经典系列 蓝色魔力',15);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(42,'glass_damage_size','经典系列 魔幻大师',15);


insert into car_service_tree(id,tree_type,name,parent_id)
                    values(27,'service','车身改色贴膜',25);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(28,'service','DVD导航一体机',25);
insert into car_service_tree(id,tree_type,name,parent_id)
                    values(29,'service','疝气大灯改装',25);
