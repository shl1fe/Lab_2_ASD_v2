from dataclasses import dataclass
from models.date import Date
from models.fio import FIO


@dataclass
class Key:
    """Класс ключа для сортировки, дата, ФИО и дополнительные данные"""
    key_date: Date
    key_fio: FIO
    other_data: str = ''

    def __repr__(self):
        return f"{self.key_date} {self.key_fio} {self.other_data}"

    def compare_keys(self, other):
        """
                Сравнение двух ключей для сортировки

                Args:
                    other (Key): Другой ключ для сравнения

                Returns:
                    bool: True если текущий ключ должен стоять перед другим при сортировке
                          Сначала сравниваются даты (по возрастанию), затем ФИО (по убыванию)
                """
        if self.key_date.year != other.key_date.year:
            return self.key_date.year < other.key_date.year
        if self.key_date.month != other.key_date.month:
            return self.key_date.month < other.key_date.month
        if self.key_date.day != other.key_date.day:
            return self.key_date.day < other.key_date.day

        if self.key_fio.f != other.key_fio.f:
            return self.key_fio.f > other.key_fio.f
        if self.key_fio.i != other.key_fio.i:
            return self.key_fio.i > other.key_fio.i
        return self.key_fio.o > other.key_fio.o