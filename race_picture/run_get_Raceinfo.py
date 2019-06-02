import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re
from race_picture import reload_excel
from race_picture import get_Race_Dinfo
from race_picture import email_attention

race_id=[]
race_name=[]
race_picture_site=[]
race_location=[]
race_score=[]
race_summary=[]
race_followed=[]
race_participant=[]
race_comment=[]
race_diaries=[]
number=0

race_id_norm=reload_excel.get_RaceIdList_norm()

# for idnumber in range(0,10):
for idnumber in race_id_norm:
    racecpinfo_tuple=get_Race_Dinfo.getRaceInfo(idnumber)
    # racecpinfo_tuple = get_Race_Dinfo.getRaceInfo(race_id_norm[idnumber])
    number=number+1
    race_id.append(racecpinfo_tuple[0])
    race_name.append(racecpinfo_tuple[1])
    race_picture_site.append(racecpinfo_tuple[2])
    race_location.append(racecpinfo_tuple[3])
    race_score.append(racecpinfo_tuple[4])
    race_summary.append(racecpinfo_tuple[5])
    race_followed.append(racecpinfo_tuple[6])
    race_participant.append(racecpinfo_tuple[7])
    race_comment.append(racecpinfo_tuple[8])
    race_diaries.append(racecpinfo_tuple[9])
    print('第'+str(number)+'条赛事详细信息已获取完成！id为：'+str(idnumber)+'\n')
    time.sleep(2)

data1 = pd.DataFrame({'race_id':race_id,
                      'race_name':race_name,
                      'race_picture_site':race_picture_site,
                      'race_location':race_location,
                      'race_score':race_score,
                      'race_summary':race_summary,
                      'race_followed':race_followed,
                      'race_participant':race_participant,
                      'race_comment':race_comment,
                      'race_diaries':race_diaries
                      })
data1.to_excel(u'../based_resources/race_Dinfo.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')
email_attention.mail()