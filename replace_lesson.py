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
            with connection.cursor() as cursor:  # Заменить конкретную пару в расписании. Осталось лишь передавать
                # Значения в переменную. А так - оно полностью работает. Для примера поставил "Понедельник1", 
                # "Алгебра", "11Л
                replace_lesson = f"UPDATE `класс` SET `{original}` = '{new}' WHERE `Класс` = '{klass}';"
                cursor.execute(replace_lesson)
                connection.commit()

        finally:  # закрываем подключение
            connection.close()

    replacing("Понедельник1", "Алгебра", "11Л")

except Exception as ex:  # вывод ошибок
    print(ex)
