import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re

based_comment_site='http://iranshao.com/races/{}/comments'
race_id=2740


# print(html)

def test_race_state(race_id):
    race_comment_site = based_comment_site.format(str(race_id))
    response = requests.get(race_comment_site).text
    selctor=etree.HTML(response)
    comment_all_num=selctor.xpath('//div[@id="racecomments"]/div/h2/span/span/text()')
    comment_site_num=selctor.xpath('//ul[@class="pagination pagination-v1"]/li/a/text()')[-2]
    return comment_site_num

print(test_race_state(583))
