class Traveling:
    def traveltofront(self):
        import Base
        tp = ('Tories Cafe', 'Sycamore Lakeview Park', 'Lake Fest')  # tp is short for travel places, places to travel too.
        print('You can think of the following places to travel to:')
        print(tp[0], tp[1], tp[2])
        travelarea = input("Where do you want to go?").lower()

        if travelarea in ['tories', 'the cafe', 'eat', 'tories cafe', 'cafe']:
            Base.tories_cafe.thecafe()

        elif travelarea in ['park', 'the park' 'sycamore lakeview park']:
            Base.sycamore_park.lakepark()
        elif travelarea in ['festival', 'fest', 'lake', 'lake fest' 'lake festival', 'lf']:
            import Festival
            if Festival.festival_area.bus_ride_completed is False:
                Festival.festival_area.bus_ride()
            elif Festival.festival_area.bus_ride_completed is True:
                Festival.festival_area.festival_entrance()

        else:
            print("Invalid input")
            return self.traveltofront()


travel_function = Traveling()