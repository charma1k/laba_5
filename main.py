"""
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#Вариант 15: F(0) = 1, F(1) = 1, F(n) = (-1)n*(2*F(n–1)/n! + F(n-2)), при n > 1
"""

import timeit
import matplotlib.pyplot as plt

# Кэш для хранения вычисленных значений факториалов и функции F
cache_factorial = {}
cache_F = {0: 1, 1: 1}

# Рекурсивная функция для вычисления F(n)
def recursive_F(n):
    if n in cache_F:
        return cache_F[n]
    result = (-1)**n * (2 * recursive_F(n-1) / recursive_factorial(n) + recursive_F(n-2))
    cache_F[n] = result
    return result

# Итеративная функция для вычисления F(n)
def iterative_F(n):
    F = [1, 1]
    for i in range(2, n + 1):
        F.append((-1)**i * (2 * F[i-1] / iterative_factorial(i) + F[i-2]))
    return F[n]

# Динамическая функция для вычисления F(n)
def dynamic_F(n, cache=cache_F):
    if n in cache:
        return cache[n]
    result = (-1)**n * (2 * dynamic_F(n-1, cache) / dynamic_factorial(n) + dynamic_F(n-2, cache))
    cache[n] = result
    return result

# Рекурсивная функция для вычисления факториала
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

# Итеративная функция для вычисления факториала
def iterative_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Динамическая функция для вычисления факториала
def dynamic_factorial(n, cache=cache_factorial):
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    result = 1
    for i in range(2, n + 1):
        result *= i
        cache[i] = result
    return result

# Функция для измерения времени выполнения
def score_time(func, n):
    return timeit.timeit(lambda: func(n), number=1000)

# Значения n для которых мы хотим измерить время выполнения
n_values = range(1, 21)
recursive_times = []
iterative_times = []
dynamic_times = []

# Измерение времени выполнения для каждого значения n
for n in n_values:
    recursive_times.append(score_time(recursive_F, n))
    iterative_times.append(score_time(iterative_F, n))
    dynamic_times.append(score_time(dynamic_F, n))

# Вывод результатов в табличной форме
print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}{'Динамическое время (мс)':<25}")
for i, n in enumerate(n_values):
    print(f"{n:<10}{recursive_times[i]:<25}{iterative_times[i]:<25}{dynamic_times[i]:<25}")

# Построение и вывод графика результатов
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(n_values, recursive_times, label='Рекурсивно', marker='o', linewidth=2)
ax.plot(n_values, iterative_times, label='Итерационно', marker='o', linewidth=2)
ax.plot(n_values, dynamic_times, label='Динамическое', marker='o', linewidth=2)
ax.set_xlabel('n', fontsize=14)
ax.set_ylabel('Время (в миллисекундах)', fontsize=14)
ax.legend(fontsize=12)
ax.set_title('Сравнение времени вычисления функции F(n)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=12)
plt.grid(True)
plt.show()
