import random

MIN_RANDOM_ELEMENT = 1
MAX_RANDOM_ELEMENT = 50
MIN_RANDOM_STEP = 1
MAX_RANDOM_STEP = 10
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
RULES_PROGRESSION = 'What number is missing in the progression?'


def generate_progression(element, step, progression_length):
    progression = [
        str(element + step) 
        for _ in range(progression_length + 1)
    ]
    return progression


def create_question_and_answer():
    element = random.randint(
        MIN_RANDOM_ELEMENT, 
        MAX_RANDOM_ELEMENT
    ) 
    step = random.randint(
        MIN_RANDOM_STEP, 
        MAX_RANDOM_STEP
    )
    progression_length = random.randint(
        MIN_PROGRESSION_LENGTH, 
        MAX_PROGRESSION_LENGTH
    )
    progression = generate_progression(
        element, 
        step, 
        progression_length
    )
    unknown_element = random.randint(0, len(progression) - 1)
    correct_answer = progression[unknown_element]
    progression[unknown_element] = '..'
    question = ' '.join(progression)
    return question, correct_answer