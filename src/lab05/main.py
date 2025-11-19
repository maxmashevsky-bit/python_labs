from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx, xlsx_to_csv
import os
import sys


def validate_paths(in_path: str, out_path: str) -> None:
    """
    Проверяет корректность путей для конвертации.
    
    Args:
        in_path (str): Входной файл
        out_path (str): Выходной файл
        
    Raises:
        ValueError: Если пути совпадают или форматы одинаковые
    """
    if os.path.abspath(in_path) == os.path.abspath(out_path):
        raise ValueError("Нельзя конвертировать файл в самого себя!")
    
    in_ext = os.path.splitext(in_path)[1].lower()
    out_ext = os.path.splitext(out_path)[1].lower()
    
    if in_ext == out_ext:
        raise ValueError(
            f"Нельзя конвертировать {in_ext} в {out_ext} - одинаковые форматы!"
        )


def convert_json_csv() -> None:
    """Конвертирует JSON в CSV"""
    validate_paths(base + 'people.json', out + 'people.csv')
    json_to_csv(base + 'people.json', out + 'people.csv')


def convert_csv_json() -> None:
    """Конвертирует CSV в JSON"""
    validate_paths(base + 'people.csv', out + 'people.json')
    csv_to_json(base + 'people.csv', out + 'people.json')


def convert_csv_xlsx() -> None:
    """Конвертирует CSV в XLSX"""
    validate_paths(base + 'cities.csv', out + 'cities.xlsx')
    csv_to_xlsx(base + 'cities.csv', out + 'cities.xlsx')


def convert_xlsx_csv() -> None:
    """Конвертирует XLSX в CSV"""
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