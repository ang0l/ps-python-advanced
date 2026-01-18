"""Модуль конфигурации приложения"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppSettings:
    """Установки приложения"""

    data_deirctory: Path
    app_name: str = 'Менеджер заметок'
    app_version: str = '0.1.0'

    @classmethod
    def from_defaults(cls) -> 'AppSettings':
        """Дефолтные установки приложения"""

        base_path = Path(__file__).parent.parent.parent
        data_path = base_path / 'data'

        return cls(data_deirctory=data_path)

    @classmethod
    def from_custom_path(cls, data_path: str | Path) -> 'AppSettings':
        """Установки приложения с передачей аргумента"""

        return cls(data_deirctory=Path(data_path))
