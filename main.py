"""
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#Вариант 15: F(0) = 1, F(1) = 1, F(n) = (-1)n*(2*F(n–1)/n! + F(n-2)), при n > 1
"""

import timeit
import matplotlib.pyplot as plt

factorial_cache = {0: 1, 1: 1}
F_cache = {0: 1, 1: 1}

def dynamic_factorial(n):
    if n not in factorial_cache:
        factorial_cache[n] = n * dynamic_factorial(n-1)
    return factorial_cache[n]

def recursive_F(n):
    if n in F_cache:
        return F_cache[n]
    else:
        result = (-1)**n * (2 * recursive_F(n-1) / dynamic_factorial(n) + recursive_F(n-2))
        F_cache[n] = result
        return result

def iterative_F(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    F_n_minus_2 = 1
    F_n_minus_1 = 1
    F_n = 0
    for i in range(2, n + 1):
        F_n = (-1)**i * (2 * F_n_minus_1 / dynamic_factorial(i) + F_n_minus_2)
        F_n_minus_2, F_n_minus_1 = F_n_minus_1, F_n
    return F_n

def score_time(func, n):
    return timeit.timeit(lambda: func(n), number=100)

n_values = range(0, 10)
recursive_times = []
iterative_times = []

for n in n_values:
    recursive_times.append(score_time(recursive_F, n))
    iterative_times.append(score_time(iterative_F, n))

print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}")
for i, n in enumerate(n_values):
    print(f"{n:<10}{recursive_times[i]:<25}{iterative_times[i]:<25}")

plt.plot(n_values, recursive_times, label='Рекурсивно')
plt.plot(n_values, iterative_times, label='Итерационно')
plt.xlabel('n')
plt.ylabel('Время (в миллисекундах)')
plt.legend()
plt.title('Сравнение времени вычисления функции F(n)')
plt.show()
