import Festival


class Traveling:
    def __init__(self):
        self.tp = ['Tories Cafe', 'Sycamore Lakeview Park']  # tp is short for travel places, places to travel too.

    def traveltofront(self):
        print('You can think of the following places to travel to:')
        print(self.tp)
        travelarea = input("Where do you want to go?").lower()

        if travelarea in ['tories', 'the cafe', 'eat', 'tories cafe', 'cafe']:
            import Base
            Base.tories_cafe.thecafe()

        elif travelarea in ['park', 'the park' 'sycamore lakeview park']:
            import Base
            Base.sycamore_park.lakepark()

        elif travelarea in ['festival', 'fest', 'lake', 'lake fest' 'lake festival', 'lf']:
            if Festival.festival_area.bus_ride_completed is False:
                Festival.festival_area.bus_ride()
            elif Festival.festival_area.bus_ride_completed is True:
                Festival.festival_area.festival_entrance()

        else:
            print("Invalid input")
            return self.traveltofront()


travel_function = Traveling()