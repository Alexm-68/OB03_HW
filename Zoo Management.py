# 1. Базовый класс Animal
# Базовый класс, представляющий общее поведение и характеристики всех животных.
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age    # Возраст животного

    def make_sound(self):
        # Метод, который будет переопределен в подклассах для специфических звуков
        pass

    def eat(self):
        # Метод для вывода информации о том, что животное ест
        print(f"{self.name} ест.")

# 2. Подклассы, наследующие от Animal
# Подкласс Bird, представляющий птиц
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Размах крыльев, специфический атрибут для птиц

    def make_sound(self):
        # Переопределение метода для звуков птиц
        print(f"{self.name} чирикает.")

    def fly(self):
        # Метод, показывающий способность летать
        print(f"{self.name} летит с размахом крыльев {self.wing_span} м.")

# Подкласс Mammal, представляющий млекопитающих
class Mammal(Animal):
    def __init__(self, name, age, diet):
        super().__init__(name, age)
        self.diet = diet  # Диета, специфический атрибут для млекопитающих

    def make_sound(self):
        # Переопределение метода для звуков млекопитающих
        print(f"{self.name} ревет.")

    def describe_diet(self):
        # Метод, описывающий диету животного
        print(f"{self.name} питается {self.diet}.")

# Подкласс Reptile, представляющий рептилий
class Reptile(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat  # Среда обитания, специфический атрибут для рептилий

    def make_sound(self):
        # Переопределение метода для звуков рептилий
        print(f"{self.name} шипит.")

    def describe_habitat(self):
        # Метод, описывающий среду обитания
        print(f"{self.name} обитает в {self.habitat}.")

# 3. Полиморфизм
# Функция, демонстрирующая полиморфизм, вызывая метод make_sound для каждого животного


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()