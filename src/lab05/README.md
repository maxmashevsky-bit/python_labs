<h1>Python_Labs</h1>



# Лабораторная работа 5
### csv_xlsx.py
```python
import csv
import os
import openpyxl

def validate_extension(path, ext):
    if not path.lower().endswith(ext.lower()):
        raise ValueError(f"Неверный формат: {path}. Ожидается {ext}")

def csv_to_xlsx(csv_path, xlsx_path):
    validate_extension(csv_path, '.csv')
    validate_extension(xlsx_path, '.xlsx')
    if not os.path.exists(csv_path): raise FileNotFoundError(f"CSV не найден: {csv_path}")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        data = list(csv.reader(f))
        if not data: raise ValueError("CSV файл пуст")
    
    wb = openpyxl.Workbook()
    ws = wb.active
    for row_idx, row in enumerate(data, 1):
        for col_idx, value in enumerate(row, 1):
            ws.cell(row=row_idx, column=col_idx, value=value)
    
    os.makedirs(os.path.dirname(xlsx_path), exist_ok=True)
    wb.save(xlsx_path)
    print(f"CSV -> XLSX: {xlsx_path}")

def xlsx_to_csv(xlsx_path, csv_path):
    validate_extension(xlsx_path, '.xlsx')
    validate_extension(csv_path, '.csv')
    if not os.path.exists(xlsx_path): raise FileNotFoundError(f"XLSX не найден: {xlsx_path}")
    
    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb.active
    if ws.max_row == 0 or ws.max_column == 0: raise ValueError("XLSX файл пуст")
    
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows([cell if cell is not None else '' for cell in row] for row in ws.iter_rows(values_only=True) if any(cell is not None for cell in row))
    
    print(f"XLSX -> CSV: {csv_path}")
```

### json_csv.py
```python
from pathlib import Path
import json
import csv
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../lib'))
from io_helpers import read_file, write_file, get_file_extension

def validate_extension(path: str, expected_ext: str) -> None:

    actual_ext = get_file_extension(path)
    if actual_ext != expected_ext.lower():
        raise ValueError(f"Неверный формат: {path}. Ожидается {expected_ext}")

def json_to_csv(json_path: str, csv_path: str) -> None:

    validate_extension(json_path, '.json')
    validate_extension(csv_path, '.csv')
    json_content = read_file(json_path)
    data = json.loads(json_content)
    
    if not data:
        raise ValueError("JSON файл пуст")
    
    fieldnames = list(data[0].keys())
    csv_content = []   
    csv_content.append(','.join(fieldnames))

    for item in data:
        row = [str(item.get(field, '')) for field in fieldnames]
        csv_content.append(','.join(row))
    write_file(csv_path, '\n'.join(csv_content))
    print(f"JSON -> CSV завершено: {csv_path}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    validate_extension(csv_path, '.csv')
    validate_extension(json_path, '.json')
    csv_content = read_file(csv_path)
    from io import StringIO
    csv_file = StringIO(csv_content)
    data = list(csv.DictReader(csv_file))
    
    if not data:
        raise ValueError("CSV файл пуст")
    json_content = json.dumps(data, indent=2, ensure_ascii=False)
    write_file(json_path, json_content)
    
    print(f"CSV -> JSON завершено: {json_path}")
```

### csv_xlsx.py
```python
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx, xlsx_to_csv
import os
import sys


def validate_paths(in_path: str, out_path: str) -> None:
    if os.path.abspath(in_path) == os.path.abspath(out_path):
        raise ValueError("Нельзя конвертировать файл в самого себя!")
    
    in_ext = os.path.splitext(in_path)[1].lower()
    out_ext = os.path.splitext(out_path)[1].lower()
    
    if in_ext == out_ext:
        raise ValueError(
            f"Нельзя конвертировать {in_ext} в {out_ext} - одинаковые форматы!"
        )


def convert_json_csv() -> None:
    """ JSON в CSV"""
    validate_paths(base + 'people.json', out + 'people.csv')
    json_to_csv(base + 'people.json', out + 'people.csv')


def convert_csv_json() -> None:
    """ CSV в JSON"""
    validate_paths(base + 'people.csv', out + 'people.json')
    csv_to_json(base + 'people.csv', out + 'people.json')


def convert_csv_xlsx() -> None:
    """ CSV в XLSX"""
    validate_paths(base + 'cities.csv', out + 'cities.xlsx')
    csv_to_xlsx(base + 'cities.csv', out + 'cities.xlsx')


def convert_xlsx_csv() -> None:
    """ XLSX в CSV"""
    validate_paths(base + 'cities.xlsx', out + 'cities.csv')
    xlsx_to_csv(base + 'cities.xlsx', out + 'cities.csv')


def display_menu() -> None:
    """Отображает главное меню программы"""
    print("\n" + "="*50)
    print("Конвертер файлов)".center(50))
    print("="*50)
    print("1. JSON → CSV")
    print("2. CSV → JSON")
    print("3. CSV → XLSX")
    print("4. XLSX → CSV")
    print("5. Выход")
    print("="*50)


def get_user_choice() -> str:
    """Безопасно получает выбор пользователя"""
    try:
        choice = input("Выберите действие (1-5): ").strip()
        return choice
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем. До свидания!")
        sys.exit(0)
    except EOFError:
        print("\n\nНеожиданный конец ввода. До свидания!")
        sys.exit(1)


def main() -> None:
    """Основная функция программы"""
    
    # Глобальные переменные для путей
    global base, out
    base = 'src/data/samples/'
    out = 'src/data/out/'

    try:
        while True:
            display_menu()
            choice = get_user_choice()

            if choice == '5':
                print("До свидания!")
                break

            try:
                if choice == '1':
                    convert_json_csv()
                    print("✅ Конвертация JSON → CSV завершена успешно!")
                    
                elif choice == '2':
                    convert_csv_json()
                    print("✅ Конвертация CSV → JSON завершена успешно!")
                    
                elif choice == '3':
                    convert_csv_xlsx()
                    print("✅ Конвертация CSV → XLSX завершена успешно!")
                    
                elif choice == '4':
                    convert_xlsx_csv()
                    print("✅ Конвертация XLSX → CSV завершена успешно!")
                    
                else:
                    print("❌ Неверный выбор! Введите цифру от 1 до 5")
                    
            except FileNotFoundError as e:
                print(f"❌ Файл не найден: {e}")
                
            except ValueError as e:
                print(f"❌ Ошибка валидации: {e}")
                
            except Exception as e:
                print(f"❌ Неожиданная ошибка: {e}")

            # Пауза перед следующим выбором
            if choice in ['1', '2', '3', '4']:
                input("\nНажмите Enter для продолжения...")

    except KeyboardInterrupt:
        print("\n\nПрограмма завершена. До свидания!")
    except Exception as e:
        print(f"\nКритическая ошибка: {e}")


if __name__ == "__main__":
    main()
```
![image1.jpg](misc/img/lab05/image1.jpg)
### Полученный файл
![cities_csv_1.png](misc/img/lab05/cities_csv_1.png)
### Полученный файл
![cities_xlsx_1.png](misc/img/lab05/cities_xlsx_1.png)
### Полученный файл
![people_csv_1.png](misc/img/lab05/people_csv_1.png)
### Полученный файл
![people_json_1.png](misc/img/lab05/people_json_1.png)
### Итог:
![itog.jpg](misc/img/lab05/itog.jpg)
### WEB
![image2.jpg](misc/img/lab05/image2.jpg)