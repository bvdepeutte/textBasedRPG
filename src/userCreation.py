from livesForm import Human,Cyborg

class characterCreation:

    def __init__(self):
        self.character = None

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