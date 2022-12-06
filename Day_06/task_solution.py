from typing import List
import re
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



task_solution()
