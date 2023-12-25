"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def halving_method(number) -> int:
    """ Угадывает число по методу деления пополам

    Args:
        halving_method (_type_): функция угадывания числа

    Returns:
        int: Количество попыток для угадывания числа
    """

    count = 0
    
    min = 1
    max = 100
    predict = (min + max) // 2 # формируем начальное число для сравнения с загаданным 
    
    while number != predict:

        count += 1
        
        # создаем условия для сравнения предполагаемого и загаданного чисел
        if number > predict:
            min = predict + 1
            predict = (min + max) // 2
        elif number < predict:
            max = predict - 1
            predict = (min + max) // 2

    return count


def score_game(predict_count) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция генерации числа и подсчета среднего числа угадывания после 1000 попыток

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(halving_method(number))

    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")

    return score


if __name__ == "__main__":
    # RUN
    score_game(halving_method)
    
