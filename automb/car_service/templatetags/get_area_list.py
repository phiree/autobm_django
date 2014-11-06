from django import template

register = template.Library()
from ..models import AreaInfo

"""
Decorator to facilitate template tag creation
"""
def get_area_list():
   return {'area_list': AreaInfo.objects.all()}
register.inclusion_tag('car_service/share/area_list.html')(get_area_list)

