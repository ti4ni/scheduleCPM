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


    def switching(lesson1, lesson2, klass):
        try:
            with connection.cursor() as cursor:  # Смена двух пар местами между собой. Все работает, осталось лишь
                # передавать значения в переменную (сейчас стоят тестовые)
                selected_lesson1 = f"SELECT `{lesson1}` FROM `класс`;"
                selected_lesson2 = f"SELECT `{lesson2}` FROM `класс`;"
                cursor.execute(selected_lesson1)
                str_selected_lesson1 = str(cursor.fetchall())
                cursor.execute(selected_lesson2)
                str_selected_lesson2 = str(cursor.fetchall())
                pre_done_selected_lesson1 = str_selected_lesson1.replace("(('", "")
                pre_done_selected_lesson2 = str_selected_lesson2.replace("(('", "")
                done_selected_lesson1 = pre_done_selected_lesson1.replace("',),)", "")  # значение в виде строки из
                # Понедельник1 из БД
                done_selected_lesson2 = pre_done_selected_lesson2.replace("',),)", "")  # значение в виде строки из
                # Понедельник2 из БД
                switching_lessons1 = f"UPDATE класс SET `{lesson1}` = '{done_selected_lesson2}' WHERE `Класс` = '{klass}';"
                cursor.execute(switching_lessons1)
                switching_lessons2 = f"UPDATE класс SET `{lesson2}` = '{done_selected_lesson1}' WHERE `Класс` = '{klass}';"
                cursor.execute(switching_lessons2)
                connection.commit()

        finally:  # закрываем подключение
            connection.close()
    switching("Понедельник1", "Понедельник2", "11Л")

except Exception as ex:  # вывод ошибок
    print(ex)
