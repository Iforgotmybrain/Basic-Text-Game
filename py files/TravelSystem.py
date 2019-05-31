import Base


class Traveling:
    def traveltofront(self):
        travelplaces = ("Tories Cafe", "Sycamore Lakeview Park", "Pool")
        print('You can think of the following places to travel to:')
        print(travelplaces)
        travelarea = input("Where do you want to go?")

        if travelarea in ['tories', 'the cafe', 'eat']:
            Base.tories_cafe.thecafe()

        elif travelarea in ['park', 'the park']:
            Base.sycamore_park.lakepark()


travel_function = Traveling()
