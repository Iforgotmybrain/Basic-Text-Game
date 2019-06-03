class PlayerStats:
    """This class takes and store info about the player character. This includes their user-defined name, their sex, and
    their race. As of recent it also keeps track of their location. This was needed to implement the save system"""
    def __init__(self, race, sex, name, money):  # Make it so user cannot enter garbage values for these.
        self.name = name
        self.sex = sex
        self.race = race
        self.player_location = ""
        self.money = money


class PlayerCharacter(PlayerStats):
    """This is where the user defines their character. This probably one of the things I'm most proud of in this project.
    This class allows for me to easily add features as I need. Such as the money system. It literally took me two lines of
    code to add that. I could easily add a health system if needed."""
    def __init__(self):
        super().__init__(name=input("What is your name? ").title(), sex=input("Do you wish to play as male or female? ").title(),  # I barely remember how the fuck I built this. Seems really complex for my knowledge level of python at the time.
                         race=input(
                             "Which race do you want to play as? Wolf, Lion, Fox or Dragon? (This is will not have a large effect on the game) ").title(), money=1200)

player_info = PlayerCharacter()