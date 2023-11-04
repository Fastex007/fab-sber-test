"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total
time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is
the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

https://www.codewars.com/kata/57b06f90e298a7b53d000a86

Пояснение:
# Инициализируем массив размером n для представления касс
# Перебираем каждого покупателя в очереди
# Находим кратчайшую очередь, найдя минимальное значение в массиве tills
# Добавляем время оформления покупателя в кратчайшую очередь
# Возвращаем максимальное значение в массиве tills, которое представляет общее время,
необходимое для оформления всех покупателей
"""

from typing import List


def queue_time(customers: List[int], n: int) -> int:
    tills = [0] * n
    for one in customers:
        shortest_queue = min(tills)
        short_index = tills.index(shortest_queue)
        tills[short_index] += one
    return max(tills)
