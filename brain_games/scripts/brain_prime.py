from brain_games.basic_logic import launch_game
from brain_games.constants import EXERCISE_PRIME
from brain_games.games.prime_logic import run_game_brain_prime


def main():
    launch_game(EXERCISE_PRIME, run_game_brain_prime)


if __name__ == "__main__":
    main()