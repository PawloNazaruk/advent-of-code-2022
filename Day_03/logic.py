from typing import List, Tuple
from math import floor

INPUT_FILE = "input_file.txt"


def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def clean_data(data: List[str]) -> List[str]:
    return [x.replace("\n", "") for x in data]


def split_to_halves(text: str) -> Tuple:
    half_at: int = int(floor(len(text) / 2))
    return text[:half_at], text[half_at:]


def get_priority(letter: str) -> int:
    numbers = [x for x in range(1, 58)]
    small_letters = [chr(x) for x in range(97, 123)]
    big_letters = [chr(x) for x in range(65, 91)]
    table = dict(zip(small_letters + big_letters, numbers))
    return table.get(letter)


def task_solution() -> None:
    rows: List[str] = clean_data(get_data_from_file(INPUT_FILE))

    # First part
    total: int = 0
    for text in rows:
        half_first, half_second = split_to_halves(text)
        half_first = set(half_first)
        half_second = set(half_second)
        for common_letter in half_first & half_second:
            total += get_priority(common_letter)
    print(total)

    # Second part
    total: int = 0
    group: List[set] = []
    for i, text in enumerate(rows, start=1):
        group.append(set(text))
        if i % 3 == 0:
            for common_letter in group[0] & group[1] & group[2]:
                total += get_priority(common_letter)
            group = []
    print(total)
