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