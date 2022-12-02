from typing import List


INPUT_FILE = "input_data.txt"


def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def parse_data(data: List[str]) -> List[List[int]]:
    data = [x.replace('\n', '') for x in data]
    calories_to_elves: List = []
    per_elf: List = []
    for calories in data:
        if calories != '':
            per_elf.append(int(calories))
        else:
            calories_to_elves.append(per_elf)
            per_elf: List = []
    return calories_to_elves


def task_solution() -> None:
    elves_calories: List[List[int]] = parse_data(get_data_from_file(INPUT_FILE))

    # First part
    top_elf: int = max([sum(x) for x in elves_calories])
    print(top_elf)

    # Second part
    top_three_elves: int = sum(sorted([sum(x) for x in elves_calories], reverse=True)[:3])
    print(top_three_elves)
