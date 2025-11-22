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

def save_in_newFile(array_to_save: list[Key], filepath: str, filename: str = "out.txt"):
    """
        Сохранение отсортированного массива в файл

        Args:
            array_to_save (list): Массив для сохранения
            name_output_File (str): Имя выходного файла (без расширения)
        """
    file = open(f"{filepath+filename}", "w", encoding="utf-8")
    for i in array_to_save:
        file.write(f"{i}\n")
    file.close()

if __name__ == "__main__":
    df = read_data_from_file("static/input/input_1000000.txt")
    df = df[0:10000]
    time_start = time.perf_counter()
    sorted_DATA = quick_sort(df)
    time_end = time.perf_counter()

    print(f"Время выполнения Быстрая : {time_end - time_start:.6f} секунд")

    save_in_newFile(sorted_DATA, "static/out/")

    time_start = time.perf_counter()
    sorted_DATA = two_way_insert_sort(df)
    time_end = time.perf_counter()

    print(f"Время выполнения Двухпутевые вставки : {time_end - time_start:.6f} секунд")

    save_in_newFile(sorted_DATA, "static/out/", filename="out_stab.txt")
