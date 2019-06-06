import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re
import math

based_comment_site = 'http://iranshao.com/races/{}/comments?page={}'


# race_id = 2740


# print(html)

def get_race_state(race_id, site_num=1):
    race_comment_site = based_comment_site.format(str(race_id), str(site_num))
    response = requests.get(race_comment_site).text
    selctor = etree.HTML(response)
    comment_all_num = selctor.xpath('//div[@id="racecomments"]/div/h2/span/span/text()')[0]
    if int(float(comment_all_num)) <= 20:
        comment_site_num='1'
    else:
        comment_site_num = selctor.xpath('//ul[@class="pagination pagination-v1"]/li/a/text()')[-2]
    return response, comment_all_num, comment_site_num


def get_comment_list(url_response):
    selctor = etree.HTML(url_response)
    race_comment_list = selctor.xpath('//ol[@id="race_comment_tab"]/li')
    race_comment_len = len(race_comment_list)
    return race_comment_list


def get_comment_userinfo(comments_list, response_text):
    user_name_list = []
    user_id_list = []
    tp_ytime_all = []
    tp_event_all = []
    tp_finishedtime_all = []

    for user in comments_list:
        user_id = user.xpath('h4/a/@href')[0]
        user_name = user.xpath('h4/a/@title')[0]

        user_id_list.append(user_id)
        user_name_list.append(user_name)

    user_tp = re.findall('<p class="result">(.*?)class="comment-score">', response_text, re.S)
    for item in user_tp:
        tp_state = re.findall('<span>(.*?)</span>', item, re.S)
        '''网页中出现当只有点评赛事年份信息时，span的列表长度为1；
           而出现参赛项目与完赛时间时，即列表长度为2，3时显示正常；
           所以添加循环判断span的列表长度'''
        if len(tp_state) == 1:
            tp_ytime = tp_state[0].replace('点评了', '').replace('年赛事', '')
            tp_event = 'null'
            tp_finishedtime = 'null'
        elif len(tp_state) == 2:
            tp_ytime = tp_state[0].replace('点评了', '').replace('年赛事', '')
            tp_event = tp_state[1]
            tp_finishedtime = 'null'
        else:
            tp_ytime = tp_state[0].replace('点评了', '').replace('年赛事', '')
            tp_event = tp_state[1]
            tp_finishedtime = tp_state[2]

        tp_ytime_all.append(tp_ytime)
        tp_event_all.append(tp_event)
        tp_finishedtime_all.append(tp_finishedtime)

    return user_id_list, user_name_list, tp_ytime_all, tp_event_all, tp_finishedtime_all


def get_comment_scoreinfo(comments_list):
    score_s = []
    score_o = []
    score_a = []
    score_m = []
    for user in comments_list:
        score_state = user.xpath('div[@class="comment-score"]/span/span[@class="score-item"]')
        if len(score_state) == 3:
            score_sight_str = score_state[0].xpath('span/@data-score')[0]
            score_sight = int(float(score_sight_str))
            score_organize_str = score_state[1].xpath('span/@data-score')[0]
            score_organize = int(float(score_organize_str))
            score_atomsphere_str = score_state[2].xpath('span/@data-score')[0]
            score_atomsphere = int(float(score_atomsphere_str))
            score_mean = (score_sight + score_organize + score_atomsphere) / 3
        elif len(score_state) == 2:
            score_sight_str = score_state[0].xpath('span/@data-score')[0]
            score_sight = int(float(score_sight_str))
            score_organize_str = score_state[1].xpath('span/@data-score')[0]
            score_organize = int(float(score_organize_str))
            score_atomsphere = None
            score_mean = (score_sight + score_organize) / 2
        elif len(score_state) == 1:
            score_sight_str = score_state[0].xpath('span/@data-score')[0]
            score_sight = int(float(score_sight_str))
            score_organize = None
            score_atomsphere = None
            score_mean = float(score_sight_str)
        else:
            score_sight = None
            score_organize = None
            score_atomsphere = None
            score_mean = None

        score_s.append(score_sight)
        score_o.append(score_organize)
        score_a.append(score_atomsphere)
        score_m.append(score_mean)

    return score_s, score_o, score_a, score_m


def get_comment_content(comments_list):
    comments_all = []
    for user in comments_list:
        comment_state = user.xpath('div[@class="comment-body"]/p/text()')
        if comment_state != []:
            comment = comment_state[0]
        else:
            comment = 'null'
        comments_all.append(comment)
    return comments_all


def get_comment_time(comments_list):
    commit_time = []
    for user in comments_list:
        time_state = user.xpath('p[@class="comment-meta"]/span/text()')
        if time_state != []:
            time = time_state[0]
        else:
            time = 'null'
        commit_time.append(time)
    return commit_time


race_response = get_race_state(583, 70)[0]
comment_list = get_comment_list(race_response)
get_comment_scoreinfo(comment_list)
get_comment_userinfo(comment_list, race_response)
