import time
import secrets
import sys
import os
import pickle
import SaveSystem
import CharInfo
import TravelSystem
import Festival
import Phone
import ValeryTransition

class PCBedrooms:
    def chap3_mid_bedroom(self):
        print("The ending point value is currently {}".format(CharInfo.player_info.ending_points))
        if CharInfo.misc_checks.halfway_chap3 is True and CharInfo.player_info.ending_points <= -4:
            print("You're standing in your bedroom, your curtains are closed and no lights are on, making the room fairly dark.")

        elif CharInfo.misc_checks.halfway_chap3 is True and CharInfo.player_info.ending_points >= 5:
            print("You're standing in your bedroom, your curtains are lifted up, lighting up the room and giving it a cozy vibe.")

        elif CharInfo.misc_checks.halfway_chap3 is True:
            print("You're standing in your bedroom, your curtains are open a bit, giving the room a bit of natural light.")
        print("The doorway to the hallway is to the north, and your bathroom is to the east.")
        print("You see your computer over to the south of you.")
        print("You also see your phone laying on the desk.")
        chap3_bedroom_input = input("What do you do?").lower()
        if chap3_bedroom_input in ['north', 'n', 'hallway']:
            print("placeholder")

        elif chap3_bedroom_input in ['east', 'e', 'bathroom']:
            print("Placeholder")

        elif chap3_bedroom_input in ['computer', 'pc', 'south', 's']:
            print("Placeholder")

        elif chap3_bedroom_input in ['phone', 'smartphone', 'call', 'text']:
            Phone.smart_phone_placement.phone_placing()

class MidChapComputer:
    def computer_placement(self):


    def bank_balance(self):
        print("")


PC_bedrooms = PCBedrooms()
