from enum import Enum
from typing import List, Tuple


INPUT_FILE: str = "input_data.txt"


class Hand(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class GameResult(Enum):
    LOSE = 0
    TIE = 3
    WIN = 6

def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def parse_hands_data(data: List[str]) -> List[Tuple[Hand, Hand]]:
    data = [x.replace(' ', '').replace('\n', '') for x in data]
    parsed_data = []
    elf_hand = {'A': Hand.ROCK, 'B': Hand.PAPER, 'C': Hand.SCISSORS}
    player_hand = {'X': Hand.ROCK, 'Y': Hand.PAPER, 'Z': Hand.SCISSORS}
    for elf_pick, player_pick in data:
        parsed_data.append((elf_hand.get(elf_pick), player_hand.get(player_pick)))
    return parsed_data


def parse_results_data(data: List[str]) -> List[Tuple[Hand, GameResult]]:
    data = [x.replace(' ', '').replace('\n', '') for x in data]
    parsed_data = []
    elf_hand = {'A': Hand.ROCK, 'B': Hand.PAPER, 'C': Hand.SCISSORS}
    match_result = {'X': GameResult.LOSE, 'Y': GameResult.TIE, 'Z': GameResult.WIN}

    for elf_pick, result in data:
        parsed_data.append((elf_hand.get(elf_pick), match_result.get(result)))
    return parsed_data


def game_outcome(choice_1: str, choice_2: str) -> str:
    if choice_1 == "ROCK":
        return {"ROCK": "tie", "PAPER": "lose", "SCISSORS": "win"}.get(choice_2)
    elif choice_1 == "PAPER":
        return {"ROCK": "win", "PAPER": "tie", "SCISSORS": "lose"}.get(choice_2)
    elif choice_1 == "SCISSORS":
        return {"ROCK": "lose", "PAPER": "win", "SCISSORS": "tie"}.get(choice_2)


def find_hand_by_result(choice_1: str, result: str) -> str:
    print(f"{choice_1=}")
    print(f"{result=}")
    if choice_1 == "ROCK":
        outcome = {"ROCK": "TIE", "PAPER": "LOSE", "SCISSORS": "WIN"}
        for key, value in outcome.items():
            if value == result:
                return key
    elif choice_1 == "PAPER":
        outcome = {"ROCK": "WIN", "PAPER": "TIE", "SCISSORS": "LOSE"}
        for key, value in outcome.items():
            if value == result:
                return key
    elif choice_1 == "SCISSORS":
        matches = {"ROCK": "LOSE", "PAPER": "WIN", "SCISSORS": "TIE"}
        for key, value in matches.items():
            if value == result:
                return key


def task_solution() -> None:
    outcome_table: dict = {"lose": 0, "tie": 3, "win": 6}

    # First Part
    rounds: List[Tuple] = parse_hands_data(get_data_from_file(INPUT_FILE))
    score: int = 0
    for elf, player in rounds:
        result: str = game_outcome(player.name, elf.name)
        score += player.value + outcome_table.get(result)
    print(score)

    # Second Part
    rounds: List[Tuple] = parse_results_data(get_data_from_file(INPUT_FILE))
    score: int = 0
    for elf, result in rounds[:2]:
        print("aaaa")
        print(f"{result=}")
        print(f"{result.name=}")
        player: str = find_hand_by_result(elf.name, result.name)
        score += player.value + result.value
    print(score)
