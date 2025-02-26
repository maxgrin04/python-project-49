from brain_games.engine_logic import launch_game
from brain_games.games.progression_logic import RULES_PROGRESSION
from brain_games.games.progression_logic import create_progression_question_and_answer


def main():
    launch_game(RULES_PROGRESSION, create_progression_question_and_answer)


if __name__ == "__main__":
    main()