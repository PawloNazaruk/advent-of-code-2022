from typing import List
from pprint import pprint


INPUT_FILE = "input_file.txt"


def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def clean_data(data: List[str]) -> List[str]:
    return [x.replace("\n", "") for x in data]


def task_solution() -> None:
    text: str = clean_data(get_data_from_file(INPUT_FILE))[0]

    # First part
    MARKER: int = 4
    index: int = 0
    for i, _ in enumerate(text):
        packet: str = text[i:MARKER + i]
        if len(set(packet)) == MARKER:
            index = MARKER + i
            break
    pprint(f"result: {index=}")

    # Second part
    MARKER: int = 14
    index: int = 0
    for i, _ in enumerate(text):
        packet: str = text[i:MARKER + i]
        if len(set(packet)) == MARKER:
            index = MARKER + i
            break
    pprint(f"result: {index=}")


task_solution()
