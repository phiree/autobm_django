__author__ = '20141220'
import re
from bs4 import BeautifulSoup
from soupselect import select
#import regex as re


class ParseHtmlFile():
    def __init__(self,html_file):
        self.html_file=html_file
        with open(html_file) as f:
            self.html_content=f.read()

    def parse_carinfo(self):
        pattern_car_section= r'<div\sclass="t_H"[^>]*>.*<div\s+class="m_t8\s+auto_framewarp">'
        match_car_section=re.search(pattern_car_section,self.html_content,re.IGNORECASE | re.VERBOSE | re.DOTALL)
        if not match_car_section:
            print('No match')
            return None
        car_section=match_car_section.group(0)
        pattern_carinfo=r'<a.*?>(.*?)</a>'
        match_car_brand_series=re.findall(pattern_carinfo,car_section,re.IGNORECASE|re.DOTALL)
        self.brand=match_car_brand_series[2]
        self.series_parents=match_car_brand_series[3:]
        pattern_series=r'[^\n]\s+&gt;&nbsp;([^a]+)&gt;'
        match_series=re.findall(pattern_series,car_section)
        self.series=match_series[0]
        pattern_transmission=r'&nbsp;(.+变速.+)'
        self.transmission=re.findall(pattern_transmission,car_section)[0]
        pattern_summary=r'class="notes">(.*?)●更换'
        match_maintain_summary=re.search(pattern_summary,self.html_content,re.MULTILINE|re.DOTALL|re.IGNORECASE)
        self.maintain_summary=match_maintain_summary.group(1)

    def parse_maitain(self):
        soup=BeautifulSoup(self.html_content)
        maintain_table=select(soup,'.t_H3 tr')
        self.mileage_cols=[]
        self.mileage_rows=[]
        for index,tr in enumerate(maintain_table):
            row_mileage_list=tr.findAll('td')
            row=[]
            for index2,td_mileage in enumerate(row_mileage_list):
                mileage_string=td_mileage.text
                if any(x in mileage_string for x in ( '总计','备注')):
                    break
                if index==0:
                #is mileage row
                    if index2<2:#标题部分 直接跳过.
                        continue
                    mileage_mileage=int(re.search(r'(\d+)公里', mileage_string).group(1))
                    mileage_period=int( re.search(r'(\d+)个月',mileage_string).group(1))
                    self.mileage_cols.append((mileage_mileage,mileage_period))
                else:
                    row.append(mileage_string)
            if row:
                self.mileage_rows.append(row)
        pass

if __name__=="__main__":
    import os
    file_path=os.path.dirname(os.path.realpath(__file__))
    print('-')
    print(file_path)
    print('--')
    parser=ParseHtmlFile('D:/Code/autobm_django/automb/car_service/test_files/detail_3_871_0_0_0_57.html')
    parser.parse_carinfo()






