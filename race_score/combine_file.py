from race_score import get_Race_Score
from race_picture import reload_excel, email_attention
import pandas as pd
import time
import xlrd


def get_RaceCommentExcel(race_id):
    filename = r'../comment_resource/{}_comments.xls'.format(str(race_id))
    data = xlrd.open_workbook(filename=filename)
    sheet1 = data.sheet_by_index(0)
    comment_content = sheet1.col_values(0)
    comment_content.remove('comment_contents')
    comment_race_id = sheet1.col_values(1)
    comment_race_id.remove('comment_race_id')
    score_atomsphere = sheet1.col_values(2)
    score_atomsphere.remove('comment_score_atomsphere')
    score_organize = sheet1.col_values(4)
    score_organize.remove('comment_score_organize')
    score_sight = sheet1.col_values(5)
    score_sight.remove('comment_score_sight')
    score_mean = sheet1.col_values(3)
    score_mean.remove('comment_score_mean')
    comment_times = sheet1.col_values(6)
    comment_times.remove('comment_times')
    comment_tp_event = sheet1.col_values(7)
    comment_tp_event.remove('comment_tp_event')
    comment_tp_finishedtimes = sheet1.col_values(8)
    comment_tp_finishedtimes.remove('comment_tp_finishedtime')
    comment_tp_ytime = sheet1.col_values(9)
    comment_tp_ytime.remove('comment_tp_ytime')
    comment_racer_id = sheet1.col_values(10)
    comment_racer_id.remove('comment_user_id')
    comment_racer_name = sheet1.col_values(11)
    comment_racer_name.remove('comment_user_name')

    return comment_content, comment_race_id, score_atomsphere, score_organize, score_sight, score_mean, comment_times, comment_tp_event, comment_tp_finishedtimes, comment_tp_ytime, comment_racer_id, comment_racer_name


race_id_all = reload_excel.get_RaceID_CommentList()
race_len = len(race_id_all)

# race_id = 583
# print(get_RaceCommentExcel(race_id))

for race_index in range(100):
    race_id = race_id_all[race_index]
    race_comment_detail=get_RaceCommentExcel(race_id)
    '''need to create every list of set-name,
     then extend result set to the corresponding list'''
