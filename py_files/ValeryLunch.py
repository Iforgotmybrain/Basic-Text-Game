import os
import sys
import CharInfo
import TravelSystem
import SaveSystem
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class ValeryLunchStart:
    def valery_lunch_intro(self):
        print("The weekend is finally here, and with it comes the various outings that you’ve been expecting.")
        input()
        if CharInfo.player_info.ending_points <= -4:
            print("Today you’ll be going to get lunch with Valery, you’re a bit nervous about the whole thing but it’ll probably work out fine.")
            input()

        elif CharInfo.player_info.ending_points >= -4:
            print("Today you’ll be going to get lunch with Valery. It should be nice to get to know him a bit better.")
            input()

        if CharInfo.holly_checks.holly_relationship_status in ['dating']:
            print("You also have a date with Holly tomorrow, guess this weekend is quite busy.")
            input()

        print("Pretty much the only thing you have going on today is lunch with Valery, so you’ll probably just end up hanging around the house until lunch.")
        input()
        clear()
        print("A couple of hours pass and before you know It it’s time to head out to The Rat’s Place for lunch. You finish up the video you were watching on the computer and head to your car to drive to the restaurant.")
        input()
        CharInfo.player_info.player_location = val_lunch.valery_lunch_rats
        SaveSystem.save_sys.saving()
        clear()

    def valery_lunch_rats(self):
        print("You arrive about 10 minutes before 12, you always like to give yourself some extra time.")
        input()
        print("Seems like Valery hasn’t gotten here yet; you’ll have to wait around a bit and see if he shows up. If not you’ll just head in and get a table.")
        print("It takes a couple more minutes for Valery to finally arrive, as he pulls into the parking lot you exit your car and head towards the entrance of the restaurant.")
        input()
        print("The Rat’s Place is situated just off the lake, the building itself is painted in a light blue color, with white accents. The side facing the lake is made almost entirely of glass, offering a spectacular view.")
        print("And according to a plaque mounted near the seating area, the restaurant is named after a set of critically acclaimed movies, called “The Rat Movies”.")
        input()
        print("You enter the restaurant and wait for Valery to make his way in, he ends up arriving very shortly after you.")
        print("“Hello there, {}. I’ve been looking forward to this lunch all week!”".format(CharInfo.player_info.name))
        input()
        print("You tell Valery you have as well, it’s always good to try and get to know new people.")


val_lunch = ValeryLunchStart()