"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадывает число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # счетчик попыток
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    upper_digit = 100  # верхняя граница интервала угадывания
    lower_digit = 1  # нижняя граница интервала угадывания
       
    while number != predict_number:
        count += 1
        if number < predict_number:
            upper_digit = predict_number
        elif number > predict_number:
            lower_digit = predict_number
        predict_number = round((upper_digit+lower_digit))/2    
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
