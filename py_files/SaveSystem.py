import pickle
import CharInfo
import CharLocator


class GameState:
    def saving(self):
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([CharInfo.player_info.player_location, CharInfo.player_info.name, CharInfo.player_info.sex,
                    CharInfo.player_info.race, CharInfo.misc_checks.bathroom_bd, CharInfo.sasha_checks.sasha_talk,
                    CharInfo.sasha_checks.sasha_living, CharInfo.jacob_checks.jacob_kitchen, CharInfo.misc_checks.cafe_finished,
                    CharInfo.park_checks.park_lake_path, CharInfo.park_checks.park_roommate_path], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        return

    def loading(self):
        print("Loading game")
        pickle_in = open('gamestate.pickle', 'rb')
        [CharInfo.player_info.player_location, CharInfo.player_info.name, CharInfo.player_info.sex,
         CharInfo.player_info.race, CharInfo.misc_checks.bathroom_bd, CharInfo.sasha_checks.sasha_talk,
         CharInfo.sasha_checks.sasha_living, CharInfo.jacob_checks.jacob_kitchen, CharInfo.misc_checks.cafe_finished,
         CharInfo.park_checks.park_lake_path, CharInfo.park_checks.park_roommate_path] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        CharLocator.playerlocation()

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
            import Festival
            Festival.festival_area.festival_entrance()

save_sys = GameState()