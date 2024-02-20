#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def command_add():
    # Список студентов
    students = []
     # Запросить данные о студенте.
    name = input("Фамилия и инициалы? ")
    group = input("Номер группы? ")
    grade = list(map(int, input("Успеваемость студента? (Пять оценок через пробел) ").split()))
    while True:
        if len(grade) < 5:
            print("Введное количество оценок меньше 5, введите оценки еще раз: ", file=sys.stderr)
            grade = list(map(int, input("Успеваемость студента? (Пять оценок через пробел) ").split()))
        else:
            break

    # Создать словарь.
    if sum(grade)/len(grade) >= 4.0:
        student = {
            'name': name,
            'group': group,
            'grade': sum(grade)/len(grade),
        }
        # Добавить словарь в список.
        students.append(student)
    
    # Отсортировать список в случае необходимости.
    if len(students) > 1:
        students.sort(key=lambda item: item.get('name', ''))
    
    return students
