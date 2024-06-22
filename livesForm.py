# Definition of the Human Class
class Human:
    def __init__():
        _defaultHealth = 100 #100 hp by default
        caracteristics = {
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
        _playable = True

        weaknesses = ["poison",
                    "fire",
                    "acid",
                    "fear"
                    ]
        strength = ["social",
                    "adaptative",
                    "creative",
                    "partialHealing",
                    "easyLearner"
                    ]
        _canBeEnhanced = True
    
    def mapMovement(self,direction):
        print(f"You walk to the {direction}.")
    

