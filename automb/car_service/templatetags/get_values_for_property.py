from django.template import Library
from ..models import Supplier,Service2,ServicePropertyValue
register = Library()

@register.filter
def get_values_for_property(p,ids):
    """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views

    """
    results=[]
    sid=int(ids.split('_')[1])
    tid=int(ids.split('_')[0])
    services=Service2.objects.filter(supplier__id=sid,servicetype__id=tid)
    for s in services:
        for v in s.servicevalue_set.all():
            if v.servicepropertyvalue.serviceproperty==p:
                if  v.servicepropertyvalue in results:
                    continue
                results.append(ServicePropertyValue.objects.get_subclass(pk=v.servicepropertyvalue.id))
    return results

