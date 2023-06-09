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


    def replacing(original, new, klass):
        try:
            with connection.cursor() as cursor:  # Заменить конкретную пару в расписании. Все работает, осталось лишь
                # передавать значения в переменную (сейчас стоят тестовые)
                replace_lesson = f"UPDATE `класс` SET `{original}` = '{new}' WHERE `Класс` = '{klass}';"
                cursor.execute(replace_lesson)
                connection.commit()

        finally:  # закрываем подключение
            connection.close()


    replacing("Понедельник2", "Алгебра", "9Д")

except Exception as ex:  # вывод ошибок
    print(ex)
