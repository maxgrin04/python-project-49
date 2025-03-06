import random

OPERATORS = ('*', '+', '-')
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
RULES_CALC = 'What is the result of the expression?'


def calculate_operation(rand_operator, number_1, number_2):
    match rand_operator:
        case '*':
            correct_answer = number_1 * number_2
        case '+':
            correct_answer = number_1 + number_2
        case '-':
            correct_answer = number_1 - number_2
    return correct_answer


def create_question_and_answer():
    rand_operator = random.choice(OPERATORS)
    number_1 = random.randint(
        MIN_RANDOM_NUMBER,
        MAX_RANDOM_NUMBER
    )
    number_2 = random.randint(
        MIN_RANDOM_NUMBER,
        MAX_RANDOM_NUMBER
    )
    question = f'{number_1} {rand_operator} {number_2}'
    correct_answer = calculate_operation(
       rand_operator,
       number_1,
       number_2
    )
    correct_answer = str(correct_answer)
    return question, correct_answer