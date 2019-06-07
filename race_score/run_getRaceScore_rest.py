from race_score import get_Race_Score
from race_picture import reload_excel, email_attention
import pandas as pd
import time

based_comment_site = 'http://iranshao.com/races/{}/comments?page={}'
race_id_all = reload_excel.get_RaceID_CommentList()
race_len = len(race_id_all)

# print(race_id_all[100])
# for batch in range(150, race_len, 50):
#     print('********************************\n' +
#           '开始获取第' + str(batch - 50) + ' 到第' + str(batch) + ' 个的赛事评论信息\n' +
#           '起始赛事id:' + str(race_id_all[batch - 50]) + '    末端赛事id:' + str(race_id_all[batch - 1]) + '\n' +
#           '********************************\n')
#
#     # print(batch)
#     race_count = 0
#     race_tcount = 0
#     '''初始化每个batch的最终list'''
#     comment_race_id = []
#     comment_user_id = []
#     comment_user_name = []
#     comment_tp_ytime = []
#     comment_tp_event = []
#     comment_tp_finishedtime = []
#     comment_score1 = []
#     comment_score2 = []
#     comment_score3 = []
#     comment_scoreM = []
#     comment_contents = []
#     comment_times = []
#
#     for race_index in range(batch - 50, batch):
#         race_count += 1
#         race_id = race_id_all[race_index]
#         race_state = get_Race_Score.get_race_state(str(race_id))
#         race_comment_num = int(float(race_state[1]))
#         race_comment_sitenum = int(float(race_state[2]))
#         '''判断赛事的评论数量是否为0，为0的话跳过这个赛事，进入下一个赛事'''
#         if race_comment_num == 0:
#             print('NO.' + str(race_count) + ' id:' + str(race_id_all[race_index]) + '的评论信息为0！ 已跳过评论信息获取！')
#             continue
#
#         print('NO.' + str(race_count) + ' id:' + str(race_id) + '的评论信息开始收集！共' + str(race_state[1]) + '条评论信息！')
#         race_tcount += 1
#         '''首先为这各赛事所有的评论信息建一个对应的race_id列表'''
#         for i in range(race_comment_num):
#             comment_race_id.append(race_id)
#
#         '''判断赛事的评论页数是否为1，为1的情况下单独获取1页；多页情况下，循环获取'''
#         if race_comment_sitenum == 1:
#             '''单独爬取单页的赛事评论信息'''
#             comment_list = get_Race_Score.get_comment_list(race_state[0])
#             comment_user_info = get_Race_Score.get_comment_userinfo(comment_list, race_state[0])
#             comment_score_info = get_Race_Score.get_comment_scoreinfo(comment_list)
#             comment_content = get_Race_Score.get_comment_content(comment_list)
#             comment_time = get_Race_Score.get_comment_time(comment_list)
#
#             comment_user_id.extend(comment_user_info[0])
#             comment_user_name.extend(comment_user_info[1])
#             comment_tp_ytime.extend(comment_user_info[2])
#             comment_tp_event.extend(comment_user_info[3])
#             comment_tp_finishedtime.extend(comment_user_info[4])
#             comment_score1.extend(comment_score_info[0])
#             comment_score2.extend(comment_score_info[1])
#             comment_score3.extend(comment_score_info[2])
#             comment_scoreM.extend(comment_score_info[3])
#             comment_contents.extend(comment_content)
#             comment_times.extend(comment_time)
#             print('已完成id:' + str(race_id) + '赛事的评论信息收集！')
#             print('此赛事评论数小于20')
#             time.sleep(2)
#
#         elif race_comment_sitenum > 1:
#             '''使用循环获取多页赛事信息'''
#             for site_num in range(race_comment_sitenum):
#                 site_num += 1
#                 site_response = get_Race_Score.get_race_state(race_id, site_num)[0]
#                 comment_list = get_Race_Score.get_comment_list(site_response)
#
#                 comment_user_info = get_Race_Score.get_comment_userinfo(comment_list, site_response)
#                 comment_score_info = get_Race_Score.get_comment_scoreinfo(comment_list)
#                 comment_content = get_Race_Score.get_comment_content(comment_list)
#                 comment_time = get_Race_Score.get_comment_time(comment_list)
#
#                 comment_user_id.extend(comment_user_info[0])
#                 comment_user_name.extend(comment_user_info[1])
#                 comment_tp_ytime.extend(comment_user_info[2])
#                 comment_tp_event.extend(comment_user_info[3])
#                 comment_tp_finishedtime.extend(comment_user_info[4])
#                 comment_score1.extend(comment_score_info[0])
#                 comment_score2.extend(comment_score_info[1])
#                 comment_score3.extend(comment_score_info[2])
#                 comment_scoreM.extend(comment_score_info[3])
#                 comment_contents.extend(comment_content)
#                 comment_times.extend(comment_time)
#                 print('已完成id:' + str(race_id) + '赛事的第 ' + str(site_num) + ' 页评论信息收集！')
#                 time.sleep(2)
#         print('已完成id:' + str(race_id) + '赛事的评论信息收集！现有评论信息共计 ' + str(len(comment_times)) + ' 条\n')
#
#     data1 = pd.DataFrame({'comment_race_id': comment_race_id,
#                           'comment_user_id': comment_user_id,
#                           'comment_user_name': comment_user_name,
#                           'comment_tp_ytime': comment_tp_ytime,
#                           'comment_tp_event': comment_tp_event,
#                           'comment_tp_finishedtime': comment_tp_finishedtime,
#                           'comment_score_sight': comment_score1,
#                           'comment_score_organize': comment_score2,
#                           'comment_score_atomsphere': comment_score3,
#                           'comment_score_mean': comment_scoreM,
#                           'comment_contents': comment_contents,
#                           'comment_times': comment_times
#                           })
#     data1.to_excel(u'../comment_resource/{}_{}_comments.xls'.format(str(batch - 50), str(batch)), index=False,
#                    encoding='"utf_8_sig')
#     print('第' + str(batch - 50) + ' 到第' + str(batch) + ' 个的赛事评论信息已写入完成！')
#     print('共计 ' + str(race_tcount) + ' 个赛事存在赛事评论信息，共 ' + str(len(comment_times)) + ' 条。' + '\n\n\n')
#     # email_attention.mail(race_id)
#     time.sleep(3)




'''4900-4940的赛事评论信息获取'''

print('********************************\n' +
      '开始获取第4900-第4940条赛事的评论信息\n' +
      '起始赛事id:' + str(race_id_all[4900]) + '    末端赛事id:' + str(race_id_all[race_len - 1]) + '\n' +
      '********************************\n')
race_count = 0
race_tcount = 0
'''初始化每个batch的最终list'''
comment_race_id = []
comment_user_id = []
comment_user_name = []
comment_tp_ytime = []
comment_tp_event = []
comment_tp_finishedtime = []
comment_score1 = []
comment_score2 = []
comment_score3 = []
comment_scoreM = []
comment_contents = []
comment_times = []

for race_index in range(4850, 4900):
    race_count += 1
    race_id = race_id_all[race_index]
    race_state = get_Race_Score.get_race_state(str(race_id))
    race_comment_num = int(float(race_state[1]))
    race_comment_sitenum = int(float(race_state[2]))
    '''判断赛事的评论数量是否为0，为0的话跳过这个赛事，进入下一个赛事'''
    if race_comment_num == 0:
        print('NO.' + str(race_count) + ' id:' + str(race_id_all[race_index]) + '的评论信息为0！ 已跳过评论信息获取！')
        continue

    print('NO.' + str(race_count) + ' id:' + str(race_id) + '的评论信息开始收集！共' + str(race_state[1]) + '条评论信息！')
    race_tcount += 1
    '''首先为这各赛事所有的评论信息建一个对应的race_id列表'''
    for i in range(race_comment_num):
        comment_race_id.append(race_id)

    '''判断赛事的评论页数是否为1，为1的情况下单独获取1页；多页情况下，循环获取'''
    if race_comment_sitenum == 1:
        '''单独爬取单页的赛事评论信息'''
        comment_list = get_Race_Score.get_comment_list(race_state[0])
        comment_user_info = get_Race_Score.get_comment_userinfo(comment_list, race_state[0])
        comment_score_info = get_Race_Score.get_comment_scoreinfo(comment_list)
        comment_content = get_Race_Score.get_comment_content(comment_list)
        comment_time = get_Race_Score.get_comment_time(comment_list)

        comment_user_id.extend(comment_user_info[0])
        comment_user_name.extend(comment_user_info[1])
        comment_tp_ytime.extend(comment_user_info[2])
        comment_tp_event.extend(comment_user_info[3])
        comment_tp_finishedtime.extend(comment_user_info[4])
        comment_score1.extend(comment_score_info[0])
        comment_score2.extend(comment_score_info[1])
        comment_score3.extend(comment_score_info[2])
        comment_scoreM.extend(comment_score_info[3])
        comment_contents.extend(comment_content)
        comment_times.extend(comment_time)
        print('已完成id:' + str(race_id) + '赛事的评论信息收集！')
        print('此赛事评论数小于20')
        time.sleep(2)

    elif race_comment_sitenum > 1:
        '''使用循环获取多页赛事信息'''
        for site_num in range(race_comment_sitenum):
            site_num += 1
            site_response = get_Race_Score.get_race_state(race_id, site_num)[0]
            comment_list = get_Race_Score.get_comment_list(site_response)

            comment_user_info = get_Race_Score.get_comment_userinfo(comment_list, site_response)
            comment_score_info = get_Race_Score.get_comment_scoreinfo(comment_list)
            comment_content = get_Race_Score.get_comment_content(comment_list)
            comment_time = get_Race_Score.get_comment_time(comment_list)

            comment_user_id.extend(comment_user_info[0])
            comment_user_name.extend(comment_user_info[1])
            comment_tp_ytime.extend(comment_user_info[2])
            comment_tp_event.extend(comment_user_info[3])
            comment_tp_finishedtime.extend(comment_user_info[4])
            comment_score1.extend(comment_score_info[0])
            comment_score2.extend(comment_score_info[1])
            comment_score3.extend(comment_score_info[2])
            comment_scoreM.extend(comment_score_info[3])
            comment_contents.extend(comment_content)
            comment_times.extend(comment_time)
            print('已完成id:' + str(race_id) + '赛事的第 ' + str(site_num) + ' 页评论信息收集！')
            time.sleep(2)

    print('已完成id:' + str(race_id) + '赛事的评论信息收集！现有评论信息共计 ' + str(race_comment_num) + ' 条')

data1 = pd.DataFrame({'comment_race_id': comment_race_id,
                      'comment_user_id': comment_user_id,
                      'comment_user_name': comment_user_name,
                      'comment_tp_ytime': comment_tp_ytime,
                      'comment_tp_event': comment_tp_event,
                      'comment_tp_finishedtime': comment_tp_finishedtime,
                      'comment_score_sight': comment_score1,
                      'comment_score_organize': comment_score2,
                      'comment_score_atomsphere': comment_score3,
                      'comment_score_mean': comment_scoreM,
                      'comment_contents': comment_contents,
                      'comment_times': comment_times
                      })
data1.to_excel(u'../comment_resource/4850_4900_comments.xls', index=False,
               encoding='"utf_8_sig')
print('第4850 到第4900 个的赛事评论信息已写入完成！')
print('共计 ' + str(race_tcount) + ' 个赛事存在赛事评论信息，共 ' + str(len(comment_times)) + ' 条。' + '\n\n\n')
# email_attention.mail(race_id)
time.sleep(3)
