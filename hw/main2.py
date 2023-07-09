# Задача: Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение

def calculate_average(numbers):
    """
    Функция принимает список чисел и возвращает их среднее значение.

    Args:
        numbers (list): Список чисел.

    Returns:
        float: Среднее значение чисел.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Пример использования функции
numbers = [1, 2, 3, 4, 5]
result = calculate_average(numbers)
print(result)  # Вывод: 3.0
