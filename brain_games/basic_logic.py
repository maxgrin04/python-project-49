import prompt


# Приветствие, имя пользователя и задание
def greet_and_exercise(exercise):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(exercise)
    return name


# Проверка ответа
def check_answer(question, correct_answer, name):
    print(f'Question: {question}')
    answer = prompt.string('You answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
        print(f"Let's try again, {name}")
        return False


# Успешное завершение игры
def game_win(name):
    print(f'Congratulations, {name}!')


# Запускаем игру
def launch_game(exercise, game, cycle=3):
    name = greet_and_exercise(exercise)
    for _ in range(cycle):
        question, correct_answer = game()
        if not check_answer(question, correct_answer, name):
            return 
    game_win(name)
