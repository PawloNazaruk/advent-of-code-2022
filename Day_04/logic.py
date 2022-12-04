from typing import List

INPUT_FILE = "input_file.txt"


def get_data_from_file(file: str) -> List[str]:
    try:
        with open(file, 'r+') as file_txt:
            return file_txt.readlines()
    except FileNotFoundError as err:
        print(f"File({file}) not found due to: {err}")


def clean_data(data: List[str]) -> List[str]:
    return [x.replace("\n", "") for x in data]


def parse_into_set(data: str) -> set:
    start, end = (data.split("-"))
    return set([i for i in range(int(start), int(end) + 1)])


def task_solution() -> None:
    rows = clean_data(get_data_from_file(INPUT_FILE))

    # First part
    total: int = 0
    for text in rows:
        is_subset: int = 0
        part_1, part_2 = text.split(",")
        elf_1: set = parse_into_set(part_1)
        elf_2: set = parse_into_set(part_2)
        if elf_1.issubset(elf_2):
            is_subset = 1
        if elf_2 .issubset(elf_1):
            is_subset = 1
        total += is_subset
    print(total)


task_solution()
