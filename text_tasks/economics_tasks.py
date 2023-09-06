import random
import math

'''Пример задачи с решуегэ https://ege.sdamgia.ru/problem?id=548855:
Вклад планируется открыть на четыре года.
Первоначальный вклад составляет целое число миллионов рублей.
В конце каждого года банк увеличивает вклад на 10% по сравнению с его размером в начале года.
Кроме этого, в начале третьего и четвертого годов вкладчик ежегодно пополняет вклад на 10 млн рублей.
Найдите наибольший размер первоначального вклада, при котором банк за четыре года начислит на вклад меньше 15 млн рублей.'''

def right_namenigs(parametrs, keys):
    units = {
        'year': [' года', ' лет', ' год'],
        'money': [' миллиона', ' миллионов', ' миллион'],
        'percent': [' процента', ' процентов', ' процент']
    }
    result = []
    for par, key in zip(parametrs, keys):
        if par == 'X':
            result.append('X'+ units[key][1])
        elif par % 10 == 1 and str(par)[-2:] != '11':
            result.append(str(par) + units[key][2])
        elif (par % 10 == 2 or par % 10 == 3 or par % 10 == 4) and (str(par)[-2:] != '12' and str(par)[-2:] != '13' and str(par)[-2:] != '14'):
            result.append(str(par) + units[key][0])
        else:
            result.append(str(par) + units[key][1])
    return result


def generate_economics_task_548855():
    #Генерируем условия задачи
    years = random.randint(4, 6)
    start_capital = random.randint(10, 30)
    percent = random.randint(3, 10)
    addition_capital = random.randint(5, 15)
    years_to_add = random.randint(2, years - 1)

    # Выбираем неизвестный параметр: время вклада, стартовый капитал или добавляемый капитал.
    # Теоретически можно и проценты - но тогда задача станет слишком сложной для решения.
    question = random.randint(0, 2)

    parameters = [years, start_capital, addition_capital, percent]

    result = float(start_capital)

    for i in range(years):
        if i >= years_to_add - 1:
            result += addition_capital
        result += result * float(percent) / 100

    result -= addition_capital * (years - years_to_add + 1) + start_capital
    answer = parameters[question]
    parameters[question] = 'X'
    parameters = right_namenigs(parameters, ['year', 'money', 'money', 'percent'])

    return (f'Вклад планируется открыть на {parameters[0]}. ' \
           f'Первоначальный вклад составляет {parameters[1]} рублей. ' \
           f'В конце каждого года банк увеличивает вклад на {parameters[3]} по сравнению с его размером в начале года. ' \
           f'Кроме этого, начиная с {years_to_add}-го года вкладчик ежегодно пополняет вклад на {parameters[2]} рублей. ' \
           f'Найдите наименьший целый X, при котором банк начислит на вклад как минимум {math.floor(result * 1000) / 1000} млн рублей.''', answer)


print(generate_economics_task_548855())


