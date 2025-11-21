from dataclasses import dataclass

@dataclass
class FIO:
    """Класс для представления ФИО (фамилия, имя, отчество)"""
    f: str
    i: str
    o: str

    def __repr__(self):
        return f"{self.f} {self.i} {self.o}"