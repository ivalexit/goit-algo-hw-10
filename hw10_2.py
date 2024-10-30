import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та меж інтегрування
def f(x):
    return np.sin(x)

a = 0      # нижня межа
b = np.pi  # верхня межа 

# Обчислення інтегралу за допомогою методу Монте-Карло
def monte_carlo_integration(func, a, b, num_points=10000):
    # Генерація випадкових точок у прямокутнику [a, b] x [0, max_y]
    max_y = 1  # Максимум для sin(x) в межах [0, pi]
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, max_y, num_points)
    
    # Кількість точок, що потрапили під криву
    under_curve = np.sum(random_y < func(random_x))
    
    # Площа прямокутника і обчислення інтегралу методом Монте-Карло
    rectangle_area = (b - a) * max_y
    integral_mc = (under_curve / num_points) * rectangle_area
    return integral_mc

# Виконання інтегрування методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b, num_points=10000)

# Обчислення інтегралу за допомогою функції quad
quad_result, quad_error = spi.quad(f, a, b)

# Виведення результатів
print("Інтеграл методом Монте-Карло:", monte_carlo_result)
print("Інтеграл за допомогою функції quad:", quad_result)
print("Абсолютна похибка:", abs(monte_carlo_result - quad_result))

# Побудова графіка функції та інтегральної області
x = np.linspace(0, np.pi, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(x, y, color='gray', alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Графік інтегрування f(x) = sin(x) від 0 до π')
plt.grid()
plt.show()