def binary_search(arr, el):
  start = 0
  end = len(arr) - 1
  while start <= end:
    middle = (start + end) // 2
    current = arr[middle]
    if current == el:
      return middle
    elif current < el:
      start = middle + 1
    else:
      end = middle - 1
  return -1
