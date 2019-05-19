# Text game
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import secrets
import pygame

from pygame.locals import  *
# Room functions. This is the bulk of the game. Not sure if this is the best way to program this type of game
# But this seems to be the organized way, and the easiest way to edit things if needed.


# Idea to possibly implement: Replace the time.sleep commands with input commands to give the player more control.

class PlayerStats:
    def __init__(self, race, sex, name):
        self.name = name
        self.sex = sex
        self.race = race


class PlayerCharacter(PlayerStats):  # Grabs and stores info about player
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
    print("You enter a hallway with a doorway to your east and a staircase to your south")
    hallway = input("Which direction do you go? ").lower()
    if hallway in ["south", "s"]:
        entranceway()
    elif hallway in ["east", "e"]:
        if sasha_encounter.sashatalked == False:  # Checks to see if player has talked to sasha before
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
            print("You enter what looks to be a bedroom, you see the typical items you'd expect to see in a bedroom") # Change wording
            print("To your left you see a German Shepard sitting at a desk, to the south you see the doorway to the hallway")
            bedroomoption = input("What do you do? ").lower()
            if bedroomoption in ["talk", "t"]:
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
            print("The German Shepard is one of your roommates, Sasha. She's a trustworthy sort. But a bit absent-minded at times")
            time.sleep(10)
            print(""" "Where have you been all this time! I haven't seen you in over a week! I figured you most have went on an unannounced vacation." """)
            time.sleep(10)
            print(""" "I’ve kept on top of all your chores, you’re gonna owe me for the weeks’ time you decided to disappear. I was thinking you could take of my work for 2 or so weeks." """)
            self.sashatalked = True  # Indicates that the player has talked to Sasha allowing for more dialog
            self.sashabedroom()
        elif self.sashatalked == True:
            print(""" "You know, I actually had a friend in college once that disappeared for like 2 weeks" """)
            time.sleep(10)
            print(""" " Turns out she basically gave up and wasn't leaving her dorm. She was in a pretty bad place mentally, and ended up dropping all her classes and leaving college." """)
            time.sleep(10)
            print(""" "It was depressing watching my friend essentially fall apart. And by the time I knew something was up it was too late to intervene." """)
            time.sleep(5)
            print(""" "Makes me think of how I simply dismissed your disappearance as nothing to worry about. Who knows where could have been or what you could have been up too!" """)
            time.sleep(10)
            print(""" "Anyway, your fine now and that's all that matters. You might want to check in with Jacob, he was gone for half the week so he wasn't entirely sure how long you were gone for" """)
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
        print("You have entered the entrance way")
        time.sleep(2)
        print("You see a kitchen to your west, a living area to your east, the stairs to your south, and the front door to your north.")
        entrancewaydirection = input("Which way do you go? ").lower()
        if entrancewaydirection in ["north", "n"]:
            first_world.fronthousearea()
            break
        elif entrancewaydirection in ["west", "w"]:
            jacob_kitchen.startingkitchen()
            break
        elif entrancewaydirection in ["east", "e"]:
            print("You enter the living area and see nothing of note. You return to the entrance way.")
            time.sleep(3)
            return entranceway()
        elif entrancewaydirection in ["south", "s"]:
            hallway()
        else:
            print("Invalid input")
            return entranceway()


class JacobKitchen:
    def __init__(self):
        self.jacobtalked = False

    def startingkitchen(self):
        print("You enter the kitchen, there's various kitchen appliances and a table and chairs over to the right. You see a Deer to your left and the entrance way to the east. ")
        kitchendirection = input("What do you do? ")
        if kitchendirection in ["talk", "t"]:
            if self.jacobtalked == False:  # Dialog if Jacob hasn't been talked to before
                print("The Deer is one of your roommates, Jacob. You give him a pat on the shoulder and strike up a conversation")
                time.sleep(2)
                print('"Hey"', player_info.name, '"Where have you been these last few days? I haven’t seen you since I left for vacation last week. I got back about 3 days ago and haven’t seen you since."')
                time.sleep(5)
                print("Sasha told me she hadn’t seen you for a minute, but she wasn't exactly sure how long you'd been gone.")
                time.sleep(3)
                print('"Regardless, it’s good to see you. I dont know where you were for the past week or so but just know that I’m here if you need help or need someone to talk too."')
                self.jacobtalked = True  # Marks that the player has talked to Jacob
                self.startingkitchen()
            elif self.jacobtalked == True: # Dialog for Jacob after initial conversation
                print("Hey buddy. I've not nothing new to say.")
                self.startingkitchen()
        elif kitchendirection in ['east', 'e']:
            entranceway()
        else:
            print("Invalid input")
            return self.startingkitchen()


class FirstWorld:
    def fronthousearea(self):
        if sycamore_park.parkroommatepath is False or sycamore_park.parklakepath is False:
            print("You are standing on the front porch of your home. You can think of 3 places to travel too. The local community pool, the nearest park, or your favorite lunch spot, the cafe. You could also enter your house to the south.")
        elif sycamore_park.parkroommatepath is True or sycamore_park.parklakepath is True:
            print("You return home. You can enter the front dooor to your south, travel to the park again, go to the pool, or visit the cafe for lunch.")
        fronthouseareadirection = input("Where will you go? ").lower()
        if fronthouseareadirection in ["cafe", "lunch"]:
            tories_cafe.thecafe()
        elif fronthouseareadirection in ['park','p']:
            sycamore_park.lakepark()
        if fronthouseareadirection in ['south', 's']:
            entranceway()
        else:
            print("Invalid input or area in progress")


class ToriesCafe:
    def thecafe(self):
        print("You catch a ride on the bus and end up at Tories Place, your all-time favorite place to grab lunch")
        time.sleep(5)
        print("It’s a popular place amongst the younger crowd. The place has a modern aesthetic with colorful furniture and ample natural lighting giving the place a cheery vibe.")
        time.sleep(5)
        print("They’re famous for their fantastic wraps, and also have some pretty good soups.")
        time.sleep(3)
        print("Looking around you see the line to order, it’s a bit after lunch so there isn’t much of a wait. You also see a familiar face sitting down at one of the tables")
        time.sleep(5)
        cafedecision = input("Will you order first or go and say hi to the familiar face? ").lower()
        if cafedecision in ['order', 'eat', ]:
            print("You decide to order some food before going to say hi.")
            time.sleep(5)
            print("The line moves quick and before you know it’s your turn to order.")
            print("You decide to order your usual combo; a tuna wrap with a bag of chips and a drink. Not a bad deal for $4!")
            print("Having ordered your food, you head over to the table of Holly, a friend of yours from high school.") # Experimenting with a new text printing system
            input()
            print("Holly is a vixen, no, not like that. In the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
            input()
            print("You exchange greetings with Holly and start convesing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for proper conversation.")
            print('"Hey"', player_info.name,'.' '"Its been a while hasn\'t it? Last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!"')
            input()
            print("You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics")
            print("You ask what Holly’s been up too since then, a faint look of worry and disappointment fills her face as she describes her falling out from college")
            input()
            print('"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying college. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life"')
            print('"Like I said, my grades weren’t bad enough too have them kick me out, but they weren’t great either. I was holding about a 2.5 (out of 4) GPA"')
            input()
            print("You nod in agreement, remembering how many times you second guessed your major choice throughout college")
            input()
            print('"And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
            input()
            print("You can definitely see yourself understanding Holly’s decision, thinking back to all the workplace drama and rejected proposals you’ve dealt with…")
            print("You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer.")
            input()
            print('"I draw art for a living now! I’ve always been interested in drawing before, I’m sure you remember some of my drawings from back in high school. I never really thought of it as a legitimate career path, but I’ve managed to find a niche that pays a decent amount of money through commissions."')
            print('"I love it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
            input()
            print('"So, what have you been doing since graduating college? I know you finished college with a couple internships and a great GPA, so that’s probably gotten you somewhere right?"')
            input()
            print("You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons she stated, like project managers ignoring ideas.")
            print("You state that you had luckily saved up enough money to live comfortably for around 2 years before quitting. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
            input()
            print("'Man, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine being able to have a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and half!'")
            print("'Still, like I said, I enjoy my work and I wouldn’t want it any other way.'")
            input()
            print("Well", player_info.name, "it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around.")
            print("You say goodbye to Holly and decide to head home for the day")
            input()
            hallway()
        elif cafedecision in ['talk', 't', 'face' 'hi']:
            print("You decide to first go over and say hi to Holly.")
            print("Holly is a vixen, no, not like that. In the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
            input()
            print("You exchange greetings with Holly and start convesing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for proper conversation.")
            print('"Hey"', player_info.name, "." "'Last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!'")
            input()
            print("You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics")
            print("You ask what Holly’s been up too since then, a faint look of worry and disappointment fills her face as she describes her falling out from college")
            input()
            print("'Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying college. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life'")
            print("'Like I said, my grades weren’t bad enough too have them kick me out, but they weren’t great either. I was holding about a 2.5 (out of 4) GPA'")
            input()
            print("You nod in agreement, remembering how many times you second guessed your major choice throughout college")
            input()
            print("'And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me.'")
            input()
            print("You can definitely see yourself understanding Holly’s decision, thinking back at all the workplace drama and rejected proposals you’ve dealt with…")
            print("You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer")
            input()
            print("'I draw art for a living now! I’ve always been interested in drawing before, I’m sure you remember some of my drawings from back in high school. I never really thought of it as a legitimate career path, but I’ve managed to find a niche that pays a decent amount of money through commissions.'")
            print("'I love it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do.'")
            input()
            print("'So, what have been doing since graduating college? I know you finished with couple internships and a great GPA, so that’s had to have gotten you somewhere right?'")
            input()
            print("You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons she stated, like project managers ignoring ideas.")
            print("You state that you had luckily saved up enough money to live comfortably for around 2 years before quitting. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
            input()
            print("'Man, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine being able to have a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and half!'")
            print("'Still, like I said, I enjoy my work and I wouldn’t want it any other way.'")
            input()
            print("'Well'", player_info.name, "'it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around.'")
            print("You say goodbye to Holly and decide to head home for the day")
            input()
            hallway()


class SycamorePark:
    def __init__(self):
        self.parkroommatepath = False
        self.parklakepath = False

    def lakepark(self):
        if self.parkroommatepath is False or self.parklakepath is False:
            print("You arrive at Sycamore Lakeview Park after a short walk down the street. You’ve never really been too this park (or any park really) despite being close to home.")
            time.sleep(5)
            print("You’ve never really felt like going to the park, you were always preoccupied by something else, just not up to going out, or sacred by the various flying insects that call this place home. ")
            time.sleep(8)
            print("You’re here now and ready to make the most it. As you enter the park you see two separate walking paths you could take. One to the west, the other to the east. Or you could just say forget this whole thing and head back home.")
        else:
            print("You arrive at the park entrance, you see the two walking paths to your east and to your west. You could also head home.")
        pathdialog = [self.parkpathrommates, self.parkpathself]  # In order to sort functions you can't call the function in this list.

        parkdecision = input("After thinking about it, you decide to go... ").lower()
        if parkdecision in ['home', 'away',]:
            print("You decide you still aren’t feeling up to a walk in the park and head home")
            first_world.fronthousearea()

        elif parkdecision in ['east', 'e']:
            print("You head down the path to your right.")
            time.sleep(4)
            if self.parkroommatepath is False and self.parklakepath is False: # Randomly picks which path to go down
                print(secrets.choice(pathdialog)()) # Instead you call the function from the randomization bit. Like this
            elif self.parkroommatepath is True and self.parklakepath is False: # If the player has not seen the self reflection path it will play that instead of a random selection or roommate path.
                self.parkpathself()
            elif self.parkroommatepath is False and self.parklakepath is True: # If the player has not seen the roommate path has not been seen it will play that instead of the random selection or self path
                self.parkpathrommates()

        elif parkdecision in ['west', 'w']:
            print("You head down the path to your left.")
            time.sleep(3)
            if self.parklakepath is False and self.parkroommatepath is False: # Randomly picks which path to go down first
                print(secrets.choice(pathdialog)())
            elif self.parklakepath is True and self.parkroommatepath is False: # If the player has seen the self reflection path the roommate path is played instead
                self.parkpathrommates()
            elif self.parklakepath is False and self.parkroommatepath is True: # If the player has seen the roommate path then the self reflection path is played
                self.parkpathself()


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
        print("The rest is history, you’ve been good friends with him ever since. To the point that you decided to room up with him starting your 4th year at college.")
        time.sleep(10)
        print("You ended up meeting Sasha in a similar way. You ran into her at one of the dining halls your very first year at college. You were sitting by yourself, and she came up and asked to sit with you. It seems a bit odd now but during your first year of college people will find practically any excuse to become friends with someone.")
        time.sleep(20)
        print("You started off with the usual small talk, ‘Hey, what’s your major?’ ‘What dorm do you live in?’ She ended up living in one of the nearby dorm complexes, which shared a dining hall with your building. This led to you and her getting lunch together on a regular basis")
        time.sleep(20)
        print("You talked quite a bit during lunch, and you eventually ended up hanging out with her outside of lunch quite a bit. You didn’t have as much in common with her as Jacob, but you still appreciated her company. As she did with you.")
        time.sleep(20)
        print("You always kept in touch with her throughout the semesters, often attending various on-campus event together, and helping each other with classes. The relationship never really advanced beyond being good friends. You’ve never had very strong feelings for her, and apparently neither has she. Although, you did have some feelings for her your 1st year but they faded soon after that.")
        time.sleep(20)
        print("She’s been a really great friend to you, though she can be a bit forgetful at times. You’re really glad you met her and Jacob during your time at college, who knows how different your current life would be if you didn’t!")
        time.sleep(20)
        print("Caught up in your thoughts you find yourself at the end of your walk before you know it. You are now back at the park entrance way.")
        time.sleep(5)
        self.parkroommatepath = True
        self.lakepark()


    def parkpathself(self):
        print("15 minutes into the walk you come across a familiar sight, the Sycamore Lake. Hence the park’s name.")
        time.sleep(5)
        print("You’ve seen this lake at least a thousand times throughout your life. In both good and bad times. You normally never give a second thought when looking out upon its seemingly never-ending horizon, but this time was different.")
        time.sleep(20)
        print("The scenery reminds you of a past story, of past friendships. Memories from 15 years ago rush into your mind. It was a happier time, sometimes you think it might have even been the happiest you’ve ever been.")
        time.sleep(20)
        print("Back then, you had the best friend-circle. You had no worries. Every summer you and your family would go a lake house on the weekends. Which was where most of your real friends were.")
        time.sleep(20)
        print("The lake house wasn’t much, in fact it wasn’t a house at all. But rather a trailer that your parents were paying the equivalent of a car payment to own.")
        time.sleep(10)
        print("You had your core group of friends, and then from there you’d have a best friend or two that you’d always hang out with. For you, those friends were Jane and Abbey.")
        time.sleep(15)
        print("They were sisters, in-fact. Whenever your other friends left, either for home or for another one of their friends, you knew that one of them would be there for you.")
        time.sleep(10)
        print("It’s not an exaggeration to say that those two were some of the biggest non-family influences on your life. For both good and bad reasons")
        time.sleep(10)
        print("The good parts have already been mentioned for the most part. They were always there for you. They supported you and you supported them. You can recall countless memories from your childhood revolving around them.")
        time.sleep(20)
        print("Like that time their family took you to the water park. It was fantastic. You’d never been too such a wounderful place. Water rides and pools as far as your small eyes could see.")
        time.sleep(10)
        print("It wasn’t all perfect, as they brought along another one of their friends that you weren’t really fond of. But still, it was that kind of stuff that really solidified your friendship. None of your other friends that did that kind of stuff for you. They still don’t")
        time.sleep(20)
        print("As you look back at those memories it feels bittersweet. It’s like the saying ‘Don’t be sad that it’s over, be glad that it happened’ expect you just can’t get over the sadness of it being all over.")
        print("The memories are nice but still having those people in your life would be better.")
        time.sleep(25)
        print("Unfortunately, people drift apart, they change. You grow up, your interests change, you move away from those people… Sometimes you can get over it, but when someone has that much of an impact on your life, it’s tough. Even 7 years after its happened.")
        time.sleep(25)
        print("As you reminisce on your memories you realize that over an hour has passed, you snap out of it and finish your walk prematurely before heading back to the park entrance way.")
        self.parklakepath = True
        self.lakepark()







# Starts the game and gets info such as name and class the player picks

sasha_encounter = SashaEncounter()  # Global instance of class SashaEncounter,very useful.

jacob_kitchen = JacobKitchen()  # Global instance of JacobKitchen

player_info = PlayerCharacter()  # Provides info for the player character

first_world = FirstWorld()

sycamore_park = SycamorePark()

tories_cafe = ToriesCafe()

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
