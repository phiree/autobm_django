import sys,os,shutil
from django.conf import settings
from decimal import  Decimal, InvalidOperation

sys.path.append(r'D:\Code\autobm_django\automb')
os.environ['DJANGO_SETTINGS_MODULE'] = 'automb.settings'
from car_service.biz.parse_maintain_data import ParseHtmlFile
from car_service.models import CarBrand,CarSeries,CarInfo,Maintain_Transmission,Maintain_Tip,Maintain_Item,Maintain_Mileage
import re
from os.path import  join
import datetime
import glob
#import regex as re
class Import_Maintain():
    def __init__(self,html_file_folder,html_file_folder_completed):
        self.html_file_folder=html_file_folder
        self.html_file_folder_completed=html_file_folder_completed


    def import_from_file(self):
        listing =glob.glob(self.html_file_folder+'/detail*.html')
        total_files=len(listing)
        for file_index,file in enumerate(listing):#os.listdir(self.html_file_folder):
            parser=ParseHtmlFile(join(self.html_file_folder,file))
            #开始解析汽车数据
            parser.parse_carinfo()
            if parser==None:
                print('no match:'+file)
                continue
            #brand
            time_begin=datetime.datetime.now()
            print(''.join(['开始解析:',file,'--total:',str(total_files),'--current:',str(file_index+1)]))
            brand_name=self._strip(parser.brand)
            brand,created= CarBrand.objects.get_or_create(name=self._strip(brand_name))
            arr_series_parents=[]
            for ind, series_parent_name in enumerate(parser.series_parents):
                if ind==0:
                    series_parent,created=CarSeries.objects.get_or_create(name=self._strip(series_parent_name),parent=None,brand=brand)
                else:
                    series_parent,created=CarSeries.objects.get_or_create(name=self._strip(series_parent_name),brand=brand,parent=arr_series_parents[ind-1])
                arr_series_parents.append(series_parent)
            last_parent_series=arr_series_parents[-1]
            last_parent_series.maintain_summary=parser.maintain_summary
            last_parent_series.save()
            series_name=parser.series
            series,created=CarSeries.objects.get_or_create(name=self._strip(series_name),brand=brand,parent=last_parent_series)
            transmission_name=self._strip(parser.transmission)
            transmission,created=Maintain_Transmission.objects.get_or_create(name=transmission_name)
            carinfo,created=CarInfo.objects.get_or_create(name=self._strip(series.name),series=series,transmission=transmission)
            #开始解析保养数据
            parser.parse_maitain()
            mileage_obj_list=[]
            for col in parser.mileage_cols:
                m_item,created=Maintain_Mileage.objects.get_or_create(mile=col[0],period=col[1])
                mileage_obj_list.append(m_item)
            for row in parser.mileage_rows:
                item_name=self._strip(row[0])
                maintain_item,created=Maintain_Item.objects.get_or_create(name=item_name)
                tip_price=self._strip(row[1])
                if tip_price=='-':
                    tip_price=None
                else:
                    try:
                        tip_price=Decimal(tip_price)
                    except InvalidOperation:
                        print(tip_price)

                for index,mileage_obj in enumerate(mileage_obj_list):
                    index_for_row=index+2
                    if len(row)==3:
                        index_for_row=2
                    row_item=row[index_for_row]
                    if row_item=='●':
                        tip=Maintain_Tip.tip_choice[1][0]
                    elif row_item=='○':
                        tip=Maintain_Tip.tip_choice[0][0]
                    elif row_item=='':
                        tip=None
                    else:
                        tip=Maintain_Tip.tip_choice[2][0]
                    if tip==None:
                        continue
                    maitain_tip,created=Maintain_Tip.objects.get_or_create(car_info=carinfo
                                                                            ,item=maintain_item
                                                                           ,mileage=mileage_obj
                                                                           #,transmission=transmission
                                                                           ,price=tip_price,tip=tip)




            time_end=datetime.datetime.now()
            timespan=(time_end-time_begin).seconds
            print('解析完成:'+file+'-Elapsed time:'+str(timespan))
            shutil.move(file,self.html_file_folder_completed)


    def _strip(self,str):
        return str.strip(' \t\n\r')
if __name__=='__main__':
    importer=Import_Maintain(r'F:\Code\autobm_django\docs\保养手册_Teleport_From_Autohome\autohome',
                             r'F:\Code\autobm_django\docs\保养手册_Teleport_From_Autohome\completed')
    importer.import_from_file()