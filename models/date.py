from dataclasses import dataclass

@dataclass
class Date:
    day: int
    month: int
    year: int
    def __repr__(self):
        return f"{self.day} {self.month} {self.year}"
