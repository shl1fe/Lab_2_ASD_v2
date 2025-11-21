from dataclasses import dataclass

@dataclass
class FIO:
    f: str
    i: str
    o: str

    def __repr__(self):
        return f"{self.f} {self.i} {self.o}"