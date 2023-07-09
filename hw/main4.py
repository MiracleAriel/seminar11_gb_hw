# Задача: Напишите функцию, которая принимает на вход список чисел и возвращает наибольшее число из списка

def find_max_number(numbers):
    """
    Функция принимает список чисел и возвращает наибольшее число из списка.

    Args:
        numbers (list): Список чисел.

    Returns:
        int: Наибольшее число из списка.
    """
    return max(numbers)

# Пример использования функции
numbers = [1, 5, 3, 7, 2]
result = find_max_number(numbers)
print(result)  # Вывод: 7
