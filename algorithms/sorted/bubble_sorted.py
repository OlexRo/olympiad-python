def bubble_sorted(arr):
  print(f"Исходный массив: {arr}")
  for i in range(len(arr) - 1):
    swapped = False
    step = i + 1
    for j in range(len(arr) - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    print(f"Проход {step}: {arr}")  # Для наглядности
    if not swapped:
      print(f"Досрочный выход на проходе {step}")
      break
  print(f"Отсортированный массив: {arr}")
  return arr

nums = [64, 34, 25, 12, 22, 11, 90]
bubble_sorted(nums)
