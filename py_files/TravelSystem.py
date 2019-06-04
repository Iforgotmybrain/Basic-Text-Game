tp = ['Tories Cafe', 'Sycamore Lakeview Park', 'Home']

class Traveling:
    def __init__(self, travel_point_cafe, travel_point_park, travel_point_festival_one, travel_point_home):
        self.travel_point_cafe = travel_point_cafe
        self.travel_point_park = travel_point_park
        self.travel_point_festival_one = travel_point_festival_one
        self.travel_point_home = travel_point_home

    def traveltofront(self):
        print('You can think of the following places to travel to:')
        print(tp)
        travel_test.portal()

class TravelPortal(Traveling):
    def __init__(self):
        super().__init__(travel_point_park='', travel_point_cafe='', travel_point_festival_one='',
                         travel_point_home='')

    def portal(self):
        travelarea = input("Where do you want to go?").lower()

        if travelarea in ['tories', 'the cafe', 'eat', 'tories cafe', 'cafe']:
            travel_function.travel_point_cafe()

        elif travelarea in ['park', 'the park', 'sycamore lakeview park']:
            travel_function.travel_point_park()

        elif travelarea in ['fest', 'lake fest', 'festival']:
            travel_function.travel_point_festival_one()

        elif travelarea in ['home', 'house']:
            travel_function.travel_point_home()


        else:
            print("Invalid input")
            return


travel_function = Traveling(travel_point_cafe=Traveling, travel_point_park=Traveling,
                            travel_point_festival_one=Traveling, travel_point_home=Traveling)

travel_test = TravelPortal()