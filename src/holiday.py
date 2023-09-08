import json
import urllib.request
from typing import Final

HOLIDAY_URL: Final[str] = "https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv"


class HolidayMap(dict[str, str]):
    def __init__(self, any=None):
        if any is None:
            super().__init__()
        else:
            super().__init__(any)

    @property
    def json_str(self) -> str:
        return json.dumps(self, ensure_ascii=False, indent=2)

    @property
    def csv_str(self) -> str:
        return "\n".join([f"{k},{v}" for k, v in self.items()])


def get_holiday_csv_str() -> str:
    """[国民の祝日について - 内閣府](https://www8.cao.go.jp/chosei/shukujitsu/gaiyou.html) の CSV 文字列を取得する

    Returns:
        str: CSV 文字列
    """
    req = urllib.request.Request(HOLIDAY_URL)
    with urllib.request.urlopen(req) as res:
        response_bytes: bytes = res.read()
        return response_bytes.decode("cp932")  # SJIS に注意


def format_date(date_str_with_slash: str) -> str:
    """YYYY/M/D の文字列を YYYY-MM-DD に変更する

    Args:
        date_str_with_slash (str): YYYY/M/D 形式の文字列

    Returns:
        str: YYYY-MM-DD 形式の文字列

    >>> format_date("2022/1/1")
    '2022-01-01'
    >>> format_date("2022/11/23")
    '2022-11-23'
    """
    y, m, d = map(int, date_str_with_slash.split("/"))
    return f"{y:04d}-{m:02d}-{d:02d}"


def parse_holiday_to_dict(holiday_csv_str: str) -> HolidayMap:
    """CSV文字列から key:value = 日付: 祝日の名前 の dict を生成する

    Args:
        holiday_csv_str (str): CSV 文字列
    """
    d = HolidayMap()
    for i, line in enumerate(holiday_csv_str.split("\n")):
        # ヘッダーを除去
        if i == 0:
            continue
        line = line.strip()
        line_splited = line.split(",")
        if len(line_splited) == 2:
            yyyymmdd, name = line_splited
            d[format_date(yyyymmdd)] = name
    return d
