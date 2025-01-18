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

# 4. Класс Zoo
# Класс Zoo, который содержит информацию о животных и сотрудниках
class Zoo:
    def __init__(self, name):
        self.name = name  # Название зоопарка
        self.animals = []  # Список животных в зоопарке
        self.staff = []    # Список сотрудников зоопарка

    def add_animal(self, animal):
        # Метод для добавления животного в зоопарк
        self.animals.append(animal)

    def add_staff(self, employee):
        # Метод для добавления сотрудника в зоопарк
        self.staff.append(employee)

    def show_animals(self):
        # Метод для отображения всех животных в зоопарке
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name} ({animal.__class__.__name__}), возраст: {animal.age}")

# 5. Классы сотрудников
# Класс ZooKeeper, представляющий смотрителя зоопарка
class ZooKeeper:
    def feed_animal(self, animal):
        # Метод для кормления животного
        print(f"Смотритель кормит {animal.name}.")

# Класс Veterinarian, представляющий ветеринара
class Veterinarian:
    def heal_animal(self, animal):
        # Метод для лечения животного
        print(f"Ветеринар лечит {animal.name}.")

# Создание объектов и тестирование функциональности
zoo = Zoo("Городской зоопарк")

# Создание объектов животных с уникальными атрибутами
parrot = Bird("Попугай", 3, 0.5)  # Размах крыльев 0.5 м
tiger = Mammal("Тигр", 5, "мясо")  # Диета: мясо
snake = Reptile("Змея", 2, "джунгли")  # Среда обитания: джунгли

# Добавление животных в зоопарк
zoo.add_animal(parrot)
zoo.add_animal(tiger)
zoo.add_animal(snake)

# Создание объектов сотрудников
keeper = ZooKeeper()
vet = Veterinarian()

# Добавление сотрудников в зоопарк
zoo.add_staff(keeper)
zoo.add_staff(vet)

# Проверка работы методов
# Демонстрация полиморфизма: каждый объект животного вызывает свой метод make_sound
animal_sound(zoo.animals)

# Демонстрация методов сотрудников
keeper.feed_animal(tiger)
vet.heal_animal(snake)

# Вывод информации о животных
zoo.show_animals()