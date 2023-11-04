"""
The goal of this exercise is to convert a string to a new string where each character in the new string
is "(" if that character appears only once in the original string, or ")" if that character appears more than once
in the original string. Ignore capitalization when determining if a character is a duplicate.

https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

Пояснение:
# Производится обход каждого символа из входной строки, которая переведена в нижний регистр
# Проверяем наличие текущего символа в словаре result, если нет, то добавляем (, или ), если есть
# Проходим еще раз по всей входной строке и получаем значения из словаря,
# объединяем их в единую строку, и результат отдаем
"""


SINGLE_CHAR = "("
MULTIPLE_CHAR = ")"


def duplicate_encode(word: str) -> str:
    result = dict()
    for char in word.lower():
        if char not in result:
            result[char] = SINGLE_CHAR
        else:
            result[char] = MULTIPLE_CHAR
    return "".join([result[one] for one in word.lower()])
