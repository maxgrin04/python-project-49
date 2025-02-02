from brain_games.basic_logic import launch_game
from brain_games.constants import EXERCISE_PROGRESSION
from brain_games.games.progression_logic import run_game_brain_progression


def main():
    launch_game(EXERCISE_PROGRESSION, run_game_brain_progression)


if __name__ == "__main__":
    main()