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
            self.slowPrint("It was supposed to be a quick and painless victory...")
            time.sleep(2)            
            self.slowPrint("Now you are save, the medical shuttle will bring you back to safety")
            self.slowPrint("You'll be able to start the trades as soon as you land in the next statioport")

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
            # TODO => add traits for each class based on story
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