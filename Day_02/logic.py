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


def find_game_result(choice_1: str, choice_2: str) -> GameResult:
    if choice_1 == "ROCK":
        return {"ROCK": GameResult.WIN, "PAPER": GameResult.LOSE, "SCISSORS": GameResult.WIN}.get(choice_2)
    elif choice_1 == "PAPER":
        return {"ROCK": GameResult.WIN, "PAPER": GameResult.TIE, "SCISSORS": GameResult.LOSE}.get(choice_2)
    elif choice_1 == "SCISSORS":
        return {"ROCK": GameResult.LOSE, "PAPER": GameResult.WIN, "SCISSORS": GameResult.LOSE}.get(choice_2)


def find_hand_from_result(choice_1: str, result: str) -> Hand:
    if choice_1 == "ROCK":
        outcome = {"TIE": Hand.ROCK, "WIN": Hand.PAPER, "LOSE": Hand.SCISSORS}
        return outcome.get(result)
    elif choice_1 == "PAPER":
        outcome = {"TIE": Hand.PAPER, "WIN": Hand.SCISSORS, "LOSE": Hand.ROCK}
        return outcome.get(result)
    elif choice_1 == "SCISSORS":
        outcome = {"TIE": Hand.SCISSORS, "WIN": Hand.ROCK, "LOSE": Hand.PAPER}
        return outcome.get(result)


def task_solution() -> None:
    # First Part
    rounds: List[Tuple] = parse_hands_data(get_data_from_file(INPUT_FILE))
    score: int = 0
    for elf, player in rounds:
        result: GameResult = find_game_result(player.name, elf.name)
        score += player.value + result.value
    print(score)

    # Second Part
    rounds: List[Tuple] = parse_results_data(get_data_from_file(INPUT_FILE))
    score: int = 0
    for elf, result in rounds:
        player: Hand = find_hand_from_result(elf.name, result.name)
        score += player.value + result.value
    print(score)
