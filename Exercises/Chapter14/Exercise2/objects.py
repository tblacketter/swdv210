from dataclasses import dataclass

@dataclass
class Movie:
    name: str
    year: int

    def __init__(self, nameInit, yearInit):
        self.name = nameInit
        self.year = yearInit

    def getStr(self) -> str:
        return (f"{self.name} ({self.year})")

