# Text game
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# Room functions. This is the bulk of the game. Not sure if this is the best way to program this type of game
# But this seems to be the organized way, and the easiest way to edit things if needed.


class Player:
    def __init__(self):
        self.race = playerrace
        self.name = playername
        self.sex = playersex


def rollintro ():
    print("In the beginning, there was nothing but this line of text")
    time.sleep(2)
    print("But soon that changed, and this game began to develop")


def startingroomlightswitch ():
    lightswitch = ""
    while lightswitch != "north" and lightswitch != "east":
        lightswitch = input("Which way do you go? ")
        if lightswitch == "north":
            hallway()
        elif lightswitch == "east":
            bathroom()
    return lightswitch


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
        print("You see a kitchen to your west, a living area to your east, and the stairs to your north")
        entrancewaydirection = input("Which way do you go? ").lower()
        if entrancewaydirection in ["north", "n"]:
            hallway()
        elif entrancewaydirection in ["west", "w"]:
            jacob_kitchen.startingkitchen()
            break
        elif entrancewaydirection in ["east", "e"]:
            print("Area is a work in progress")
        else:
            print("Invalid input")


class JacobKitchen:
    def __init__(self):
        Jacobtalked = False

    def startingkitchen(selfs):
        print("You enter a kitchen, there's a various kitchen appliances and a table and chairs over to the right. You see a Deer to the west. ")
        kitchendirection = input("What do you do? ")
        if kitchendirection in ["west", "w"]:
            print("The Deer is your roommate, Jacob. You give him a pat on the shoulder and strike up a conversation")
 print("Hey {}" .format(player_info.playername), """ "Where have you been these last few days? I haven’t seen you since I left for vacation last week. I got back about 3 days ago and you’ve appeared missing since" """)


# Starts the game and gets info such as name and class the player picks

sasha_encounter = SashaEncounter()  # Global instance of class SashaEncounter,very useful.

jacob_kitchen = JacobKitchen()  # Global instance of JacobKitchen

player_info = Player()

rollintro()

playername = input("What is your name? > ")

print("Hello {}" .format(playername))
time.sleep(3)
print("You are about to embark on a hastily made journey involving animal people")
time.sleep(3)
print("I'm not sure of the details quite yet, since I'm basically writing this as I go.")
time.sleep(3)
print("I'm sure it will be a perfectly coded, well wrote, masterpiece")
time.sleep(3)


print("But first, we'll create your character")
time.sleep(3)
playersex = input("Do you want to be male or female? ").lower()
if playersex in ["male"]:
    print("You have choose to be male.")
elif playersex in ["female"]:
    print("You have choose to be female.")
else:
    print("Please choose either male or female. ")

print("Now, let's pick your race")
time.sleep(2)
print("Your race options are: Wolf, Fox, Lion, or Dragon")
time.sleep(3)
playerrace = input("Which do you choose? ")
if playerrace in ['Wolf', 'wolf']:
    print("You have choose to be a Wolf")
elif playerrace in ['Fox', 'fox']:
    print("You have choose to be a Fox")
elif playerrace in ['Lion', 'lion']:
    print("You have choose to be a Lion")
elif playerrace in ['Dragon', 'dragon']:
    print("You have choose to be a Dragon")

time.sleep(2)
print("With that out of the way, let's get started")
time.sleep (5)
print("You are in a dimly-lit room, you see a doorway to your north and to your east")
time.sleep(5)
startingroomlightswitch()