from brain_games.engine_logic import launch_game
from brain_games.games.prime_logic import RULES_PRIME
from brain_games.games.prime_logic import create_prime_question_and_answer


def main():
    launch_game(RULES_PRIME, create_prime_question_and_answer)


if __name__ == "__main__":
    main()