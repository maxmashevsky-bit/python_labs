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