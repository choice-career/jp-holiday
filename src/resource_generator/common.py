import pathlib


class File:
    def __init__(self, out_path: pathlib.Path, data: str) -> None:
        self.out_path = out_path
        self.data = data

    def write(self) -> None:
        self.out_path.parent.mkdir(parents=True, exist_ok=True)
        open(self.out_path, "w").write(self.data)
