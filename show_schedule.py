import pymysql
import json

try:  # подключение к бд
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        charset="utf8",
        database="schedulecpm",
    )

    try:
        with connection.cursor() as cursor:  # Показ расписания для определённого класса на всю неделю. Оно работает
            # Нормально, но я тут вручную класс выставил. Нужно прикрутить, чтобы можно было как-то вводить, какой
            # конкретно класс нужен. И выводит оно без кодировки, нужной для русского языка в json
            show_class = f"SELECT `Понедельник1`, `Понедельник2`, `Понедельник3`, `Понедельник4`, `Понедельник5`, " \
                         f"`Вторник1`, `Вторник2`, `Вторник3`, `Вторник4`, `Вторник5`, `Среда1`, `Среда2`, `Среда3`, " \
                         f"`Среда4`, `Среда5`, `Четверг1`, `Четверг2`, `Четверг3`, `Четверг4`, `Четверг5`, `Пятница1`,"\
                         f"`Пятница2`, `Пятница3`, `Пятница4`, `Пятница5`, `Суббота1`, `Суббота2`, `Суббота3`, " \
                         f"`Суббота4`, " \
                         f"`Суббота5` FROM `класс` WHERE `Класс` = '11Л';"
            cursor.execute(show_class)
            rows = cursor.fetchall()
            for row in rows:
                server_json = json.dumps(row)
                normal_json = json.loads(server_json)
            monday_1 = normal_json[0]  # это переменные, в которых хранятся названия пар, соответствующие названиям
            monday_2 = normal_json[1]
            monday_3 = normal_json[2]
            monday_4 = normal_json[3]
            monday_5 = normal_json[4]
            tuesday_1 = normal_json[5]
            tuesday_2 = normal_json[6]
            tuesday_3 = normal_json[7]
            tuesday_4 = normal_json[8]
            tuesday_5 = normal_json[9]
            wednesday_1 = normal_json[10]
            wednesday_2 = normal_json[11]
            wednesday_3 = normal_json[12]
            wednesday_4 = normal_json[13]
            wednesday_5 = normal_json[14]
            thursday_1 = normal_json[15]
            thursday_2 = normal_json[16]
            thursday_3 = normal_json[17]
            thursday_4 = normal_json[18]
            thursday_5 = normal_json[19]
            friday_1 = normal_json[20]
            friday_2 = normal_json[21]
            friday_3 = normal_json[22]
            friday_4 = normal_json[23]
            friday_5 = normal_json[24]
            saturday_1 = normal_json[25]
            saturday_2 = normal_json[26]
            saturday_3 = normal_json[27]
            saturday_4 = normal_json[28]
            saturday_5 = normal_json[29]

            l1 = [monday_1, monday_2, monday_3, monday_4, monday_5, tuesday_1, tuesday_2, tuesday_3, tuesday_4,
                  tuesday_5,
                  wednesday_1, wednesday_2, wednesday_3, wednesday_4, wednesday_5, thursday_1, thursday_2, thursday_3,
                  thursday_4,
                  thursday_5, friday_1, friday_2, friday_3, friday_4, friday_5, saturday_1, saturday_2, saturday_3,
                  saturday_4,
                  saturday_5]  # собираем все пары за целый день в единый список
            l2 = ["monday_1", "monday_2", "monday_3", "monday_4", "monday_5", "tuesday_1", "tuesday_2", "tuesday_3",
                  "tuesday_4",
                  "tuesday_5", "wednesday_1", "wednesday_2", "wednesday_3", "wednesday_4", "wednesday5_", "thursday_1",
                  "thursday_2", "thursday_3", "thursday_4", "thursday_5", "friday_1", "friday_2", "friday_3",
                  "friday_4",
                  "friday_5", "saturday_1", "saturday_2", "saturday_3", "saturday_4", "saturday_5"]
            result = {l2[i]: l1[i] for i in range(len(l2))}  # тут нужно добавить decoding для русского языка
            json_show_class = json.dumps(result)  # это результат показа, упакованный в json

    finally:  # закрываем подключение
        connection.close()

except Exception as ex:  # вывод ошибок
    print(ex)
