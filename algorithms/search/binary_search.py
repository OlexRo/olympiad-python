def binary_search(arr, el):
  start = 0
  end = len(arr) - 1
  while start <= end:
    middle = (start + end) // 2
    current = arr[middle]
    if current == el:
      print(f"Элемент {arr[middle]} на {middle} индексе")
      return middle
    elif current < el:
      print("Элемент меньше сдвигаемся вправо")
      start = middle + 1
    else:
      print("Элемент больше сдвигаемся влево")
      end = middle - 1
  print(f"Элемент {el} не найден")
  return - 1
