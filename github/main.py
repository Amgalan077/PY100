# money = int(input('Введите стоимость за км.'))
# point1 = input('Откуда?: ')
# point2 = input('Куда?: ')
# dict_= {
#     'Дом': {'Работа': 10, 'Магазин': 50, 'Парк': 100},
#     'Работа': {'Дом': 10, 'Магазин': 40, 'Парк': 90},
#     'Магазин': {'Дом': 50, 'Работа': 40, 'Парк': 50},
#     'Парк':{'Дом': 100, 'Работа': 90, 'Магазин': 50}
# }
# print(dict_[point1.title()][point2.title()] * money,'руб.')

users = [
    {"id": 0, "name" : "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Clein"}
]
friendship = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
D = {i["id"]:[] for i in users}
for i,j in friendship:
    D[i].append(j)
    D[j].append(i)
for i,j in D.items():
    print(f'{i}:{j}')
    #sdfjasdkfjasdfjklfsdaljk;