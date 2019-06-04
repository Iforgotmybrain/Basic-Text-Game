class PlayerStats:
    """This class takes and store info about the player character. This includes their user-defined name, their sex, and
    their race. As of recent it also keeps track of their location. This was needed to implement the save system"""
    def __init__(self, race, sex, name, money, player_location):  # Make it so user cannot enter garbage values for these.
        self.name = name
        self.sex = sex
        self.race = race
        self.player_location = player_location
        self.money = money


class PlayerCharacter(PlayerStats):
    """This is where the user defines their character. This probably one of the things I'm most proud of in this project.
    This class allows for me to easily add features as I need. Such as the money system. It literally took me two lines of
    code to add that. I could easily add a health system if needed."""
    def __init__(self):
        super().__init__(name=input("What is your name? ").title(), sex=input("Do you wish to play as male or female? ").title(),  # I barely remember how the fuck I built this. Seems really complex for my knowledge level of python at the time.
                         race=input(
                             "Which race do you want to play as? Wolf, Lion, Fox or Dragon? (This is will not have a large effect on the game) ").title(), money=1200, player_location='')


class GlobalCheckSasha:
    def __init__(self, sasha_talk, sasha_living):
        self.sasha_talk = sasha_talk
        self.sasha_living = sasha_living

class GlobalCheckJacob:
    def __init__(self, jacob_kitchen, jacob_bedroom):
        self.jacob_kitchen = jacob_kitchen
        self.jacob_bedroom = jacob_bedroom

class GlobalCheckMisc:
    def __init__(self, cafe_finished, bathroom_bd):
        self.cafe_finished = cafe_finished
        self.bathroom_bd = bathroom_bd

class GlobalCheckLakePark:
    def __init__(self, park_lake_path, park_roommate_path):
        self.park_lake_path = park_lake_path
        self.park_roommate_path = park_roommate_path

class GlobalCheckFestival:
    def __init__(self, bus_ride_complete, painting_purchase, wooden_sculpture, trash_vendor, festival_item_purchased):
        self.bus_ride_complete = bus_ride_complete
        self.painting_purchase = painting_purchase
        self.wooden_sculpture = wooden_sculpture
        self.festival_item_purchased = festival_item_purchased
        self.trash_vendor = trash_vendor

player_info = PlayerCharacter()
sasha_checks = GlobalCheckSasha(sasha_talk=GlobalCheckSasha, sasha_living=GlobalCheckSasha)
jacob_checks = GlobalCheckJacob(jacob_kitchen=GlobalCheckJacob, jacob_bedroom=GlobalCheckJacob)
misc_checks = GlobalCheckMisc(cafe_finished=GlobalCheckMisc, bathroom_bd=GlobalCheckMisc)
park_checks = GlobalCheckLakePark(park_lake_path=GlobalCheckLakePark, park_roommate_path=GlobalCheckLakePark)
festival_checks = GlobalCheckFestival(bus_ride_complete=GlobalCheckFestival, painting_purchase=GlobalCheckFestival,
                                      wooden_sculpture=GlobalCheckFestival, festival_item_purchased=GlobalCheckFestival,
                                      trash_vendor=GlobalCheckFestival)