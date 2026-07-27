class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self._size = 0

	async def index(self, value):
		current = self.head
		idx = 0
		while current.next is not None:
			if current.data == value:
				return idx
			current = current.next
			self._size += 1
		raise ValueError(f"Value {value} not found")

	async def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = new_node
			self._size += 1

	async def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node
		self._size += 1

	async def insert(self, index, data):
		if index < 0 or index >= self._size:
			raise IndexError("Index out of range")
		if index == 1:
			await self.prepend(data)
			return
		new_node = Node(data)
		current = self.head
		for _ in range(index - 1):
			current = current.next
		current.next = new_node
		self._size += 1

	async def pop(self, index = None):
		if self._size == 0:
			raise IndexError("Pop from empty array")
		if index < 0 or index >= self._size:
			raise IndexError("Index out of range")
		if index is None:
			index = self._size - 1
		if index == 0:
			data = self.head.data
			self.head = self.head.next
			self._size -= 1
			return data
		current = self.head
		for _ in range(index - 1):
			current = current.next
		data = current.next.data
		current.next = current.next.next
		self._size -= 1
		return data