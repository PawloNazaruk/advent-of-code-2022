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
    #return [x.replace("\n", "").replace("[", "").replace("]", "") for x in data]
    return [x.replace("\n", "") for x in data]


def task_solution() -> None:
    rows = clean_data(get_data_from_file(INPUT_FILE))
    #pprint(rows)
    cargo_crane = rows[9::-1]
    #pprint(cargo_crane)

    tab = []
    for row in rows[0::-1]:
        pprint(f"{row}")
        temp = []
        for chars in row[::3]:
            pprint(f"{chars=}")



task_solution()
