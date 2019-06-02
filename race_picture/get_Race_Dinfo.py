import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re

race_based_url = 'http://iranshao.com/races/{}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


def getRaceInfo(race_id_input):
    url = race_based_url.format(str(race_id_input))
    html = requests.get(url, headers=headers).content.decode('utf-8')
    # print(html.decode('utf-8'))

    selector = etree.HTML(html)
    race_website_state = selector.xpath('//div[@class="racememu hidden-xs"]/div/h1')
    if race_website_state != []:
        '''get race name'''
        race_name_state = selector.xpath('//div[@class="racememu hidden-xs"]/div/h1/a/text()')
        if race_name_state != []:
            race_name = race_name_state[0].replace('\n', '').replace(' ', '')
        else:
            race_name = 'null'

        '''get race picture site'''
        race_picture_site_state = selector.xpath('//div[@class="item active"]/a/img/@src')
        if race_picture_site_state != []:
            race_picture_site = race_picture_site_state[0]
        else:
            race_picture_site = 'null'

        '''get race location'''
        race_location_state = selector.xpath('//div[@class="race-his"]/p/text()')
        if race_location_state != []:
            race_location = race_location_state[0].replace('\n', '').replace(' ', '')
        else:
            race_location = 'null'

        '''get race score'''
        race_score = selector.xpath('//section[@class="race-scores"]/div/span/@data-score')[0]

        '''get race summary'''
        race_summary_state = selector.xpath('//div[@class="race-info"]/p/text()')
        if race_summary_state != []:
            race_summary = race_summary_state[0]
        else:
            race_summary = 'null'
        race_followed = selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[0]
        race_participant = selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[1]
        race_comment_state = selector.xpath('//div[@id="racecomments"]/div/h2/span/a/span/text()')
        if race_comment_state != []:
            race_comment = race_comment_state[0]
        else:
            race_comment = '赛事评论少于5条'
        race_diaries_state = selector.xpath('//div[@id="racediary"]/div/h2/span/a/span/text()')
        if race_diaries_state != []:
            race_diaries = race_diaries_state[0]
        else:
            race_diaries = selector.xpath('//div[@id="racediary"]/div/h2/span/span/text()')[0]
    else:
        race_name = 'null'
        race_picture_site='null'
        race_location = 'null'
        race_score = 'null'
        race_summary = 'null'
        race_followed = 'null'
        race_participant = 'null'
        race_comment = 'null'
        race_diaries = 'null'

    print('id为' + str(race_id_input) + '的赛事信息已获取完成！')
    return race_id_input, race_name, race_picture_site,race_location, race_score, race_summary, race_followed, race_participant, race_comment, race_diaries


# print(getRaceInfo(9272))
