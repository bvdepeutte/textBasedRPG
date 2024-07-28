class Traits:
    def __init__(self):
        self.traits = {
            "poison":{
                "name":"Poison",
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
                "name":"Fire",
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
                "name":"Acid",
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
            "psychological":{
                "name":"Psychological",
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
                "name":"Social",
                "description": "The character lives in community. His skills (outside combat) will be better used in a group than in solo.",
                "value":10,
                "effect":{
                    "diceBonus":1,
                    "description":"You feel great surrounded by people, it helps you focus"
                },
                "enable":False,
                "available":True,
                "exclusive":"asocial"
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
                "name":"Energy",
                "description": "The character needs energy to perform some actions",
                "value":5,
                "enable":False,
                "available":True,
                "exclusive":None              
                },
            "easylearner":{
                "name":"Easy Learner (easyLearner)",
                "description": "During the game, the caracter won't receive a malus for starting a new carreer path",
                "value":10,
                "enable":False,
                "available":True,
                "exclusive":None                
                },
            "healing":{
                "name":"Healing",
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
                "name":"Mecanic",
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
                "name":"IEM",
                "description": "The caracter is subject to electromagnetic attack.",
                "value":-5,
                "effect":{
                    "damageRatio": 1.5,
                    "description":"Weak against IEM attacks"
                },
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
                "description": "The character will gain less energy and/or stamina from items.",
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
                "name":"Frugal",
                "description": "The character will gain more energy and/or stamina from items.",
                "value":10,
                "effect":{
                    "itemsEffect":1.25,
                    "description":"You managed to extract the maximum of the item"
                },
                "enable":False,
                "available":True,
                "exclusive":"gluttony"
                },
            "poorvision":{
                "name":"Poor Vision (poorVision)",
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
                "value":-10,
                "enable":False,
                "available":True,
                "exclusive":"gluttony"
                },
            "amputee":{
                "name": "Amputee",
                "description": "You've lost an arm during the war, you can only use one hand weapon",
                "value": -10,
                "enable": False,
                "available": False,
                "exclusive": None
                },
            "greed":{
                "name": "Greed",
                "description": "Money is everything, it's your goal, it's your life",
                "value": -5,
                "enable": False,
                "available": True,
                "exclusive": None
                },
            "rebel":{
                "name": "Rebel",
                "description": "You've never loved the hierarchy. You don't trust them, you won't listen",
                "value": -5,
                "enable": False,
                "available": True,
                "exclusive": None
                }
        }
    
    def getMaxLengthName(self):
        traits = self.traits
        max = float("-inf")
        for trait in traits:
            if max < len(traits[trait]["name"]):
                max = len(traits[trait]["name"])
        return max

    def getMaxLengthDescription(self):
        traits = self.traits
        max = float("-inf")
        for trait in traits:
            if max < len(traits[trait]["description"]):
                max = len(traits[trait]["description"])
        return max
    
    def get_all_traits(self):
        traits = []
        for trait in self.traits:
            if self.traits[trait]["exclusive"] == None:
                traits.append(trait)
        return traits


    def getAvailableTraits(self):
        available = []
        for trait in self.traits:
            if self.traits[trait]["available"]:
                available.append(trait)
        return available
    
    def getEnabledTraits(self):
        selected = []
        for trait in self.traits:
            if self.traits[trait]["enable"]:
                selected.append(trait)
        return selected

    def getAvailablePoints(self):
        points = 0
        enabledTraits = self.getEnabledTraits()
        for trait in enabledTraits:
            points += self.traits[trait]["value"]
        return points
    
    def traitSelection(self,trait):
        exclusive = None
        # check if the input matches an available traits
        if  trait in self.traits:
            # check if the traits is available to selection        
            if self.traits[trait]["available"] == False:
                return print("Trait not available or already selected")
            else:
                self.traits[trait]["enable"] = True
                self.traits[trait]["available"] = False
                # check if the selected traits is an exclusive traits 
                if self.traits[trait]["exclusive"] is not None:
                    exclusive = self.traits[trait]["exclusive"]
                    self.traits[exclusive]["available"] = False
        else:
            return print("Please enter a valid trait")
    
    def traitUnselection(self,trait):
        exclusive = None
        # check if the input matches an available traits
        if  trait in self.traits:
            # check if the traits is available to selection        
            if self.traits[trait]["available"] == True:
                return print("Trait already unabled for the character")
            else:
                self.traits[trait]["enable"] = False
                self.traits[trait]["available"] = True
                # check if the selected traits is an exclusive traits 
                if self.traits[trait]["exclusive"] is not None:
                    exclusive = self.traits[trait]["exclusive"]
                    self.traits[exclusive]["available"] = True
        else:
            return print("Please enter a valid trait")        