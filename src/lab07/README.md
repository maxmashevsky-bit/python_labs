

# Лабораторная работа №7
## Установка зависимостей
```bash
pip install black pytest pytest-cov
```
## Запуск тестов
### Тесты для `text.py`
```bash
py -m pytest tests/test_text.py -v
```
**Тестируемые функции:**

* `normalize()` — нормализация текста
* `tokenize()` — токенизация текста
* `count_freq()` — подсчёт частот слов
* `top_n()` — топ-N частых слов

**Вывод консоли:**
![image1.jpg](misc/img/lab07/image1.jpg)

---

### Тесты для `json_csv.py`

```bash
py -m pytest tests/test_json_csv.py -v
```

**Тестируемые функции:**

* `json_to_csv()` — конвертация JSON → CSV
* `csv_to_json()` — конвертация CSV → JSON

**Вывод консоли:**
![image2.jpg](misc/img/lab07/image2.jpg)

---

## Результаты покрытия кода

```bash
py -m pytest --cov=src --cov-report=term-missing
```

**Покрытие:**

* `src/lib/text.py` — **95%**
* `src/lab05/json_csv.py` — **81%**

**Вывод консоли:**
![image3.jpg](misc/img/lab07/image3.jpg)

---

## Проверка стиля кода

```bash
py -m black .
py -m black --check .
```

**Вывод консоли:**
![image4.jpg](misc/img/lab07/image4.jpg)
