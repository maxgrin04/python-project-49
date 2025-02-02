import operator
import random


def operation(rand_operator, number_1, number_2):
    match rand_operator:
        case '*':
            correct_answer = operator.mul(number_1, number_2)
        case '+':
            correct_answer = operator.add(number_1, number_2)
        case '-':
            correct_answer = operator.sub(number_1, number_2)
    return correct_answer


def run_game_brain_calc():
    operators = ['*', '+', '-']
    rand_operator = random.choice(operators)
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {rand_operator} {number_2}'
    correct_answer = operation(rand_operator, number_1, number_2)
    correct_answer = str(correct_answer)
    return question, correct_answer