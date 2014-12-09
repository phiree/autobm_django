from django.db.models import Model, CharField,ForeignKey,TimeField,DateTimeField,\
                            FilePathField,DecimalField,FloatField,ImageField,ManyToManyField,\
                    BooleanField,OneToOneField, Max, Min,IntegerField

# Create your models here
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from model_utils.managers import InheritanceManager
from django.db import connection
from django.utils import timezone as DateTime


class AreaInfo(Model):
    name=CharField(max_length=200)
    code=CharField(max_length=20)
    parent=ForeignKey("AreaInfo", null=True,blank=True)
    def __str__(self):
        return self.name
    #depth=Inter
    class Meta:
        verbose_name_plural=verbose_name='区域'


class ServiceType(Model):#汽车美容, 洗车....
    name=CharField(max_length=200,verbose_name='名称')
    parent=ForeignKey("ServiceType", null=True,blank=True,verbose_name='父类型')
    description=CharField(max_length=2000,verbose_name='描述')
    def __str__(self):
        return self.name
    def get_supplier_list(self):
        supplier_list=self.service2_set.all().values('supplier').distinct()
        min_price=self.service2_set.all().aggregate(Min('price'))
        return (supplier_list,min_price)
    class  Meta:
        verbose_name_plural=verbose_name='服务类型'


class ServiceProperty(Model):
    name=CharField(max_length=200,verbose_name='属性名称',help_text='例如,"洗车方式","品牌","贴膜类型"')
    servicetype=ForeignKey(ServiceType,verbose_name='所属类型')
    def __str__(self):
        return self.servicetype.name +'_'+ self.name
    class Meta:
        verbose_name_plural=verbose_name='服务属性'


class ServicePropertyValue(Model):
    objects = InheritanceManager()
    serviceproperty=ForeignKey(ServiceProperty,verbose_name='服务属性')
    value=CharField(max_length=200,verbose_name='选项值',help_text='服务属性的可选值.比如 对于品牌这个服务属性,可选值是 3M,等.')
    is_brand=BooleanField(verbose_name='是品牌' ,help_text='品牌值 需要做特殊处理')
    is_foil_type=BooleanField('是贴膜类型',help_text='贴膜类型值 需要做单独处理')
    def __str__(self):
        return self.value
    class Meta:
        verbose_name_plural=verbose_name='服务属性选项'


#和品牌有关联的值 需要选择品牌
class ServicePropertyValue_Brand(ServicePropertyValue):
    brand=ForeignKey(ServicePropertyValue, related_name='spv_brand', limit_choices_to={'is_brand':True},verbose_name='品牌')
    class Meta:
        verbose_name_plural=verbose_name='品牌值'

#和贴膜有关联的值  需要选择品牌 和 贴膜类型.
class ServicePropertyValue_Brand_FoilType(ServicePropertyValue_Brand):
    foiltype=ForeignKey(ServicePropertyValue,verbose_name='贴膜类型', related_name='spv_b_foil',limit_choices_to={'is_foil_type':True})
    class Meta:
       verbose_name_plural=verbose_name='贴膜类型值'


class CarInfo(Model):
    name=CharField(max_length=100, verbose_name='名称')
    car_type_choice=(('small','小型'),('midium','中型'),('large','大型'))
    info_type_choice=(('brand','品牌'),('series','车系'),('type','型号'))
    car_type=CharField(choices=car_type_choice,max_length=10, null=True,blank=True,verbose_name='体积类型')
    info_type=CharField(choices=info_type_choice,max_length=10, null=True,blank=True,verbose_name='')
    #todo add limit_choice_to
    parent=ForeignKey('CarInfo',null=True,blank=True,verbose_name='父类型')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=verbose_name='车辆信息'


class Service2(Model):
    supplier=ForeignKey('Supplier',verbose_name='服务提供商')
    title=CharField(max_length=100,verbose_name='标题')#服务title,
    description=CharField(max_length=8000,verbose_name='描述') #服务详情
    servicetype=ForeignKey(ServiceType,verbose_name='服务类型')
    price=DecimalField(decimal_places=0, max_digits=5,null=True,verbose_name='价格')
    price_market=DecimalField(decimal_places=0, max_digits=5,null=True,verbose_name='市场价格')
    disabled=BooleanField(default=False,verbose_name='停用')
    class Meta:
        verbose_name_plural=verbose_name='服务详情'

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
    service=ForeignKey(Service2,verbose_name='所属服务')
    #todo 限制该值, limit_choices_to= servicepropert.servicetype=service.servicetype
    servicepropertyvalue=ForeignKey(ServicePropertyValue,verbose_name='所选值')
    def __str__(self):
        return str(self.servicepropertyvalue)
    class Meta:
        verbose_name_plural=verbose_name='服务定义的值'


class Supplier(Model):
    name=CharField(max_length=100,verbose_name='名称')
    area=ForeignKey(AreaInfo,verbose_name='区域')
    address=CharField(max_length=100,verbose_name='地址')
    coordinate_x=FloatField(verbose_name='经度')
    coordinate_y=FloatField(verbose_name='维度')
    photo= ImageField(blank=True,null=True,upload_to='photos/suppliers',verbose_name='照片')
    phone=CharField(max_length=100,verbose_name='电话')
    time_open=TimeField(verbose_name='开门时间')
    time_close=TimeField(verbose_name='打烊时间')
    description=CharField(max_length=1000,verbose_name='描述')
    owner=ForeignKey(User,verbose_name='店主账号')
    class Meta:
        verbose_name_plural=verbose_name='供应商'
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


class Bill(Model):
    service=ForeignKey(Service2)
    order_date=DateTimeField()
    user=ForeignKey(User)
    service_snapshot=CharField(max_length=2000)
    sms_content=CharField(max_length=1000)
    final_price=DecimalField(decimal_places=0, max_digits=5)
    status_choice=(('ordered','已预订'),('paid','已付款'),('complete','已完成'),)
    status=CharField(choices=status_choice,max_length=10,default=status_choice[0][0])

    created_time=DateTimeField(default=DateTime.now())
    complete_time=DateTimeField(null=True)
    #订单代码, 结帐时核对.
    bill_code=CharField(max_length=20)

    #给用户发送短信
    def send_sms(self):
        pass

    def save(self,*args,**kwargs):
        self.bill_code=randrange(10000,99999)
        super(Bill,self).save(*args,**kwargs)



from random import randrange
#返利  和  推荐 优惠.
class promote_register(Model):
    pass


class UserComment(Model):
    """
    用户评论
    """
    bill=ForeignKey(Bill)
    stars_choice=((1,'差'),(2,'一般'),(3,'好'),(4,'不错'),(5,'非常好'))
    #星级-服务态度
    stars_service=IntegerField(choices=stars_choice)
    #星级 施工效果
    stars_treatment=IntegerField(choices=stars_choice)
    #星级 性价比
    stars_cost=IntegerField(choices=stars_choice)
    comment_content=CharField(max_length=1000)
    comment_date=DateTimeField(default=DateTime.now())
    is_approved=BooleanField(default=False)
    pass


