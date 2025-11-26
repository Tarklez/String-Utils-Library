# string_utils.py

def reverse_string(s):
    """Переворачивает строку без использования срезов"""
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

def capitalize_string(s):
    """Делает первую букву заглавной"""
    if not s:
        return ""
    # Получаем код первого символа
    first_char_code = ord(s[0])
    # Если это маленькая буква (a-z)
    if 97 <= first_char_code <= 122:
        first_char = chr(first_char_code - 32)  # Преобразуем в заглавную
    else:
        first_char = s[0]
    return first_char + s[1:]

def strip_string(s):
    """Удаляет пробелы в начале и конце строки"""
    if not s:
        return ""
    
    # Находим первый непробельный символ
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    # Находим последний непробельный символ
    end = len(s) - 1
    while end >= 0 and s[end] == ' ':
        end -= 1
    
    # Если вся строка из пробелов
    if start > end:
        return ""
    
    return s[start:end + 1]

def count_chars(s, char):
    """Считает количество вхождений символа в строку"""
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом (игнорируя пробелы и регистр)"""
    # Очищаем строку от пробелов и приводим к нижнему регистру
    cleaned = to_lower_case(s)
    cleaned_without_spaces = ""
    for char in cleaned:
        if char != ' ':
            cleaned_without_spaces += char
    
    # Проверяем палиндром
    return cleaned_without_spaces == reverse_string(cleaned_without_spaces)

def replace_char(s, old_char, new_char):
    """Заменяет все вхождения одного символа на другой"""
    result = ""
    for c in s:
        if c == old_char:
            result += new_char
        else:
            result += c
    return result

def to_lower_case(s):
    """Преобразует строку в нижний регистр"""
    result = ""
    for c in s:
        char_code = ord(c)
        # Если это заглавная буква (A-Z)
        if 65 <= char_code <= 90:
            result += chr(char_code + 32)  # Преобразуем в маленькую
        else:
            result += c
    return result

def to_upper_case(s):
    """Преобразует строку в верхний регистр"""
    result = ""
    for c in s:
        char_code = ord(c)
        # Если это маленькая буква (a-z)
        if 97 <= char_code <= 122:
            result += chr(char_code - 32)  # Преобразуем в заглавную
        else:
            result += c
    return result

def split_string(s, delimiter=' '):
    """Разделяет строку по разделителю"""
    if not s:
        return [""]
    
    result = []
    current = ""
    
    for char in s:
        if char == delimiter:
            result.append(current)
            current = ""
        else:
            current += char
    
    result.append(current)
    return result