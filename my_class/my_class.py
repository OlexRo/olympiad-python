from abc import ABC, abstractmethod

class LoggerMixin:
  def log(self, message: str):
    print(f"[{self.__class__.__name__}] {message}")

class Collar:
  def __init__(self, color: str, size: str = "M"):
    self.color = color
    self.size = size

  def __str__(self):
    return f"Collar (color='{self.color}', size='{self.size}')"

class Animal(ABC, LoggerMixin):
  _instance_counter = 0

  def __init__(self, name, age):
    super().__init__()
    Animal._instance_counter += 1
    self._id = Animal._instance_counter
    self._name = name
    self._age = age
    self.__energy = 100
    self.log(f"The instance created {self.__class__.__name__} #{self._id}")

  @property
  def id(self) -> str:
    return self._id

  @property
  def name(self) -> str:
    return self._name

  @property
  def age(self) -> int:
    return self._age

  @property
  def energy(self) -> int:
    return self.__energy

  @name.setter
  def name(self, value):
    if not value:
      raise ValueError("Name cannot empty")
    self._name = value

  @age.setter
  def age(self, value):
    if value < 0:
      raise ValueError("Age cannot be negative")
    self._age = value

  def move(self, distance) -> float:
    self.__energy = max(0, self.__energy - distance * 0.5)
    return f"{self._name} moved {distance}m. Energy: {self.__energy}"

  @classmethod
  def get_instance_count(cls) -> int:
    return cls._instance_counter

  @abstractmethod
  def speak(self) -> str:
    pass

  def __str__(self) -> str:
    return f"{self.__class__.__name__} (name = {self._name}), age = {self._age}, energy = {self.__energy}"

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}(name='{self._name}', age={self._age})"

  def __eq__(self, other) -> bool:
    if not isinstance(other, Animal):
      return False
    return self._name == other._name and self._age == other._age

  def __lt__(self, other) -> bool:
    if not isinstance(other, Animal):
      return NotImplemented
    return self._age < other._age

  def __hash__(self):
    return hash((self.name, self.age))

class Dog(Animal):
  _species = "Canis familiaris"

  def __init__(self, name, age, breed = "Mixed"):
    super().__init__(name, age)
    self._breed = breed
    self._collar = Collar("red", "L")

  @property
  def breed(self) -> str:
    return self._breed

  @property
  def collar(self) -> Collar:
    return self._collar

  @breed.setter
  def breed(self, value: str):
    if not value:
      raise ValueError("Breed cannot be empty")
    self._breed = value

  def speak(self) -> str:
    return f"{self._name} says: Woof!"

  @staticmethod
  def info() -> str:
    return "Dogs are amazing!"

  @classmethod
  def from_dict(cls, data: dict) -> "Dog":
    return cls(data["name"], data["age"])

  @classmethod
  def get_species(cls) -> str:
    return cls._species

  def __str__(self) -> str:
    return f"🐕 Dog(name='{self._name}', age={self._age}, breed='{self._breed}')"
