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
                        day = "'" + day_main + str(k) + "'"
                        days.append(day)
                        k += 1
                zip_result = zip(days, lessons)  # Попарное объединение элементов из списка дней с элементами из списка
                # уроков
                for i in zip_result:
                    pairs = (":".join(i)).replace('"', "")
                    list_result.append(pairs)
                    pre_result = str(list_result).replace("[", "{").replace("]", "}")  # Итоговая строка
                    result = pre_result.replace('"', '')  # Осталось это переписать в цикл

                lessons = ["Разговоры о важном", "Биология", "Математика", "Искусство", "Литература", "Английский язык",
                           "География", "Русский язык", "Технология", "Физическая культура", "История",
                           "Общая и неорганическая химия", "Биология (доп. главы)", "Физика",
                           "Олимпиадный практикум по истории", "Обществознание", "Искусство (МХК)",
                           "Олимпиадный практикум по литература", "Олимпиадный практикум по русскому языку",
                           "Информатика", "Практикум по математике", "Факультатив по информатике",
                           "Физика (доп. главы)", "Химия", "Физический практикум",
                           "Математика: выполнение задач повышенной сложности",
                           "Олимпиадный практикум по обществознанию", "Решение экономических задач",
                           "Экономика (доп. главы)", "Биология (доп.образование)", "Химия (подготовка к ОГЭ)",
                           "Биология (подготовка к ОГЭ)", "Олимпиадный практикум по литературе", "Страноведение",
                           "Математика: решение задач повышенной сложности", "История языка", "Физика гр. 2",
                           "Физика гр. 1", "Математический анализ", "Астрономия", "Ботаника высших растений",
                           "Зоология беспозвоночных", "Устойчивое развитие", "Прикладная экология",
                           "Индивидуальный проект", "История отечественной культуры", "Всеобщая история",
                           "Искусство (МХК) (доп. главы)", "Зарубежная литература", "Математика (подготовка к ЕГЭ)",
                           "Анализ данных", "Социология", "Создание и анализ академического текста", "Право",
                           "Экономика (доп. главы)", "Химия гр. 1", "Физическая химия гр. 1", "Химия гр. 2",
                           "Физическая химия гр. 2", "Физический практикум гр. 2", "Физический практикум гр. 1",
                           "Биоэкология", "Политология", "Риторика и академический текст", "История идей",
                           "Межпредметные квалификации", "Правовая грамотность", "Английский язык гр. 2",
                           "Основы программирования (ППО)", "Английский язык гр. 1", "Уроки критического мышления",
                           "История политических учений", "Философия и логика", "Методы социальных исследований",
                           "Государственная власть", "Профориентационный семинар", "Философия и логика",
                           "История экономики и экономической мысли", "Культурология и МХК",
                           "История русской культуры", "Историко-литературный курс",
                           "ТГП и историко-юридический практикум", "Математика гр. 2", "Математика гр. 3",
                           "Математика гр. 1", "Экономика (доп. образование)", "История (доп.главы)",
                           "Олимпиадная математика", "Органическая химия", "Неорганическая химия", "Физическая химия",
                           "Сложная органическая химия", "История (доп.образование)", "Обществознание (доп.главы)"]
                # Это все виды уроков, которые есть в ЦПМ

                for les in lessons:
                    if les in result:
                        result = result.replace(les, "'" + les + "'")
                return result  # Преобразование в строку по типу JSON

        finally:  # закрываем подключение
            connection.close()


    print(show("11Л"))

except Exception as ex:  # вывод ошибок
    print(ex)
