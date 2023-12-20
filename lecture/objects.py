class Dog:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = age

    def speak(self):
        print(f'{self.name} says "Borf"')


dog1 = Dog('Boo', 14)

dog1.speak()
dog2 = Dog('Kimchee', 5)
dog2.speak()


