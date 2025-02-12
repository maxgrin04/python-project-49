import random
import math


def is_prime(number):
    if number < 2:
        return False
    number_sqrt = int(math.sqrt(number))
    for element in range(2, number_sqrt + 1):
        if number % element == 0:
            return False
    return True


def run_game_brain_prime():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer