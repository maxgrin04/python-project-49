#!/usr/bin/env python3

from brain_games.engine_logic import launch_game
from brain_games.games.calc_logic import RULES_CALC
from brain_games.games.calc_logic import create_calc_question_and_answer


def main():
    launch_game(RULES_CALC, create_calc_question_and_answer)


if __name__ == "__main__":
    main()