import pickle


class GameState:
    def saving(self):
        import Base
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([Base.player_info.player_location, Base.player_info.name, Base.player_info.sex,
                     Base.player_info.race, Base.player_bathroom.bathroombaddragon, Base.sasha_encounter.sashatalked,
                     Base.sasha_living.sashalivingroomdialogue, Base.jacob_kitchen.jacobtalked, Base.tories_cafe.cafefinished,
                     Base.sycamore_park.parklakepath, Base.sycamore_park.parkroommatepath], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        return

    def loading(self):
        import Base
        pickle_in = open('gamestate.pickle', 'rb')
        [Base.player_info.player_location, Base.player_info.name, Base.player_info.sex,
         Base.player_info.race, Base.player_bathroom.bathroombaddragon, Base.sasha_encounter.sashatalked,
         Base.sasha_living.sashalivingroomdialogue, Base.jacob_kitchen.jacobtalked, Base.tories_cafe.cafefinished,
         Base.sycamore_park.parklakepath, Base.sycamore_park.parkroommatepath] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        self.playerlocation()

    def playerlocation(self):
        import Base
        if Base.player_info.player_location in ['PC Bedroom', 'Sasha Living Room']:
            Base.pcbedroom()
        elif Base.player_info.player_location in ["Sasha First Dialogue", 'Sasha Second Dialogue', 'Holly Cafe']:
            Base.hallway()
        elif Base.player_info.player_location in ['Jacob Kitchen Dialogue']:
            Base.entranceway()
        elif Base.player_info.player_location in ['Park Walk']:
            Base.sycamore_park.lakepark()


save_load = GameState()
