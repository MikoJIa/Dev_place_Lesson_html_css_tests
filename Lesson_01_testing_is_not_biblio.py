# 1) Написать функцию, которая будет заполнять список степенями числа 2 (от 2^1 до 2^n). n - целое число.
# 2) """Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).
# Чтобы получить список ключей - использовать метод .keys()"""
# 3)"""Ввести строку. Если длина строки больше 10 то создать новую строку с 3 восклицательными
# знаками и
# вывести на экран. Если у нас меньше чем 10 то вывести второй символ строки"""


num1 = 10
num2 = 1

assert num2 != 0, 'The devision is zero'
print(f'The result {num1 / num2}')


# def avf(ranks):
#     assert  len(ranks) != 0, f'wrong'
#     assert type(ranks) == list, f'wrong'
#     return sum(ranks) / len(ranks)
#
#
# ranks = tuple((i for i in range(6)))
# print(f'Среднее ариф. {avf(ranks)}')

def func(d):
    assert type(d) == dict, 'wrong'
    d1 = []
    for k, v in d.items():
        if v not in d:
            d1.append(v)
            summ = sum(d1)
            return summ
    # assert type(d) == dict, 'wrong'


res = {'a': 10, 'b': 2}
print(func(res))

assert type(func(res)) == int, 'wrong'


def func2(n):
    res = [2 ** n for n in range(2, n)]
    assert type(n) == int,  'wrong'
    return res


print(func2(10))


def func3(d):
    assert type(d) == dict, 'wrong'
    d1 = {}
    for k, v in d.items():
        len_key = len(k)
        new_key = k + str(len_key)
        d1[new_key] = v
    return d1


print(func3({'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}))


def func4(string: str):
    assert type(string) == str, 'wrong'
    if len(string) >= 10:
        return string + '!!!'
    elif len(string) < 10:
        return string[2:3]

print(func4('afsgdtriyt'))


