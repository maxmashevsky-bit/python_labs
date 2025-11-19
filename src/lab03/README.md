
# Лабораторная работа 3
### Задание 1:
```python
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    if casefold == True:
        result = result.casefold()    
    if yo2e == True:
        result = result.replace('ё', 'е').replace('Ё', 'е')
    for char in ['\t', '\r', '\n']:
        result = result.replace(char, ' ')
    result = re.sub(r'\s+', ' ', result).strip()
    return result

def tokenize(text: str) -> list[str]:
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    frequency_dict = {}
    for token in tokens:
        frequency_dict[token] = frequency_dict.get(token, 0) + 1
    return frequency_dict

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка")) 
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

# print(tokenize("привет мир" ))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год" ))
# print(tokenize("emoji 😀 не слово" ))

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb", "aa", "bb", "aa", "cc"]))

# freq1 = {"a": 3, "b": 2, "c": 1}
# print(top_n(freq1, 2))
# freq2 = {"bb": 2, "aa": 2, "cc": 1}
# print(top_n(freq2, 2))
```
Результат выполнения:

![001.jpg](misc/img/lab03/001.jpg)
### Задание 2:
```python
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.pt1 import normalize, tokenize, count_freq, top_n

def main() -> None:
    text = sys.stdin.read().strip()

    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()

"""
1. Сначала вставляешь в терминал  python3 src/lab03/text_stats.py
2. Затем втсавляешь текст, то есть Привет, мир! Привет!!!
3. Потом клавишами CTRL+D
"""
```
Результат выполнения:
![002.jpg](misc/img/lab03/002.jpg)