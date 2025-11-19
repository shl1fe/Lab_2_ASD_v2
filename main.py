from dataclasses import dataclass
import  time
@dataclass
class Date:
    day: int
    month: int
    year: int

@dataclass
class FIO:
    f: str
    i: str
    o: str

@dataclass
class Key:
    date: Date
    fio: FIO
    other_data : str = ''

def read_data_from_file(filename):
    keys = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
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

def compare_keys(a, b):
    if a.date.year != b.date.year:
        return a.date.year < b.date.year
    if a.date.month != b.date.month:
        return a.date.month < b.date.month
    if a.date.day != b.date.day:
        return a.date.day < b.date.day

    if a.fio.f != b.fio.f:
        return a.fio.f > b.fio.f
    if a.fio.i != b.fio.i:
        return a.fio.i > b.fio.i
    return a.fio.o > b.fio.o

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if compare_keys(arr[mid], target):
            low = mid + 1
        else:
            high = mid - 1
    return low


def two_way_insert_sort(arr):
    if  len(arr) <= 1:
        return arr

    left = [arr[0]]
    right = []

    for i in range(1, len(arr)):
        current = arr[i]
        if compare_keys(current, left[0]):
            left.insert(binary_search(left, current), current)
        else:
            right.insert(binary_search(right, current), current)

    return left + right


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    stack = [(0, len(result) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            mid = (low + high) // 2
            opor = result[mid]
            i, j = low - 1, high + 1

            while True:
                i += 1
                while compare_keys(result[i], opor): i += 1
                j -= 1
                while compare_keys(opor, result[j]): j -= 1
                if i >= j: break
                result[i], result[j] = result[j], result[i]

            stack.append((low, j))
            stack.append((j + 1, high))

    return result

if __name__ == "__main__":
    DATA_for_sort = read_data_from_file("input_1000000_v2.txt")

    print("\n")

    time_start = time.perf_counter ()

    file = open("output_input_1000000_v2.txt", "w", encoding="utf-8")
    for i in two_way_insert_sort(DATA_for_sort):
        file.write(f"{i.date.day} {i.date.month} {i.date.year} {i.fio.f} {i.fio.i} {i.fio.o} {i.other_data}\n")
    file.close()
    time_end = time.perf_counter()
    print(f"Время выполнения: {time_end - time_start:.6f} секунд")