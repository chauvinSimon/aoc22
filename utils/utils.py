from pathlib import Path


def read_file(p: Path):
    with p.open() as f:
        data = f.read().splitlines()
    return data
