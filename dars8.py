class Animal:
  
  def sound(self):
    pass

class Dog(Animal):
  
  def sound(self):
    return f'Woof!'

class Cat(Animal):

  def sound(self):
    return f'Meow!'

class Bird(Animal):
  
  def sound(self):
    return f'chirp and sings!'
  
dog = Dog()
cat = Cat()
bird = Bird()

for animal in [dog,cat,bird]:
  print(animal.sound())

##########################

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")


class China():
    def capital(self):
        print("Beijing is the capital of China.")

    def language(self):
        print("Mandarin Chinese is the official language of China.")


ind = India()
usa = USA()
china = China()
for country in (ind, usa, china):
    country.capital()
    country.language()


#############################

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     

for x in (car1, boat1, plane1):
  x.move()