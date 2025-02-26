import random
import math


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    number_sqrt = int(math.sqrt(number))
    for element in range(2, number_sqrt + 1):
        if number % element == 0:
            return False
    return True


def create_prime_question_and_answer():
    number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer