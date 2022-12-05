from typing import List
import re

INPUT_FILE = "input_file.txt"


def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def clean_data(data: List[str]) -> List[str]:
    return [x.replace("\n", "") for x in data]


def create_stacks(rows: List[str]) -> List[List[str]]:
    tab: List[List[str]] = [[] for _ in range(9)]
    for text in rows:
        for i, letter in enumerate(text[1:-1:4]):
            if letter not in " ":
                tab[i].append(letter)
    return tab


def task_solution() -> None:
    rows: List[str] = clean_data(get_data_from_file(INPUT_FILE))

    # First part
    cargo_order: List[str] = rows[7::-1]
    cargo_movements: List[str] = rows[10:]

    stacks: List[List[str]] = create_stacks(cargo_order)

    for movement in cargo_movements:
        quantity, from_stack, to_stack = [int(x) for x in re.findall(r"[0-9]+", movement)]
        from_stack -= 1
        to_stack -= 1
        for i in range(0, quantity):
            stacks[to_stack].append(stacks[from_stack].pop())

    result: str = "".join([x[-1] for x in stacks])
    print(f"{result=}")


task_solution()
