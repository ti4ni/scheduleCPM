import pymysql

try:  # Подключение к бд
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
                bd_selected_lesson1 = f"SELECT `{lesson1}` FROM `класс` WHERE `Класс` = '{klass}';"  # 1 урок из БД
                bd_selected_lesson2 = f"SELECT `{lesson2}` FROM `класс` WHERE `Класс` = '{klass}';"  # 2 урок из БД
                cursor.execute(bd_selected_lesson1)
                selected_lesson1 = str(cursor.fetchall()).replace("(('", "").replace("',),)", "")  # 2 урок из БД в виде
                # строки
                cursor.execute(bd_selected_lesson2)
                selected_lesson2 = str(cursor.fetchall()).replace("(('", "").replace("',),)", "")  # 2 урок из БД в виде
                # строки
                switching_lessons1 = f"UPDATE класс SET `{lesson1}` = '{selected_lesson2}' WHERE `Класс` = '{klass}';"
                cursor.execute(switching_lessons1)  # SQL запрос на смену 1 урока
                switching_lessons2 = f"UPDATE класс SET `{lesson2}` = '{selected_lesson1}' WHERE `Класс` = '{klass}';"
                cursor.execute(switching_lessons2)  # SQL запрос на смену 2 урока
                connection.commit()

        finally:  # Закрываем подключение к базе данных
            connection.close()
    switching("Понедельник2", "Понедельник3", "9Д")  # Вызываем функцию

except Exception as ex:  # Вывод ошибок
    print(ex)
