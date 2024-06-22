# Definition of the Human Class
class Human:
    def __init__(self,name):
        self.name = name
        # default HP can be impacted by many other elements
        self.health = 100
        # default Stamina can be impacted by many other elements
        self.stamina = 100
        # default energy can be impacted by many other elements
        self.energy = 0

        self.caracteristics = {
            "strength": 1,
            "agility": 1,
            "constitution":1,
            "intelligence": 1,
            "luck": 1,
            "persuasion": 1,
            "stealth": 1,
            "speed": 1,
            "intiative": 1
            }
        # define if the player can select this class during the character creation
        self._playable = True

        self.weaknesses = ["poison",
                    "fire",
                    "acid",
                    "fear"
                    ]
        self.strength = ["social",
                    "adaptative",
                    "creative",
                    "partialHealing",
                    "easyLearner",
                    "nonEnergyBase"
                    ]
        self._canBeEnhanced = True
        self.alive = True
    
    def move(self,direction):
        if self.stamina > 5:
            self.stamina -= 5
            return print(f"You walk to the {direction.lower()}.")
        else:
            return print(f"Your stamina is too low:{self.stamina}. Refill it before making an action")

    def isALive(self):
        if self.health == 0:
            self.alive = False
            return print(f"{self.name} is dead!")

    def getStatus(self):
    # By default a human don't need energy to function. Howerver, some enhancement can be added during the adventure. Those enhancement can require energy to function
        if "nonEnergyBase" in self.strength and self.health < 20:
                return print(f'''You are low health! You still have {self.health} hp.
                             You still have {self.stamina} stamina.''')
        elif "nonEnergyBase" in self.strength:
            return (f'''You still have {self.health} hp.
                    You still have {self.stamina} stamina.''')
        elif "nonEnergyBase" not in self.strength and self.health < 20:
                return print(f'''You are low health! You still have {self.health} hp.
                             You still have {self.stamina} stamina and {self.energy} energy''')
        else:
                return print(f'''You still have {self.health} hp.
                             You still have {self.stamina} stamina and {self.energy} energy''')

class Cyborg(Human):
     def __init__(self):
          super().__init__()
          self.energy = 75
          
          # Adaptation of the weaknesses of the Human Class
          self.weaknesses.remove("fear")
          self.weaknesses.append("electromagnetic")

          # Adaptation of the strength of the Human Class
          self.strength.remove("nonEnergyBase")
          self.strength.append("partialMaintenance")
    
     def getStatus(self):
        if self.health < 20:
            return print(f'''You are low health! You still have {self.health} hp.
                         You still have {self.stamina} stamina and {self.energy} energy''')
        elif self.energy < 20:
             return print(f'''Your energy level is low. You still have {self.energy} energy.
                          You still have {self.stamina} stamina and {self.health} hp''')
        else:
            return print(f'''You still have {self.health} hp.
                          You still have {self.stamina} stamina and {self.energy} energy''')