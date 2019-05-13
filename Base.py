# Text game
import time
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Room functions. The bulk of the game


def rollintro ():
    print("In the beginning, there was nothing but this line of text")
    time.sleep(2)
    print ("But soon that changed, and the program began to develop")


def startingroomlightswitch ():
    lightswitch = ""
    while lightswitch != "north" and lightswitch != "east":
        lightswitch = input("Which way do you go?")
        if lightswitch == "north":
            hallway()
        elif lightswitch == "east":
           bathroom()
    return lightswitch

def bathroom ():
    while True:
        print("You enter a bathroom, you see a trunk on the floor and the doorway you entered to your west")
        bathroom = input("What do you do?")
        if bathroom in ["trunk", "Trunk", "Chest", "chest"]:
            print("You open the trunk and find a mysterious silicone sculpture")
            time.sleep(5)
        elif bathroom in ["west", "w", "West"]:
            print("You return to the dim room, you see a doorway to your north and the bathroom to your east")
            return startingroomlightswitch()


def hallway ():
    print("You enter a hallway with a doorway to your north and a staircase to your south")
    hallway = input("Which direction do you go?")
    if hallway in ["south", "South", "s", "S"]:
        entranceway()
    elif hallway in ["north", "North", "n", "N"]:
        bedroom()

def bedroom():
    while True:
        print("You enter what seems to be a bedroom, you see the typically items you'd expect to see in a bedroom")
        print("To your west you see a German Shepard sitting at a desk, to the south you see the doorway to the hallway")
        bedroomoption = input("What do you do?").lower()
        if bedroomoption == "talk":
            sashabedroomdialog()
        elif bedroomoption == "south" or "s":
            hallway()


def sashabedroomdialog():
    i = 1
    while i == 1:
        print("You approach the German Shepard and exchange greetings.")
        time.sleep(5)
        print("The German Shepard is your roommate, Sasha. She's a trustworthy sort. But a bit absent-minded at times")
<<<<<<< HEAD
        time.sleep(3)
        print("You’re alive! You’d been locked up in your room for so long \
        I thought you either died or got transported to another universe.")
        time.sleep(3)
        print("I’ve kept on top of all your chores, you’re gonna owe me for the weeks’ time you decided to disappear.\
        I was thinking you could take of my work for 2 or so weeks.")
        time.sleep(3)
=======
        time.sleep(10)
        print("""You’re alive! You’d been locked up in your room for so long I figured you either died or got transported to another universe.""")
        time.sleep(10)
        print("""I’ve kept on top of all your chores, you’re gonna owe me for the weeks’ time you decided to disappear. I was thinking you could take of my work for 2 or so weeks.""")
        i = i + 1
        if i == 2:
            break
    sashabedroom()
    while i == 2:
        print("Testing test")

def sashabedroom():
    print("You see Sasha, your roommate in the bedroom, and the doorway to the hallway to your south")
    direction = input("What do you wish to do?").lower()
    if direction == "south" or "s":
        hallway()
    elif direction == "talk":
        sashabedroomdialog()
>>>>>>> b04635f8bcbc26b96d0163de1ad6274f8dfd60a7

def entranceway ():
    print("You head down the stairs and enter the entrance way")
    print("You see a kitchen to your west, a living area to your east, and a front door to your north")
    entrancewaydirection = input("Which way do you go?").lower()
    if entrancewaydirection == "north":
        print("Placeholder text")

# Starts the game and gets info such as name and class the player picks

rollintro()

playername = input("What is your name? >")

print("Hello {}" .format(playername))
time.sleep(3)
print("You are about to embark on a hastily made journey involving animal people")
time.sleep(3)
print("I'm not sure of the details quite yet, since I'm basically writing this as I go.")
time.sleep(3)
print("I'm sure it will be a perfectly coded, well wrote, masterpiece")
time.sleep(3)

print("But first, you must create your character")
time.sleep(3)
print("Your options are a Wolf, Fox, Lion, or Dragon")
time.sleep(3)
playerclass = input("Which do you choose?")
if playerclass in ['Wolf', 'wolf']:
    print("You have choose to be a Wolf")
elif playerclass in ['Fox', 'fox']:
    print("You have choose to be a Fox")
elif playerclass in ['Lion', 'lion']:
    print("You have choose to be a Lion")
elif playerclass in ['Dragon', 'dragon']:
    print("You have choose to be a Dragon")
time.sleep(2)
print("With that out of the way, let's get started")
time.sleep (5)
print("You are in a dimly-lit room, you see a doorway to your north and to your east")
time.sleep(5)
startingroomlightswitch()