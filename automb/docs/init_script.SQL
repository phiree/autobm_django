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
    --top service
insert into  car_service_servicetype values(1,'汽车美容',null);
    -- child service
insert into  car_service_servicetype values(2,'洗车',1);
INSERT INTO car_service_servicetype VALUES(3,'打蜡',1,'');
INSERT INTO car_service_servicetype VALUES(4,'封釉',1,'');
INSERT INTO car_service_servicetype VALUES(5,'镀膜',1,'');
INSERT INTO car_service_servicetype VALUES(6,'内饰清洗',1,'');
INSERT INTO car_service_servicetype VALUES(7,'空调清洗',1,'');
INSERT INTO car_service_servicetype VALUES(8,'真皮座椅保养',1,'');
INSERT INTO car_service_servicetype VALUES(9,'发动机舱清洗',1,'');
INSERT INTO car_service_servicetype VALUES(10,'前风挡镀膜',1,'');
--serviceproperty

insert into  car_service_serviceproperty values(1,'洗车方式',2,'');
insert into  car_service_servicepropertyvalue values(1,1,'人工洗车');
insert into  car_service_servicepropertyvalue values(2,1,'电脑洗车');

insert into  car_service_serviceproperty values(2,'品牌',3);
insert into  car_service_servicepropertyvalue values(3,2,'3M',0,0);
insert into  car_service_servicepropertyvalue values(4,2,'美光',0,0);

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

