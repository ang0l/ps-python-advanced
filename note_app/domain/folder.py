
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Folder:
    name: str
    path: Path

    def __post_init__(self):
        if self.name or self.name.strip() == '':
            raise ValueError('Папка должна иметь имя')
