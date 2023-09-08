from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Final

from holiday import HolidayMap
from resource_generator.common import File

BASE_PATH: Final[str] = "list"


class GenerateList:
    def __init__(self, repository_root_path: Path) -> None:
        self.root_path = repository_root_path
        self.base_path = self.root_path.joinpath(BASE_PATH)

    def generate(self, holiday_map: HolidayMap) -> None:
        files = self.gen_all(holiday_map) + self.gen_each_year(holiday_map)
        for file in files:
            file.write()

    def gen_all(self, holiday_map: HolidayMap) -> list[File]:
        return [
            # JSON ファイル
            File(
                self.base_path.joinpath("all/date.json"),
                holiday_map.json_str,
            ),
            # CSV ファイル
            File(
                self.base_path.joinpath("all/date.csv"),
                holiday_map.csv_str,
            ),
        ]

    def gen_each_year(self, holiday_map: HolidayMap) -> list[File]:
        # key:value = 2023: 2023だけが含まれたholiday_map を生成する
        years_to_holiday_map = defaultdict(HolidayMap)
        for k, v in holiday_map.items():
            year = k.split("-")[0]
            years_to_holiday_map[year][k] = v

        files: list[File] = []
        for year, hm in years_to_holiday_map.items():
            # JSON 用ファイル
            files.append(
                File(
                    self.base_path.joinpath(f"{year}/date.json"),
                    hm.json_str,
                )
            )
            # CSV 用ファイル
            files.append(
                File(
                    self.base_path.joinpath(f"{year}/date.csv"),
                    hm.csv_str,
                )
            )

        # 去年、今年、来年を含んだlistをデフォルトとして置く
        this_year = datetime.now().year
        hm_default = HolidayMap()
        for year in map(str, [this_year - 1, this_year, this_year + 1]):
            hm_default.update(years_to_holiday_map[year])
        # JSON 用ファイル
        files.append(
            File(
                self.base_path.joinpath(f"date.json"),
                hm_default.json_str,
            )
        )
        # CSV 用ファイル
        files.append(
            File(
                self.base_path.joinpath(f"date.csv"),
                hm_default.csv_str,
            )
        )

        return files
