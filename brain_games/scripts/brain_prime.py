#!/usr/bin/env python3

from brain_games.engine_logic import launch_game
from brain_games.games.prime import (
    RULES_PRIME,
    create_question_and_answer,
)


def main():
    launch_game(RULES_PRIME, create_question_and_answer)


if __name__ == "__main__":
    main()