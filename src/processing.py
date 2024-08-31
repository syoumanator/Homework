list_of_dictionaries = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_data: list, state: str):
    """Функция возвращает список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""
    new_list = []
    for i in list_data:
        if i["state"] == state:
            new_list.append(i)
    return new_list


print(filter_by_state(list_of_dictionaries, state="EXECUTED"))


def sort_by_date(sorted_list: list):
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(sorted_list, key=lambda x: x["date"], reverse=True)


print(sort_by_date(list_of_dictionaries))
