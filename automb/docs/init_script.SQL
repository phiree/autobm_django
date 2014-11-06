--- carinfo
INSERT INTO  car_service_carinfo VALUES(1,'本田',NULL,'brand',NULL);
INSERT INTO  car_service_carinfo VALUES(2,'飞渡',NULL,'series',1);
INSERT INTO  car_service_carinfo VALUES(3,'飞渡2014款','type','small',2);

-- areainfo
INSERT INTO  car_service_areainfo VALUES(1,'广州','519000',NULL);
-- service
    -- top service
INSERT INTO  car_service_servicetype VALUES(1,'汽车美容',NULL,'');
    -- child service
INSERT INTO  car_service_servicetype VALUES(2,'洗车',1,'');
INSERT INTO car_service_servicetype VALUES(3,'打蜡',1,'');
INSERT INTO car_service_servicetype VALUES(4,'封釉',1,'');
INSERT INTO car_service_servicetype VALUES(5,'镀膜',1,'');
INSERT INTO car_service_servicetype VALUES(6,'内饰清洗',1,'');
INSERT INTO car_service_servicetype VALUES(7,'空调清洗',1,'');
INSERT INTO car_service_servicetype VALUES(8,'真皮座椅保养',1,'');
INSERT INTO car_service_servicetype VALUES(9,'发动机舱清洗',1,'');
INSERT INTO car_service_servicetype VALUES(10,'前风挡镀膜',1,'');
-- serviceproperty

INSERT INTO  car_service_serviceproperty VALUES(1,'洗车方式',2);
INSERT INTO  car_service_servicepropertyvalue VALUES(1,1,'人工洗车',0,0);
INSERT INTO  car_service_servicepropertyvalue VALUES(2,1,'电脑洗车',0,0);

INSERT INTO  car_service_serviceproperty VALUES(2,'品牌',3);
INSERT INTO  car_service_servicepropertyvalue VALUES(3,2,'3M',0,0);
INSERT INTO  car_service_servicepropertyvalue VALUES(4,2,'美光',0,0);

-- 供应商
INSERT INTO  car_service_supplier VALUES(1,'佛山美丽天使汽车养护店','1','门店地址门店地址门店地址门店地址',12,12,NULL,'1342333333','08:00:00','18:00:00','门店简介门店简介门店简介门店简介',1);