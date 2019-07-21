# _*_ coding: utf-8 _*_
import time
import secrets
import os
import SaveSystem
import CharInfo
import TravelSystem
import Phone
import ValeryTransition
import Debug

clear = lambda: os.system('cls')

class PCBedrooms:
    def chap3_mid_bedroom(self):
        CharInfo.player_info.player_location = PC_bedrooms.chap3_mid_bedroom
        if CharInfo.misc_checks.halfway_chap3 is True and CharInfo.player_info.ending_points <= -4:
            print("You're standing in your bedroom, your curtains are closed and no lights are on, making the room fairly dark.")

        elif CharInfo.misc_checks.halfway_chap3 is True and CharInfo.player_info.ending_points >= 4:
            print("You're standing in your bedroom, your curtains are lifted up, lighting up the room and giving it a cozy vibe.")

        elif CharInfo.misc_checks.halfway_chap3 is True:
            print("You're standing in your bedroom, your curtains are open a bit, giving the room a bit of natural light.")

        print("The doorway to the hallway is to the north, and your bathroom is to the east.")
        print("You see your computer over to the south.")
        print("You also see your phone laying on the desk.")
        chap3_bedroom_input = input("What do you do? ").lower()

        if chap3_bedroom_input in ['north', 'n', 'hallway']:
            hallwaymid()

        elif chap3_bedroom_input in ['east', 'e', 'bathroom']:
            print("You see nothing new in the bathroom.")
            return self.chap3_mid_bedroom()

        elif chap3_bedroom_input in ['computer', 'pc', 'south', 's']:
            chap_computer.computer_placement()

        elif chap3_bedroom_input in ['phone', 'smartphone', 'call', 'text']:
            Phone.smart_phone_placement.phone_placing()

        elif chap3_bedroom_input in ['save', 'saving']:
            SaveSystem.save_sys.saving()

        else:
            print("Invalid input")
            return self.chap3_mid_bedroom()


class LaterChapComputer:
    def __init__(self):
        self.computer_websites = ['Check bank account', 'Check Pawbook']

    def computer_placement(self):
        print("You can visit or do the following things on your computer:")
        print(self.computer_websites)
        computer_choice = input("What do you want to do? ").lower()

        if computer_choice in ['bank', 'bank account', 'check bank account', 'check bank', 'money', 'check money',
                               'bank website']:
            self.bank_balance()

        elif computer_choice in ['pawbook', 'check pawbook']:
            self.pawbook()

        else:
            print("Invalid input")
            return self.computer_placement()



    def bank_balance(self):
        print("You hop on your bank account and check your balance.")
        input()
        print("The website states that your balance is {}".format(CharInfo.player_info.money))
        input()
        return self.computer_placement()

    def pawbook(self):
        print("There's nothing new on Pawbook.")
        input()
        return self.computer_placement()  # + Stuff regarding checks, but there's really no checks for no so its blank.

def hallwaymid():
    CharInfo.player_info.player_location = hallwaymid
    print("You enter the hallway. You see the door to your bedroom to the south, Sasha's bedroom door to the west, and Jacob's bedroom door to the north.")
    print("You also see stairs over to the east that lead to the entrance way.")
    hallway_direction = input("What way do you go? ").lower()

    if hallway_direction in ['north', 'n', 'jacob\'s room', 'jacob bedroom']:
        print("The door is locked. Seems Jacob is busy or away at the moment.")
        input()
        return hallwaymid()

    elif hallway_direction in ['west', 'w', 'sasha bedroom', 'sasha\'s bedroom']:
        print("Sasha's door is locked. She must be away right now.")
        input()
        return hallwaymid()

    elif hallway_direction in ['south', 's', 'bedroom']:
        PC_bedrooms.chap3_mid_bedroom()

    elif hallway_direction in ['east', 'e', 'entrance way', 'stairs']:
        entrancewaymid()

    elif hallway_direction in ['save', 'saving']:
        SaveSystem.save_sys.saving()

    elif hallway_direction in ["debug"]:
        Debug.ending_point_debug()

    else:
        print("Invalid input")
        return hallwaymid()

def entrancewaymid():
    CharInfo.player_info.player_location = entrancewaymid
    print("You are standing in the entrance way. To your west you see the kitchen, and to the east you see the living room.")
    print("You also see the doorway to the outside directly to the north, and the stairs to the hallway right behind you to the south.")
    entrance_way_direction = input("What direction will you go? ").lower()

    if entrance_way_direction in ['north', 'n', 'outside', 'doorway']:
        print("You stand on your porch ready for adventure.")
        travel_or_stay = input("Will you travel or return home? ")

        if travel_or_stay in ['travel', 't', 'go']:
            TravelSystem.travel_function.traveltofront()

        elif travel_or_stay in ['home', 'south']:
            return entrancewaymid()

    elif entrance_way_direction in ['west', 'w', 'kitchen']:
        print("You enter the kitchen but don't see anything of interest.")
        print("You return to the entrance way")
        input()
        return entrancewaymid()

    elif entrance_way_direction in ['east', 'e', 'living room']:
        print("You look to the living room but there doesn't seem to be anything going on.")
        input()
        return entrancewaymid()

    elif entrance_way_direction in ['south', 's', 'stairs', 'hallway', 'upstairs']:
        hallwaymid()

    elif entrance_way_direction in ['save', 'saving']:
        SaveSystem.save_sys.saving()

    else:
        print("Invalid input")
        return entrancewaymid()






PC_bedrooms = PCBedrooms()

chap_computer = LaterChapComputer()