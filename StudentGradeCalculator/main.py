name = ""
surname = ""
age = 0
grades = []
profile_created = False

while True:
    print("\033[32m----- Калькулятор для оценивания студентна -----\033[0m")
    print("\033[36m1. Ввести данные студента\033[0m")
    print("\033[36m2. Добавить оценку\033[0m")
    print("\033[36m3. Показать все оценки\033[0m")
    print("\033[36m4. Рассчитать итоговый результат\033[0m")
    print("\033[36m5. Выход\033[0m")

    choice = input("Выберите пункт меню: ").strip()

    if choice == "1":
        while True:
            new_name = input("Введите имя: ").strip()
            if new_name == "":
                print("\033[31mОшибка: имя не может быть пустым.\033[0m")
            else:
                break
        while True:
            new_surname = input("Введите фамилию: ").strip()
            if new_surname == "":
                print("\033[31mОшибка: фамилия не может быть пустой.\033[0m")
            else:
                break
        while True:
            new_age = input("Введите возраст (5-100): ").strip()
            is_number = True
            for i in new_age:
                if i not in "0123456789":
                    is_number = False
            if new_age == "":
                is_number = False
            if not is_number:
                print("\033[31mОшибка: возраст должен быть целым положительным числом.\033[0m")
            else:
                new_age = int(new_age)
                if new_age < 5 or new_age > 100:
                    print("\033[31mОшибка: возраст должен быть от 5 до 100.\033[0m")
                else:
                    break

        name = new_name
        surname = new_surname
        age = new_age
        grades = []
        profile_created = True
        print("\033[32mПрофиль создан. Прежние оценки удалены.\033[0m")

    elif choice == "2":
        if not profile_created:
            print("\033[31Сначала создайте профиль студента (пункт 1).\033[0m")
        else:
            while True:
                grade_text = input("Введите оценку (0-100): ").strip()
                is_number = True
                for i in grade_text:
                    if i not in "0123456789":
                        is_number = False
                if grade_text == "":
                    is_number = False
                if not is_number:
                    print("\033[31mОшибка: оценка должна быть целым числом.\033[0m")
                else:
                    grade = int(grade_text)
                    if grade < 0 or grade > 100:
                        print("\033[31mОшибка: оценка должна быть от 0 до 100.")
                    else:
                        break
            grades.append(grade)
            print("\033[32mОценка добавлена.\033[0m")

    elif choice == "3":
        if not profile_created:
            print("\033[31mСначала создайте профиль студента (пункт 1).\033[0m")
        elif len(grades) == 0:
            print("Оценок пока нет.")
        else:
            print("Оценки студента:")
            for i in range(len(grades)):
                print(str(i + 1) + ". " + str(grades[i]))

    elif choice == "4":
        if not profile_created:
            print("\033[31mСначала создайте профиль студента (пункт 1).\033[0m")
        elif len(grades) == 0:
            print("\033[31mНельзя сформировать отчёт без оценок.\033[0m")
        else:
            count = len(grades)
            average = sum(grades) / count
            highest = max(grades)
            lowest = min(grades)

            if average >= 90:
                category = "A"
                description = "Отлично"
            elif average >= 80:
                category = "B"
                description = "Хорошо"
            elif average >= 70:
                category = "C"
                description = "Удовлетворительно"
            elif average >= 60:
                category = "D"
                description = "Слабо"
            else:
                category = "F"
                description = "Неудовлетворительно"

            if average >= 60:
                status = "Сдал"
            else:
                status = "Не сдал"

            print()
            print("========== ОТЧЁТ ==========")
            print("ФИО: " + name + " " + surname)
            print("Возраст: " + str(age))
            print("Оценки: " + str(grades))
            print("Количество оценок: " + str(count))
            print("Средний балл: " + format(average, ".2f"))
            print("Максимальная оценка: " + str(highest))
            print("Минимальная оценка: " + str(lowest))
            print("Категория: " + category + " (" + description + ")")
            print("Статус: " + status)
            if average >= 90:
                print("\033[32mОтличник!\033[0m")
            print("\033[32m===========================\033[0m")

    elif choice == "5":
        print("\033[32mДо свидания!\033[0m")
        break