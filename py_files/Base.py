# Tales from the Road
# -*- coding: utf-8 -*-
import time
import secrets
import sys
import os
import requests
import SaveSystem
import CharInfo
import TravelSystem
import Festival
import Phone
import ValeryTransition
import MidChapBase
import version

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')  # Thank you Poke on Stack Overflow


def bank_money():  # Checks the money value from the player info class in CharInfo. Not used past first half of chap 3
    print("You fire up your smartphone and check your bank balance")
    print("Your current balance is ${}".format(CharInfo.player_info.money))
    return pcbedroom()


def intro():
    print("As you finish the 5th and final season of Barking Bad you feel a sense of satisfaction, but also a feeling of sadness. The culmination of 5 years work is over in the span of an hour.")
    input()
    print("While you’re satisfied with the ending of the show, you can’t help but feel disappointed that there won’t be any more episodes to look forward to. You find that it’s a common feeling when it comes to finishing excellent media.")
    print("That feeling has been a familiar one recently, as you’ve binge watched 3 different shows this past week while staying at Teuton Resorts. This vacation has given yourself a break from your obligations, and from your housemates.")
    input()
    print("Unfortunately, this is your last day here, as your reservation is up tomorrow. It feels like your long-awaited vacation is over almost as soon as it began.")
    input()
    print("You spend the rest of the day packing and cleaning the room. The next day you grab breakfast and head off for home.")
    input()
    print("You eventually arrive at home in the evening, with none of your housemates to be seen. You bring your stuff inside and unpack it before getting something to eat. Afterwards you watch a short movie in your room and go to bed. Another day in paradise.")
    input()
    pcbedroom()


def pcbedroom():
    if CharInfo.sasha_checks.sasha_living is not True: # Checks player progression
        print(
            "You wake up the next morning, your bedroom is dimly lit with the only source of light being the sun as it sneaks through the blinds.")

    elif CharInfo.sasha_checks.sasha_living is True and CharInfo.jacob_checks.jacob_bedroom is not True:  # Makes it so the dialogue doesn't repeat
        print("You wake up the next day feeling pretty good. Your conversation with Sasha helped ease your mind.")
        print("You think about possibly asking Jacob about something on your mind. He should be in his bedroom.")
        input()

    elif CharInfo.festival_checks.festival_ending is True and CharInfo.chris_checks.chris_computer_list is not True:  # Same thing.
        print("You wake up the next morning still a bit surprised by the events of last night.")
        input()
        print("You think that now would be a good time to plan out the road trip, maybe try and figure out who you’d want to bring along, where you’d want to go, stuff like that.")
        input()
        print("You can think of a couple other things you could do; you might try asking your roommates for suggestions on where to go, and ask them if they’d want to go on the road trip with you.")
        input()
        print("You could also check out Chris the Tiger’s Pawbook account and see what he suggests checking out. You could do that on your computer in your bedroom.")
        input()

        if CharInfo.festival_checks.holly_stay is True:  # Only brings up this dialogue if the player stuck around with Holly.
            print("Maybe not strictly related to the road trip, but you could look into maybe going on another date with Holly as well. You might try and Call Holly to see if she’d be up for that.")
            input()
        print("It’s quite a nice day out as well, you might go on a walk just for the hell of it.")
        input()
    print("You are standing in your bedroom. You see the door to the bathroom to your east, and the doorway to the hallway directly ahead to the north.")

    if CharInfo.festival_checks.festival_ending is True:  # Makes it so the player cannot access the phone or computer before they complete the festival. Which is when they become functional.
        print("There is also your computer to the south of the room.")

        if CharInfo.jacob_checks.jacob_post_fest is True and CharInfo.sasha_checks.sasha_post_fest is True and CharInfo.festival_checks.holly_stay is True:
            print("You could also use your Phone.")

        if CharInfo.chris_checks.chris_computer_list_completed is True:
            print("You might also end the day going to Sleep in your bed.")

    print("You could also check your bank balance.")
    pcbedroomdirection = input('Which do you do? ').lower()
    CharInfo.player_info.player_location = pcbedroom  # Set players location

    if pcbedroomdirection in ['east', 'e']:
        player_bathroom.bathroompc()

    elif pcbedroomdirection in ['north', 'n']:
        hallway()

    elif pcbedroomdirection in ['save']:
        SaveSystem.save_sys.saving()

    elif pcbedroomdirection in ['bank', 'money', 'balance']:
        bank_money()

    elif pcbedroomdirection in ['south', 's', 'computer', 'pc']:
        pccomputer()

    elif pcbedroomdirection in ['phone', 'smartphone', 'cellphone', 'call', 'text', 'cell', 'call holly']:
        Phone.smart_phone_placement.phone_placing()

    elif pcbedroomdirection in ['sleep'] and CharInfo.chris_checks.chris_computer_list_completed is True:
        print("This will end the day and lock out any content you haven't completed.")
        input()
        pcsleep = input("Do you still want to go to sleep? (Yes or no) ").lower()
        if pcsleep in ['yes', 'y']:
            if TravelSystem.travel_points.tp in ['A quick walk']:

                TravelSystem.travel_points.tp.remove('A quick walk')

            CharInfo.valery_checks.valery_first_walk = 'no walk'
            ValeryTransition.quick_walk.chapter_3_halfway_transistion()

        elif pcsleep in ['no', 'n']:
            return pcbedroom()

        else:
            print("Invalid input")
            return pcbedroom()

    else:
        print("Invalid input")
        return pcbedroom()


def pccomputer():
    if CharInfo.chris_checks.chris_computer_list is not True:
        print("You turn on the computer and log in, opening Firefox and hitting up Pawbook.")  # Thank you FireFox. I don't even need to come up with a name.
        print("You look up the full name Chris gave you; Chris Feldman.")
        input()
        print("You find him on the first page, his profile picture is a selfie of him at the Grand Canyon.")
        print("He also has quite the following it would seem, with over 600 ‘pals’.")
        input()
        print(
            "You add him as a pal and sent him a message, telling him that you’re going to take up his suggestions on where to go.")
        print("After a short 5 minute wait he replies: 'I knew you’d end up going for it!'")
        input()
        print(
            '"I’m assuming you’re going to head west? It wouldn’t quite be a coast to coast road trip but it’ll be close enough. You’ll probably end up skipping out on a half days worth of driving, miss out on a couple of, in my opinion, cool stops, but there’s still plenty of other stuff ahead."')
        input()
        print('"I\'m guessing you’ll be starting off where you are now, in Iridium City.."')
        print(
            '"I’ll have to look up some routes you might go and get back to you on points of interest. Shouldn’t take me to long, I’ll probably have you a nice list by the end of the day."')
        input()
        print(
            "You reply to Chris and thank him for helping you out, you tell him that you’ll be awaiting his list.")
        CharInfo.chris_checks.chris_computer_list = True
        SaveSystem.save_sys.saving()
        pcbedroom()

    elif CharInfo.chris_checks.chris_computer_list is True and CharInfo.sasha_checks.sasha_post_fest \
            is True and CharInfo.jacob_checks.jacob_post_fest is True and \
            CharInfo.chris_checks.chris_computer_list_completed is not True:
        print("You hop back on the computer and check your Pawbook messages.")
        input()
        print("It would seem that Chris has uploaded his list of road trip destinations that you asked him for, time to dive in and see what you’ve got to work with.")
        input()
        print("It would seem he sent you a word document, you download it and open it up. ")
        print("The document says the following:")
        print("“Hey {}, here’s the list I came up with for you. The route I came up with has you going west until you hit Ourses, then you’ll be going more northwest.”".format(CharInfo.player_info.name))
        input()
        print("“Of course, you can edit it and mess around with it however you like, this is just what I came up with for ya.”")
        print("“Anyway, here’s the full list of places I recommend checking out along that route. It’s a big list, so don’t go into this expecting to hit them all.”")
        input()
        print("The list includes over 30 locations to check out. It’s going to take some time to shift through all the stuff here.")
        print("There are some duplicates, as Jacob and Holly have already mentioned some of the locations on here.")
        input()
        print("You take a minute to shift through the recommendations, instantly eliminating some of them based off your interests.")
        print("With the list trimmed down a bit, and the redundant locations merged together, you have about 15 places total you’d like to check out, with a few more places that you’d consider checking out if you had the time.")
        input()
        print("The list includes the following places:")
        input()
        print("Beaver 17 Aviation Museum in Choloco.\
               Occidentale State Park in Loba. \
               Black Hills National Forest in Rapid Falls, Omero.. \
               Ulysses’ Island in Fromage")
        input()
        print("There are a lot more on the list but it seems the author had issues with formatting. Perhaps the rest will be in a text file within a folder of some sort.")  # It's in your game folder silly
        input()
        print("(There should be a text file in your game folder containing the rest of the locations.)")
        input()
        print("Odds are you won’t end up going to every place on that list, but this is a really good place to start.")
        input()
        print("You could knock some places off your list as you travel. It'll depend a lot on what your timeline looks like, or depending on what your passengers want to do.")
        input()
        CharInfo.chris_checks.chris_computer_list_completed = True
        if CharInfo.holly_checks.holly_relationship_status in ['rejected', 'dating', 'hold', 'ignored'] or CharInfo.festival_checks.holly_stay is not True:
            print("With the road trip destinations mostly sorted out, you could go for that walk you were thinking of.")
            input()
            print("Since it's getting late, you could also just stay in for the rest of day.")
            input()
            TravelSystem.travel_points.tp.append('A quick walk')
            SaveSystem.save_sys.saving()
            clear()
            pcbedroom()

        elif CharInfo.holly_checks.holly_relationship_status not in ['rejected', 'dating', 'hold', 'ignored'] and CharInfo.festival_checks.holly_stay is True:
            print("Now that you've got the road trip destinations mostly out of the way you could text Holly and see about another date.")
            input()
            if CharInfo.player_info.ending_points > -4:
                print("Or you could just forget about texting her and go on that walk you were thinking of.")
                input()
                print("You also just say forget both of them and go to bed.")
            elif CharInfo.player_info.ending_points < -4:
                print("You could also just go on the walk and not text Holly about another date. Though she likely won't appreciate being left hanging.")
                input()
                print("You could also just go to bed and skip texting Holly and going on the walk.")
            TravelSystem.travel_points.tp.append('A quick walk')
            SaveSystem.save_sys.saving()
            clear()
            pcbedroom()
    elif CharInfo.chris_checks.chris_computer_list_completed is True:
        print("There's nothing new to check out on your computer")
        input()
        pcbedroom()

    else:
        print("You check your Pawbook messages and don’t see anything from Chris. He’s probably still working on it")
        input()
        pcbedroom()


class PCBathroom:
    def bathroompc(self):
        while True:
            if CharInfo.misc_checks.bathroom_bd is True:
                print("You see the opened trunk on the floor and the doorway to the bedroom to your west.")

            elif CharInfo.misc_checks.bathroom_bd is not True:
                print("You enter the bathroom, you see a trunk on the floor and the doorway to your bedroom to the west")

            bathroomoption = input("What do you do? ").lower()

            if bathroomoption in ["trunk", "chest"] and CharInfo.misc_checks.bathroom_bd is not True:  # Prevents user from opening trunk more than once
                print("You open the trunk and find a mysterious sculpture. It doesn't seem to have any significance, it must have been put here for some sort of testing.")
                CharInfo.misc_checks.bathroom_bd = True
                input()
                return self.bathroompc()

            elif bathroomoption in ['trunk', 'chest'] and CharInfo.misc_checks.bathroom_bd is True:
                print("There's nothing more in the trunk.")
                input()

            elif bathroomoption in ["west", "w",]:
                print("You return to your bedroom.")
                return pcbedroom()

            elif bathroomoption in ['fix', 'debug', 'teleport']:  # Teleport to other house file. For debugging.
                MidChapBase.entrancewaymid()



def hallway():
    while True:
        print("You enter a hallway. You can enter your bedroom to the south. There's also Sasha's bedroom to the west, a staircase downstairs to your east, and Jacob's bedroom to the north.")
        CharInfo.player_info.player_location = hallway
        hallwaydirection = input("Which direction do you go? ").lower()
        if hallwaydirection in ["west", "w"]:

            if CharInfo.sasha_checks.sasha_talk is not True:  # Checks to see if player has talked to sasha before
                sasha_encounter.bedroom()
                break

            elif CharInfo.sasha_checks.sasha_talk is True and CharInfo.festival_checks.festival_ending is not True:
                sasha_encounter.sashabedroom()
                break

            elif CharInfo.festival_checks.festival_ending is True and CharInfo.sasha_checks.sasha_post_fest is not True:
                sasha_encounter.sasha_post_fest_dialogue()
                break

            elif CharInfo.sasha_checks.sasha_post_fest is True:
                print("You knock on the door but no one answers. Seems Sasha is either busy or away.")
                input()
                CharInfo.player_info.player_location = hallway
                clear()
                return

        elif hallwaydirection in ["east", "e"]:
            entranceway()
            break

        elif hallwaydirection in ['save']:
            SaveSystem.save_sys.saving()

        elif hallwaydirection in ['north', 'n']:

            if CharInfo.sasha_checks.sasha_living is not True or CharInfo.festival_checks.festival_ending is True:
                print("The door is locked. Maybe you should come back later.")
                input()
                return hallway()

            elif CharInfo.sasha_checks.sasha_living is True and CharInfo.jacob_checks.jacob_bedroom is not True:
                jacob_kitchen.bedroomdialogue()

            else:
                print("The door is locked.")
                return hallway()

        elif hallwaydirection in ['south', 's']:
            pcbedroom()

        else:
            print("Invalid input")
            return hallway()

class SashaEncounter:

    def bedroom(self):
        while True:
            print(
                "You knock on Sasha's door and she welcomes you in. Her bedroom is fairly typical with nothing out of the ordinary, except of course for Sasha the German Shepard sitting at the desk.")
            print(
                "To your left you see Sasha sitting at a desk, to the south you see the doorway to the hallway.")
            bedroomoption = input("What do you do? ").lower()

            if bedroomoption in ["talk", "t", 'left', 'l', 'german shepard', 'shepard', 'sasha'] and CharInfo.festival_checks.festival_ending is not True:
                self.sashabedroomdialog()

            elif bedroomoption in ["south", "s"]:
                hallway()
            else:
                print("Invalid input")
                return self.bedroom()

    def sashabedroomdialog(self):  # This is much better now
        if CharInfo.sasha_checks.sasha_talk is not True:
            print("You approach Sasha and exchange greetings.")
            print(
                "Sasha is your roommate, she's a trustworthy sort but can be a bit absent-minded at times.")
            print("She also looks fairly unusual for a German Shepard, with her fur being almost completely black.")
            input()
            print('"Oh hey, {}. I see you\'re back from vacation, most have gotten home last night when I was at work."'.format(
                    CharInfo.player_info.name))
            print('"You were gone for like 2 weeks, right? Guess that\'s one of the perks of your lifestyle, you can take long vacations like that. Gotta admit I\'m a bit jealous, can\'t remember the last time my work let me take even just one week off."')
            input()
            print('"So, how was Teuton Resorts? I heard it\'s a pretty nice place, lots of trails to walk, and they have those beautiful waterfalls."')
            input()
            while True:
                print(
                    "(1): Tell Sasha that the vacation was alright, but that you didn't really get to experience all the resort had to offer.")
                print(
                    "(2): Explain to Sasha that you pretty much just sat in your room the whole time and watched movies and binged TV shows.")
                print("(3): Describe to Sasha a wildly inaccurate representation of what you did.")
                sasha_vacation = input("Choose a response ")

                if sasha_vacation in ['1']:
                    print(
                        "You tell Sasha that you didn't really get the check out everything the resort had on offer but that the things you did check out were pretty nice.")
                    input()
                    print(
                        '"You were there for 2 weeks but didn\'t get to see everything? That sounds just like you. Next thing you\'ll tell me is that you just sat around and watched movies instead of exploring the resort."')
                    input()
                    print(
                        "You just laugh and agree with Sasha, she doesn't need to know that was almost exactly how it played out.")
                    input()
                    break

                elif sasha_vacation in ['2']:
                    print(
                        "You tell Sasha you didn't do much except for checking out the hot tub and walking on one of the short trails when you first got there. You mainly just loafed around in your room watching movies and TV.'")
                    input()
                    print(
                        '"God, that\'s just like you. You go to one of the best resorts in the nation and you just spend the entire time there doing shit you could do here."')
                    print('"Sometimes I wonder how the hell you managed to get where you are."')
                    input()
                    break

                elif sasha_vacation in ['3']:
                    print(
                        "You lie and tell Sasha that your trip was pretty nice, and that you spent most of your time walking the trails and seeing all the landmarks.")
                    input()
                    print(
                        '"Uh huh, guess you had a sudden change of heart because I\'ve never seen you walk more than like, one trail."')
                    print('"Or you could be lying, but would the point of that be?"')
                    input()
                    break
            print(
                '"Anyway, I kept on top of all your chores while you were gone just like you asked. I expect that you\'ll be covering for me the next month, right?"')
            input()
            print("You nod in agreement with Sasha, you told Sasha that if she took care of your chores while you were gone you'd handle all of hers for a month.")
            input()
            print("You say goodbye to Sasha and head back to the hallway.")
            input()
            CharInfo.sasha_checks.sasha_talk = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()

        elif CharInfo.sasha_checks.sasha_talk is True:
            print('"Hey, nothing new to say."')
            input()
            hallway()

        # elif CharInfo.sasha_checks.sasha_talk is True:  # Oh lawd. This is gonna be cut for now and replaced later.
        #     print(""" "You know, I actually had a friend once that basically disappeared for 2 weeks." """)
        #     input()
        #     print(
        #         """ "Turns out she was hiding out in her apartment. She didn't leave it for 2 weeks and only answered text messages to tell people she was ‘ok’" """)
        #     input()
        #     print(
        #         """ "It was quite sad hearing about that for the first time, my friend was basically tearing herself apart, and by the time I knew something was up it was too late to intervene." """)
        #     print(""" "She did end up getting help thankfully, and last time I heard from her she was doing pretty good." """)
        #     input()
        #     print(
        #         """ "It makes me think of how I simply dismissed your disappearance as nothing to worry about. Who knows where you could have been or what you could have been up too!" """)
        #     input()
        #     print(
        #         """ "Anyway, you're fine now and that's all that matters. You might want to check in with Jacob, he was gone for half the week so he wasn't entirely sure how long you were gone for." """)
        #     input()
        #     print("You exit Sasha's room and enter the hallway")
        #     clear()
        #     CharInfo.player_info.player_location = hallway
        #     hallway()
        # elif CharInfo.sasha_checks.sasha_talk is True and CharInfo.sasha_checks.sasha_living is True:
        #     print('"Hey, {}. Can\'t think of anything new going on"'.format(CharInfo.player_info.name))

    def sashabedroom(self):
        while True:
            print("You see Sasha, your roommate, and the doorway to the hallway to your south")
            direction = input("What do you wish to do? ").lower()

            if direction in ["south", "s"]:
                hallway()
                break

            elif direction in ["talk", 't']:
                self.sashabedroomdialog()
                break

            else:
                print("Invalid input")
                return self.sashabedroom()

    def sasha_post_fest_dialogue(self):
        print("You knock on Sasha’s door, hoping to get some input on your road trip itinerary.")
        input()
        print("While Sasha isn’t very well-traveled, you figured it couldn’t hurt to ask her what she thinks about the whole thing.")
        input()
        print("She answers the door and invites you in, her room largely unchanged from when you last saw it.")
        input()
        print("“So what brings you to me today? Wanna talk about someone or something?”")
        input()
        print("You tell Sasha that you were actually here to talk about something a bit different.")
        input()
        print("“Alright, let's hear it.”")
        input()
        print("You mention to Sasha that the main reason you came here was to discuss destinations for a road trip.")
        print("You take a brief moment to explain what the road trip is exactly, and what you currently plan on doing.")
        input()
        print("“Seems like a good time, bit of a different approach I suppose. I’ve always thought of road trips as just driving across the country, not really sightseeing.”")
        input()
        print("You ask Sasha if she has any suggestions on where to stop. You’re not expecting her to have a list as extensive as Chris or Jacob, but she might have some good suggestions from when she lived out of state.")
        input()

        if CharInfo.jacob_checks.jacob_post_fest is True:
            print("“Want some places to check out, huh? Seems like Jacob’s given you a pretty good start on local places already.”")
            input()

        elif CharInfo.jacob_checks.jacob_post_fest is not True:
            print("“Hah, maybe I’m not the best person to ask for travel destinations since I’m not the most well-traveled person. Jacob would probably be a good bet if you wanted some suggestions that are actually decent.”")
            input()
        print("“Regardless, I can think of couple places back in my old state of Choloco you could check out.”")
        input()
        print("“Let’s see, I always enjoyed checking out the aviation museum in Iridium City. Think it was called Beaver 17 Aviation Museum. Might be a bit out of the way though, since it’s in a more rural area of the state.”")
        input()
        print("“There’s also a big roller coaster park near Yinzville, it’s right along the turnpike so it shouldn’t be out of the way much.”")
        input()
        print("“Honestly that’s about all I can think of really. There’re a few nice parks but none I’d go out of my way to visit. Sorry I couldn’t be much help, I guess Choloco just isn’t that interesting of a state.”")
        input()
        print("You tell Sasha you appreciate her help anyway; any help is better than no help.")
        print("You’ve thought about bringing along Sasha for the road trip, she’s been a great friend, and there’s not many other people you could see yourself trekking across the country with.")
        input()
        print("You do have to keep in mind the amount of people you’re planning on taking with you. You were thinking a max of 3 people too keep the car from being too crowded or busy.")
        print("It might not be bad idea to ask even if you’re not sure on who you’re taking. Since it would give you an idea of who wants to go and who doesn’t.")
        input()
        print("You’re not making any final decisions yet, you’ve still got a fair bit of time to assemble and finalize your crew.")
        input()
        print("You decide to ask Sasha how she would feel about going on the road trip with you, telling her that it would likely be a months' trip, and that you’d be taking a total of 3 people.")
        input()
        print("“I’d be interested. 3 people seems like a good amount, and I’ve always wanted to get out and travel more.”")
        print("“A months’ time though… That’s going to be really tough to try and get off at work. I don’t know if I even have that much vacation time…”")
        input()
        print("“Say, do you have anyone else interested in going? I figured you’d probably ask Jacob if you haven’t already. And then who knows who the 3rd person will be.”")
        input()
        if CharInfo.jacob_checks.jacob_post_fest is True:
            print("You tell Sasha that you have indeed asked Jacob about tagging along, and that he’ll have to check with his boss first.")
            input()
        elif CharInfo.jacob_checks.jacob_post_fest is not True:
            print("You tell Sasha she’s the first person you’ve asked about it.")
            input()
        print("“Okay, tell you what, I’ll check out my vacation time and get back to you on an answer. If I can somehow get the time off, it’ll likely be a yes.”")
        input()
        print("You give Sasha an enthusiastic cheer, telling her that you’re looking forward to hearing back from her.")
        input()

        if CharInfo.jacob_checks.jacob_post_fest is True and CharInfo.festival_checks.holly_stay is True:
            print("You exit Sasha’s room. You should probably see about getting in contact with Holly. Your smartphone in the bedroom might be a good way to go about it.")
            input()
            clear()
            CharInfo.sasha_checks.sasha_post_fest = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()

        elif CharInfo.jacob_checks.jacob_post_fest is not True:
            print("You exit Sasha’s room. You should probably go talk to Jacob about the road trip.")
            input()
            clear()
            CharInfo.sasha_checks.sasha_post_fest = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()

        elif CharInfo.jacob_checks.jacob_post_fest is True and CharInfo.festival_checks.holly_stay is not True:
            print("You exit Sasha’s room. Chris probably has his list posted on Pawbook by now.")
            clear()
            CharInfo.sasha_checks.sasha_post_fest = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()





def entranceway():
    CharInfo.player_info.player_location = entranceway
    while True:
        print("You have entered the entrance way")
        print(
            "You see the kitchen to your west, the living area to your east, the stairs to your south, and the front door to your north.")
        entrancewaydirection = input("Which way do you go? ").lower()
        if entrancewaydirection in ["north", "n"]:
            first_world.fronthousearea()
            break

        elif entrancewaydirection in ["west", "w"]:
            jacob_kitchen.startingkitchen()
            break

        elif entrancewaydirection in ["east", "e"]:

            if CharInfo.jacob_checks.jacob_kitchen is True and CharInfo.misc_checks.cafe_finished is True and CharInfo.park_checks.park_lake_path is True and CharInfo.sasha_checks.sasha_talk is True and CharInfo.festival_checks.festival_ending is not True:
                sasha_living.sashadialogue()

            elif CharInfo.festival_checks.festival_ending is True:
                jacob_kitchen.jacob_post_fest()

            else:
                print(
                    "You enter the living area and see nothing of note. Perhaps you should return here after visiting a couple places.")
                input()
            return entranceway()

        elif entrancewaydirection in ["south", "s"]:
            hallway()

        elif entrancewaydirection in ['save']:
            SaveSystem.save_sys.saving()

        elif entrancewaydirection in ['phone', 'smartphone', 'cellphone', 'call', 'text', 'cell']:
            Phone.smart_phone_placement.phone_placeing()


        else:
            print("Invalid input")
            return entranceway()


class LivingRoom:
    def sashadialogue(self):  # This gonna suck
        if CharInfo.sasha_checks.sasha_living is not True:
            print("You return to the living room once again, Sasha is sitting on the couch watching something on the television. You can talk to her or return to the entrance way to your south.")
        elif CharInfo.sasha_checks.sasha_living is True:
            print("You see Sasha still, she has nothing new to say.")
        livingroomdirection = input("What will you do? ").lower()
        if livingroomdirection in ['south', 's']:
            entranceway()
        elif livingroomdirection in ['talk', 't', 'sasha', 'couch']:
            self.sashaconversastion()
        else:
            print("Invalid input")
            return self.sashadialogue()

    def sashaconversastion(self):
        print(
            "You walk up to Sasha and sit in the chair beside the couch. The TV is playing a superhero movie involving some sort of pink titan.")
        input()
        print(
            '"Like the movie? It’s called Revengers: Titan Attack. One of the last movies in the LM Movie Universe. There’s one more that comes after this, but it isn’t out on disc yet"')  # God these are some cheesy names
        input()
        print(
            '"Actually, do you even like superhero movies? I won’t say anymore about it just In-case you want to watch it at some point."')
        input()
        print(
            "You state your preference for superhero movies, saying that you haven’t really kept up with the LM movies since the first one")
        input()
        print(
            '"Oh boy, you are in for a treat if you ever decide to catch up on them. Definitely let me know before you do, I’d love to re-watch all of them with you."')
        print('"Anyway, you want something or just here to chat?"')
        input()
        sasha_talk_or_confess = input("(1): Tell Sasha you wanted to talk about finding your purpose. (2): Just keep chatting. ").lower()

        if sasha_talk_or_confess in ['1']:
            print("You tell Sasha you want to talk about finding a purpose in life.")
            input()
            print("“Purpose, huh? Yeah that doesn’t surprise me. Figured it wouldn't be long before you got sick of your current work style.”")
            print("“Well I’m assuming your issue is that you’re tired of not having something to chase after. The way you live now, you basically work for 2 weeks a month and then the rest of your time is just spent pissing around.”")
            input()
            print("“I have a little bit of experience with this myself, which of course makes me an expert on the topic. Back when I graduated high school, I was a mess. I had zero idea what I wanted to do. My parents wanted me to go to college, but I didn’t feel like I would be cut out for it.”")
            print("“I didn’t want to go straight to working either because there just wasn’t really a viable career path.”")
            input()
            print("“So, I took a gap year to try and figure myself out. Told myself I’d work part time while ‘researching’ career paths. Now, you know me, how well do you think that worked out?”")
            print("“I just worked my part time job and didn’t do jack shit else. Worked my 20 hours a week and then pissed off and went partying with my friends or sat at home all day.”")
            input()
            print("“It was fun for a few months, but your mind wants something to work towards, and this lifestyle was a dead end.”")
            print("“I started to feel lost after those few months, I had no long-term goals, no real ambition, I wasn’t too far off from just being a deadbeat for the rest of my life truth be told. You surround yourself with negative people like that and you\'ll find yourself tangled in plaid quicker than you think.”")
            input()
            print("“After talking with my parents and a couple of my friends who actually did something after high school, I decided that I’d give college a try. I wasn’t going straight to university though; I’d go to community college and then transfer if I ended up enjoying it.”")
            print("“Wasn’t my ideal path, but my way of doing things kind of turned out to be a disaster, so I said, “fuck it” and decided to give the more traditional post high school path a go.”")
            print("“Ended up liking college quite a bit as you might have guessed. I went in as undecided but found my passion pretty quick, which was Geology.”")
            input()
            print("“Point is, sometimes you have to go outside your comfort zone to find what you want. Sometimes you don’t know exactly what you want and you’ve gotta just say 'fuck it' and")
            print("“If I were you, I’d start trying out new stuff. Maybe pick up a new hobby, meet someone new, volunteer. Just find something and see if you like it.”")
            input()
            while True:
                print("(1): Thank Sasha for advice.")
                print("(2): Ask Sasha if she as any ideas that are more specific.")
                sasha_confess_response = input("Choose a response ")

                if sasha_confess_response in ['1']:
                    print(
                        "“Of course, anything for my best friend. If you wanna talk about anything else, you just let me know. And if you find yourself sinking deeper, don’t struggle, ask for help.”")
                    input()
                    print("You say goodbye to Sasha and head up for the night. You have quite a lot to consider.")
                    input()
                    break

                elif sasha_confess_response in ['2']:
                    print(
                        "“I don’t know. There’s that festival thing coming up tomorrow. Maybe go there and see if you meet someone. Jacob might have an idea too. Couldn’t hurt to ask him.”")
                    input()
                    print(
                        "You thank Sasha and head up for the night. You'll have to ask Jacob some questions tomorrow.")
                    input()
                    break

            clear()
            CharInfo.player_info.player_location = pcbedroom
            CharInfo.sasha_checks.sasha_living = True
            CharInfo.player_info.ending_points += 4
            SaveSystem.save_sys.saving()
            pcbedroom()

        elif sasha_talk_or_confess in ['2']:
            print("You tell Sasha you just wanted to chat with her for a bit.")
            input()
            print("“Alright, just like old times! It's been awhile since we've just sat down and talked”")
            input()
            print("“So, what kind of movies do you like? Can’t remember ever talking about it with you, and I know we haven’t gone to see any together.”")
            print("You spent the next half an hour talking about movies with Sasha, maybe not exactly what you had in mind when you came to talk with her, but it works.")
            input()
            clear()
            print("“And that’s why I think the prequel movies are underrated. I’m telling you that they would have been seen in a more positive light during the initial release if the audience expectations weren’t set sky high.”")
            input()
            print("As Sasha finishes her rant on the prequel movies you start to plan your exit.")
            input()
            print("“Anyway, I really enjoyed talking about movies with you. We really need to watch the LM movies sometime, I know you’ll love them.”")
            input()
            print("You tell Sasha you’re looking forward to watching them with her sometime. Now is not that time though, as you also tell Holly you’ll be heading up to bed.")
            input()
            print(" “Alright, see you around then. We’ve really gotta talk more often!”")
            input()
            print("You nod your head in agreement with Holly before getting up and walking up to your room.")
            input()
            clear()
            CharInfo.player_info.player_location = pcbedroom
            CharInfo.sasha_checks.sasha_living = True
            CharInfo.player_info.ending_points += 2
            SaveSystem.save_sys.saving()
            pcbedroom()


class JacobDialogue:
    def startingkitchen(self):
        while True:
            print(
                "You enter the kitchen, there's various kitchen appliances and a table and chairs over to the right. You see Jacob the Deer to your left over by the fridge, and the entrance way to the east. ")
            kitchendirection = input("What will you do? ").lower()
            if kitchendirection in ["talk", "t", 'fridge', 'jacob', 'talk jacob the deer', 'jacob the deer']:
                if CharInfo.jacob_checks.jacob_kitchen is not True:  # Dialogue if Jacob hasn't been talked to before
                    print(
                        "Jacob is one of your roommates, he's a fairly tall Deer with brown eyes and a somewhat muscular build.")
                    print("And he always seems fond of wearing sweatshirts for some reason.")
                    input()
                    print("you walk over to Jacob and give him a pat on the shoulder and strike up a conversation")
                    input()
                    print(
                        '"Hey {}! What’s up? Back from that vacation you were on I see."'.format(CharInfo.player_info.name))
                    print(
                        '"Man, it\'s seriously been almost a month since I last saw you. I was at my parents the week before you went off for vacation, and then when I got back from there you were off for 2 weeks. "')
                    input()
                    print('"So, do anything exciting up at Teuton? I\'ve been there a couple of times myself, I know they have some awesome hiking trails."')
                    input()
                    while True:
                        print(
                            "(1): Give Jacob an accurate summary of your trip to the Teuton Resorts, telling him that you mostly just chilled in your room and watched movied and TV.")
                        print(
                            "(2): Exaggerate your trip a bit and tell him that you walked a couple of the trails but spent a fair bit of time just sitting in your room.")
                        print(
                            "(3): Completely lie about your time at the resort by telling him you spent pretty much all your time walking the trails.")
                        jacob_vacation = input("Choose a response ")

                        if jacob_vacation in ['1']:
                            print(
                                "You tell Jacob the truth, stating that you just spent your time in the room watching media.")
                            input()
                            print(
                                '"Not gonna lie that\'s pretty disappointing. You could have just done that stuff here, why spend 100+ dollars a day just to go up there and watch movies?"')
                            print(
                                '"Eh, whatever. It\'s not my time or money so you can do whatever makes you happy. Even I don\'t really understand it."')
                            input()
                            break

                        elif jacob_vacation in ['2']:
                            print(
                                "You bend the truth a bit and tell Jacob that you walked a couple of the trails in between watching movies and soaking in the hot tub.")
                            input()
                            print(
                                '"Yeah that honestly sounds about right for you. You\'ve never been one to be overly adventurous or outdoorsy."')
                            print('"So long as you had a good time I guess it doesn\'t really matter what you do."')
                            input()
                            break

                        elif jacob_vacation in ['3']:
                            print(
                                "You tell a complete lie to Jacob and explain that you pretty much did nothing but walk the many trails the resort has.")
                            input()
                            print(
                                '"Well good for you, I never thought of you as an outdoorsy hiking type but I guess you\'re changing."')
                            print('"Hope you had a good time, I know I did when I went up there 2 years ago."')
                            input()
                            break

                    print('"Well buddy, my lunch is about done cooking in the microwave so I\'ll be seeing you around."')
                    input()
                    print("You say goodbye to Jacob and head back to the entrance way.")
                    input()
                    CharInfo.jacob_checks.jacob_kitchen = True  # Marks that the player has talked to Jacob
                    CharInfo.player_info.player_location = entranceway
                    entranceway()

                elif CharInfo.jacob_checks.jacob_kitchen is True:  # Dialogue for Jacob after initial conversation
                    print("'Hey buddy. I've got nothing new to say.'")
                    input()
                    return self.startingkitchen()

            elif kitchendirection in ['east', 'e']:
                entranceway()
                break

            else:
                print("Invalid input")
                return self.startingkitchen()

    def bedroomdialogue(self):
        print("You knock on Jacob’s door, he opens the door and welcomes you in.")
        input()
        print("As you enter Jacob's room you notice how nicely decorated it is. You see the various landscape paintings he has hung on the walls, and the house plants he has. It all meshes together great and creates a soothing atmosphere.")
        input()
        print('"What’s up?  Come to talk ‘bout something?"')
        print("You tell Jacob that you were thinking of planning something but that you wanted to pick his brain for a bit first.")
        input()
        print('"Alrighty, pick away."')
        input()
        print('You start by telling Jacob that you wanted to talk about his past trips. You and him had talked previously about going on long trips out of state, something that you might be interested in doing yourself.')
        input()
        print('"Yeah, I’ve gone on a few trips out of state, I think furthest I’ve went was about a days’ worth of driving away"')
        print('"That was when I went to Yellowstone. What a fantastic place to visit."')
        input()
        print('"Honestly I’m not a very big fan of long ass drives like that. It gets really tired after about 6 hours"')
        print('You can find yourself agreeing with Jacob, staying in a car for most of the day doesn’t exactly seem like the greatest time.')
        input()
        print('You tell Jacob that’s part of the reason you’ve never really gone vacation anywhere too far away. The drive can really get too you.')
        input()
        print('"Yeah, I think that ends up being the case with a lot of people. You could fly, of course. In fact, that’s probably the best way to go for long distance vacations. But if you’re going only, say, 6 hours away, flying isn’t really an economical option."')
        print('"That said, driving for long periods of time wouldn\'t be too bad if you were to sort of split up your driving time. Maybe take a break and visit a place that\'s on the way to your destination instead of going straight there."')
        input()
        print("You thank Jacob for his advice and for shedding some light on his past trip. You’re still not sure if something like that is for you, you’ll just have to think about it.")
        input()
        clear()
        print("After talking with Jacob, you take some time and finish the current contract you’re working on. The deadline was still 1 week away but of course it's best to get it done early.")
        print("You are awarded $800 for the contract, you put 200 in your checking account, and the rest goes into an investment account.")
        input()
        CharInfo.player_info.money += 200
        print("Your bank balance is now {}".format(CharInfo.player_info.money))
        input()
        print("New travel area unlocked: Lake Fest.")
        CharInfo.jacob_checks.jacob_bedroom = True
        TravelSystem.travel_points.tp.append('Lake Fest')
        input()
        pcbedroom()

    def jacob_post_fest(self):
        if CharInfo.jacob_checks.jacob_post_fest is not True:
            print(
                "You check out the living room yet again, it would seem Jacob is sitting in a chair watching something on his phone")
            input()
            print("He invites you to sit on the couch next to the chair, you have a seat and start talking about the lake festival.")
            print(
                '"Hey, how was Lake Fest yesterday? Every year I tell myself I’m gonna go but something comes up or I procrastinate and end up missing it."')
            input()
            print("You tell Jacob about your day at the festival, including your purchase at the vendor.")
            input()

            if CharInfo.festival_checks.painting_purchase in ['husky', 'wraith', 'lake']:
                print(
                    '"A piece of artwork, huh? Never had you figured as that type, probably because I’ve never seen you hang so much as a picture on your walls."')
                input()

            elif CharInfo.festival_checks.wooden_sculpture in ['box', 'plane']:
                print(
                    '"Wood sculptures are pretty cool, I tried taking wood carving up as hobby but didn’t have much luck with it. Just didn’t have the ‘artistic vision’ I suppose."')
                input()

            elif CharInfo.festival_checks.trash_vendor in ['snoop', 'hat', 'troll']:
                print(
                    '"Man guess I better be on the look out now, it’d be just like you to gift me something like that for my birthday."')
                input()

            print("You also tell Jacob about your time spent hanging out with Holly at the festival.")
            input()
            if CharInfo.festival_checks.holly_stay is True:
                print(
                    '"Hell yeah buddy, sounds like you two really hit it off. You better be planning on a follow up date; not every day you find someone like that."')
                input()

            elif CharInfo.festival_checks.holly_stay is not True:
                print(
                    '"Hey, if you don’t click, you don’t click. Guess there’s a reason you didn’t really stay friends, right?"')
                input()

            print("You thank Jacob for the words of encouragement. Now on too the real reason you came here to talk.")
            input()
            print("You tell Jacob that you’ve decided to commit to a road trip, like you mentioned to him earlier.")
            print("You ask him if he has any ideas on where you should go or what you should see.")
            input()
            print(
                '"Hah, I was just thinking of that road trip comment this morning. I didn’t think you really had it in you."')
            input()
            print(
                '"Man, there’s a handful of places I can think of. There’s an awesome natural history museum in Jonstown, which is along I-23 heading west. Should be right on the route you’d take."')
            input()
            print(
                '"There’s also a beautiful state park in Loba, which is in the next state over. Place is called Occidentale State Park, they’ve got camping sites near by if you’re up for that as well. I went there about 3 years ago for spring break with an ex."')
            input()
            print(
                '"Another place to check out is the Ragniti pop factory, it’s on Interstate 65 in Loba, which you’ll probably be taking in order to get on 23. They give tours everyday, might be a nice little thing to check out. Could give yourself a break from driving."')
            input()
            if CharInfo.sasha_checks.sasha_post_fest is not True:
                print("You take a list of all the places Jacob gave you, this should be a good start.")
                input()
            elif CharInfo.sasha_checks.sasha_post_fest is True:
                print(
                    "You take a list of the places Jacob gave you, they should be a fine addition to your collection.")
                input()
            print(
                "With Jacob’s experience traveling, you feel that he might be a good person to take along on your trip.")
            print("Although, this would limit who you can take on the road trip. As you’re thinking of taking no more then 3 people. Anymore and it would get a bit crowded in the car.")
            input()
            print("Still, it might not hurt to ask him anyway. That way you'd know if he's even willing to go.")
            print("After all, you don’t have to make a final decision on who you’re taking until later. ")
            input()
            print(
                "You decide to ask him if he’d want to travel with you, saying that he doesn’t have too but that you’d definitely appreciate his experience and friendship out on the road.")
            input()
            print('"That’s a pretty nice offer, might take you up on it. How long till you take off?"')
            input()
            print("You tell Jacob that you were planning on heading out in around a months' time.")
            input()
            print(
                '"A bit short notice too put in vacation time for work, I’ll have to discuss it with Joe and see if we can work something out. Probably be on the road about 3 or so weeks, yeah?"')
            input()
            print("You tell Jacob that you were planning on the road trip being no more than 4 weeks.")
            input()
            print(
                '"Alright, I’ll check it out with my work and get back to you then, if I get the time off I’ll let you know and we can work it out."')
            input()

            if CharInfo.sasha_checks.sasha_post_fest is not True:
                print("You tell Jacob you’re looking forward too it. Now to see what Sasha has to say.")
                input()
                clear()
                CharInfo.jacob_checks.jacob_post_fest = True
                SaveSystem.save_sys.saving()
                entranceway()

            elif CharInfo.sasha_checks.sasha_post_fest is True and CharInfo.festival_checks.holly_stay is True:
                print("You tell Jacob you’re looking forward to it. Maybe now you should see what Holly's up to using your phone in the bedroom.")  # (This is placeholder. I want to make it so the player can use the phone at all locations)
                input()
                clear()
                CharInfo.jacob_checks.jacob_post_fest = True
                SaveSystem.save_sys.saving()
                entranceway()

            elif CharInfo.sasha_checks.sasha_post_fest is True and CharInfo.festival_checks.holly_stay is not True:
                print(
                    "You tell Jacob you’re looking forward to it. By now Chris should have gotten his list together, you should probably check the computer and see what he said.")
                input()
                clear()
                CharInfo.jacob_checks.jacob_post_fest = True
                SaveSystem.save_sys.saving()
                entranceway()

        elif CharInfo.jacob_checks.jacob_post_fest is True:
            print("There's nobody in the living room, guess Jacob went to do something else.")
            input()
            entranceway()


class FirstWorld:
    def fronthousearea(self):
            print("You stand on your front porch ready for adventure! You could also return home by entering the door to your south.")
            fronthouseareadirection = input("Will you travel or return home? ").lower()
            if fronthouseareadirection in ['travel', 't', 'go', 'adventure']:
                TravelSystem.travel_function.traveltofront()
            elif fronthouseareadirection in ['south', 's', 'home', 'door']:
                entranceway()
            else:
                print("Invalid input or area in progress")
                return self.fronthousearea()


class ToriesCafe:
    def thecafe(self):
        print("You catch a ride on the bus and end up at Tories Place, your all-time favorite place to grab lunch.")
        print(
            "It’s a popular place amongst the younger crowd. The place has a modern aesthetic with colorful furniture and ample natural lighting giving the place a cheery vibe.")
        input()
        print("They’re known for their fantastic wraps, and also have some pretty good soups.")
        print(
            "Looking around you see the line to order, it’s a bit after lunch so there isn’t much of a wait. You can also see a familiar face sitting down at one of the tables.")
        input()
        cafedecision = input("(1): Order food and then go over say hi to Holly. (2): Go over and say hi to Holly right away. (3): Just order some food and go home. ").lower()

        if cafedecision in ['1', '3']:
            if cafedecision in ['1']:
                print("You decide to order some food real quick before going over to say hi")
            elif cafedecision in ['3']:
                print("You decide to just do your own thing and order some food.")
            print("The line moves quick and before you know it’s your turn to order.")
            input()
            print(
                "You decide to order your usual combo; a tuna wrap with a bag of chips and a drink. Not a bad deal for $4!")
            CharInfo.player_info.money -= 4
            print("Your bank balance is now ${}".format(CharInfo.player_info.money))

            if cafedecision in ['3']:
                print("You sit down at a table after grabbing your food.")
                print("Nothing much happens while eating. Although, looking over at Holly's table you feel like you might have missed an opportunity.")
                input()
                print("She doesn't seem to be preoccupied by anything, it might have been interesting to go over and talk about what's been going on since you last saw her.")
                input()
                print("Oh well, you might end up meeting her some other time. If not you could always message her on Pawbook to see if she wants to get lunch sometime.")
                input()
                print("You finish up your meal and throw your trash away before hopping on the bus to go back home for the day.")
                input()
                clear()
                TravelSystem.travel_points.tp.remove('Tories Cafe')
                CharInfo.misc_checks.cafe_finished = True
                CharInfo.player_info.player_location = pcbedroom
                CharInfo.player_info.ending_points -= 3
                SaveSystem.save_sys.saving()
                pcbedroom()

            print("Having ordered your food, you head over to the table of Holly, a friend of yours from high school.")
            self.hollydialoguecafe()

        elif cafedecision in ['2']:
            print("You decide to first go over and say hi to Holly.")
            input()
            self.hollydialoguecafe()

        else:
            print("Invalid input")
            return self.thecafe()

    def hollydialoguecafe(self):  # Could make this have more user input but that's a lot of work for not a lot of reward. Dialogue here is fine.
        print(
            "Holly is a vixen. No, not like that; in the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
        input()
        print(
            "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for a proper conversation.")
        print(
            '"Hey {}! It\'s been awhile. I think the last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends.'.format(
                CharInfo.player_info.name))
        print('"And the last time I saw you regularly was back before you went off to college in 2013!"')
        input()
        print(
            "You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics.")
        print(
            "You ask what Holly’s been up to since then, a faint look of discomfort fills her face as she describes her falling out from college.")
        input()
        print(
            '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying "the college life". I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there."')
        print('"I couldn\'t see myself working as a marketer for the rest of my life either, which was my field of study."')
        input()
        print(
            "You nod in agreement, remembering how many times you second guessed your choice to attend college.")
        input()
        print(
            '"More on the marketer thing. I knew after I started my first internship that I would have hated that kind job and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
        print(
            '"You know I\'ve never been one to suck up and deal with other people’s bullshit"')
        input()
        print(
            "You can definitely see yourself understanding Holly’s decision, thinking back to all the workplace drama and rejected proposals you’ve dealt with…")
        print(
            "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer.")
        input()
        print(
            '"I draw art for a living now! I was always interested in it, I’m sure you remember some of my drawings from back in high school."')
        print('"I never really thought of it as a legitimate career path, but I’ve managed to build a decent enough profile that I can get by on commissions."')
        input()
        print(
            '"And you know, I really enjoy it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
        input()
        print(
            '"So, what have you been doing since graduating college? I know you finished with a couple of internships and a great GPA, so that’s had to have gotten you somewhere right?"')
        input()
        print(
            "You explain that you used to work for Spherion, but eventually quit for various reasons, including reasons she stated, like project managers ignoring ideas.")
        print(
            "You state that you had luckily saved up enough money to live comfortably for around 2 years before quitting. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
        input()
        print(
            '"Wow, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine having a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and a half!"')
        print('"Still, like I said, I enjoy my work and I\'m pretty happy with where I am in life."')
        input()
        print(
            '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Maybe I’ll see you around some other time."'.format(
                CharInfo.player_info.name))
        print("You say goodbye to Holly and decide to head home for the day.")
        input()
        print("When you arrive home you work on your contract for a bit before heading to bed.")
        input()
        clear()
        TravelSystem.travel_points.tp.remove('Tories Cafe')
        CharInfo.player_info.ending_points += 1
        CharInfo.player_info.player_location = hallway
        CharInfo.misc_checks.cafe_finished = True
        SaveSystem.save_sys.saving()
        pcbedroom()


class SycamorePark:
    def lakepark(self):
        if CharInfo.park_checks.park_roommate_path is not True and CharInfo.park_checks.park_lake_path is not True:
            print(
                "You arrive at Sycamore Lakeview Park after a short walk down the street. You’ve never really been to this park despite it being close to home.")
            print(
                "That's mainly because you've never really felt like going to the park. You were always preoccupied by something else, just not up to going out, or sacred by the various insects that call this place home. ")
            input()
            print("The park itself is pretty nice, it features various walking paths and is situated right on the lake. Giving it some fantastic views.")
            print("Most of the paths go through heavily wooded areas, providing amble shade and making it so you can stay relatively comfortable while walking")
            input()
            print(
                "Well, you’re here and ready to make the most it. As you enter the park you see two separate walking paths you'd like to take. One to the west, the other to the east. Or you could just say 'forget this' and head back home.")
        else:
            print(
                "You arrive at the park entrance, you see the two walking paths to your east and to your west. You could also head home.")
        pathdialog = [self.parkpathrommates,  # Used to randomize the path choice
                      self.parkpathself]  # In order to sort functions you can't call the function in this list.

        parkdecision = input("After thinking about it, you decide to go... (east, west, or home) ").lower()
        if parkdecision in ['home', 'away', 'forget this']:
            print("You decide to head home.")
            entranceway()

        elif parkdecision in ['east', 'e']:
            print("You head down the path to your east.")
            if CharInfo.park_checks.park_roommate_path is not True and CharInfo.park_checks.park_lake_path is not True:  # Randomly picks which path to go down
                print(
                    secrets.choice(pathdialog)())  # Instead you call the function from the randomization bit. Like this
            elif CharInfo.park_checks.park_roommate_path is True and CharInfo.park_checks.park_lake_path is not True:  # If the player has not seen the self reflection path it will play that instead of a random selection or roommate path.
                self.parkpathself()
            elif CharInfo.park_checks.park_roommate_path is not True and CharInfo.park_checks.park_lake_path is not True:  # If the player has not seen the roommate path has not been seen it will play that instead of the random selection or self path
                self.parkpathrommates()
            else:
                print("You've already gone this way.")
                self.lakepark()

        elif parkdecision in ['west', 'w']:
            print("You head down the path to your west.")
            if CharInfo.park_checks.park_lake_path is not True and CharInfo.park_checks.park_roommate_path is not True:  # Randomly picks which path to go down first
                print(secrets.choice(pathdialog)())
            elif CharInfo.park_checks.park_lake_path is True and CharInfo.park_checks.park_roommate_path is not True:  # If the player has seen the self reflection path the roommate path is played instead
                self.parkpathrommates()
            elif CharInfo.park_checks.park_lake_path is not True and CharInfo.park_checks.park_roommate_path is True:  # If the player has seen the roommate path then the self reflection path is played
                self.parkpathself()
            else:
                print("You've already gone this way.")
                self.lakepark()

        elif parkdecision in ['save']:
            SaveSystem.save_sys.saving()
        else:
            print("Invalid input")
            return self.lakepark()

    def parkpathrommates(self):
        print("This path is slightly shorter than the other one, as it doesn't go past the lake.")
        input()
        print("As you walk across the park you see someone with a Redding University shirt on. It reminds you of your days in college, and how you met your roommates.")
        input()
        print("Yes, you remember how you met both of them in college. At different times of course.")
        print(
            "You met Jacob in one of your upper-division elective courses, the one about environmental ethics or something like that. Very fitting considering Jacob has been a very outdoorsy type of guy ever since you’ve known him")
        input()
        print(
            "You ended up starting a study group with him since you weren’t exactly having a great time in that class. Mainly because it was taught by a not so great professor.")
        input()
        print("It started off as a pretty standard study group, consisting of you, Jacob, and a couple other students. About half way into the semester you started to get to know Jacob a bit better, and you started to hang out with him a bit more outside of the study group.")
        print("You had a fair bit in common with him. You liked the same sports teams, played on the same gaming platform, and as it turned out the both of you minored in the same thing.")
        input()
        print(
            "After that the rest is history, you’ve been good friends with him ever since. To the point that you decided to roommate up with him starting your 4th year at college.")
        input()
        print(
            "You ended up meeting Sasha in a similar way. You ran into her at one of the dining halls your very first year at college. You were sitting by yourself, and she came up and asked to sit with you.")
        print(
            "You started off with the usual college small talk, ‘Hey, what’s your major?’ ‘What dorm do you live in?’ She ended up living in one of the nearby dorm complexes, which shared a dining hall with your building. This led to you and her getting lunch together on a fairly regular basis.")
        input()
        print(
            "You talked quite a bit during lunch, and you eventually ended up hanging out with her outside of lunch quite a bit. You didn’t have as much in common with her as Jacob, but you still appreciated her company.")
        print(
            "You always kept in touch with her throughout the year, often attending various on-campus events together, and helping each other with classes.")
        input()
        print(
            "She’s been a really great friend to you, though she can be a bit forgetful and snarky at times. You’re really glad you met her and Jacob during your time at college, who knows how different your current life would be if you didn’t!")
        input()
        print(
            "Caught up in your thoughts you find yourself at the end of your walk before you know it. You are now back at the park entrance way.")
        clear()
        CharInfo.park_checks.park_roommate_path = True
        CharInfo.player_info.player_location = sycamore_park.lakepark
        input()
        self.lakepark()

    def parkpathself(self):  # No more sob story. This is just going to be about the PC's struggle with finding purpose.
        print("15 minutes into the walk you come across a familiar sight, the Great Sycamore Lake. Hence the park’s name.")
        print("It's evening so the Sun is starting to set over the lake, you see the sky starting to turn an orange color with the Sun being reflected off the water. ")
        print(
            "You decide to sit down at a bench overlooking the lake and take a moment to reflect on some things.")
        input()
        print("Recently you’ve been having some trouble finding purpose in your life. It’s why you went off to the Teuton Resorts, you were hoping to go there and ‘find yourself’.")
        print("That didn’t happen of course because you just spent your time there doing the same shit you do everyday. Watching videos on YouTube and streaming movies and TV.")
        input()
        print("You’re in a pretty good situation, at least economically. Your fortunes early on in your career lets you just do the occasional contract work in order to get by. You supplement that contract income with a bunch of money you saved up when you were making close to 6 figures at Spherion.")
        print("It’s an easy life but not a particularly fulfilling one. It was fun at first but 1 year into living this kind of life and you’re finding yourself uncertain and a bit depressed.")
        input()
        print("You feel like you lack purpose and direction. You’re just wasting away your life watching mindless media day after day. You don’t have anything to dedicate yourself to.")
        print("It’s getting to you, and if you don’t take care of it now you fear you’ll end up spiraling into a very unhealthy mindset.")
        input()
        print("There are a few things you’ve thought of to try and remedy this issue. Including doing volunteer work, getting a part time job doing something you enjoy, or even taking on the dating scene again.")
        print("One thing that’s come to mind recently is a cross-country road trip. While the road trip itself wouldn’t permanently fix your lack of declining mental state, you wonder if maybe you’d discover something that piques your interest while traveling.")
        print("Or maybe even find someone that you wouldn’t mind getting to know a bit better.")
        input()
        print("It’s an interesting idea, but that’s all it is for right now. An idea.")
        input()
        print("You decide to get up and continue your walk, you feel pretty good after reflecting on your recent issues.")
        input()
        clear()
        if "Sycamore Lakeview Park" in TravelSystem.travel_points.tp:
            TravelSystem.travel_points.tp.remove('Sycamore Lakeview Park')
        CharInfo.player_info.player_location = sycamore_park.lakepark
        CharInfo.park_checks.park_lake_path = True
        self.lakepark()

# Version Checking


try:
    version_check = requests.get("https://iforgotmybrain.github.io/version.json")
    version_latest = requests.get("https://iforgotmybrain.github.io/version.txt")

except requests.exceptions.ConnectionError:
    requests.status_code = "Connection failed. You're probably offline. This won't affect anything related to the game, you just won't be notified if there's an update."

# Global Classes


jacob_kitchen = JacobDialogue()  # Global instance of JacobKitchen  # Provides info for the player character

first_world = FirstWorld()

sycamore_park = SycamorePark()

tories_cafe = ToriesCafe()

player_bathroom = PCBathroom()  # Make sure to include the () when adding classes)

sasha_living = LivingRoom()

sasha_encounter = SashaEncounter()

# Starts the game


TravelSystem.travel_function.travel_point_cafe = tories_cafe.thecafe  # Sets travel points. Make sure you don't call them.

TravelSystem.travel_function.travel_point_park = sycamore_park.lakepark

TravelSystem.travel_function.travel_point_festival_one = Festival.festival_area.bus_ride

TravelSystem.travel_function.travel_point_early_bedroom = pcbedroom

TravelSystem.travel_function.travel_point_hallway = hallway

TravelSystem.travel_function.travel_point_home_one = entranceway

TravelSystem.travel_function.travel_quick_walk = ValeryTransition.quick_walk.valery_first_walk

TravelSystem.travel_function.travel_point_mid_bedroom = MidChapBase.PC_bedrooms.chap3_mid_bedroom

TravelSystem.travel_function.travel_point_valery_house = ValeryTransition.valery_lunch.valery_house

TravelSystem.travel_function.travel_point_mid_entranceway = MidChapBase.entrancewaymid

TravelSystem.travel_function.travel_point_home_two = MidChapBase.entrancewaymid

try:
    print(
        "Checking Game Version...")  # Why not just use two files? A text file to have a pretty print, and than JSON for the computer to read.
    print("Latest Version: {}".format(version_latest.text))
    print("Current Version: {}".format(version.__version__))
    if version_check.json() not in [{'version': '0.1.5'}]:
        print(
            "An update for Tales from the Road seems to be available. Check the GitHub page or Itch.io page for more details.")
    elif version_check.json() in [{'version': '0.1.5'}]:
        print("The game is running on the latest version, yay!")
except NameError:
    print("Connection failed. You\'re probably offline. This won\'t affect anything related to the game, you just won\'t be notified if there\'s an update.")

while True:
    loadingoption = input("Do you wish to load a game? ").lower()  # Make it so this is the first question asked.
    if loadingoption in ['yes', 'y', 'load', 'l']:
        SaveSystem.save_sys.loading()
    elif loadingoption in ['no', 'n']:
        break
    else:
        print("Invalid input. Try again.")

print("Hello", CharInfo.player_info.name)
time.sleep(3)
print("Welcome to Tales from the Road. A slice of life text game with furry characters")
time.sleep(2)
print("Your journey will soon begin as you return from vacation, but before that let's go over some details.")
time.sleep(4)
print("First, let's go over the character choices you've made.")
time.sleep(2)
print("Your name is", CharInfo.player_info.name, "you're a", CharInfo.player_info.sex, "and your race is a", CharInfo.player_info.race)
time.sleep(2)
print(
    "If you are okay with those options, then we're good. If not you'll want to restart and select the options you want.")
time.sleep(5)
print("Please note that If you input invalid options at sex, or input a race that wasn't a lion, wolf, fox, or dragon, events in the story will not work as intended. So keep that in mind.")
time.sleep(4)
input("If you understand this and are happy with your name, race, and sex, hit enter to continue")
print("Excellent. This game follows typical interactive fiction rules, e.g you type north or n to go north. If you want to interact with an object you can type in its name and interact with it.")
print(
    "In order to advance most dialogue in the game, you will have to press a key first. So you'll have line printed out and than to get to the next piece of dialogue you'll have to hit, say, enter.")
input("Like this. except you won't have any text telling you to press a key to continue. Press a key to continue.")
print("Sometimes you'll able to pick your dialogue response from a list. The options will be numbered which allows you to type in the corresponding number and select that dialogue option.")
input()
while True:
    print("It will look like this:")
    print("(1): This is how most player dialogue response choices will look.")
    print("(2): It's pretty simple. Just the type in the number to select your response.")
    tutorial_test = input("Choose a response ")
    if tutorial_test in ['1', '2']:
        break
    else:
        print("Not like that. Try again.")
        input()
print("With that out of the way, let's get started. Press any key when you're ready.")
input()
clear()
intro()
