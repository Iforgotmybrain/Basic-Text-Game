# _*_ coding: utf-8 _*_
import CharInfo
import TravelSystem

def ending_point_debug():
    while True:
        print("Current ending points are {}".format(CharInfo.player_info.ending_points))
        input()
        print("Would you like to edit them?")
        debug_points = input("Yes or no").lower()
        if debug_points in ['yes', 'y']:
            print("By how much?")
            ending_point_edit = input("(1): + 2  (2): + 4  (3) + 8  (4) - 2  (5) - 4  (6) - 8")

            if ending_point_edit in ['1']:
                CharInfo.player_info.ending_points += 2
                return ending_point_debug()

            elif ending_point_edit in ['2']:
                CharInfo.player_info.ending_points += 4
                return ending_point_debug()

            elif ending_point_edit in ['3']:
                CharInfo.player_info.ending_points += 8
                return ending_point_debug()

            elif ending_point_edit in ['4']:
                CharInfo.player_info.ending_points -= 2
                return ending_point_debug()

            elif ending_point_edit in ['5']:
                CharInfo.player_info.ending_points -= 4
                return ending_point_debug()

            elif ending_point_edit in ['6']:
                CharInfo.player_info.ending_points -= 8
                return ending_point_debug()

        elif debug_points in ['no', 'n']:
            TravelSystem.travel_function.travel_point_mid_bedroom()