def filter_by_state(list_dict, state):
    """Функция возвращает список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    list_1 = []
    for i in list_dict:
        if i['state'] == state:
            list_1.append(i)
    return list_1


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], state="EXECUTED"))