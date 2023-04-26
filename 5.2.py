def sum_of_numbers(num_1: int, num_2: int) -> int:
    """Рекурсивная сумма двух чисел"""
    if num_2 == 0:
        return num_1
    return sum_of_numbers(num_1 + 1, num_2 - 1)


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
print(f'{number1} + {number2} = {sum_of_numbers(number1, number2)}')
