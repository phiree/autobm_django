from django.test import TestCase
from django.conf import settings
from .biz.parse_maintain_data import ParseHtmlFile
from .biz.import_maintain_data import Import_Maintain

class regex_test(TestCase):
    def setUp(self):
        self.parser= ParseHtmlFile(settings.BASE_DIR+'/car_service/test_files/detail_1001_18_0_0_0_58.html')
        self.parser.parse_maitain()
    def test_parse_maintain(self):
        self.assertEqual(10,len(self.parser.mileage_rows))

