#!/usr/bin/env python3

from brain_games.engine_logic import launch_game
from brain_games.games.even_logic import RULES_EVEN
from brain_games.games.even_logic import create_even_question_and_answer


def main():
    launch_game(RULES_EVEN, create_even_question_and_answer)


if __name__ == "__main__":
    main()