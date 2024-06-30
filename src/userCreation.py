from livesForm import Human,Cyborg
import time

class characterCreation:

    def __init__(self):
        self.character = None
        self.classSelection = None

    def slowPrint(text, delay=0.1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # Move to the next line after printing the text

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
            self.slowPrint("There was a battle, one of the greatest you have ever seen. You are trying to remember it... you don't know why but it hurts, way worse than any physical pain... ")
            self.slowPrint("And your arm... your arm is killing you even if...")
            time.sleep(2)
            self.slowPrint("You are now on a medical ship taking you away, away from Hell. You'll be able to rest, at least for a while...")
        
        if self.classSelection.lower() == "trader":
            self.slowPrint("What a year. You've made a lot of money thank's to the crusade against the Ennemy but you've almost lost everything. How is it possible?")
            time.sleep(0.5)
            self.slowPrint("")
            self.slowPrint("There was a battle, one of the greatest you have ever seen. You are trying to remember it... you don't know why but it hurts, way worse than any physical pain... ")
            self.slowPrint("And your arm... your arm is killing you even if...")
            time.sleep(2)
            self.slowPrint("You are now on a medical ship taking you away, away from Hell. You'll be able to rest, at least for a while...")
            # total value = 45

        if self.classSelection.lower() == "pilot":
            pass
            # total value = 45

        if self.classSelection.lower() == "farmer":
            pass
            # total value = 45    
    
    def classImpact(self):
        if self.classSelection.lower() == "soldier":
            self.character.caracteristics["strength"] = 7
            self.character.caracteristics["agility"] = 4
            self.character.caracteristics["constitution"] = 3
            self.character.caracteristics["intelligence"] = 4
            self.character.caracteristics["luck"] = 3
            self.character.caracteristics["persuassion"] = 3
            self.character.caracteristics["stealth"] = 5
            self.character.caracteristics["speed"] = 6
            self.character.caracteristics["initiative"] = 5
            # total value = 40
        
        if self.classSelection.lower() == "trader":
            self.character.caracteristics["strength"] = 2
            self.character.caracteristics["agility"] = 2
            self.character.caracteristics["constitution"] = 5
            self.character.caracteristics["intelligence"] = 8
            self.character.caracteristics["luck"] = 5
            self.character.caracteristics["persuassion"] = 8
            self.character.caracteristics["stealth"] = 1
            self.character.caracteristics["speed"] = 3
            self.character.caracteristics["initiative"] = 6
            # total value = 40

        if self.classSelection.lower() == "pilot":
            self.character.caracteristics["strength"] = 4
            self.character.caracteristics["agility"] = 7
            self.character.caracteristics["constitution"] = 5
            self.character.caracteristics["intelligence"] = 7
            self.character.caracteristics["luck"] = 3
            self.character.caracteristics["persuassion"] = 1
            self.character.caracteristics["stealth"] = 1
            self.character.caracteristics["speed"] = 5
            self.character.caracteristics["initiative"] = 7
            # total value = 40

        if self.classSelection.lower() == "farmer":
            self.character.caracteristics["strength"] = 6
            self.character.caracteristics["agility"] = 5
            self.character.caracteristics["constitution"] = 8
            self.character.caracteristics["intelligence"] = 4
            self.character.caracteristics["luck"] = 5
            self.character.caracteristics["persuassion"] = 2
            self.character.caracteristics["stealth"] = 2
            self.character.caracteristics["speed"] = 3
            self.character.caracteristics["initiative"] = 5
            # total value = 40