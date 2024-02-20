#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def command_list(students):
    if students:
                print("Список студентов с успеваемостью больше 4.0")
                # Заголовок таблицы.
                line = '+-{}-+-{}-+-{}-+'.format(
                    '-' * 4,
                    '-' * 30,
                    '-' * 20
                )
                print(line)
                print(
                    '| {:^4} | {:^30} | {:^20} |'.format(
                        "No",
                        "Ф.И.О.",
                        "Группа"
                    )
                )
                print(line)

                # Вывести данные о всех сотрудниках.
                for idx, student in enumerate(students, 1):
                    print(
                        '| {:>4} | {:<30} | {:<20} |'.format(
                            idx,
                            student.get('name', ''),
                            student.get('group', '')
                        ) 
                    )

                print(line)
    
    else:
                print("Студентов с успеваемостью выше 4.0 нет")