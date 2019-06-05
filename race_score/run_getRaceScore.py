from race_score import get_Race_Score
from race_picture import reload_excel,email_attention
import pandas as pd
import time


based_comment_site='http://iranshao.com/races/{}/comments?page={}'
race_id_all=reload_excel.get_RaceID_CommentList()
race_len=len(race_id_all)


for race_id_index1 in range(2,100):
    '''初始化最终list'''
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


    race_id=race_id_all[race_id_index1]
    race_state=get_Race_Score.get_race_state(str(race_id))
    race_comment_num = race_state[1]

    '''判断赛事的评论数量是否为0，为0的话跳过这个赛事，进入下一个赛事'''
    if int(float(race_comment_num)) == 0:
        print('id:' + str(race_id_all[race_id_index1]) + '的评论信息为0')
        continue
    print('id:' + str(race_id) + '的评论信息开始收集！共'+str(race_state[1])+'条评论信息！')

    '''首先为这各赛事所有的评论信息建一个对应的race_id列表'''
    for i in range(int(float(race_comment_num))):
        comment_race_id.append(race_id)

    '''单独爬取第一页的赛事评论信息'''
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
    print('已完成id:' + str(race_id) + '赛事的第 1 页评论信息收集！')
    time.sleep(2)

    comment_site_num=int(float(race_state[2]))
    for site_num in range(1,comment_site_num):
        site_num+=1
        site_response=get_Race_Score.get_race_state(race_id,site_num)[0]
        comment_list=get_Race_Score.get_comment_list(site_response)

        comment_user_info=get_Race_Score.get_comment_userinfo(comment_list,site_response)
        comment_score_info=get_Race_Score.get_comment_scoreinfo(comment_list)
        comment_content=get_Race_Score.get_comment_content(comment_list)
        comment_time=get_Race_Score.get_comment_time(comment_list)

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
        print('已完成id:' + str(race_id) + '赛事的第 '+str(site_num)+' 页评论信息收集！')
        time.sleep(2)

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
    data1.to_excel(u'../comment_resource/{}_comments.xls'.format(str(race_id)), index=False, encoding='"utf_8_sig')
    print('id：'+str(race_id)+' 的赛事信息已写入完成！'+'\n\n\n')
    email_attention.mail(race_id)
    time.sleep(3)




# for batch in range(0,race_len,50):
#     for race_id_index in range(batch-50,batch):
#         # print(batch)
#         print('id:'+str(race_id_all[race_id_index])+'的评论信息开始收集：')
#         race_comment_num = get_Race_Score.get_race_state(race_id_all[race_id_index])[1]
#
#         if int(float(race_comment_num))==0:
#             print('id:'+str(race_id_all[race_id_index])+'的评论信息为0')
#             continue
#
#         race_response = get_Race_Score.get_race_state(2740)[0]
#         comment_list = get_Race_Score.get_comment_list(race_response)
#         get_Race_Score.get_comment_userinfo(comment_list, race_response)
#
