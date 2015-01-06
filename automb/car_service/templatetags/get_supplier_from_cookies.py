# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278

from django import template
from ..models import Supplier
register = template.Library()
@register.filter
def get_supplier_from_cookies(request):
    supplier_id=request.COOKIES.get('supplier_id')
    return Supplier.objects.get(pk=supplier_id)