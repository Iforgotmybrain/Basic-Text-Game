# Text game
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import secrets

# Room functions. This is the bulk of the game. Not sure if this is the best way to program this type of game
# But this seems to be the organized way, and the easiest way to edit things if needed.


class PlayerStats:
    def __init__(self, race, sex, name):
        self.name = name
        self.sex = sex
        self.race = race


class PlayerCharacter(PlayerStats):
    def __init__(self):
        super(). __init__(name=input("What is your name? "), sex=input("Do you wish to play as male or female? "),
                          race=input("Which race do you want to play as? Wolf, Lion, Fox or Dragon? (This is simply for role playing) "))


def startingroomlightswitch ():
    lightswitch = ""
    while lightswitch != "north" and lightswitch != "east":
        lightswitch = input("Which way do you go? ")
        if lightswitch == "north":
            hallway()
        elif lightswitch == "east":
            bathroom()
    return lightswitch


def rollintro ():
    print("In the beginning, there was nothing but this line of text")
    time.sleep(2)
    print("But soon that changed, and this game began to develop")


def bathroom():
    while True:
        print("You enter a bathroom, you see a trunk on the floor and the doorway you entered to your west")
        bathroom = input("What do you do? ")  # Maybe change this vars name
        if bathroom in ["trunk", "Trunk", "Chest", "chest"]:  # Prevent user from opening this more than once
            print("You open the trunk and find a mysterious silicone sculpture")
            time.sleep(5)
        elif bathroom in ["west", "w", "West"]:
            print("You return to the dim room, you see a doorway to your north and the bathroom to your east")
            return startingroomlightswitch()


def hallway():
    print("You enter a hallway with a doorway to your north and a staircase to your south")
    hallway = input("Which direction do you go? ").lower()
    if hallway in ["south", "s"]:
        entranceway()
    elif hallway in ["north", "n"]:
        if sasha_encounter.sashatalked == False:
            sasha_encounter.bedroom()
        elif sasha_encounter.sashatalked == True:
            sasha_encounter.sashabedroom()
        else:
            print("Invalid input")
            return hallway


class SashaEncounter:
    def __init__(self):
        self.sashatalked = False

    def bedroom(self):
        while True:
            print("You enter what seems to be a bedroom, you see the typically items you'd expect to see in a bedroom") # Change wording
            print("To your west you see a German Shepard sitting at a desk, to the south you see the doorway to the hallway")
            bedroomoption = input("What do you do? ").lower()
            if bedroomoption == "talk":
                self.sashabedroomdialog()
            elif bedroomoption in ["south", "s"]:
                hallway()
            else:
                print("Invalid input")
                return self.bedroom()

    def sashabedroomdialog(self):
        if self.sashatalked == False:
            print("You approach the German Shepard and exchange greetings.")
            time.sleep(5)
            print("The German Shepard is your roommate, Sasha. She's a trustworthy sort. But a bit absent-minded at times")
            time.sleep(10)
            print(""" "You’re alive! You’d been locked up in your room for so long I figured you either died or got transported to another universe." """)
            time.sleep(10)
            print(""" "I’ve kept on top of all your chores, you’re gonna owe me for the weeks’ time you decided to disappear. I was thinking you could take of my work for 2 or so weeks" """)
            self.sashatalked = True
            self.sashabedroom()
        elif self.sashatalked == True:
            print(""" "You know, I actually had a roommate in college once that didn't leave our dorm for 2 weeks" """)
            time.sleep(10)
            print(""" "She was in a pretty bad place mentally, and ended up dropping all her classes and leaving college." """)
            time.sleep(10)
            print(""" "It's unbelievably depressing watching someone you know fall apart from mental illness." """)
            time.sleep(5)
            print(""" "Makes me think of how I simply dismissed your disappearance as nothing to worry about. Who knows what could have happened to you!" """)
            time.sleep(10)
            print(""" "Anyway, your fine now and that's all that matters. You might want to check in with Jacob, he was gone for half the week so he wasn't entirely sure how long you locked yourself up for" """)
            time.sleep(10)
            print(""" "He should be somewhere downstairs." """)
            time.sleep(5)
            print("You exit Sasha's room and enter the hallway")
            hallway()

    def sashabedroom(self):
        print("You see Sasha, your roommate, and the doorway to the hallway to your south")
        direction = input("What do you wish to do? ")
        if direction in ["south", "s"]:
            hallway()
        elif direction == "talk":
            self.sashabedroomdialog()
        else:
            print("Invalid input")
            return self.sashabedroom


def entranceway ():
    while True:
        print("You head down the stairs and enter the entrance way")
        time.sleep(2)
        print("You see a kitchen to your west, a living area to your east, the stairs to your south, and the front door to your north.")
        entrancewaydirection = input("Which way do you go? ").lower()
        if entrancewaydirection in ["north", "n"]:
            first_world.fronthousearea()
        elif entrancewaydirection in ["west", "w"]:
            jacob_kitchen.startingkitchen()
            break
        elif entrancewaydirection in ["east", "e"]:
            print("Area is a work in progress")
        elif entrancewaydirection in ["south", "s"]:
            hallway()
        else:
            print("Invalid input")


class JacobKitchen:
    def __init__(self):
        jacobtalked = False

    def startingkitchen(selfs):
        print("You enter a kitchen, there's a various kitchen appliances and a table and chairs over to the right. You see a Deer to the west. ")
        kitchendirection = input("What do you do? ")
        if kitchendirection in ["west", "w"]:  # Change this to talk
            print("The Deer is your roommate, Jacob. You give him a pat on the shoulder and strike up a conversation")
            print('"Hey"', player_info.name,'"Where have you been these last few days? I haven’t seen you since I left for vacation last week. I got back about 3 days ago and just figured you were taking a short trip to somewhere."')


class FirstWorld:

    def fronthousearea(self):
        print("You exit out the front door. You think of 3 places to travel too. The local community pool, the nearest park, or your favorite lunch spot, the cafe.")
        fronthouseareadirection = input("Where will you go first? ")
        if fronthouseareadirection in ["cafe", "lunch"]:
            cafetories.cafe()
        elif fronthouseareadirection in ['park','p']:
            self.lakepark()
        else:
            print("Invalid input")

    def lakepark(self):
        print("You arrive at the park after a short walk down the street. You’ve never really been too this park (or any park really) despite being close to home.")
        time.sleep(5)
        print("You’ve never really felt like going to the park, you were always preoccupied by something else, just not up to going out, or sacred by the various flying insects that call this place home. ")
        time.sleep(8)
        print("You’re here now and ready to make the most it. As you enter the park you see two separate walking paths you could take. One to the west, the other to the east. Or you could just say forget this whole thing and head back home.")
        parkdecision = input("After thinking about it, you decide to go... ")
        pathdialog = [self.parkpathrommates, self.parkpathself]  # In order to sort functions you can't call the function in this list.
        if parkdecision in ['home', 'away',]:
            print("You decide you still aren’t feeling up to a walk in the park and head home")
            self.fronthousearea()
        elif parkdecision in ['east', 'e']:
            print("You head down the path to your right.")
            time.sleep(4)
            print(secrets.choice(pathdialog)())  # Instead you cal the function from the randomization bit. Like this

    def parkpathrommates(self):
        print("This path is a slightly shorter path than the other one, as it doesn't go past the lake.")
        time.sleep(3)
        print("About 25 minutes into your hour or so walk you come across a group of 20-somethings hanging out on a set of benches. They remind you of your more recent years spent around Sasha and Jacob.")
        time.sleep(7)
        print("You remember how you met both of them your 3rd year of college. At different times of course.")
        time.sleep(5)
        print("You met Jacob in one of your upper-division elective courses, the one about environmental ethics or something of the sort. Very fitting considering Jacob has been a very outdoorsy, tree hugging type of guy ever since you’ve known him")
        time.sleep(15)
        print("You ended up starting a study group with him since you weren’t exactly having a great time in class. As it was taught by a not so fantastic instructor. It started off as a pretty standard study group, consisting of you, Jacob and a couple other students. Eventually you started hanging out with him outside of the group and found out that he’s a really cool guy. You liked the same kind of movies, both loved pasta, and even ended up owning the same kind of car")
        time.sleep(25)
        print("The rest is history, you’ve been good friends with him ever since. Too the point that you decided to room up with him starting your 4th year at college.")
        time.sleep(10)


    def parkpathself(self):
        print("Does this work?")





# Starts the game and gets info such as name and class the player picks

sasha_encounter = SashaEncounter()  # Global instance of class SashaEncounter,very useful.

jacob_kitchen = JacobKitchen()  # Global instance of JacobKitchen

player_info = PlayerCharacter()  # Provides info for the player character

first_world = FirstWorld()

print("Hello", player_info.name)
time.sleep(3)
print("You are about to embark on a hastily made journey involving animal people")
time.sleep(3)
print("I'm not sure of the details quite yet, since I'm basically writing this as I go.")
time.sleep(3)
print("I'm sure it will be a perfectly coded, well wrote, masterpiece")
time.sleep(2)
print("First, let's go over your character choices you made.")
time.sleep(2)
print("Your name is", player_info.name, "you're a", player_info.sex, "and your race is a", player_info.race)
time.sleep(2)
print("If you are okay with those options, then we're good. If not you'll want to restart and select the options you want.")
time.sleep(5)
print("If you input garbage or invalid options at sex, or input a race that wasn't a lion, wolf, fox, or dragon, events in the story might end up not working. So keep that in mind.")
time.sleep(4)
input("If you understand this and are happy with your name, race, and sex, hit enter to continue")
print("With that out of the way, let's get started")
time.sleep(5)
print("You are in a dimly-lit room, you see a doorway to your north and to your east")
time.sleep(5)
startingroomlightswitch()
