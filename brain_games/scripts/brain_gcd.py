from brain_games.engine_logic import launch_game
from brain_games.games.gcd_logic import RULES_GCD
from brain_games.games.gcd_logic import create_gcd_question_and_answer


def main():
    launch_game(RULES_GCD, create_gcd_question_and_answer)


if __name__ == "__main__":
    main()