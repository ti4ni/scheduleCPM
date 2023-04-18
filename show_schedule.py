import pymysql

try:  # подключение к бд
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        charset="utf8",
        database="schedulecpm",
    )


    def show(klass):
        try:
            with connection.cursor() as cursor:
                select = f"SELECT * FROM `класс` WHERE `Класс` = '{klass}';"  # SQL запрос
                cursor.execute(select)
                list_result = []
                lessons = str(cursor.fetchall()).replace("(('", "").replace("),)", "").replace("'", "").replace("None", "null").split(",")[2:]  # Все уроки этого класса в виде списка
                days_main = "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"  # Дни недели
                days = []
                for day_main in days_main:  # Генератор пар, учитывая дни недели
                    k = 1
                    while k != 6:
                        day = day_main + str(k) + "'"
                        days.append(day)
                        k += 1
                zip_result = zip(days, lessons)  # Попарное объединение элементов из списка дней с элементами из списка
                # уроков
                for i in zip_result:
                    pairs = (":".join(i)).replace('"', "")
                    list_result.append(pairs)
                    pre_result = str(list_result).replace("[", "{").replace("]", "}")  # Итоговая строка
                    result = pre_result.replace('"', '').replace(",", "',").replace("А", "'А").replace("Б", "'Б") \
                        .replace("В", "'В").replace("Г", "'Г").replace("Д", "'Д").replace("Е", "'Е").replace("Ё", "'Ё")\
                        .replace("Ж", "'Ж").replace("З", "'З").replace("И", "'И").replace("Й", "'Й").replace("К", "'К")\
                        .replace("Л", "'Л").replace("М", "'М").replace("Н", "'Н").replace("О", "'О").replace("П", "'П")\
                        .replace("Р", "'Р").replace("С", "'С").replace("Т", "'Т").replace("У", "'У").replace("Ф", "'Ф")\
                        .replace("Х", "'Х").replace("Ц", "'Ц").replace("Ч", "'Ч").replace("Ш", "'Ш").replace("Щ", "'Щ")\
                        .replace("Ъ", "'Ъ").replace("Ы", "'Ы").replace("Ь", "'Ь").replace("Э", "'Э").replace("Ю", "'Ю")\
                        .replace("Я", "'Я").replace("null'", "null")  # Осталось это переписать в цикл

                return result

        finally:  # закрываем подключение
            connection.close()


    show("11Л")

except Exception as ex:  # вывод ошибок
    print(ex)
