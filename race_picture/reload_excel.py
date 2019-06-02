import xlrd

def get_RaceIdList_norm():
    filename = r'../based_resources/race_info_test.xls'
    data = xlrd.open_workbook(filename=filename)
    sheet1 = data.sheet_by_index(0)
    race_id_set = sheet1.col_values(1)
    race_id_set.remove('race_id')
    race_id_set2=list(map(int,race_id_set))
    return race_id_set2

def get_RaceIdList_all():
    filename = r'../based_resources/race_dinfo_test.xls'
    data = xlrd.open_workbook(filename=filename)
    sheet1 = data.sheet_by_index(0)
    user_id_set = sheet1.col_values(3)
    # user_id_len = len(user_id_set)
    user_id_set.remove('race_id')
    user_id_set2 = list(map(int, user_id_set))
    return  user_id_set2

# print(get_RaceIdList_norm())