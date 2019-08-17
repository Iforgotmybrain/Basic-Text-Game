import CharInfo
class TravelPoints:
    def __init__(self):
        self.tp = ['Tories Cafe', 'Sycamore Lakeview Park', 'Home']


class Traveling:
    def __init__(self, travel_point_cafe, travel_point_park, travel_point_festival_one, travel_point_home_one,
                 travel_point_early_bedroom, travel_point_hallway, travel_point_quick_walk,
                 travel_point_mid_bedroom, travel_point_valery_house, travel_point_mid_entranceway,
                 travel_point_home_two):
        self.travel_point_cafe = travel_point_cafe
        self.travel_point_park = travel_point_park
        self.travel_point_festival_one = travel_point_festival_one
        self.travel_point_home_one = travel_point_home_one
        self.travel_point_early_bedroom = travel_point_early_bedroom
        self.travel_point_hallway = travel_point_hallway
        self.travel_quick_walk = travel_point_quick_walk
        self.travel_point_mid_bedroom = travel_point_mid_bedroom
        self.travel_point_valery_house = travel_point_valery_house
        self.travel_point_mid_entranceway = travel_point_mid_entranceway
        self.travel_point_home_two = travel_point_home_two

    def traveltofront(self):
        print('You can think of the following places to check out:')
        print(travel_points.tp)
        travel_test.portal()


class TravelPortal(Traveling): # Don't forget to set these points up when you add a new one. I have them all setup in Base.py
    def __init__(self):
        super().__init__(travel_point_park='', travel_point_cafe='', travel_point_festival_one='',
                         travel_point_home_one='', travel_point_early_bedroom='', travel_point_hallway='',
                         travel_point_quick_walk='', travel_point_mid_bedroom='', travel_point_valery_house='',
                         travel_point_mid_entranceway='', travel_point_home_two='')

    def portal(self):
        travelarea = input("Where do you want to go? ").lower()

        if travelarea in ['tories', 'the cafe', 'eat', 'tories cafe', 'cafe']:
            travel_function.travel_point_cafe()

        elif travelarea in ['park', 'the park', 'sycamore lakeview park', 'lakeview', 'sycamore', 'lakeview park']:
            travel_function.travel_point_park()

        elif travelarea in ['fest', 'lake fest', 'festival']:
            travel_function.travel_point_festival_one()

        elif travelarea in ['home', 'house']:
            if CharInfo.misc_checks.halfway_chap3 is not True:
                travel_function.travel_point_home_one()
            elif CharInfo.misc_checks.halfway_chap3 is True:
                travel_function.travel_point_home_two()

        elif travelarea in ['bed', 'bedroom']:
            travel_function.travel_point_early_bedroom()

        elif travelarea in ['hallway']:
            travel_function.travel_point_hallway()

        elif travelarea in ['walk', 'quick walk', 'a quick walk']:
            travel_function.travel_quick_walk()

        elif travelarea in ['valery\'s house', 'valery', 'valery house', 'valery\'s']:
            travel_function.travel_point_valery_house()

        else:
            print("Invalid input")
            return self.portal()


travel_function = Traveling(travel_point_cafe=Traveling, travel_point_park=Traveling,
                            travel_point_festival_one=Traveling, travel_point_home_one=Traveling,
                            travel_point_early_bedroom=Traveling, travel_point_hallway=Traveling,
                            travel_point_quick_walk=Traveling, travel_point_mid_bedroom=Traveling,
                            travel_point_valery_house=Traveling, travel_point_mid_entranceway=Traveling,
                            travel_point_home_two=Traveling)

travel_test = TravelPortal()

travel_points = TravelPoints()