import math
import random


def is_gcd(number_1, number_2):
    return str(math.gcd(number_1, number_2))


def run_game_brain_gcd():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    correct_answer = is_gcd(number_1, number_2)
    return question, correct_answer