from brain_games.basic_logic import launch_game
from brain_games.constants import EXERCISE_GCD
from brain_games.games.gcd_logic import run_game_brain_gcd


def main():
    launch_game(EXERCISE_GCD, run_game_brain_gcd)


if __name__ == "__main__":
    main()