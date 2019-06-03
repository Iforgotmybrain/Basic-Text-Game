import pickle
import Festival
import CharInfo


class GameState:  # Might have to put this in base because the import is causing all kinds of issues.
    def saving(self):
        import Base
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([CharInfo.player_info.player_location, CharInfo.player_info.name, CharInfo.player_info.sex,
                    CharInfo.player_info.race, Base.player_bathroom.bathroombaddragon, Base.sasha_encounter.sashatalked,
                    Base.sasha_living.sashalivingroomdialogue, Base.jacob_kitchen.jacobtalked, Base.tories_cafe.cafefinished,
                    Base.sycamore_park.parklakepath, Base.sycamore_park.parkroommatepath], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        return

    def loading(self):
        print("Loading game")
        import Base
        pickle_in = open('gamestate.pickle', 'rb')
        [CharInfo.player_info.player_location, CharInfo.player_info.name, CharInfo.player_info.sex,
         CharInfo.player_info.race, Base.player_bathroom.bathroombaddragon, Base.sasha_encounter.sashatalked,
         Base.sasha_living.sashalivingroomdialogue, Base.jacob_kitchen.jacobtalked, Base.tories_cafe.cafefinished,
         Base.sycamore_park.parklakepath, Base.sycamore_park.parkroommatepath] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        self.playerlocation()

    def playerlocation(self):
        import Base
        if CharInfo.player_info.player_location in ['PC Bedroom', 'Sasha Living Room']:
            Base.pcbedroom()

        elif CharInfo.player_info.player_location in ["Sasha First Dialogue", 'Sasha Second Dialogue', 'Holly Cafe']: \
            Base.hallway()

        elif CharInfo.player_info.player_location in ['Jacob Kitchen Dialogue']:
            Base.entranceway()

        elif CharInfo.player_info.player_location in ['Park Walk']:
            Base.sycamore_park.lakepark()

        elif CharInfo.player_info.player_location in ['Festival Start']:
            Festival.festival_area.festival_entrance()


save_load = GameState()
