import random


def creating_progression():
    progression = []
    element = random.randint(1, 50) 
    step = random.randint(1, 10)
    number_of_elements = random.randint(5, 10)
    progression.append(str(element))
    for _ in range(number_of_elements + 1):
        element += step
        progression.append(str(element))
    return progression


def run_game_brain_progression():
    progression = creating_progression()
    unknown_element = random.randint(0, len(progression) - 1)
    correct_answer = progression[unknown_element]
    progression[unknown_element] = '..'
    question = ' '.join(progression)
    return question, correct_answer