class traits:
    def __init__(self):
        self.traits = {
            "poison":{
                "name":"Poison resistance",
                "description": "The character takes less damage from poison",
                "effect":{
                    "damageRatio": 0.75,
                    "description":"Resistance to poison"
                },
                "value":7,
                "enable":False,
                "available":True,
                "exclusive":None  
                },
            "fire":{
                "name":"Fire resistance",
                "description": "The character takes less damage from fire",
                "effect":{
                    "damageRatio": 0.75,
                    "description":"Resistance to fire"
                },
                "value":7,
                "enable":False,
                "available":True,
                "exclusive":None  
                },
            "acid":{
                "name":"Acid resistance",
                "description": "The character takes less damage from acid",
                "effect":{
                    "damageRatio": 0.75,
                    "description":"Resistance to acid"
                },
                "value":7,
                "enable":False,
                "available":True,
                "exclusive":None  
                },
            "psycho":{
                "name":"Psychological resistance",
                "description": "The character is immuned to psychological effect",
                "effect":{
                    "damageRatio": 1,
                    "description":"Immune to psychological effect"
                },
                "value":7,
                "enable":False,
                "available":True,
                "exclusive":None  
                },
            "social":{
                "name":"Social skills",
                "description": "The character lives in community. His skills (outside combat) will be better used in a group than in solo.",
                "value":10,
                "effect":{
                    "diceBonus":1,
                    "description":"You feel great surrounded by people, it helps you focus"
                },
                "enable":False,
                "available":True,
                "exclusive":"egoist"
                },
            "adaptative":{
                "name":"Adaptative",
                "description": "At creation, the character can select any carreer path",
                "value":5,
                "enable":False,
                "available":True,
                "exclusive":None
                },
            "energy":{
                "name":"Based on energy",
                "description": "The character needs energy to perform some actions",
                "value":0,
                "enable":False,
                "available":True,
                "exclusive":None              
                },
            "easylearner":{
                "name":"Easy Learner",
                "description": "During the game, the caracter won't receive a malus for starting a new carreer path",
                "value":0,
                "enable":False,
                "available":True,
                "exclusive":None                
                },
            "healing":{
                "name":"First Aid",
                "description": "The caracter can administrate first aid in order to recover some HP.",
                "value":10,
                "effect":{
                    "baseHPRecovery":0.05,
                    "description":"You recover your hp"
                },
                "enable":False,
                "available":True,
                "exclusive":None
                },
            "mecanic":{
                "name":"Basic Mecanic",
                "description": "The caracter can perform basic reparation during the game.",
                "value":10,
                "effect":{
                    "baseHPRecovery":0.05,
                    "description":"You repair your hp"
                },
                "enable":False,
                "available":True,
                "exclusive":None                
                },
            "iem":{
                "name":"Electromagnetic",
                "description": "The caracter is subject to electromagnetic attack.",
                "value":0,
                "enable":False,
                "available":True,
                "exclusive":None
                },
            "asocial":{
                "name":"Asocial",
                "description": "The caracter is ascoial and will loose skills if working in a team",
                "value":-10,
                "effect":{
                    "diceBonus":-1,
                    "description":"There are too many people around you, it disturb your focus"
                },
                "enable":False,
                "available":True,
                "exclusive":"social"
                },
            "gluttony":{
                "name":"Gluttony",
                "description": "The character to will gain less energy and/or stamina from items.",
                "value":-10,
                "effect":{
                    "itemsEffect":0.75,
                    "description":"You'll definetely need more to fullfill your hunger"
                },
                "enable":False,
                "available":True,
                "exclusive":"frugal"
                },
            "frugal":{
                "name":"Gluttony",
                "description": "The character to will gain more energy and/or stamina from items.",
                "value":10,
                "effect":{
                    "itemsEffect":1.25,
                    "description":"You managed to extract the maximum of the item"
                },
                "enable":False,
                "available":True,
                "exclusive":"gluttony"
                },
            "poorVision":{
                "name":"Poor Vision",
                "description": "The character has poor vision. Giving him a malus when using range weapon.",
                "value":-10,
                "effect":{
                    "damageRatio":0.50,
                    "description":"You cannot see the target so far away..."
                },
                "enable":False,
                "available":True,
                "exclusive":None
                },
            "dumb":{
                "name":"Dumb",
                "description": "The character can only learn one carreer path",
                "value":10,
                "enable":False,
                "available":True,
                "exclusive":"gluttony"
                }
        }
    
    def getAvailableTraits(self):
        available = []
        for trait in self.traits:
            if self.traits[trait]["available"]:
                available.append(trait)
        return available
    
    def traitSelection(self,trait):
        exclusive = None

        # check if the input matches an available traits
        if  trait in self.traits:
            # check if the traits is available to selection        
            if self.traits[trait]["available"] == False:
                return "Trait Not Available"
            # check if the traits has already been selected
            elif self.traits[trait]["enable"] == True:
                return "Trait already selected"
            else:
                self.traits[trait]["enable"] = True
                # check if the selected traits is an exclusive traits 
                if self.traits[trait]["exclusive"] is not None:
                    exclusive = self.traits[trait]["exclusive"]
                    self.traits[exclusive]["available"] = False
        else:
            return "Please enter a valid trait"