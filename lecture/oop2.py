class Pet:
    petsAreAgitated = False

    @staticmethod
    def patpatpat():
        Pet.petsAreAgitated = False

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.isAgitated = False
    def speak(self):
        if Pet.petsAreAgitated == False:
            print(f'{self.name}: bork')
        else:
            print(f'{self.name}: BORKBORKBORK')
        Pet.petsAreAgitated = True     


    def __repr__(self):
        return f"Pet {self.name} is {self.age} years old"
        
    def __eq__(self, other):
        return (isinstance(other,Pet) and (self.name == other.name) 
                                        and (self.age == other.age))
 
class Axolotl(Pet):
    def __init__(self, name, age, numberOfGills):
        super().__init__(name, age)
        self.gills = numberOfGills
        self.name = name
        self.age = age

    def blowBubble(self):
        print('***bubb***')

    def speak(self):
        print(f"{self.name}: BEEP BEEP")



s = Pet("Spot", 5)
c = Axolotl("Chee", 5 , 6)

s.speak()
Pet.petsAreAgitated = True
s.speak()
Pet.patpatpat()
c.speak()
c.blowBubble()

print(s==c)