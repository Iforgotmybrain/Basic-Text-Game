import pickle
import CharInfo

class GameState:
    def saving(self):
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
                     CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        CharInfo.player_info.player_location()

    def loading(self):
        print("Loading game")
        pickle_in = open('gamestate.pickle', 'rb')
        [CharInfo.holly_checks, CharInfo.chris_checks, CharInfo.jacob_checks, CharInfo.sasha_checks,
         CharInfo.festival_checks, CharInfo.misc_checks, CharInfo.player_info] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        CharInfo.player_info.player_location()

save_sys = GameState()


#  Read me idiot. This is what you need to do now: Add more Charinfo variables for the future in order to reduce the
#  the need for new saves. Maybe find a way to make it so no new saves are needed at all? Don't think I can do this.
#  This seems to be the best pickle solution. If I just add more class variables then I need I should be good.
