# ===============================================================================
# Стек (Stack) - LIFO (Last In, First Out) – на основе односвязного списка O(1)
# ===============================================================================
#
#  push(10)     push(20)     push(30)     pop() -> 30   pop() -> 20
#
#       top          top          top          top           top
#        │            │            │            │             │
#        ▼            ▼            ▼            ▼             ▼
#    ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐       ┌─────┐
#    │     │      │ 20  │      │ 30  │      │ 20  │       │ 10  │
#    │     │      │  │  │      │  │  │      │  │  │       │  │  │
#    │     │      └─────┘      └─────┘      └─────┘       └─────┘
#    │     │      ┌─────┐      ┌─────┐      ┌─────┐       ┌─────┐
#    │     │      │ 10  │      │ 20  │      │ 10  │       │     │
#    └─────┘      └─────┘      └─────┘      └─────┘       └─────┘
#    ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐
#    │ 10  │      │ 10  │      │ 10  │      │     │
#    └─────┘      └─────┘      └─────┘      └─────┘
#
# ===============================================================================

# Класс узла
class Node:
	def __init__(self, data):
		self.data = data  # Данные, которые хранит узел
		self.next = None  # Ссылка на следующий узел

# Класс стека
class Stack:
	def __init__(self):
		self._top = None # Вершина стека
		self._size = 0   # Количество элементов

	# Магический метод для получения длины массива
	def __len__(self):
		return self._size

	# Магический метод для строкового представления
	def __str__(self):
		values = []
		current = self._top
		while current:
			values.append(str(current.data))
			current = current.next
		return f"Stack({', '.join(values)})"

	# Магический для возвращения в строковом представлении для разработчиков
	def __repr__(self):
		return self.__str__()

	# Метод для преобразования стека в список
	def to_list(self):
		return list(self)

	# Свойство для проверки пуст ли массив
	def is_empty(self):
		return self._size == 0

	# Метод для добавления элемента на вершину стека
	def push(self, value):
		new_node = Node(value)    # Создаём новый узел
		new_node.next = self._top # Новый узел указывает на старую вершину
		self._top = new_node      # Новый узел становится вершиной
		self._size += 1

	# Метод для Удаления и возвращения элемента с вершины стека
	def pop(self):
		if self._size == 0:
			raise IndexError("Pop from empty stack")
		value = self._top.data     # Сохраняем данные вершины
		self._top = self._top.next # Перемещаем вершину на следующий узел
		self._size -= 1
		return value

	# Метод для возвращения элемента на вершине стека без удаления
	def peek(self):
		if self._size == 0:
			raise IndexError("Peek from empty stack")
		return self._top.data