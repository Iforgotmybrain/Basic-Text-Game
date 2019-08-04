class PlayerStats:
    """This class takes and store info about the player character. This includes their user-defined name, their sex, and
    their race. As of recent it also keeps track of their location. This was needed to implement the save system"""
    def __init__(self, race, sex, name, money, player_location, ending_points):  # Make it so user cannot enter garbage values for these.
        self.name = name
        self.sex = sex
        self.race = race
        self.player_location = player_location
        self.money = money
        self.ending_points = ending_points  # Ending points are now at a 30 to -30 scale.


class PlayerCharacter(PlayerStats):
    """I cannot remember how or why I did this. Please send help."""
    def __init__(self):
        super().__init__(name=input("What is your name? ").title(), sex=input("Do you wish to play as male or female? ").title(),  # I barely remember how I built this. Seems really complex for my knowledge level of python at the time.
                         race=input(
                             "Which race do you want to play as? Wolf, Lion, Fox or Dragon? (This is will not have a large effect on the game) ").title(), money=1200, player_location='', ending_points=0)


class GlobalCheckSasha:
    def __init__(self, sasha_talk, sasha_living, sasha_post_fest):
        self.sasha_talk = sasha_talk
        self.sasha_living = sasha_living
        self.sasha_post_fest = sasha_post_fest


class GlobalCheckJacob:
    def __init__(self, jacob_kitchen, jacob_bedroom, jacob_post_fest):
        self.jacob_kitchen = jacob_kitchen
        self.jacob_bedroom = jacob_bedroom
        self.jacob_post_fest = jacob_post_fest  # Marks that the player has talked to Jacob about the road trip.


class GlobalCheckHolly:
    def __init__(self, holly_relationship_status, holly_date_restaurant):
        self.holly_relationship_status = holly_relationship_status
        self.holly_date_restaurant = holly_date_restaurant


class GlobalCheckMisc:
    def __init__(self, cafe_finished, bathroom_bd, halfway_chap3, money_scene, valery_open,):
        self.cafe_finished = cafe_finished
        self.bathroom_bd = bathroom_bd
        self.halfway_chap3 = halfway_chap3
        self.money_scene = money_scene
        self.valery_open = valery_open

class GlobalCheckLakePark:
    def __init__(self, park_lake_path, park_roommate_path):
        self.park_lake_path = park_lake_path
        self.park_roommate_path = park_roommate_path


class GlobalCheckFestival:
    def __init__(self, bus_ride_complete, painting_purchase, wooden_sculpture, trash_vendor, festival_item_purchased,
                 holly_stay, festival_walk, festival_game, festival_ending):
        self.bus_ride_complete = bus_ride_complete
        self.painting_purchase = painting_purchase
        self.wooden_sculpture = wooden_sculpture
        self.festival_item_purchased = festival_item_purchased
        self.trash_vendor = trash_vendor
        self.holly_stay = holly_stay
        self.festival_walk = festival_walk
        self.festival_game = festival_game
        self.festival_ending = festival_ending


class GlobalCheckChris:
    def __init__(self, chris_computer_list, chris_computer_list_completed):
        self.chris_computer_list = chris_computer_list
        self.chris_computer_list_completed = chris_computer_list_completed


class GlobalCheckValery:
    def __init__(self, valery_first_walk, valery_lunch, valery_date_points, valery_heart_to_heart):
        self.valery_first_walk = valery_first_walk
        self.valery_lunch = valery_lunch
        self.valery_date_points = valery_date_points
        self.valery_heart_to_heart = valery_heart_to_heart


class GlobalCheckRoadTrip:
    pass


class GlobalCheckDestinationOne:
    pass


class GlobalCheckDestinationTwo:
    pass


class GlobalCheckDestinationThreeFour:
    pass


class GlobalCheckDestinationFiveSix:
    pass


class GlobalCheckDestinationSevenEight:
    pass

player_info = PlayerCharacter()

sasha_checks = GlobalCheckSasha(sasha_talk=GlobalCheckSasha, sasha_living=GlobalCheckSasha,
                                sasha_post_fest= GlobalCheckSasha)

jacob_checks = GlobalCheckJacob(jacob_kitchen=GlobalCheckJacob, jacob_bedroom=GlobalCheckJacob,
                                jacob_post_fest=GlobalCheckJacob)

holly_checks = GlobalCheckHolly(holly_relationship_status=GlobalCheckHolly, holly_date_restaurant=GlobalCheckHolly)

misc_checks = GlobalCheckMisc(cafe_finished=GlobalCheckMisc, bathroom_bd=GlobalCheckMisc, halfway_chap3=GlobalCheckMisc,
                              money_scene=GlobalCheckMisc, valery_open=GlobalCheckMisc)

park_checks = GlobalCheckLakePark(park_lake_path=GlobalCheckLakePark, park_roommate_path=GlobalCheckLakePark)

festival_checks = GlobalCheckFestival(bus_ride_complete=GlobalCheckFestival, painting_purchase=GlobalCheckFestival,
                                      wooden_sculpture=GlobalCheckFestival, festival_item_purchased=GlobalCheckFestival,
                                      trash_vendor=GlobalCheckFestival, holly_stay = GlobalCheckFestival,
                                      festival_walk=GlobalCheckFestival, festival_game=GlobalCheckFestival,
                                      festival_ending=GlobalCheckFestival)

chris_checks = GlobalCheckChris(chris_computer_list=GlobalCheckChris, chris_computer_list_completed=GlobalCheckChris)

valery_checks = GlobalCheckValery(valery_first_walk=GlobalCheckValery, valery_lunch=GlobalCheckValery,
                                  valery_date_points=GlobalCheckValery, valery_heart_to_heart=GlobalCheckValery)

dest_one = GlobalCheckDestinationOne()

dest_two = GlobalCheckDestinationTwo()

dest_three_four = GlobalCheckDestinationThreeFour()

dest_five_six = GlobalCheckDestinationFiveSix()

dest_seven_eight = GlobalCheckDestinationSevenEight()
