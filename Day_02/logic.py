from enum import Enum
from typing import List, Tuple


INPUT_FILE: str = "input_data.txt"


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def parse_data(data: List[str]) -> List[Tuple[Hand, Hand]]:
    data = [x.replace(' ', '').replace('\n', '') for x in data]
    parsed_data = []
    elf_hand = {'A': Hand.ROCK, 'B': Hand.PAPER, 'C': Hand.SCISSORS}
    player_hand = {'X': Hand.ROCK, 'Y': Hand.PAPER, 'Z': Hand.SCISSORS}
    for elf_pick, player_pick in data:
        parsed_data.append((elf_hand.get(elf_pick), player_hand.get(player_pick)))
    return parsed_data


def game_outcome(choice_1, choice_2):
    if choice_1 == "ROCK":
        return {"ROCK": "tie", "PAPER": "lose", "SCISSORS": "win"}.get(choice_2)
    elif choice_1 == "PAPER":
        return {"ROCK": "win", "PAPER": "tie", "SCISSORS": "lose"}.get(choice_2)
    elif choice_1 == "SCISSORS":
        return {"ROCK": "lose", "PAPER": "win", "SCISSORS": "tie"}.get(choice_2)


def task_solution() -> None:
    score: int = 0
    outcome_table: dict = {"lose": 0, "tie": 3, "win": 6}
    rounds: List[Tuple] = parse_data(get_data_from_file(INPUT_FILE))
    for elf, player in rounds:
        result: str = game_outcome(player.name, elf.name)
        score += player.value + outcome_table.get(result)

    # First Part
    print(score)
