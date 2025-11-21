import time
from models.key import Key
from models.date import Date
from models.fio import FIO
from sorts.quick_sort import quick_sort
from sorts.two_way_insert_sort import two_way_insert_sort

def read_data_from_file(filename):
    """
       Чтение данных из файла и преобразование в список объектов Key

       Args:
           filename (str): Имя файла для чтения

       Returns:
           list: Список объектов Key
       """
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

def save_in_newFile(array_to_save : list, name_output_File : str):
    """
        Сохранение отсортированного массива в файл

        Args:
            array_to_save (list): Массив для сохранения
            name_output_File (str): Имя выходного файла (без расширения)
        """
    file = open(f"{name_output_File}.txt", "w", encoding="utf-8")
    for i in array_to_save:
        file.write(f"{i}\n")
    file.close()

if __name__ == "__main__":
    DATA_for_sort = read_data_from_file("input_1000000.txt")

    print("\n")

    time_start = time.perf_counter ()

    sorted_DATA = quick_sort(DATA_for_sort)

    time_end = time.perf_counter()
    print(f"Время выполнения Быстрая : {time_end - time_start:.6f} секунд")

    save_in_newFile(sorted_DATA, "output_input_1000000")

    time_start = time.perf_counter()

    sorted_DATA = two_way_insert_sort(DATA_for_sort)

    time_end = time.perf_counter()

    print(f"Время выполнения Двухпутевые вставки : {time_end - time_start:.6f} секунд")