import pulp

# 1.Формулювання задачі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# 2.Визначення змінних
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# 3.Цільова функція: максимізація виробництва напоїв
model += lemonade + fruit_juice, "Total Production"

# Обмеження
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar Constraint"
model += 1 * lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# 4.Розвʼязання задачі
model.solve()

# 5.Аналіз результатів
print("Max volume of Lemonade:", lemonade.varValue)
print("Max volume of Fruit Juice:", fruit_juice.varValue)
print("Total volume of produced drinks", pulp.value(model.objective))