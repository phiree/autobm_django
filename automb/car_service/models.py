from django.db.models import Model, CharField,ForeignKey,TimeField,DateTimeField,\
                            FilePathField,DecimalField,FloatField,ImageField,ManyToManyField,\
                    BooleanField,OneToOneField, Max, Min

# Create your models here
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from model_utils.managers import InheritanceManager
from django.db import connection
from django.utils import timezone as DateTime
class  AreaInfo(Model):
    name=CharField(max_length=200)
    code=CharField(max_length=20)
    parent=ForeignKey("AreaInfo", null=True,blank=True)
    def __str__(self):
        return self.name
    #depth=Inter

class ServiceType(Model):#汽车美容, 洗车....
    name=CharField(max_length=200)
    parent=ForeignKey("ServiceType", null=True,blank=True)
    description=CharField(max_length=2000)
    def __str__(self):
        return self.name
    def get_supplier_list(self):
        supplier_list=self.service2_set.all().values('supplier').distinct()
        min_price=self.service2_set.all().aggregate(Min('price'))
        return (supplier_list,min_price)

class ServiceProperty(Model):
    name=CharField(max_length=200)
    servicetype=ForeignKey(ServiceType)
    def __str__(self):
        return self.servicetype.name +'_'+ self.name




class ServicePropertyValue(Model):
    objects = InheritanceManager()
    serviceproperty=ForeignKey(ServiceProperty,verbose_name='服务属性')
    value=CharField(max_length=200)
    is_brand=BooleanField()
    is_foil_type=BooleanField()
    def __str__(self):
        return self.value


#和品牌有关联的值 需要选择品牌
class ServicePropertyValue_Brand(ServicePropertyValue):
    brand=ForeignKey(ServicePropertyValue, related_name='spv_brand', limit_choices_to={'is_brand':True})

#和贴膜有关联的值  需要选择品牌 和 贴膜类型.
class ServicePropertyValue_Brand_FoilType(ServicePropertyValue_Brand):
    foiltype=ForeignKey(ServicePropertyValue,verbose_name='贴膜类型', related_name='spv_b_foil',limit_choices_to={'is_foil_type':True})



class CarInfo(Model):
    name=CharField(max_length=100)
    car_type_choice=(('small','小型'),('midium','中型'),('large','大型'))
    info_type_choice=(('brand','品牌'),('series','车系'),('type','型号'))
    car_type=CharField(choices=car_type_choice,max_length=10, null=True,blank=True,)
    info_type=CharField(choices=info_type_choice,max_length=10, null=True,blank=True,)
    #todo add limit_choice_to
    parent=ForeignKey('CarInfo',null=True,blank=True)
    def __str__(self):
        return self.name

class Service2(Model):
    supplier=ForeignKey('Supplier')
    title=CharField(max_length=100)#服务title,
    description=CharField(max_length=8000) #服务详情
    servicetype=ForeignKey(ServiceType)
    price=DecimalField(decimal_places=0, max_digits=5,null=True)
    price_market=DecimalField(decimal_places=0, max_digits=5,null=True)
    disabled=BooleanField(default=False)


    @property
    def minus_price(self):
        return -1*self.price

    def __str__(self):
        s=self.servicetype.name+'_'
        for v in self.servicevalue_set.all():
            s+=v.servicepropertyvalue.serviceproperty.name+':'+v.servicepropertyvalue.value+'|'
        s+=str(self.price)
        return s




class ServiceValue(Model):
    service=ForeignKey(Service2)
    #todo 限制该值, limit_choices_to= servicepropert.servicetype=service.servicetype
    servicepropertyvalue=ForeignKey(ServicePropertyValue)
    def __str__(self):
        return str(self.servicepropertyvalue)

class Tree(Model):# 区域, 车型(品牌,系列,型号),字典, 服务 都是tree类型.

    tree_type_choice= (('area', '区域'),                 ('car', '车型'),                 ('service', '服务'),
                       ('brand', '品牌'),                ('wash_type', '洗车方式'),       ('sound_proofing_type', '隔音方式'),
                       ('foil_type', '贴膜类型'),        ('foil_model_front', '前挡型号'),('foil_model_sides_back', '侧后挡型号'),
                       ('glass_damage_size', '玻璃损坏尺寸'),('tire_repair_type', '补胎类型'),('body_damage_size', '车身损伤尺寸'),
                       ('sound_suit', '音响套装'),       ('main_light_suit', '大灯套装'),('model_common','型号'),
                    )
    car_type_choice=(('small','小型'),('midium','中型'),('large','大型'))
    tree_type=CharField(choices=tree_type_choice,max_length=100, blank=False)
    car_type=CharField(choices=car_type_choice,max_length=10, null=True, blank=True)
    name=CharField(max_length=200)
    parent=ForeignKey("Tree", null=True,blank=True)
    supplier=ForeignKey('Supplier',null=True,blank=True)
    class Meta:
        unique_together = (('tree_type', 'name'),)
    def __str__(self):
        s=self.name
        if self.tree_type==self.tree_type_choice[3][0] and self.parent!=None:
            s= self.parent.name+'_'+s
        return s
    def get_type(self,index):
        return self.tree_type_choice[index][0]

    @property
    def child_types(self):
        return Tree.objects.filter(parent=self)

    @classmethod
    def __get_service_leaves__(self):
        return Tree.objects.filter(tree_type=Tree.tree_type_choice[2][0] , parent__isnull=False).values('id')
    def natural_key(self):
        return [self.pk,self.tree_type, self.name,Tree.tree_type_choice[[a[0] for a in Tree.tree_type_choice].index(self.tree_type)]]
#车店
class Supplier(Model):
    name=CharField(max_length=100,verbose_name='名称')
    area=ForeignKey(AreaInfo,verbose_name='区域')
    address=CharField(max_length=100,verbose_name='地址')
    coordinate_x=FloatField(verbose_name='经度')
    coordinate_y=FloatField(verbose_name='维度')
    photo= ImageField(blank=True,null=True,upload_to='photos/suppliers')
    phone=CharField(max_length=100)
    time_open=TimeField()
    time_close=TimeField()
    description=CharField(max_length=1000)
    owner=ForeignKey(User)

    def __str__(self):
        return self.area.name+'-'+self.name+'-'+self.owner.username
    #商家提供的服务类型.和 每种类型的最低价格

    #@property
    def get_type_info(self):
        l=self.service2_set.all().values('servicetype','servicetype__name').distinct()
        min_price=self.service2_set.all().aggregate(Min('price'))
        sql="select a.servicetype_id,b.name,min(a.price)  \
            from car_service_service2 a inner join car_service_servicetype b on b.id=a.servicetype_id \
            where a.supplier_id=%s \
            group by a.servicetype_id,b.name"
        cursor=connection.cursor()
        cursor.execute(sql,[self.id])
        rows=cursor.fetchall()
        return rows
    #def get_min_price



#用户选择的
class Service(Model):

    supplier=ForeignKey(Supplier)               #美容店
    #supplier=ForeignKey(Supplier,related_name='supplier')-->导致反向查询supplier_list=Supplier.objects.filter(service__id__in=[3]) 失败
    service_type=ForeignKey(Tree,related_name='service_type',limit_choices_to=dict(id__in=Tree.__get_service_leaves__))          #服务类型
    description=CharField(max_length=4000)
    def __str__(self):
        return self.supplier.name+'|'+self.service_type.name+'|'+self.description+'|'

class Car(Model):
    pass
class ServiceDetail(Model):

    service=ForeignKey(Service)
    car=ManyToManyField(Tree,related_name='car' ,limit_choices_to={'tree_type':Tree.tree_type_choice[1][0]})                             #车型
    brand=ForeignKey(Tree,related_name='brand',null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[3][0]})
    wash_type=ForeignKey(Tree, null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[4][0]})
    sound_proofing_type=ForeignKey(Tree,related_name='sound_proofing_type', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[5][0]})
    foil_type=ForeignKey(Tree,related_name='foil_type', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[6][0]})
    foil_model_front=ForeignKey(Tree, related_name='foil_model_front', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[7][0]})
    foil_model_sides_back=ForeignKey(Tree, related_name='foil_model_sides_back', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[8][0]})
    glass_damage_size=ForeignKey(Tree, related_name='glass_damage_size', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[9][0]})
    tire_repair_type=ForeignKey(Tree, related_name='tire_repair_type', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[10][0]})
    body_damage_size=ForeignKey(Tree, related_name='body_damage_size', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[11][0]})
    sound_suit=ForeignKey(Tree, related_name='sound_suit', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[12][0]})  # 音响改装套餐
    main_light_suit=ForeignKey(Tree, related_name='main_light_suit', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[13][0]})  # 大灯改装套餐
    model_common=ForeignKey(Tree, related_name='model_common', null=True,blank=True,limit_choices_to={'tree_type':Tree.tree_type_choice[14][0]})  # 大灯改装套餐
    price=DecimalField(decimal_places=0, max_digits=5)
    price_preorder=DecimalField(decimal_places=0, max_digits=5)
    def __str__(self):
        r=str(self.service) if self.service else ''
        r+=self.foil_type.name+'|' if self.foil_type is not None  else ''
        r+=  self.foil_model_front.name +'|'if self.foil_model_front is not  None   else ''
        r+=  self.foil_model_sides_back.name +'|'if self.foil_model_sides_back is  not None   else ''
        r+=   self.wash_type.name +'|'if self.wash_type  is not None  else ''
        r+=  self.glass_damage_size.name +'|'if self.glass_damage_size  is  not None  else ''
        r+= self.tire_repair_type.name +'|'if self.tire_repair_type  is  not None  else ''
        r+=self.body_damage_size.name+'|' if self.body_damage_size  is  not None  else ''
        r+=self.sound_proofing_type.name +'|'if self.sound_proofing_type  is not  None  else ''
        r+=self.sound_suit.name  +'|' if self.sound_suit  is not  None  else ''
        r+=self.main_light_suit.name +'|'if self.main_light_suit is not  None   else ''
        r+=self.brand.name +'|'if self.brand is not  None   else ''
        return r




    #玻璃贴膜: 品牌,型号,贴膜类型
    #洗车: 人工洗车,电脑洗车
    #打蜡 封釉,镀膜,内饰,空调清洗,真皮座椅保养,发动机舱清洗,前风挡镀膜,:品牌,型号


class Bill(Model):
    service=ForeignKey(Service2)
    order_date=DateTimeField()
    user=ForeignKey(User)
    service_snapshot=CharField(max_length=2000)
    sms_content=CharField(max_length=1000)
    final_price=DecimalField(decimal_places=0, max_digits=5)
    status_choice=(('ordered','已预订'),('paid','已付款'),('complete','已完成'),)
    status=CharField(choices=status_choice,max_length=10)

    created_time=DateTimeField(default=DateTime.now())
    complete_time=DateTimeField(null=True)
    #给用户发送短信
    def send_sms(self):
        pass




#返利  和  推荐 优惠.
class promote_register(Model):
    pass

class UserProfiler(Model):
    user =OneToOneField(User, unique=True)
    phone =CharField(max_length=140,verbose_name= '电话号码')
    gender = CharField(max_length=140,verbose_name='性别')
    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username


