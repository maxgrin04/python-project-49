from brain_games.basic_logic import launch_game
from brain_games.constants import EXERCISE_CALC
from brain_games.games.calc_logic import run_game_brain_calc


def main():
    launch_game(EXERCISE_CALC, run_game_brain_calc)


if __name__ == "__main__":
    main()