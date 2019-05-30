from py_files.Base import ToriesCafe, SycamorePark


class Traveling:
    def traveltofront(self):
        travelplaces = ("Tories Cafe", "Sycamore Lakeview Park", "Pool")
        print('You can think of the following places to travel to:')
        print(travelplaces)
        travelarea = input("Where do you want to go?")

        if travelarea in ['tories', 'the cafe', 'eat']:
            cafe.thecafe()

        elif travelarea in ['park', 'the park']:
            park.lakepark()


cafe = ToriesCafe()
park = SycamorePark()
