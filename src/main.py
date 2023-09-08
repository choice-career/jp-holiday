from pathlib import Path
from os import environ

from holiday import get_holiday_csv_str, parse_holiday_to_dict
from resource_generator.generate_holiday import GenerateHoliday
from resource_generator.generate_list import GenerateList

REPOSITORY_ROOT = Path(__file__).parent.parent

def gen_holiday_api() -> bool:
    return environ.get("GEN_HOLIDAY_API") is not None


def generate_api() -> None:
    holiday_map = parse_holiday_to_dict(get_holiday_csv_str())

    gl = GenerateList(REPOSITORY_ROOT)
    gl.generate(holiday_map)

    if gen_holiday_api():
        gh = GenerateHoliday(REPOSITORY_ROOT)
        gh.generate(holiday_map)


generate_api()
