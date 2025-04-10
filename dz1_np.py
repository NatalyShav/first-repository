import numpy as np
import matplotlib.pyplot as plt

# Генерация двух массивов случайных чисел
random_array1 = np.random.rand(5)  # массив из 5 случайных чисел
random_array2 = np.random.rand(5)  # еще один массив из 5 случайных чисел

# Вывод массивов для проверки
print("Первый массив:", random_array1)
print("Второй массив:", random_array2)

# Построение диаграммы рассеяния
plt.scatter(random_array1, random_array2)
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('Случайные данные 1')
plt.ylabel('Случайные данные 2')
plt.grid(True)
plt.show()