from django.template import Library
from ..models import Supplier
register = Library()

@register.filter
def get_service_type_for_supplier( value,service_type ):
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
    results=value.service2_set.filter(servicetype_id=service_type)
    return results

