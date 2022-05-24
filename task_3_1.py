my_list = input('Введите число от 1 до 10 на англиском: ')
dict_number = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': "пять",
    'six': 'шесть',
    'seven': 'cемь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
def num_translate(i):
    return dict_number.get(i)

print(f'"{num_translate(my_list)}"')

