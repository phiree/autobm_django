from django import template

register = template.Library()
from car_service.models import ServiceType

"""
Decorator to facilitate template tag creation
"""
def get_typelist():
   return {'top_service_list': ServiceType.objects.filter(parent=None)}
register.inclusion_tag('car_service/share/left_menu_service_type2.html')(get_typelist)

