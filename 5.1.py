def exponentiation_of_number(num: int, exp: int) -> int:
    """Рекурсивное возведение числа в степень n"""
    if exp == 0:
        return 1
    return num*exponentiation_of_number(num, exp-1)


number = int(input('Введите число: '))
ext = int(input('Введите значение степени: '))
print(f'{number} в степени {ext} = {exponentiation_of_number(number, ext)}')
