import pickle
import CharInfo

class GameState:
    def saving(self):
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([CharInfo.player_info.player_location, CharInfo.player_info.name, CharInfo.player_info.sex,
                    CharInfo.player_info.race, CharInfo.misc_checks.bathroom_bd, CharInfo.sasha_checks.sasha_talk,
                    CharInfo.sasha_checks.sasha_living, CharInfo.jacob_checks.jacob_kitchen, CharInfo.misc_checks.cafe_finished,
                    CharInfo.park_checks.park_lake_path, CharInfo.park_checks.park_roommate_path,
                    CharInfo.jacob_checks.jacob_bedroom, CharInfo.festival_checks.bus_ride_complete,
                    CharInfo.festival_checks.painting_purchase, CharInfo.festival_checks.festival_item_purchased,
                    CharInfo.festival_checks.wooden_sculpture, CharInfo.festival_checks.trash_vendor,
                    CharInfo.festival_checks.holly_stay, CharInfo.festival_checks.festival_walk], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        CharInfo.player_info.player_location()

    def loading(self):
        print("Loading game")
        pickle_in = open('gamestate.pickle', 'rb')
        [CharInfo.player_info.player_location, CharInfo.player_info.name, CharInfo.player_info.sex,
         CharInfo.player_info.race, CharInfo.misc_checks.bathroom_bd, CharInfo.sasha_checks.sasha_talk,
         CharInfo.sasha_checks.sasha_living, CharInfo.jacob_checks.jacob_kitchen, CharInfo.misc_checks.cafe_finished,
         CharInfo.park_checks.park_lake_path, CharInfo.park_checks.park_roommate_path,
         CharInfo.jacob_checks.jacob_bedroom, CharInfo.festival_checks.bus_ride_complete,
         CharInfo.festival_checks.painting_purchase, CharInfo.festival_checks.festival_item_purchased,
         CharInfo.festival_checks.wooden_sculpture, CharInfo.festival_checks.trash_vendor,
         CharInfo.festival_checks.holly_stay, CharInfo.festival_checks.festival_walk] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        CharInfo.player_info.player_location()

save_sys = GameState()