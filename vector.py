class Vector:
  def __init__(self, capacity = 4):
    self._capacity = capacity
    self._size = 0
    self._array = [None] * capacity

  def __len__(self):
    return self._size

  def __getitem__(self, item):
    return self._array[item]

  def __setitem__(self, key, value):
    if key < 0 or key >= self._size:
      raise IndexError("Index out of range")
    self._array[key] = value

  def __iter__(self):
    for i in range(self._size):
      yield self._array[i]

  def __str__(self):
    return f"[{', '.join(str(self._array[i]) for i in range(self._size))}]"

  def __repr__(self):
    return self.__str__()

  @property
  def size(self):
    return self._size

  @property
  def capacity(self):
    return self._capacity

  @property
  def is_empty(self):
    return self._size == 0

  def clear(self):
    self._size = 0
    self._array = [None] * self._capacity

  def _resize(self, new_capacity):
    new_array = [None] * new_capacity
    for i in range(self._size):
      new_array[i] = self._array[i]
    self._array = new_array
    self._capacity = new_capacity

  def index(self, value):
    for i in range(self._size):
      if self._array[i] == value:
        return i
    raise ValueError(f"Value {value} not found")

  def append(self, value):
    if self._size == self._capacity:
      self._resize(self._capacity * 2)
    self._array[self._size] = value
    self._size += 1

  def insert(self, key, value):
    if key < 0 or key >= self._size:
      raise IndexError("Index out of range")
    if self._size == self._capacity:
      self._resize(self._capacity * 2)
    for i in range(self._size, key, -1):
      self._array[i] = self._array[i - 1]
    self._array[key] = value
    self._size += 1

  def pop(self, key = None):
    if self._size == 0:
      raise IndexError("Pop from empty array")
    if key is None:
      key = self._size - 1
    if key < 0 or key >= self._size:
      raise IndexError("Index out of range")
    value = self._array[key]
    for i in range(key, self._size - 1):
      self._array[i] = self._array[i + 1]
    self._size -= 1
    self._array[self._size] = None
    if 0 < self._size <= self._capacity // 4:
      self._resize(self._capacity // 2)
    return value

  def remove(self, value):
    for i in range(self._size):
      if self._array[i] == value:
        self.pop(i)
        return
    raise ValueError(f"Value {value} not found")