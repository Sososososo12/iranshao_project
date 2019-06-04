from race_score import get_Race_Score
from race_picture import reload_excel

race_id_all=reload_excel.get_RaceIdList_all()
race_len=len(race_id_all)

for batch in range(0,race_len,50):
    for race_id_index in range(batch-50,batch):
        # print(batch)
        print('id:'+str(race_id_all[race_id_index])+'的评论信息开始收集：')
        race_comment_num = get_Race_Score.get_race_state(race_id_all[race_id_index])[1]

        if int(float(race_comment_num))==0:
            print('id:'+str(race_id_all[race_id_index])+'的评论信息为0')
            continue

        race_response = get_Race_Score.get_race_state(2740)[0]
        comment_list = get_Race_Score.get_comment_list(race_response)
        get_Race_Score.get_comment_userinfo(comment_list, race_response)

