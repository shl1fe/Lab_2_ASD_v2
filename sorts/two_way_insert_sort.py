def binary_search_for_insert(arr: list, target) -> int:
    """
       Бинарный поиск позиции для вставки элемента в отсортированный массив

       Args:
           arr (list): Отсортированный массив элементов
           target: Элемент для вставки

       Returns:
           int: Позиция для вставки элемента
       """
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid].compare_keys(target):
            right = mid
        else:
            left = mid + 1

    return left

def two_way_insert_sort(arr):
    """
       Сортировка двухпутевыми вставками с использованием бинарного поиска

       Args:
           arr (list): Массив элементов для сортировки

       Returns:
           list: Отсортированный массив
       """
    if len(arr) <= 1:
        return arr

    result = [arr[0]]

    for i in range(1, len(arr)):
        current = arr[i]
        pos = binary_search_for_insert(result, current)
        result.insert(pos, current)

    return result