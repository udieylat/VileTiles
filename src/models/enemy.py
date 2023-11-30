from dataclasses import dataclass

from src.models.pattern import Pattern


@dataclass
class Enemy(Pattern):
    disabled: bool = False

    def disable(self):
        self.disabled = True
