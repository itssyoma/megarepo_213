#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import outer


if __name__ == "__main__":
    cnt = outer.outer()
    k = int(input("Введите значение k: "))
    result = cnt(k)
    print("Результат:", result)
