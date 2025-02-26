import random


MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    return random_number % 2 == 0


def create_even_question_and_answer():
    random_number = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    return random_number, correct_answer