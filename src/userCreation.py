from livesForm import Human,Cyborg
from button import Button
import time, pygame, sys

class characterCreation:

    def __init__(self, game):
        self.character = None
        self.classSelection = None
        self.pause = 0.75
        self.game = game

    def slowPrint(self, text, delay=0.001):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def selectLiveForm(self):
        self.game.draw_left_fix_text('''Select your character origin:
              - Human
              - Cyborg''', self.game.text_size, self.game.DISPLAY_W /6, self.game.DISPLAY_H * 1/8)
        character_selection_temp = self.game.input_box(self.game.DISPLAY_W/6, self.game.DISPLAY_H * 1/8 + 125, 200, 50, '#select_live_form_first_choice',['human', 'cyborg'])
        if character_selection_temp.lower() == "human":
            self.character = Human("Default Name")
        elif character_selection_temp.lower() == "cyborg":
            self.character = Cyborg("Default Name")
        self.game.draw_left_fix_text(f"You have selected a {self.character._character} character", self.game.text_size, self.game.DISPLAY_W /6, self.game.DISPLAY_H * 1/8 + 200)
        return self.character
    
    def selectClass(self):
        self.game.draw_left_fix_text("During the past decades, you've dedicated your life to your job as a...",self.game.text_size, self.game.DISPLAY_W /6, self.game.DISPLAY_H * 1/8+235)
        self.game.draw_left_fix_text('''Select a class:
            - Soldier
            - Trader
            - Pilot
            - Farmer''',self.game.text_size, self.game.DISPLAY_W /6, self.game.DISPLAY_H * 1/8+270)
        self.classSelection = self.game.input_box(self.game.DISPLAY_W/6, self.game.DISPLAY_H * 1/8 + 450, 200, 50, '#select_class',["soldier","trader","pilot","farmer"])
        self.game.display.fill(self.game.BLACK)
        self.game.window.blit(self.game.title_BG,(0,0))
        # text for the soldier class story
        if self.classSelection.lower() == "soldier":
            self.game.draw_text_game("You have been fighting for the last 3 years against the Ennemy.",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8)
            self.game.draw_text_game("You've shed tears, sweat and blood for the Motherland.",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8 +50)
            self.game.draw_text_game("There was a battle, one of the greatest you have ever seen.",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8+100)
            self.game.draw_text_game("You are trying to remember it... you don't know why yet but it hurts,",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8+150) 
            time.sleep(self.pause)
            self.game.draw_text_game("way worse than your wounds... ",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8+200)
            self.game.draw_text_game("Looking down, you can only see a limb instead of your left arm",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8+250)
            self.game.draw_text_game("But now you are safe on a medical ship taking you away... Away from Hell.",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8+300)
            self.game.draw_text_game("You'll be able to rest, at least for a while...",self.game.text_size, self.game.DISPLAY_W /12, self.game.DISPLAY_H * 1/8+350)
        # text for the trader class story
        if self.classSelection.lower() == "trader":
            self.game.draw_text_game("What a year. You've made a lot of money thank's to the army...",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8)
            self.game.draw_text_game("but you've almost lost everything. How is it possible?",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8 + 50)
            self.game.draw_text_game("It was supposed to be a quick and painless victory...",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+100)
            self.game.draw_text_game("All your investments are gone",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+150)
            time.sleep(self.pause)
            self.game.draw_text_game("Now you are save, the medical shuttle will bring you back to the civilisation",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+200)
            self.game.draw_text_game("As soon as we hit the ground, I'll take back what's mine",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+250)
        # text for the pilot class story
        if self.classSelection.lower() == "pilot":
            self.game.draw_text_game("You check the direction one last time before taking a quick break.",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8)
            self.game.draw_text_game("It's all good, you are away from this madness.",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+50)
            self.game.draw_text_game("This assignement was supposed to be a punition, it's a blessing",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+100)
            time.sleep(self.pause)
            self.game.draw_text_game("Are they ok?",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+150)
            self.game.draw_text_game("You don't want to think about this, there are already enough sleepless night",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+200)
        # text for the farmer class story
        if self.classSelection.lower() == "farmer":
            self.game.draw_text_game("What has happened? A magzine sitting next to you",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8)
            self.game.draw_text_game("'The new golden rush', the new american dream, what a bullshit",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8 + 50)
            self.game.draw_text_game("You've worked hard over the last 5 years...",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+100)
            time.sleep(self.pause)
            self.game.draw_text_game("for what? for nothing...",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+150)
            self.game.draw_text_game("Anxiety, fear, sadness, you can't take it anymore",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+200)
            self.game.draw_text_game("They better help me or I don't know what will happen of me...",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/8+250)

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

    def blit_screen(self):
        self.game.window.blit(self.game.title_BG, (0, 0))
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    
    def select_traits(self):
        self.print_traits()
        pass_to_next = False
        traits = self.character.traits.get_all_traits()
        available_traits = self.character.traits.getAvailableTraits()

        LEAVE_BUTTON = Button(self.game,(self.game.DISPLAY_W - 60, self.game.DISPLAY_H - 60),"Save", 45,self.game.WHITE,self.game.RED,self.game.BLACK)
        LEAVE_BUTTON.update()
        while  pass_to_next == False:
            MOUSE_POS = pygame.mouse.get_pos()
            self.game.check_events()
            print(MOUSE_POS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if LEAVE_BUTTON.checkForInput(MOUSE_POS):
                            print("tu te rapproches")
                            pass_to_next = True
            available_traits = self.character.traits.getAvailableTraits()
            enable_traits = self.character.traits.getEnabledTraits()
            choice = self.game.input_box(self.game.DISPLAY_W/6, self.game.DISPLAY_H *1/10, 400, 50, '#select_trait',traits)
            if choice in available_traits:
                self.character.traits.traitSelection(choice)
            elif choice in enable_traits:
                self.character.traits.traitUnselection(choice)
            traits_enabled = self.character.traits.getEnabledTraits()
            for trait in traits_enabled:
                print(trait)
            self.game.display.fill(self.game.BLACK)
            self.game.window.blit(self.game.title_BG,(0,0))
            self.print_traits()
            
    def print_traits(self):
        points = self.character.traits.getAvailablePoints()
        self.game.draw_left_fix_text("Select some traits in the list below",self.game.text_size, self.game.DISPLAY_W/12, self.game.DISPLAY_H * 1/10 - 40) 
        self.game.draw_left_fix_text(f"{points}",self.game.text_size, self.game.DISPLAY_W*8/12-50, self.game.DISPLAY_H * 1/10- 40)
        self.game.draw_left_fix_text("/20 points available",self.game.text_size, self.game.DISPLAY_W*8/12, self.game.DISPLAY_H * 1/10- 40)
        traits = self.character.traits.get_all_traits()
        self.game.draw_left_fix_text("name",self.game.text_size, (self.game.DISPLAY_W)*1/12, self.game.DISPLAY_H * 2/10)
        self.game.draw_left_fix_text("description",self.game.text_size, (self.game.DISPLAY_W)*4/12, self.game.DISPLAY_H * 2/10)
        i = 0
        
        for trait in traits:
            name = self.character.traits.traits[trait]["name"]
            description = self.character.traits.traits[trait]["description"]
            if self.character.traits.traits[trait]["enable"]:
                selectedColor = self.game.BLACK
            else:
                selectedColor = self.game.RED
            self.game.draw_left_fix_text(name,24,self.game.DISPLAY_W*1/12,self.game.DISPLAY_H * 2/10 + 40 + i,self.game.WHITE,selectedColor)
            self.game.draw_left_fix_text(description,24,self.game.DISPLAY_W*4/12,self.game.DISPLAY_H * 2/10 + 40 + i,self.game.WHITE,selectedColor)
            i += 35
            # maxName = self.character.traits.getMaxLengthName()
            # # to align grid - Name
            # diffName = maxName - len(name)
            # if len(name) < maxName:
            #     name = name + (' ' * diffName)
            # to align grid - Description
            # maxDesc = self.character.traits.getMaxLengthDescription()
            # diffDesc = maxDesc - len(description)
            # if len(description) < maxDesc:
            #     description = description + (' ' * diffDesc)

        #     print(f"|{name} | {description} | {value}|")
        # print("-----------------------------------------------------------")
        # print("End: type 'leave'")
        # print("List available traits: type 'traits'")
        # print("List selected traits: type 'selected'")
        # print("Unselect traits: type 'unselect 'traits''")
        # while choice != "leave":
        #     if choice in availableTraits:
        #         self.character.traits.traitSelection(choice)
        #         points = self.character.traits.getAvailablePoints()
        #         print(f"You have spent {points}/20 points:")

        #     elif choice == 'selected':
        #         selectedTraits = self.character.traits.getEnabledTraits()
        #         for trait in selectedTraits:
        #             selectedName = self.character.traits.traits[trait]["name"]
        #             print(f"-{selectedName}")

        #     elif choice == "traits":
        #             print("name - description - value")
        #             availableTraits = self.character.traits.getAvailableTraits()
        #             for trait in availableTraits:
        #                 name = self.character.traits.traits[trait]["name"]
        #                 description = self.character.traits.traits[trait]["description"]
        #                 value = self.character.traits.traits[trait]["value"]
        #                 maxName = self.character.traits.getMaxLengthName()
        #                 # to align grid - Name
        #                 diffName = maxName - len(name)
        #                 if len(name) < maxName:
        #                     name = name + (' ' * diffName)
        #                 # to align grid - Description
        #                 maxDesc = self.character.traits.getMaxLengthDescription()
        #                 diffDesc = maxDesc - len(description)
        #                 if len(description) < maxDesc:
        #                     description = description + (' ' * diffDesc)

        #                 print(f"|{name} | {description} | {value}|")
        #             print("-----------------------------------------------------------")
        #             print("End: type 'leave'")
        #             print("List available traits: type 'traits'")
        #             print("List selected traits: type 'selected'")
        #             print("Unselect traits: type 'unselect 'traits''")
        #     else:
        #         words = choice.split(" ")
        #         if words[0] == "unselect":
        #             self.character.traits.traitUnselection(words[1])
        #             # > TODO CAN BE REMOVED for amputee and basics traits for each class.
        #             points = self.character.traits.getAvailablePoints()
        #             print(f"You have spent {points}/20 points:")
        #         else:    
        #             print("The traits encoded doesn't exist. Please input a valid traits")
