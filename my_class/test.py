from abc import ABC, abstractmethod

# Миксин для логирования
class LoggerMixin:
  def log(self, message: str):
    print(f"[{self.__class__.__name__}] {message}")

# Композиция
class Collar:
  def __init__(self, color: str, size: str = "M"):
    self.color = color
    self.size = size

  def __str__(self):
    return f"Collar(color='{self.color}', size='{self.size}')"

# Абстрактный класс (аналог интерфейса)
class Animal(ABC, LoggerMixin):
  # Переменная класса (общая для всех экземпляров)
  _instance_count = 0

  # Конструктор
  def __init__(self, name: str, age: int):
    super().__init__()                #
    self._name = name                 # Защищенное поле (protected)
    self._age = age                   # Защищенное поле (protected)
    self.__energy = 100               # Приватное поле (private)
    Animal._instance_count += 1       # Счётчик экземпляров
    self._id = Animal._instance_count #
    self.log(f"Created {self.__class__.__name__} #{self._id}")

  # Геттер для получения защищенного поля _name
  @property
  def name(self) -> str:
    return self._name

  # Геттер для получения защищенного поля _age
  @property
  def age(self) -> int:
    return self._age

  # Геттер для получения приватного поля __energy
  @property
  def energy(self) -> int:
    return self.__energy

  # Геттер для получения приватного поля _id
  @property
  def id(self) -> int:
    return self._id

  # Сеттер для установления значения в защищенное поле _name
  @name.setter
  def name(self, value: str):
    if not value:
      raise ValueError("Name cannot by empty.")
    self._name = value

  # Сеттер для установления значения в защищенное поле _age
  @age.setter
  def age(self, value: int):
    if not value:
      raise ValueError("Value cannot be empty")
    self._age = value

  # Общий метод
  def move(self, distance: float) -> str:
    self.__energy = max(0, self.__energy - distance * 0.5)
    return f"{self._name} moved {distance} meters. Energy: {self.__energy}"

  # Статический метод
  @staticmethod
  def get_kingdom() -> str:
    return "Kingdom: Animalia"

  # Абстрактный метод (нужно будет перопределить в подклассе)
  @abstractmethod
  def speak(self) -> str:
    pass

  # Переопределение метода для
  def __str__(self):
    return f"{self.__class__.__name__}(name='{self._name}', age={self._age})"

  # Переопределение метода для
  def __eq__(self, other) -> bool:
    if not isinstance(other, Animal):
      return False
    return self._name == other._name and self._age == other._age

  # Переопределение метода для хеширования
  def __hash__(self):
    return hash((self.name, self.age))

# Класс наследующийся от абстрактного класса
class Dog(Animal):
  # Переменная класса (общая для всех экземпляров)
  _species = "Canis familiaris"

  # Конструктор
  def __init__(self, name: str, age: int):
    super().__init__(name, age)       # Вызов родителького конструктора
    self._tricks = []                 # Приватный метод
    self._collar = Collar("red", "L") # Композиция

  # Геттер для получения защищенного поля _tricks (copy – чтобы не изменили из вне)
  @property
  def tricks(self) -> list:
    return self._tricks.copy()

  # Реализация метода из абстрактного класса (интерфейса)
  def speak(self) -> str:
    return f"{self._name} says: Woof!"

  # Общий метод
  def learn_trick(self, trick: str) -> str:
    self._tricks.append(trick)
    return f"{self._name} learned '{trick}'!"

  # Общий метод
  def show_tricks(self) -> list:
    return self._tricks

  # Статический метод
  @staticmethod
  def info() -> str:
    return "Dogs are amazing!"

  # Метод класса (альтернативный конструктор)
  @classmethod
  def from_dict(cls, data: dict) -> "Dog":
    return cls(data["name"], data["age"])

  # Переопределение метода для
  def __str__(self):
    return f"🐕 Dog(name='{self._name}', age={self._age})"

# Особенности ООП в python:
# Нет new — просто вызывай класс как функцию
# Нет перегрузки методов — используй параметры по умолчанию
# Нет настоящих приватных — всё по договорённости
# Множественное наследование — возможно!
# @property — геттеры/сеттеры как в JavaBeans, но красивее
# Магические методы — перегрузка операторов
# *args и **kwargs — гибкие сигнатуры функций
# Dataclasses — сокращают бойлерплейт

# Что такое композиции, что такое миксин, что такое классовой переменной

# Композиция — это когда один объект содержит внутри себя другие объекты.
# Вместо того чтобы наследовать функциональность (IS-A), объект использует
# другие объекты (HAS-A).

# Миксин — это небольшой класс, который добавляет конкретную функциональность
# другим классам через множественное наследование. Миксин не предназначен
# для самостоятельного использования — он только "примешивается" к другим классам.

# Переменная класса — это переменная, которая принадлежит самому классу, а
# не его экземплярам. Она общая для всех экземпляров этого класса.
