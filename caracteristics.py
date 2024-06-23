class traits:
    def __init__(self):
        self.traits = {
            "poison":{
                "name":"Poison resistance",
                "effect": "The character is immuned to poisoning effect",
                "value":5,
                "enable":False,
                "available":True  
                },
            "fire":{
                "name":"Fire resistance",
                "effect": "The character is immuned to fire",
                "value":5,
                "enable":False,
                "available":True  
                },
            "acid":{
                "name":"Acid resistance",
                "effect": "The character is immuned to acid",
                "value":7,
                "enable":False,
                "available":True  
                },
            "psycho":{
                "name":"Psychological resistance",
                "effect": "The character is immuned to psychological effects",
                "value":7,
                "enable":False,
                "available":True  
                },
            "social":{
                "name":"Social skills",
                "effect": "The character lives in community. His skills will be better used in a group than in solo.",
                "value":5,
                "enable":False,
                "available":True,
                "exclusive":"egoist"
                },
            "adaptative":{
                "name":"Adaptative",
                "effect": "At creation, the character can select any carreer path",
                "value":5,
                "enable":False,
                "available":True
                },
            "energy":{
                "name":"Based on energy",
                "effect": "The character needs energy to perform some actions",
                "value":0,
                "enable":False,
                "available":True                
                },
            "easylearner":{
                "name":"Easy Learner",
                "effect": "During the game, the caracter won't receive a malus for starting a new carreer path",
                "value":0,
                "enable":False,
                "available":True                
                },
            "healing":{
                "name":"First Aid",
                "effect": "The caracter can administrate first aid in order to recover some HP.",
                "value":0,
                "enable":False,
                "available":True
                },
            "mecanic":{
                "name":"Basic Mecanic",
                "effect": "The caracter can perform basic reparation during the game.",
                "value":0,
                "enable":False,
                "available":True                
                },
            "iem":{
                "name":"Electromagnetic",
                "effect": "The caracter is subject to electromagnetic attack.",
                "value":0,
                "enable":False,
                "available":True
                },
            "asocial":{
                "name":"Asocial",
                "effect": "The caracter is ascoial and will loose skills if working in a team",
                "value":-5,
                "enable":False,
                "available":True,
                "exclusive":"social"
                },
            "gluttony":{
                "name":"Gluttony",
                "effect": "The character to will gain less energy and/or stamina from items.",
                "value":-10,
                "enable":False,
                "available":True,
                "exclusive":"frugal"
                },
            "frugal":{
                "name":"Gluttony",
                "effect": "The character to will gain more energy and/or stamina from items.",
                "value":10,
                "enable":False,
                "available":True,
                "exclusive":"gluttony"
                }
        }