from caracteristics import Caracteristics
from traits import Traits
# Definition of default class
class Character:
    def __init__(self,name, character=None):
        self.name = name
        # default HP can be impacted by many other elements
        self.health = 0
        # default Stamina can be impacted by many other elements
        self.stamina = 0
        # default energy can be impacted by many other elements
        self.energy = 0
        # initialize the base caracteristics
        self.caracteristics = Caracteristics()
        # define if the player can select this class during the character creation
        self._playable = True
        # initialize the traits
        self.traits = Traits()
        # can the the character have enhancement
        self._canBeEnhanced = True
        # alive by default
        self.alive = True
        # will be used to store the character type (Human, Cyborg,ET,Robot,Animals)
        self._character = character
        #will be used to store the class
        self._Class = None
    
#    def move(self,direction):
#        if self.stamina > 5:
#            self.stamina -= 5
#            return print(f"You walk to the {direction.lower()}.")
#        else:
#            return print(f"Your stamina is too low:{self.stamina}. Refill it before making an action")

    def checkALive(self):
        if self.health == 0:
            self.alive = False
            return print(f"{self.name} is dead!")

    def getStatus(self):
    # By default a human don't need energy to function. Howerver, some enhancement can be added during the adventure. Those enhancement can require energy to function
        if self.traits["energy"]["enable"]:
            if self.health < 20:
                return print(f'''You are low health! You still have {self.health} hp.
                         You still have {self.stamina} stamina and {self.energy} energy''')
            elif self.energy < 20:
                return print(f'''Your energy level is low. You still have {self.energy} energy.
                            You still have {self.stamina} stamina and {self.health} hp''')
            else:
                return print(f'''You still have {self.health} hp.
                            You still have {self.stamina} stamina and {self.energy} energy''')            
        else:    
            if self.health < 20:
                return print(f'''You are low health! You still have {self.health} hp.
                             You still have {self.stamina} stamina.''')
            else:
                return (f'''You still have {self.health} hp.
                        You still have {self.stamina} stamina.''')

class Human(Character):
    def __init__(self,name):
        super().__init__(name,"Human")
        self.health = 100
        self.stamina = 100
        self.energy = 0


class Cyborg(Character):
     def __init__(self,name):
        super().__init__(name,"Cyborg")
        self.health = 100
        self.stamina = 100        
        self.energy = 75
        self.traits.traitSelection("energy")
        self.traits.traitSelection("iem")


class Robot(Character):
     def __init__(self,name):
        super().__init__(name,"Robot")
        self.health = 100
        self.stamina = 0        
        self.energy = 75
        self.traits.traitSelection("energy")
        self.traits.traitSelection("iem")

class Alien(Character):
     def __init__(self,name):
        super().__init__(name,"Alien")
        self.health = 150
        self.stamina = 150        
        self.energy = 150
        self._character = "Alien"

class Animal(Character):
    def __init__(self,name=""):
        super().__init__(name,"Animal")
        self.health = 120
        self.stamina = 120        
        self.energy = 0