from livesForm import Human,Cyborg
import time

class characterCreation:

    def __init__(self):
        self.character = None
        self.classSelection = None

    def slowPrint(self, text, delay=0.01):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def selectLiveForm(self):
        print('''Select your character origin:
              - Human
              - Cyborg''')
        temp = input()
        while temp.lower() not in ["human","cyborg"]:
            print("Please input a correct value: Human, Cyborg")
            temp = input()
        if temp.lower() == "human":
            self.character = Human("Default Name")
        elif temp.lower() == "cyborg":
            self.character = Cyborg("Default Name")
        print(f"You have selected a {self.character._character} character")
        return self.character
    
    def selectClass(self):
        print("During the past decades, you've dedicated your life to your job as a...")
        print('''Select a class:
              - Soldier
              - Trader
              - Pilot
              - Farmer''')
        self.classSelection = input()
        while self.classSelection.lower() not in ["soldier","trader","pilot","farmer"]:
            print("Please input a correct value (Warrior, Trader, Pilot, Farmer)")
            self.classSelection = input()
        if self.classSelection.lower() == "soldier":
            self.slowPrint("You have been fighting for the last 3 years against the Ennemy. You've shed tears, sweat and blood for the Motherland.")
            self.slowPrint("There was a battle, one of the greatest you have ever seen. You are trying to remember it... you don't know why yet but it hurts, way worse than your wounds... ")
            time.sleep(2)
            self.slowPrint("Looking down, you can only see a limb instead of your left arm")
            self.slowPrint("But now you are safe on a medical ship taking you away... Away from Hell. You'll be able to rest, at least for a while...")
        
        if self.classSelection.lower() == "trader":
            self.slowPrint("What a year. You've made a lot of money thank's to the army... but you've almost lost everything. How is it possible?")
            time.sleep(0.5)
            self.slowPrint("It was supposed to be a quick and painless victory... All your investments are gone")
            time.sleep(2)            
            self.slowPrint("Now you are save, the medical shuttle will bring you back to safety")
            self.slowPrint("'As soon as we hit the ground, I'll take back what's mine'")

        if self.classSelection.lower() == "pilot":
            self.slowPrint("You check the direction one last time before taking a quick break.")
            time.sleep(0.5)
            self.slowPrint("It's all good, you are away from this madness. This assignement was supposed to be a punition, it's a blessing")
            time.sleep(2)            
            self.slowPrint("Are they ok?")
            self.slowPrint("You don't want to think about this, there are already enough sleepless night")

        if self.classSelection.lower() == "farmer":
            self.slowPrint("What has happened? A gold digging colony, the new american dream, what a bullshit")
            self.slowPrint("You've worked hard for the last 5 years...")
            time.sleep(1)
            self.slowPrint("for what? for nothing...")            
            self.slowPrint("Anxiety, fear, sadness, you can't take it anymore")
            self.slowPrint("They better help me or I don't answer to myself anymore...")
        
        self.classImpact(self.classSelection)

    def classImpact(self,selection):
        if selection.lower() == "soldier":
            self.character.caracteristics.caracteristics["strength"] = 7
            self.character.caracteristics.caracteristics["agility"] = 4
            self.character.caracteristics.caracteristics["constitution"] = 3
            self.character.caracteristics.caracteristics["intelligence"] = 4
            self.character.caracteristics.caracteristics["luck"] = 3
            self.character.caracteristics.caracteristics["persuassion"] = 3
            self.character.caracteristics.caracteristics["stealth"] = 5
            self.character.caracteristics.caracteristics["speed"] = 6
            self.character.caracteristics.caracteristics["initiative"] = 5
            self.character._Class = "Soldier"
            self.character.traits.traits["amputee"]["available"] = True
            self.character.traits.traitSelection("amputee")
            # total value = 40
        
        if selection.lower() == "trader":
            self.character.caracteristics.caracteristics["strength"] = 2
            self.character.caracteristics.caracteristics["agility"] = 2
            self.character.caracteristics.caracteristics["constitution"] = 5
            self.character.caracteristics.caracteristics["intelligence"] = 8
            self.character.caracteristics.caracteristics["luck"] = 5
            self.character.caracteristics.caracteristics["persuassion"] = 8
            self.character.caracteristics.caracteristics["stealth"] = 1
            self.character.caracteristics.caracteristics["speed"] = 3
            self.character.caracteristics.caracteristics["initiative"] = 6
            self.character._Class = "Trader"
            self.character.traits.traitSelection("greed")
            # total value = 40

        if selection.lower() == "pilot":
            self.character.caracteristics.caracteristics["strength"] = 4
            self.character.caracteristics.caracteristics["agility"] = 7
            self.character.caracteristics.caracteristics["constitution"] = 5
            self.character.caracteristics.caracteristics["intelligence"] = 7
            self.character.caracteristics.caracteristics["luck"] = 3
            self.character.caracteristics.caracteristics["persuassion"] = 1
            self.character.caracteristics.caracteristics["stealth"] = 1
            self.character.caracteristics.caracteristics["speed"] = 5
            self.character.caracteristics.caracteristics["initiative"] = 7
            self.character._Class = "Pilot"
            self.character.traits.traitSelection("rebel")
            # total value = 40

        if selection.lower() == "farmer":
            self.character.caracteristics.caracteristics["strength"] = 6
            self.character.caracteristics.caracteristics["agility"] = 5
            self.character.caracteristics.caracteristics["constitution"] = 8
            self.character.caracteristics.caracteristics["intelligence"] = 4
            self.character.caracteristics.caracteristics["luck"] = 5
            self.character.caracteristics.caracteristics["persuassion"] = 2
            self.character.caracteristics.caracteristics["stealth"] = 2
            self.character.caracteristics.caracteristics["speed"] = 3
            self.character.caracteristics.caracteristics["initiative"] = 5
            self.character._Class = "Farmer"
            self.character.traits.traitSelection("asocial")
            # total value = 40