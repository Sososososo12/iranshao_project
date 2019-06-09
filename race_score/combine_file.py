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


def get_RaceCommentExcelbatch(race_batch1, race_batch2):
    filename = r'../comment_resource/{}_{}_comments.xls'.format(str(race_batch1), str(race_batch2))
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
comment_race_id = []
comment_user_id = []
comment_user_name = []
comment_tp_ytime = []
comment_tp_event = []
comment_tp_finishedtime = []
comment_scoreA = []
comment_scoreO = []
comment_scoreS = []
comment_scoreM = []
comment_contents = []
comment_times = []

for race_index in range(100):
    race_id = race_id_all[race_index]
    race_comment_detail = get_RaceCommentExcel(race_id)
    '''need to create every list of set-name,
     then extend result set to the corresponding list'''

    comment_contents.extend(race_comment_detail[0])
    comment_race_id.extend(race_comment_detail[1])
    comment_scoreA.extend(race_comment_detail[2])
    comment_scoreO.extend(race_comment_detail[3])
    comment_scoreS.extend(race_comment_detail[4])
    comment_scoreM.extend(race_comment_detail[5])
    comment_times.extend(race_comment_detail[6])
    comment_tp_event.extend(race_comment_detail[7])
    comment_tp_finishedtime.extend(race_comment_detail[8])
    comment_tp_ytime.extend(race_comment_detail[9])
    comment_user_id.extend(race_comment_detail[10])
    comment_user_name.extend(race_comment_detail[11])
    print('No.' + str(race_index) + ' 已添加赛事id:' + str(race_id) + ' 的评论信息，共计' + str(len(race_comment_detail[5])) + ' 条')
    print('现有赛事评论信息总计' + str(len(comment_scoreM)) + '条' + '\n')
time.sleep(2)

num = 0
for batch in range(150, race_len, 50):
    num += 1
    race_comment_detail = get_RaceCommentExcelbatch(batch - 50, batch)
    comment_contents.extend(race_comment_detail[0])
    comment_race_id.extend(race_comment_detail[1])
    comment_scoreA.extend(race_comment_detail[2])
    comment_scoreO.extend(race_comment_detail[3])
    comment_scoreS.extend(race_comment_detail[4])
    comment_scoreM.extend(race_comment_detail[5])
    comment_times.extend(race_comment_detail[6])
    comment_tp_event.extend(race_comment_detail[7])
    comment_tp_finishedtime.extend(race_comment_detail[8])
    comment_tp_ytime.extend(race_comment_detail[9])
    comment_user_id.extend(race_comment_detail[10])
    comment_user_name.extend(race_comment_detail[11])
    print('No.' + str(num) + ' 已添加赛事id:' + str(batch - 50) + '_' + str(batch) + ' 的评论信息，共计' + str(
        len(race_comment_detail[5])) + ' 条')
    print('现有赛事评论信息总计' + str(len(comment_scoreM)) + '条' + '\n')
time.sleep(2)

race_comment_detail = get_RaceCommentExcelbatch(batch - 50, batch)
comment_contents.extend(race_comment_detail[0])
comment_race_id.extend(race_comment_detail[1])
comment_scoreA.extend(race_comment_detail[2])
comment_scoreO.extend(race_comment_detail[3])
comment_scoreS.extend(race_comment_detail[4])
comment_scoreM.extend(race_comment_detail[5])
comment_times.extend(race_comment_detail[6])
comment_tp_event.extend(race_comment_detail[7])
comment_tp_finishedtime.extend(race_comment_detail[8])
comment_tp_ytime.extend(race_comment_detail[9])
comment_user_id.extend(race_comment_detail[10])
comment_user_name.extend(race_comment_detail[11])
print('No.' + str(num + 1) + ' 已添加赛事id: 4900_4940' + ' 的评论信息，共计' + str(len(race_comment_detail[5])) + ' 条')
print('现有赛事评论信息总计' + str(len(comment_scoreM)) + '条' + '\n')

data1 = pd.DataFrame({'comment_race_id': comment_race_id,
                      'comment_user_id': comment_user_id,
                      'comment_user_name': comment_user_name,
                      'comment_tp_ytime': comment_tp_ytime,
                      'comment_tp_event': comment_tp_event,
                      'comment_tp_finishedtime': comment_tp_finishedtime,
                      'comment_score_sight': comment_scoreS,
                      'comment_score_organize': comment_scoreO,
                      'comment_score_atomsphere': comment_scoreA,
                      'comment_score_mean': comment_scoreM,
                      'comment_contents': comment_contents,
                      'comment_times': comment_times
                      })
data1.to_excel(u'../comment_resource/all_comments.xlsx', index=False, encoding='"utf_8_sig')
print('第4850 到第4900 个的赛事评论信息已写入完成！')
print('共计' + str(len(comment_times)) + ' 条。' + '\n\n\n')
# email_attention.mail(race_id)
time.sleep(3)
