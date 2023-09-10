import json
from calendar import monthrange
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Final, Optional

from tqdm import tqdm, trange

from holiday import HolidayMap
from resource_generator.common import File

BASE_PATH: Final[str] = "holiday"


def holiday_json_str(name: Optional[str]) -> str:
    d = {
        "holiday": name is not None,
        "name": name or "",
    }
    return json.dumps(d, ensure_ascii=False, indent=2)


class GenerateHoliday:
    def __init__(self, repository_root_path: Path) -> None:
        self.root_path = repository_root_path
        self.base_path = self.root_path.joinpath(BASE_PATH)

    def generate(self, holiday_map: HolidayMap) -> None:
        files = self.gen(holiday_map)
        print("Writing...")
        for file in files:
            file.write()

    def gen(self, holiday_map: HolidayMap) -> list[File]:
        years = list(set(map(int, [k.split("-")[0] for k in holiday_map.keys()])))
        files: list[File] = []
        print("Generating...")
        for year in years:
            for month in range(1, 12 + 1):
                for date in range(1, monthrange(year, month)[1] + 1):
                    name = holiday_map.get(f"{year:04d}-{month:02d}-{date:02d}")
                    files.append(
                        File(
                            self.base_path.joinpath(
                                f"{year:04d}/{month:02d}/{date:02d}"
                            ),
                            holiday_json_str(name),
                        )
                    )
        return files
