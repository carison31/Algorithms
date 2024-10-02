# Динамическое программирование
## 1. Введение
### 1.1 Предисловие
Динамическое программирование — один из наиболее мощных и изящных инструментов в арсенале программиста. Оно позволяет находить оптимальные решения для задач, которые, на первый взгляд, кажутся слишком сложными для решения стандартными методами. Ключевая сила этого подхода заключается в ***разбиении сложных проблем на более простые подзадачи***, а затем в эффективном использовании уже найденных решений для ускорения вычислений.

Этот **учебный материал** - заметки/шпаргалка для изучения динамического программирования и решения задач.

## 2. Наглядное применение динамического программирования.
В этой главе поговорим о главной идее динамического программирования, а именно разделение сложной главной задачи- цели на много- много подзадач, для которых результат одной подзадачи вытекает из результата другой подзадачи. Также поговорим о мемоизации - подход, позволяющий во много раз снизить число итераций, следовательно ускорить время работы.

### 2.1 Числа Фибоначчи.
Напомню, что числа Фибоначчи это последовательность такого вида: 1, 1, 2, .., F(n) + F(n+1). Где функция F(n) - это значение n- го члена последовательности:
<img width="409" alt="image" src="https://github.com/user-attachments/assets/738f6990-5eac-4818-a5a5-0da5abdf9cb9">
```
def fibRecursive(n):
  if n <= 2:
    return 1
  else:
    return fibRecursive(n-1) + fibRecursive(n-2)
```


## 3. Примеры классических задач
### 3.1 Задача о размене монеты

-Задача о размене монеты решенная методом динамического программирования (money_change.py)
-Задача о примитивном калькуляторе методом рекурсии и динамического программирования (calc.py)
