import os
import sys
import SaveSystem
import CharInfo
import TravelSystem
import Phone
import Debug
import ValeryLunch

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class PCBedrooms:
    def chap3_mid_bedroom(self):  # If I just make a little intro func for every file that doesn't return that would allow me to get around the new class instance issue.
        CharInfo.player_info.player_location = PC_bedrooms.chap3_mid_bedroom  # Just telling the game where the player is located.
        if CharInfo.misc_checks.halfway_chap3 is True and CharInfo.player_info.ending_points <= -4:  # This little opening scene comment changes depending on the ending point count of the player.
            print("You're standing in your bedroom, your curtains are closed and no lights are on, making the room fairly dark.")

        elif CharInfo.misc_checks.halfway_chap3 is True and CharInfo.player_info.ending_points >= 4:
            print("You're standing in your bedroom, your curtains are lifted up, lighting up the room and giving it a cozy vibe.")

        elif CharInfo.misc_checks.halfway_chap3 is True:
            print("You're standing in your bedroom, your curtains are open a bit, giving the room a bit of natural light.")

        print("The doorway to the hallway is to the north, and your bathroom is to the east.")
        print("You see your computer over to the south.")
        print("You also see your phone laying on the desk.")
        if CharInfo.misc_checks.money_scene in ['no investments', 'investments']:
            print("You could also relax a bit in your bed to end the day.")  # Didn't show up, fix it later.
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

        elif chap3_bedroom_input in ['relax', 'bed', 'sleep', 'end day', 'end the day']:
            print("This will prevent you from accessing any other content from this day.")
            print("If you haven't met Valery today then you will not be able to progress your relationship with him any further.")
            bed_relax = input("Proceed? (yes or no)").lower()
            if bed_relax in ['yes', 'y']:
                last_of_chapter_3_transfer()

            elif bed_relax in ['no', 'n']:
                self.chap3_mid_bedroom()

        else:
            print("Invalid input")
            return self.chap3_mid_bedroom()


class LaterChapComputer:
    def __init__(self):
        self.computer_websites = ['Check bank account', 'Check Pawbook', 'Budget for Road Trip']

    def computer_placement(self):  # Computer class works much like the travel system does. Start it up and then pick what you want to do.
        print("You can visit or do the following things on your computer:")
        print(self.computer_websites)
        computer_choice = input("What do you want to do? ").lower()

        if computer_choice in ['bank', 'bank account', 'check bank account', 'check bank', 'money', 'check money',
                               'bank website']:
            self.bank_balance()

        elif computer_choice in ['pawbook', 'check pawbook']:
            self.pawbook()

        elif computer_choice in ['budget', 'budget for trip', 'budget for road trip', 'road trip budget',
                                 'road trip']:
            self.money_management()

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

    def money_management(self):
        print("Going on this road trip is going to be a pretty big expense, the mere ${} you have in your bank account won’t be nearly enough to supply you throughout the trip.".format(CharInfo.player_info.money))
        input()
        print("So, you’ll have to look into getting some money from your savings and possibly cash-out some of your investments.")
        print("You figure it’s probably best to take money from your savings first, so you browse to your bank’s website and login to your account.")
        input()
        print("Your checking account currently has ${} in it. That would probably be enough for around 1 – 2 weeks on the road, depending on the places you decide to stop at.".format(CharInfo.player_info.money))
        input()
        print("Your savings account boasts a balance of $2000, not a ton but factoring in your checking account balance and the fact that your passengers will be chipping in some, it will probably be enough to last the entirety of the road trip.")
        print("There’s a lot of costs to factor in though. You have the expected costs such as food, gas, hotel rooms/boarding, and ticket costs for wherever you decide to visit.")
        input()
        print("You also have to consider random or unpredictable things such as repairs if the car were to end up breaking down. Or any extra days you might have to pay for, due to unexpected issues like illness, hazardous weather conditions, or traffic issues.")
        input()
        print("While the funds of your checking and savings account will suffice assuming ideal conditions, if anything unexpected pops you might find yourself relying on your friends to foot a large amount of the bill. ")
        print("If that option were to fail, you’d be looking at a fairly unpleasant outcome.")
        input()
        print("That said, if you were to dip into your investment accounts so you could foot any unexpected costs, you’d be putting yourself in a bit of a precarious situation. Since you would be hindering your long-term financial freedom just for a 1-month road trip.")
        input()
        print("There’s also the option of credit cards, but the money to pay those off would have to come from somewhere. Likely from your investment accounts since you’d have spent most of your savings. So, they don’t make much sense.")
        input()
        print("Ultimately only two choices really make sense.")
        input()
        print("You could stick with what you’ve got in your bank account, which would mean not dipping into your investments. This would likely give you a better long-term outlook, since money would be much less of an issue after the road trip.")
        print("This means you could go back to working like you were before the road trip, perhaps taking up a few extra bits of work in order to replenish your savings account.")
        input()
        print("The bad thing about this route is that you’ll be SOL if you run out of funds. As getting money from your investment accounts would likely take close to a week. If you’re out of money on the road trip you won’t really have the luxury of waiting that long.")
        input()
        print("Not counting the fact that you’d have no way to pay for food or lodging, having the road trip take an extra week could seriously mess with your passengers work or personal life. Perhaps one or more of your passengers could foot the costs while you wait, but you can’t count on them having that much money at the ready.")
        input()
        print("The other choice is of course to dip into your investment accounts. This would be nice as you wouldn’t have to worry about money while on the trip. ")
        input()
        print("The car breaks down in the middle of the country? no problem, we’ll either fix it, or rent one if it’ll take too long.")
        print("Have to delay the trip for a day because everyone’s sick? That’s fine, we can afford the extra day.")
        input()
        print("It makes the whole ordeal less stressful and a lot more enjoyable.")
        print("The downside to this being that life after the road trip would likely be a bit rougher. You wouldn’t have those cushy investment accounts to fall back on in case something comes up.")
        input()
        print("It could lead to you working as a full-time contract worker for some time after the road trip while you build up your savings and investments again, or even going back to working full-time somewhere.")
        input()
        print("It’s a difficult decision, you ponder it for a while, going back and forth between the two options. Eventually deciding too…")
        print('(1): Stick with you\'ve got and avoid taking money from investments.')
        print("(2): Dip into your investment accounts in order to ensure you have enough money for the road trip.")
        money_choice = input("Which will you pick? (1 or 2)").lower()

        if money_choice in ['1']:
            CharInfo.player_info.money += 2000
            CharInfo.misc_checks.money_scene = 'no investments'
            self.computer_websites.remove('Budget for Road Trip')
            print("You decide to stick with the money you’ve got and avoid harming your long-term prospects.")
            input()
            print("You transfer the money from your savings into your checking, your bank balance is now ${}.".format(CharInfo.player_info.money))
            input()
            print("With the funding for the road trip taken care of, you log off the computer.")

            if CharInfo.valery_checks.valery_lunch is True:
                print("You've gotten everything taken care of today, with nothing else to do you decide to just call it a day and relax a bit.")
                input()
                clear()
                CharInfo.player_info.player_location = last_of_chapter_3_transfer
                SaveSystem.save_sys.saving()
                last_of_chapter_3_transfer()

            elif CharInfo.valery_checks.valery_lunch is not True:
                print("The only thing left to do for today is check and see how Valery is doing.")
                print("And if you really don't want to go see him, you could always just call it a day and relax a bit on your bed.")
                input()
                clear()
                CharInfo.player_info.player_location = PC_bedrooms.chap3_mid_bedroom
                SaveSystem.save_sys.saving()
                PC_bedrooms.chap3_mid_bedroom()

            elif CharInfo.misc_checks.valery_open is not True:
                print("You've got nothing else to do for the day. Might as well stay in and relax a bit.")
                input()
                clear()
                CharInfo.player_info.player_location = last_of_chapter_3_transfer
                SaveSystem.save_sys.saving()
                last_of_chapter_3_transfer()

        elif money_choice in ['2']:
            CharInfo.player_info.money += 5000
            CharInfo.misc_checks.money_scene = 'investments'
            self.computer_websites.remove('Budget for Road Trip')
            print("You decide to play it safe and take some extra money form your investment accounts to make sure you have enough.")
            input()
            print("You cash-out one of your accounts, which should give you $3000 extra for the road trip once the transaction is complete. ")
            print("This brings your total budget for the road trip up to {}".format(CharInfo.player_info.money))
            input()

            if CharInfo.valery_checks.valery_lunch is True:
                print("You've gotten everything taken care of today, with nothing else to do you decide to just call it a day and relax a bit.")
                input()
                clear()
                CharInfo.player_info.player_location = last_of_chapter_3_transfer
                SaveSystem.save_sys.saving()
                last_of_chapter_3_transfer()

            elif CharInfo.valery_checks.valery_lunch is not True:
                print("The only thing left to do for today is check and see how Valery is doing.")
                print("And if you really don't want to go see him, you could always just call it a day and relax a bit on your bed.")
                input()
                clear()
                CharInfo.player_info.player_location = PC_bedrooms.chap3_mid_bedroom
                SaveSystem.save_sys.saving()
                PC_bedrooms.chap3_mid_bedroom()

            elif CharInfo.misc_checks.valery_open is not True:
                print("You've got nothing else to do for the day. Might as well stay in and relax a bit.")
                input()
                clear()
                CharInfo.player_info.player_location = last_of_chapter_3_transfer
                SaveSystem.save_sys.saving()
                last_of_chapter_3_transfer()

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

def last_of_chapter_3_transfer():
    if CharInfo.valery_checks.valery_lunch is True and CharInfo.holly_checks.holly_relationship_status in ['dating']:
        print("You’ve got a couple of things still upcoming this week, as you’re getting lunch with Valery on Saturday and going on that date with Holly on Sunday.")
        input()
        print("But for now you can just relax, and get ready for the very busy weekend.")
        input()
        clear()
        ValeryLunch.val_lunch.valery_lunch_intro()

    elif CharInfo.valery_checks.valery_lunch is True and CharInfo.holly_checks.holly_relationship_status not in ['dating'] or CharInfo.festival_checks.holly_stay is not True:
        print("Your schedule leading up to the road trip is pretty free, the only thing you really have going on is getting lunch with Valery on Saturday.")
        input()
        print("So you're going to seize the opportunity and just relax until then.")
        input()
        clear()
        ValeryLunch.val_lunch.valery_lunch_intro()

    elif CharInfo.valery_checks.valery_lunch is not True and CharInfo.holly_checks.holly_relationship_status in ['dating']:
        print("Your schedule leading up to the road trip is pretty free, the only thing you really have going on is that date with Holly on Sunday.")
        input()
        print("So you're going to seize the opportunity and just relax until then.")
        input()
        clear()
        print("Scene not currently added. The game will now quit on input.")
        input()
        sys.exit()

    elif CharInfo.valery_checks.valery_lunch is not True and CharInfo.holly_checks.holly_relationship_status not in ['dating'] or CharInfo.festival_checks.holly_stay is not True:
        print("Your schedule is essentially completely free leading up to the road trip.")
        print("guess it's time to just relax and wait it out.")
        input()
        print("This scene is currently not developed. Your game has not been saved. The game quit on input.")
        input()
        sys.exit()








PC_bedrooms = PCBedrooms()

chap_computer = LaterChapComputer()