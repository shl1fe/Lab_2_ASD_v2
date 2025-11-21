def quick_sort(arr):
    """
      Быстрая сортировка (Quick Sort) с использованием стека (нерекурсивная версия)

      Args:
          arr (list): Массив элементов для сортировки

      Returns:
          list: Отсортированный массив
      """
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