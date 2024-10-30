# Порівняння інтеграції методом Монте-Карло та функції quad

## Огляд
У цьому проєкті реалізовано обчислення визначеного інтеграла функції методом Монте-Карло. Потім результат порівнюється з інтегралом, обчисленим за допомогою аналітичного методу функції `quad` з бібліотеки SciPy. 

## Вибір функції та параметрів
Для прикладу вибрано функцію \( f(x) = \sin(x) \) з інтервалом інтегрування від 0 до \(\pi\).

## Результати експериментів
1. **Метод Монте-Карло**:
   - Інтеграл методом Монте-Карло: 2.024
   - Абсолютна похибка: 0.024

2. **Метод функції `quad`**:
   - Інтеграл функції `quad`: 2.0
   - Абсолютна похибка для методу Монте-Карло в порівнянні з функцією `quad`: близько 0.024

## Висновки
- **Точність**: Метод Монте-Карло дав результат, близький до точного значення, але з деяким відхиленням.
- **Наближення**: Точність методу Монте-Карло залежить від кількості згенерованих точок: чим більше точок, тим точніший результат.
- **Обчислювальні витрати**: Для підвищення точності Монте-Карло потрібно більше точок, що збільшує обчислювальні витрати, тоді як аналітичний метод `quad` є точним.


Висновки

Метод Монте-Карло продемонстрував результат, близький до точного значення 2.0, з невеликою абсолютною похибкою (приблизно 0.024). Це свідчить про правильність реалізації методу Монте-Карло та його здатність наближено обчислювати інтеграл. Однак, метод Монте-Карло має випадкові відхилення, які залежать від кількості згенерованих точок. У випадках із більшим числом точок точність результату буде покращуватись, хоча похибка ніколи не зникне повністю через випадкову природу цього методу.

Аналітичний метод quad забезпечує точний результат і рекомендований для використання в задачах, де необхідна висока точність і коли обчислення не є надто ресурсоємними. Метод Монте-Карло може бути корисним у ситуаціях, де аналітичний метод неможливий або важкий для реалізації, особливо при складних інтегралах або багатовимірних інтегруваннях.

Загальний висновок

Метод Монте-Карло є ефективним наближеним інструментом для обчислення інтегралів, особливо в задачах, де традиційні методи важко застосувати. Однак, коли доступні аналітичні методи, такі як quad, вони часто є більш точними і надійними.