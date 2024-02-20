#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from commands import *


if __name__ == '__main__':
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            students = command_add.command_add()
        elif command == 'list':
            command_list.command_list(students)
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
