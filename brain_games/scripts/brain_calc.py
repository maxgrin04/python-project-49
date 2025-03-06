#!/usr/bin/env python3

from brain_games.engine_logic import launch_game
from brain_games.games.calc import (
    RULES_CALC,
    create_question_and_answer,
)


def main():
    launch_game(RULES_CALC, create_question_and_answer)


if __name__ == "__main__":
    main()