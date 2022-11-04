"""Игра угадай число
Компьютер сам загадывает и сам угадывает число меньше чем за 20 попыток
"""

import numpy as np


def fast_predict(number: int = 1) -> int:
    """Рандомно загадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Загаданное число должно находится в диапазоне от min до max числа
    min_number = 1
    max_number = 100

    #number = np.random.randint(min_number, max_number+1) # загадываем число

    # количество попыток
    count = 0

    while True:
        count += 1
        predict_number = (min_number+max_number) // 2
    
        if predict_number > number:
            max_number = predict_number # Загаданное число должно быть меньше!

        elif predict_number < number:
            min_number = predict_number # Загаданное число должно быть больше!
    
        else:
            break # выход из цикла, если угадали
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
    return(count)


def score_game(fast_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Рандомно загадали список чисел

    for number in random_array:
        count_ls.append(fast_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(fast_predict)