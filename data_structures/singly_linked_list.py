# Односвязный – узел хранит ссылку на следующий узел
# Двусвязный – узел хранит ссылки на следедующий и предыдущий узел
# Кольцевой – узел хранит ссылки на следедующий, предыдущий и последний узел ссылается на первый узел

# Класс узла (один элемент списка)
class Node:
  def __init__(self, data):
    self.data = data # Данные которые хранит узел
    self.next = None # Ссылка на следующий узел

# Класс односвязного списка
class SinglyLinkedList:
  def __init__(self):
    self.head = None # Ссылка на первый узел списка
    self._size = 0   # Кол-во элементов в списке

  # Метод для поиска элемента по значению (возвращает индекс)
  def index(self, value):
    current = self.head         # Текущий узел
    idx = 0                     # Индекс ткущего узла
    while current:              # Пока current не None
      if current.data == value: # Проверка: равные ли данные в текущем узле value
        return idx              # Если да – возвращаем индекс value
      current = current.next    # Если нет – переходим к следующему узлу
      idx += 1.                 # Увеличиваем индекс на 1 (теперь idx указывает на след. элемент)
    raise ValueError(f"Value {value} not found")

  # Метод для добавления элемента в конец списка
  def append(self, data):
    new_node = Node(data)             # Создаем новый узел
    if self.head is None:             # Проверяемый пустой ли список
      self.head = new_node            # Если да – то новый узел становится первым
    else:                             # Если нет – находим последний узел
      current = self.head             # Начинаем с первого
      while current.next is not None: # Идем по по цепочке узлом, пока не найдем последний (у последнего next = None)
        current = current.next
      current.next = new_node         # Присоединяем новый узел в конец
    self._size += 1                   # Увеличиваем размер списка

  # Метод для добавления элемента в начало списка
  def prepend(self, data):
    new_node = Node(data)     # Создаем новый узел
    new_node.next = self.head # Новый узел указывает на старую голову списка
    self.head = new_node      # Новый узел становится первым элементом списка
    self._size += 1           # Увеличаем размер списка на 1

  # Метод для вставки элемента по индексу в список
  def insert(self, index, data):
    if index < 0 or index > self._size:      # Проверяем, что индекс в допустимом диапазоне
      raise IndexError("Index out of range")
    if index == 0:                           # Провереям равен ли индекс 0
      self.prepend(data)                     # Если индекс 0, то вставляем в начало списка
      return                                 # Прерываем метод
    new_node = Node(data)                    # Создаем новый узел
    current = self.head                      # Начинаем с первого
    for _ in range(index - 1):               # Идем до узла, который находится перед местом вставки
      current = current.next
    new_node.next = current.next             # Новый узел указывает на тот, что был на позиции index
    current.next = new_node                  # Предыдущий узел (на позиции index - 1) теперь указывает на новый узел
    self._size += 1                          # Увеличиваем размер списка

  # Метод для удаления и возвращения элемента
  def pop(self, index = None):
    if self._size == 0:                       # Проверяем пустой ли список
      raise IndexError("Pop from empty list")
    if index is None:                         # Проверяем, что индекс указан, если нет, указываем индекс последнего элемента
      index = self._size - 1
    if index < 0 or index >= self._size:      # Проверяем, что индекс в допустимом диапазоне
      raise IndexError("Index out of range")
    if index == 0:                            # Удаляем первый элемент если индекс 0
      data = self.head.data                   # Сохраняем данные удаляемого узла
      self.head = self.head.next              # Голова теперь указывает на второй узел
      self._size -= 1                         # Уменьшаем размер списка
      return data                             # Возвращаем сохранённые данные
    current = self.head                       # Начинаем с головы списка, если удалем не первый
    for _ in range(index - 1):                # Идем к узлу, который находится перед удаляемым
      current = current.next
    data = current.next.data                  # Сохраняем данные удаляемого узла
    current.next = current.next.next          # Перепрыгиваем через удаляемый узел
    self._size -= 1                           # Уменьшаем размер списка
    return data                               # Возвращаем сохранённые данные

  def __len__(self):
    return self._size

  def __getitem__(self, index):
    if index < 0 or index >= self._size:
      raise IndexError("Index out of range")
    current = self.head
    for _ in range(index):
      current = current.next
    return current.data

  def __iter__(self):
    current = self.head
    while current:
      yield current.data
      current = current.next

  def __str__(self):
    return f"[{', '.join(str(item) for item in self)}]"

  def __repr__(self):
    return self.__str__()
