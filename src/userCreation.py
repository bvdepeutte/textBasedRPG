from livesForm import Human,Cyborg

class characterCreation:

    def __init__(self):
        self.character = None

    def selectLiveForm(self):
        print('''Select your character origin:
              - Human
              - Cyborg
              - Robot''')
        temp = input()
        while temp.lower not in ["human","cyborg","robot"]:
            print("Please input a correct value: Human, Cyborg, Robot")
            temp = input()
        if temp.lower == "human":
            self.character = Human

        elif temp.lower == "cyborg":
            self.character = Cyborg