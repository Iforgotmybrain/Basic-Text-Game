import pickle
import CharInfo
import TravelSystem


class GameState:
    def saving(self):
        while True:
            print("Saving game")
            saving_prompt = input("Do you wish to save to slot 1, 2, or 3? You can also skip saving by typing in skip. Before version 0.1.5 saves were put in slot one. ").lower()

            if saving_prompt in ['1', 'slot 1', 'slot one', 'one']:
                pickle_out = open('gamestate.pickle', 'wb')
                pickle.dump([CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                             CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                             CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                             CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks],
                            pickle_out)
                pickle_out.close()
                print("Game Saved!")
                CharInfo.player_info.player_location()

            elif saving_prompt in ['2', 'slot 2', 'slot two', 'two']:
                pickle_out = open('gamestate2.pickle', 'wb')
                pickle.dump([CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                             CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                             CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                             CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks],
                            pickle_out)
                pickle_out.close()
                print("Game Saved!")
                CharInfo.player_info.player_location()

            elif saving_prompt in ['3', 'slot 3', 'slot three', 'three']:
                pickle_out = open('gamestate3.pickle', 'wb')
                pickle.dump([CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                             CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                             CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                             CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks],
                            pickle_out)
                pickle_out.close()
                print("Game Saved!")
                CharInfo.player_info.player_location()

            elif saving_prompt in ['skip']:
                print("Skipping game save.")
                CharInfo.player_info.player_location()

    def loading(self):
        while True:
            print("Loading game")
            loading_prompt = input("Do you wish to load slot 1, 2, or 3? Loading a slot that doesn't contain a save will result in an error. Save files were previously saved in slot one by default. ").lower()
            if loading_prompt in ['1', 'slot 1', 'slot one', 'one']:
                pickle_in = open('gamestate.pickle', 'rb')
                [CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                 CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                 CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                 CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks] = pickle.load(
                    pickle_in)
                pickle_in.close()
                print("Game Loaded!")
                CharInfo.player_info.player_location()

            elif loading_prompt in ['2', 'slot 2', 'slot two', 'two']:
                pickle_in = open('gamestate2.pickle', 'rb')
                [CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                 CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                 CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                 CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks] = pickle.load(
                    pickle_in)
                pickle_in.close()
                print("Game Loaded!")
                CharInfo.player_info.player_location()

            elif loading_prompt in ['3', 'slot 3', 'slot three', 'three']:
                pickle_in = open('gamestate3.pickle', 'rb')
                [CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                 CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info, CharInfo.park_checks,
                 CharInfo.dest_one, CharInfo.dest_two, CharInfo.dest_three_four, CharInfo.dest_five_six,
                 CharInfo.dest_seven_eight, TravelSystem.travel_points.tp, CharInfo.valery_checks] = pickle.load(
                    pickle_in)
                pickle_in.close()
                print("Game Loaded!")
                CharInfo.player_info.player_location()


save_sys = GameState()


#  Can add or remove instances as I please now. Added 2 and removed 1 with bo problems. Only thing pickle cares is that
#  the class itself is still there.
