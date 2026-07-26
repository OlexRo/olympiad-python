# =================================================================================
# Динамический массив (Vector) - массив с автоматическим изменением размера.
# =================================================================================
#
#   Внутреннее представление (capacity = 8, size = 4):
#  ┌─────────────────────────────────────────────────────────────────────────────┐
#  │  _array = [10, 20, 30, 40, None, None, None, None]                          │
#  │            ↑    ↑    ↑    ↑                                                 │
#  │          размер = 4 (активные элементы)                                     │
#  │          емкость = 8 (выделенная память)                                    │
#  └─────────────────────────────────────────────────────────────────────────────┘
#
#   При добавлении 5-го элемента:
#  ┌─────────────────────────────────────────────────────────────────────────────┐
#  │  _array = [10, 20, 30, 40, 50, None, None, None, None, None, None, None]    │
#  │            ↑    ↑    ↑    ↑    ↑                                            │
#  │          размер = 5, емкость = 16 (удвоилась)                               │
#  └─────────────────────────────────────────────────────────────────────────────┘
#
# =================================================================================

# Класс вектора
class Vector:
  def __init__(self, capacity = 4):
    self._capacity = capacity       # Выделенная память
    self._size = 0                  # Текущее количество элементов
    self._array = [None] * capacity # Внутренний массив

  # Магический метод для получения длины массива
  def __len__(self):
    return self._size

  # Магический метод для получения элемента по индексу
  def __getitem__(self, index):
    if index < 0 or index >= self._size:
      raise IndexError("Index out of range")
    return self._array[index]

  # Магический метод для установки элемента по индексу
  def __setitem__(self, index, value):
    if index < 0 or index >= self._size:
      raise IndexError("Index range of array")
    self._array[index] = value

  # Магический метод для итерации по массиву
  def __iter__(self):
    for i in range(self._size):
      yield self._array[i]

  # Магический метод для строкового представления
  def __str__(self):
    return f"[{', '.join(str(self._array[i]) for i in range(self._size))}]"

  # Геттер для возвращения текущего размер массива
  @property
  def size(self):
    return self._size

  # Геттер для возвращения текущей емкости массива
  @property
  def capacity(self):
    return self._capacity

  # Свойство для проверки пуст ли массив
  @property
  def is_empty(self):
    return self._size == 0

  # Приватный метод для изменения емкости массива
  def _resize(self, new_capacity):
    new_array = [None] * new_capacity # Создаем новый массив с новой емкостью
    for i in range(self._size):       # Копируем элементы из старого массива
      new_array[i] = self._array[i]
    self._array = new_array           # Заменяем старый массив новым
    self._capacity = new_capacity     # Обновляем емкость

  # Метод для очистки массива
  def clear(self):
    self._array = [None] * self._capacity # Пересоздаем массив с той же емкостью
    self._size = 0                        # Сбрасываем размер

  # Метод для поиска индекса элемента по значению
  def index(self, value):
    for i in range(self._size):   # Проходим по всем элементам
      if self._array[i] == value: # Если нашли совпадение
        return i                  # Возвращаем индекс
    raise ValueError(f"Value {value} not found")

  # Метод для добавления элемента в конец
  def append(self, value):
    if self._size == self._capacity:  # Если массив заполнен
      self._resize(self.capacity * 2) # Удваиваем емкость
    self._array[self._size] = value   # Вставляем элемент на первую свободную позицию
    self._size += 1                   # Увеличиваем размер

  # Метод для вставки элемента по индексу
  def insert(self, index, value):
    if index < 0 or index > self._size:   # Проверяем индекс
      raise IndexError("Index out of range")
    if self.size == self.capacity:        # Если массив заполнен
      self._resize(self.capacity * 2)     # Удваиваем емкость
    for i in range(self.size, index, -1): # Сдвигаем элементы вправо
      self._array[i] = self._array[i - 1]
    self._array[index] = value            # Вставляем элемент
    self._size += 1                       # Увеличиваем размер

  # Метод для удаления и возврата элемента по индексу
  def pop(self, index = None):
    if self._size == 0:                        # Проверяем, не пустой ли массив
      raise IndexError("Pop from empty array")
    if index is None:                          # Если индекс не указан
      index = self._size - 1                   # Удаляем последний элемент
    if index < 0 or index >= self._size:       # Проверяем индекс
      raise IndexError("Index out of range")
    value = self._array[index]                 # Сохраняем удаляемое значение
    for i in range(index, self._size - 1):     # Сдвигаем элементы влево
      self._array[i] = self._array[i + 1]
    self._size -= 1                            # Уменьшаем размер
    self._array[self._size] = None             # Очищаем последнюю ячейку
    if 0 < self._size <= self._capacity // 4:  # Если массив заполнен меньше чем на 25%
      self._resize(self.capacity // 2)         # Уменьшаем емкость вдвое
    return value                               # Возвращаем удаленное значение

  # Метод для удаления элемента по значению
  def delete(self, value):
    for i in range(self._size):   # Проходим по всем элементам
      if self._array[i] == value: # Если нашли совпадение
        self.pop(i)               # Удаляем по индексу
        return
    raise ValueError(f"Value {value} not found")