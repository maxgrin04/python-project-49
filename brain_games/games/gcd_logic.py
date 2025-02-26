import math
import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
RULES_GCD = 'Find the greatest common divisor of given numbers.'


def create_gcd_question_and_answer():
    number_1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    number_2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'{number_1} {number_2}'
    correct_answer = str(math.gcd(number_1, number_2))
    return question, correct_answer