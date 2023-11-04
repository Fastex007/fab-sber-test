"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element,
traveling clockwise.

https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

Пояснение:
# Проверяем, если array пустой список, то возвращаем пустой список result.
# Пока в исходном массиве есть элементы добавляем первую строку массива в конец списка result.
    Таким образом обходим массив по верхней границе.
    Преобразуем входном массив в список кортежей, разворачиваем массив в обратную сторону.
    Таким образом обходим правую границу массива
"""

from typing import List


def snail(array: List[List]) -> List[int]:
    result = list()
    if not array:
        return result
    while len(array):
        result.extend(array.pop(0))
        array = list(zip(*array))[::-1]
    return result
