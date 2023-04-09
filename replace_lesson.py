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

    try:
        with connection.cursor() as cursor:  # Заменить конкретную пару в расписании. Но тут нужно добавить, какую
            # Именно пару мы изменяем. В качестве примера, я тут руками поставил 1 пару в понедельник
            replace_lesson = f"UPDATE `класс` SET `Понедельник1`='Русский язык';"
            cursor.execute(replace_lesson)
            connection.commit()

    finally:  # закрываем подключение
        connection.close()

except Exception as ex:  # вывод ошибок
    print(ex)
