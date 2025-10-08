<h1>Python_Labs</h1>

# Лабораторная работа 1
### Задание 1:

Программа выводит простое приветствие в консоль.
```python
name = input()
age =int(input())
age1 = age +1
print('Имя:',name)
print('Возраст:',age)
print(f'Привет, {name}! Через год тебе будет {age1} лет.')
```
Результат выполнения:

![1.jpg](misc/img/lab01/1.jpg)

### Задание 2: 

```python
a = (input("a: ")).replace(",",".")
b = (input("b: ")).replace(",",".")
print(f"sum={round(float(a)+float(b), 2)}; avg={round((float(a)+float(b))/2, 2)}")
```
Результат выполнения:

![2.png](misc/img/lab01/2.png)

### Задание 3: 
```python

price = int(input())
discount = int(input())
vat = int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽")
print(f"НДС:               {vat_amount:.2f} ₽")
print(f"Итого к оплате:    {total:.2f} ₽")
```
Результат выполнения:

![3.jpg](misc/img/lab01/3.jpg)

### Задание 4: 
```python

m = int(input())
h = m//60
print(f"{h}:{(m-60*h):02d}")
```
Результат выполнения:

![4.png](misc/img/lab01/4.png)

### Задание 5:
```python
f = input("ФИО: ")
fio = f.strip()
c = fio.split()
с1 =  sum(len(w) for w in c)
i = "".join(p[0].upper() for p in c) + "."
print("Инициалы:", i)
print("Длина (символов):",с1+2)
```
Результат выполнения:

![5.jpg](misc/img/lab01/5.jpg)

# Лабораторная работа 2
### Задание 1:

```python
def mnmx(nums: list[float | int]):
    if not nums:  
        print('Value Error')
        return None  
    mn = min(nums)
    mx = max(nums)
    return (mn, mx)
    
def unique_sorted (nums: list[float | int]):
    return list( sorted( set(nums)))

def flatten(mat: list[list | tuple]):
    flattened_list = []
    for row in mat:
        if isinstance(row, (list, tuple)):
            flattened_list.extend(row)
        else:
            raise TypeError
    return flattened_list
```
Результат выполнения:

![image1.png](misc/img/lab02/image1.png)

### Задание 2:
```python
def transpose(mat: list[list[float | int]]):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    for row in mat:
        if len(row)!=cols:
            raise ValueError
    teleport_mat = [[mat[i][j] for i in range(rows)] for j in range(cols)]
    return teleport_mat
print(transpose([[1, 2, 3]]))
print(transpose([[1],[2], [3]]))
print(transpose([[1,2],[3,4]]))
print(transpose([[1,2],[3]]))
print(transpose([[]]))

def row_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError
    sums=[sum(row) for row in mat]
    return sums
print(row_sums([[1,2,3], [4,5,6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1,2], [3]])) 

def col_sums(mat: list[list[float | int]]):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError     
    sums = []
    for j in range(cols):
        column_sum = 0
        for i in range(rows):
            column_sum += mat[i][j]
        sums.append(column_sum)    
    return sums

print(col_sums([[1, 2, 3], [4, 5, 6]]))  
print(col_sums([[-1, 1], [10, -10]]))    
print(col_sums([[0, 0], [0, 0]]))        
print(col_sums([[1, 2], [3]]))  
```
Результат выполнения:

![imagge2.1.jpg](misc/img/lab02/imagge2.1.jpg)
![imagge2.2.jpg](misc/img/lab02/imagge2.2.jpg)
![imagge2.3.jpg](misc/img/lab02/imagge2.3.jpg)


### Задание 3:
```python
def format_record(rec: tuple[str, str, float]):
    if not isinstance(rec, tuple):
        raise TypeError(f"Ожидается tuple, получен {type(rec).__name__}")
    if len(rec) != 3:
        raise ValueError(f"Ожидается кортеж из 3 элементов, получено {len(rec)}")
    fio, group, gpa = rec
    if not isinstance(fio, str):
        raise TypeError(f"ФИО должен быть строкой, получен {type(fio).__name__}")
    if not isinstance(group, str):
        raise TypeError(f"Группа должна быть строкой, получен {type(group).__name__}")
    if not isinstance(gpa, (int, float)):
        raise TypeError(f"GPA должен быть числом, получен {type(gpa).__name__}")
    if gpa < 0 or gpa > 5:
        raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено {gpa}")
    parts = fio.strip().split()
    family = parts[0]
    initials = ""
    for part in parts[1:]:
        initials += part[0].upper() + "."
    if not initials:
        initials = ""
    form_gpa = f"{gpa:.2f}"
    return f"{family} {initials}, гр. {group}, GPA {form_gpa}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
Результат выполнения:

![image3.jpg](misc/img/lab02/image3.jpg)
