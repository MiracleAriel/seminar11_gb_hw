# Задача: Напишите функцию, которая принимает на вход строку и возвращает ее длину

def calculate_string_length(string):
    """
    Функция принимает строку и возвращает ее длину.

    Args:
        string (str): Входная строка.

    Returns:
        int: Длина строки.
    """
    return len(string)

# Пример использования функции
string = "Hello, World!"
result = calculate_string_length(string)
print(result)  # Вывод: 13
