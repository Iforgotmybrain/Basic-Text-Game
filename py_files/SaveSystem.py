import pickle
import CharInfo
import TravelSystem


class GameState:
    def saving(self):
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                     CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                     CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                     CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        CharInfo.player_info.player_location()

    def loading(self):
        print("Loading game")
        pickle_in = open('gamestate.pickle', 'rb')
        [CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
         CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
         CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
         CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        CharInfo.player_info.player_location()

save_sys = GameState()


#  Can add or remove instances as I please now. Added 2 and removed 1 with bo problems. Only thing pickle cares is that
#  the class itself is still there.
