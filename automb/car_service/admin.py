from django.contrib import admin
from car_service.models import ServiceType,ServiceProperty,ServicePropertyValue,ServicePropertyValue_Brand,ServicePropertyValue_Brand_FoilType,\
    Service2,ServiceValue,Supplier,AreaInfo
# Register your models here.
admin.site.register(ServiceType)
admin.site.register(ServiceProperty)
admin.site.register(ServicePropertyValue)
admin.site.register(ServicePropertyValue_Brand)
admin.site.register(ServicePropertyValue_Brand_FoilType)
admin.site.register(Service2)
#admin.site.register(ServiceValue)
admin.site.register(Supplier)
admin.site.register(AreaInfo)

