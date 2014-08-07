from django.test import TestCase
from car_service.models import Service,ServiceDetail,Supplier,Tree
from datetime import time
from django.contrib.auth.models  import User,UserManager
class AnimalTestCase(TestCase):
    def setUp(self):
        area= Tree.objects.create(name='广州',tree_type=Tree.get_type(0))
        car=Tree.objects.create(name='君威2014款',tree_type=Tree.get_type(1))
        service=Tree.objects.create(name='玻璃贴膜',tree_type=Tree.get_type(2))
        brand=Tree.objects.create(name='3M',tree_type=Tree.get_type(3))

        foil_type= Tree.objects.create(name='整车',tree_type=Tree.get_type(6))
        foil_model_front=Tree.objects.create(name='前挡类型',tree_type=Tree.get_type(7))


        supplier=Supplier.objects.create(
                    name='s1',
                    area=area,
                    address='address1',
                    coordinate_x=120.01234,
                    coordinate_y=30.1234,
                    #photo=# ImageField(blank=True,null=True,upload_to='photos/suppliers')
                    phone='1234567',
                    time_open=time(10,0,0),
                    time_close=time(19,0,0),
                    description='description of s1',
                    owner=UserManager.create_user('phiree', email=None, password=None)

        )
        service=Service.objects.create(supplier=supplier,service_type=service,car=car)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""

        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

        servicedetail=ServiceDetail(
            service=Service.objects.get(supplier__name='s1'),
            brand=Tree.objects.get(tree_type=Tree.get_type(3),name='君威2014款'),

        )
