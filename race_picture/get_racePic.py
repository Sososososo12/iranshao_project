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
from pathlib import Path

race_id_set = reload_excel.get_RaceIdList_all()
race_id_len=len(race_id_set)

# print(race_id_set[657])
race_based_url = 'http://iranshao.com/races/{}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


def getRacePic_State(race_id_input):
    url = race_based_url.format(str(race_id_input))
    race_html = requests.get(url, headers=headers).content.decode('utf-8')
    # print(html.decode('utf-8'))
    selector = etree.HTML(race_html)
    race_picture_status = selector.xpath('//div[@class="racedescription"]/div/div/div/div/div/a/img')
    pic_len = len(race_picture_status)
    print('ID:' + str(race_id_input) + ' 的赛事有 ' + str(pic_len) + ' 张宣传图片')
    # print(race_picture_status)
    return race_picture_status, pic_len


def getRacePic(race_Pic_Item):
    pic_address = race_Pic_Item.xpath('@src')
    # print(pic_address[0])
    return str(pic_address[0])


def open_Pic_Site(pic_url):
    require = requests.get(pic_url)
    response = require.content
    return response


def load_Pic(race_id, pic_index, pic_response):
    filename = r'../race_Pic_Download/race_{}_{}.jpg'.format(str(race_id), str(pic_index + 1))
    if os.path.isfile(filename):
        print('已存在编号' + str(pic_index + 1) + '对应地址的图片！')
    else:
        with open(filename, 'wb') as f:
            f.write(pic_response)
            f.close()
            print('race_id' + str(race_id) + ' 图片' + str(pic_index + 1) + ' 下载完成!')
    return filename

# count=0
race_id_dset=[]
pic_address_set=[]
for race_id_index in range(1290,race_id_len):
    race_id=race_id_set[race_id_index]
    count=race_id_index+1
    print('No.'+str(count)+' 开始查看id:'+str(race_id)+' 的赛事图片！')
    race_pic_state = getRacePic_State(race_id)
    if race_pic_state[1] > 0:
        for pic_index in range(race_pic_state[1]):
            race_id_dset.append(str(race_id))
            pic_address = getRacePic(race_pic_state[0][pic_index])
            # print(pic_address)
            pic_response = open_Pic_Site(pic_address)
            pic_address_set.append(load_Pic(race_id, pic_index, pic_response))
            time.sleep(1)
        print()
    else:
        print('该赛事无可下载的图片 \n')
        race_id_dset.append(str(race_id))
        pic_address_set.append('null')
    time.sleep(3)
print('所有赛事图片已下载完成！')




# print('开始保存数据')
# data1 = pd.DataFrame({'race_id':race_id_dset,
#                       'pic_path':pic_address_set
#                       })
# data1.to_excel(u'../race_Pic_Download/race_pic_path.xls', index=False, encoding='"utf_8_sig')
# print('信息写入完成！')


