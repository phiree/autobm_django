
from ..models import Supplier, Service2,ServiceValue,ServicePropertyValue
from django.db.models import Q
# Create your views here.
#字典管理

#used in both site_admin and supplier_admin
def search(kw):
    service_result=Service2.objects.filter(Q(title__contains=kw)
                                           |Q(description__contains=kw)
                                        |Q(supplier__name__contains=kw)
                                        |Q(supplier__address__contains=kw)
                                            )
    supplier_result=[]
    return (service_result,supplier_result)
    pass







