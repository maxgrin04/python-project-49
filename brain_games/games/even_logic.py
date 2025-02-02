import random


def is_even(number):
    return number % 2 == 0


def run_game_brain_even():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return number, correct_answer