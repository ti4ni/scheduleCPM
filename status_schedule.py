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


    def status(prepod, team, classroom, day):
        try:
            with connection.cursor() as cursor:

                pre_audience = f"SELECT `{day}` FROM `аудитория` WHERE `Номер` = '{classroom}';"  # Проверка на то, не
                # Занята ли аудитория в это время. Сюда нужно прикрутить проверку на вместимость класса в кабинет
                cursor.execute(pre_audience)
                audiences = cursor.fetchall()
                for aud in audiences:
                    server_audiences = json.dumps(aud)  # кривая строка
                    normal_audiences = json.loads(server_audiences)  # массив с нормальной строкой
                audience = normal_audiences[0]  # нормальная строка

                pre_klass = f"SELECT `{day}` FROM `класс` WHERE `класс` = '{team}';"  # Проверка на то, нет ли у класса
                # Занятия в это время
                cursor.execute(pre_klass)
                klasses = cursor.fetchall()
                for klas in klasses:
                    server_klasses = json.dumps(klas)  # кривая строка
                    normal_klasses = json.loads(server_klasses)  # массив с нормальной строкой
                klass = normal_klasses[0]  # нормальная строка

                pre_teacher = f"SELECT `{day}` FROM `преподаватель` WHERE `ФИО` = '{prepod}';"
                # Проверка на то, не занят ли учитель в это время. Необходимо прикрутить проверку на то, может ли он в
                # Принципе в это время. Необходимо создать отдельную таблицу с ФИО учителей и занятостями по паре
                # (понедельник1 и тд)
                cursor.execute(pre_teacher)
                teachers = cursor.fetchall()
                for teach in teachers:
                    server_teachers = json.dumps(teach)  # кривая строка
                    normal_teachers = json.loads(server_teachers)  # массив с нормальной строкой
                teacher = normal_teachers[0]  # нормальная строка

                if (audience is None) and (klass is None) and (teacher is None):
                    return "1"
                else:
                    return "0"

        finally:  # закрываем подключение
            connection.close()


    print(status("Пустовит Егор Константинович", "11Л", "310", "Понедельник1"))

except Exception as ex:  # вывод ошибок
    print(ex)
