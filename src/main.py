from pathlib import Path

from holiday import get_holiday_csv_str, parse_holiday_to_dict
from resource_generator.generate_list import GenerateList

REPOSITORY_ROOT = Path(__file__).parent.parent


def generate_api() -> None:
    holiday_map = parse_holiday_to_dict(get_holiday_csv_str())

    gl = GenerateList(REPOSITORY_ROOT)
    gl.generate(holiday_map)


generate_api()
