from dataclasses import dataclass
import  time

@dataclass
class Date:
    day: int
    month: int
    year: int
    def __repr__(self):
        return f"{self.day} {self.month} {self.year}"

@dataclass
class FIO:
    f: str
    i: str
    o: str
    def __repr__(self):
        return f"{self.f} {self.i} {self.o}"

@dataclass
class Key:
    key_date: Date
    key_fio: FIO
    other_data : str = ''
    def __repr__(self):
        return f"{self.key_date} {self.key_fio} {self.other_data}"

    def compare_keys(self, other):
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
        if self.key_fio.o != other.key_fio.o:
            return self.key_fio.o > other.key_fio.o

def read_data_from_file(filename):
    keys = []
    file = open(filename, 'r', encoding='utf-8')
    for line in file:
        if not line:
            continue

        line = line.strip().split()
        if len(line) == 6:
            day, month, year, f, i, o = line
            date = Date(int(day), int(month), int(year))
            fio = FIO(f, i, o)
            key = Key(date, fio)
            keys.append(key)

        if len(line) == 7:
                day, month, year, f, i, o, tail = line
                date = Date(int(day), int(month), int(year))
                fio = FIO(f, i, o)
                key = Key(date, fio, tail)
                keys.append(key)
    file.close()
    return keys

def binary_search_for_insert(arr: list[Key], target: Key) -> int:
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid].compare_keys(target):
            right = mid
        else:
            left = mid + 1

    return left


def two_way_insert_sort(arr):
    if len(arr) <= 1:
        return arr

    result = [arr[0]]

    for i in range(1, len(arr)):
        current = arr[i]
        pos = binary_search_for_insert(result, current)
        result.insert(pos, current)

    return result


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    stack = [(0, len(result) - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        mid = (low + high) // 2
        opor = result[mid]
        i, j = low, high

        while i <= j:
            while i <= high and result[i].compare_keys(opor):
                i += 1
            while j >= low and opor.compare_keys(result[j]):
                j -= 1
            if i <= j:
                result[i], result[j] = result[j], result[i]
                i += 1
                j -= 1

        if low < j:
            stack.append((low, j))
        if i < high:
            stack.append((i, high))

    return result

def save_in_newFile(array_to_save : list, name_output_File : str):
    file = open(f"{name_output_File}.txt", "w", encoding="utf-8")
    for i in array_to_save:
        file.write(f"{i}\n")
    file.close()

if __name__ == "__main__":
    DATA_for_sort = read_data_from_file("input_1000000_v2.txt")

    print("\n")

    time_start = time.perf_counter ()

    sorted_DATA = quick_sort(DATA_for_sort)

    time_end = time.perf_counter()
    print(f"Время выполнения Быстрая : {time_end - time_start:.6f} секунд")

    save_in_newFile(sorted_DATA, "test_output_changes")

    time_start = time.perf_counter()

    sorted_DATA = two_way_insert_sort(DATA_for_sort)

    time_end = time.perf_counter()

    print(f"Время выполнения Двухпутевые вставки : {time_end - time_start:.6f} секунд")