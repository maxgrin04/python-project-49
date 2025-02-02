from brain_games.basic_logic import launch_game
from brain_games.constants import EXERCISE_EVEN
from brain_games.games.even_logic import run_game_brain_even


def main():
    launch_game(EXERCISE_EVEN, run_game_brain_even)


if __name__ == "__main__":
    main()