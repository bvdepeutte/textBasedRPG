from userCreation import characterCreation

def main():
    playercharacter = characterCreation()
    playercharacter.selectLiveForm()
    playercharacter.selectClass()
    print("After some rest, you need a moment to come up with a plan based on your strengths and weaknesses")
    playercharacter.selectTraits()

if __name__ == "__main__":
    main() 
