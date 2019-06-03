# Text game
# -*- coding: utf-8 -*-

import time
import secrets
import sys
import os
import pickle
import TravelSystem
import SashaHouse


class PlayerStats:
    """This class takes and store info about the player character. This includes their user-defined name, their sex, and
    their race. As of recent it also keeps track of their location. This was needed to implement the save system"""
    def __init__(self, race, sex, name, money):  # Make it so user cannot enter garbage values for these.
        self.name = name
        self.sex = sex
        self.race = race
        self.player_location = ""
        self.money = money


class PlayerCharacter(PlayerStats):
    """This is where the user defines their character. This probably one of the things I'm most proud of in this project.
    This class allows for me to easily add features as I need. Such as the money system. It literally took me two lines of
    code to add that. I could easily add a health system if needed."""
    def __init__(self):
        super().__init__(name=input("What is your name? "), sex=input("Do you wish to play as male or female? "),  # I barely remember how the fuck I built this. Seems really complex for my knowledge level of python at the time.
                         race=input(
                             "Which race do you want to play as? Wolf, Lion, Fox or Dragon? (This is will not have a large effect on the game) ").title(), money=1200)

    def bank_money(self):
        print("You fire up your smartphone and check your bank balance")
        print("Your current balance is ${}".format(player_info.money))


class GameState:  # Might have to put this in base because the import is causing all kinds of issues.
    def saving(self):
        import SashaHouse
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([player_info.player_location, player_info.name, player_info.sex,
                     player_info.race, player_bathroom.bathroombaddragon, SashaHouse.sasha_encounter.sashatalked,
                     SashaHouse.sasha_living.sashalivingroomdialogue, jacob_kitchen.jacobtalked, tories_cafe.cafefinished,
                     sycamore_park.parklakepath, sycamore_park.parkroommatepath], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        return

    def loading(self):
        #import SashaHouse
        print("Loading game")
        pickle_in = open('gamestate.pickle', 'rb')
        [player_info.player_location, player_info.name, player_info.sex,
         player_info.race, player_bathroom.bathroombaddragon, SashaHouse.sasha_encounter.sashatalked,
         SashaHouse.sasha_living.sashalivingroomdialogue, jacob_kitchen.jacobtalked, tories_cafe.cafefinished,
         sycamore_park.parklakepath, sycamore_park.parkroommatepath] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        self.playerlocation()

    def playerlocation(self):
        if player_info.player_location in ['PC Bedroom', 'Sasha Living Room']:
            pcbedroom()
        elif player_info.player_location in ["Sasha First Dialogue", 'Sasha Second Dialogue', 'Holly Cafe']:
            hallway()
        elif player_info.player_location in ['Jacob Kitchen Dialogue']:
            entranceway()
        elif player_info.player_location in ['Park Walk']:
            sycamore_park.lakepark()
        elif player_info.player_location in ['Festival Start']:
            import Festival
            Festival.festival_area.festival_entrance()



def intro():
    print("As you finish the 5th and final season of Barking Bad you feel a sense of satisfaction, but also a feeling of sadness. The culmination of 5 years work is over in the span of an hour.")
    input()
    print("While you’re satisfied with the ending of the show, you can’t help but feel disappointed that there won’t be any more episodes to look forward too. You find that it’s a common feeling when it comes to finishing excellent media.")
    print("It’s been a familiar feeling as of recent, as you’ve binge watched 3 different shows this past week while staying at Teuton Resorts. The vacation giving yourself a break from your obligations, and from your housemates.")
    input()
    print("Unfortunately, this is your last day here, as your reservation is up tomorrow. Your long-awaited vacation is over almost as soon as it began, you think.")
    input()
    print("You spent the rest of the day packing and cleaning the room. The next day you grab breakfast and head off for home.")
    input()
    print("You eventually arrive at home in the evening, with none of your housemates to be seen. You bring your stuff inside and unpack it before getting something to eat. Afterwards you watch a short movie in your room and go to bed, another day in paradise.")
    input()
    pcbedroom()


def pcbedroom():
    #import SashaHouse
    if player_bathroom.bathroombaddragon is False:
        print(
            "You wake up the next morning, your bedroom is dimly lit with the only source of light being the sun as it sneaks through the blinds.")
    if tories_cafe.cafefinished is True and SashaHouse.sasha_living.sashalivingroomdialogue is False:
        print("After returning from the cafe you do work on one of your current contracts before going to bed")
    if SashaHouse.sasha_living.sashalivingroomdialogue is True and jacob_kitchen.jacobbedroom is False:
        print("You wake up the next day feeling better. Your conversation with Sasha helped ease your mind, and made you realize just how great of friends you have now.")
        print("You think about possibly asking Jacob about some of his past trips. He should be in his bedroom.")
        input()
    print("You are standing in your bedroom. You see the door to the bathroom to your east, and the doorway to the hallway directly ahead to the north.")
    print("You could also check your bank balance.")
    player_info.player_location = 'PC Bedroom'
    pcbedroomdirection = input('Which way do you go? ').lower()
    if pcbedroomdirection in ['east', 'e']:
        player_bathroom.bathroompc()

    elif pcbedroomdirection in ['north', 'n']:
        hallway()

    elif pcbedroomdirection in ['save']:
        save_load.saving()

    elif pcbedroomdirection in ['bank', 'money', 'balance']:
        player_info.bank_money()

    else:
        print("Invalid input")
        return pcbedroom()

class PCBathroom:
    def __init__(self):
        self.bathroombaddragon = False

    def bathroompc(self):
        while True:
            if self.bathroombaddragon is True:
                print("You see the opened trunk on the floor and the doorway you entered to your west")

            elif self.bathroombaddragon is False:
                print("You enter a bathroom, you see a trunk on the floor and the doorway you entered to your west")

            bathroomoption = input("What do you do? ").lower()

            if bathroomoption in ["trunk", "chest"] and self.bathroombaddragon is False:  # Prevents user from opening trunk more than once
                print("You open the trunk and find a mysterious silicone sculpture")
                self.bathroombaddragon = True
                input()
                return self.bathroompc()

            elif bathroomoption in ['trunk', 'chest'] and self.bathroombaddragon is True:
                print("There's nothing more in the trunk.")
                input()

            elif bathroomoption in ["west", "w", "West"]:
                print("You return to your bedroom.")
                return pcbedroom()


def hallway():
    #import SashaHouse
    while True:
        print("You enter a hallway. There a doorway to your east, a staircase to your west, and another doorway to the north.")
        hallwaydirection = input("Which direction do you go? ").lower()
        if hallwaydirection in ["west", "w"]:
            entranceway()
            break
        elif hallwaydirection in ["east", "e"]:
            if SashaHouse.sasha_encounter.sashatalked is False:  # Checks to see if player has talked to sasha before
                SashaHouse.sasha_encounter.bedroom()
                break
            elif SashaHouse.sasha_encounter.sashatalked is True:
                SashaHouse.sasha_encounter.sashabedroom()
                break
        elif hallwaydirection in ['save']:
            save_load.saving()
        elif hallwaydirection in ['north', 'n']:
            if SashaHouse.sasha_living.sashalivingroomdialogue is False:
                print("The door is locked. Maybe you should come back later.")
                return hallway()
            elif SashaHouse.sasha_living.sashalivingroomdialogue is True:
                jacob_kitchen.bedroomdialogue()
        else:
            print("Invalid input")
            return hallway()


def entranceway():
    while True:
        print("You have entered the entrance way")
        print(
            "You see a kitchen to your west, a living area to your east, the stairs to your south, and the front door to your north.")
        entrancewaydirection = input("Which way do you go? ").lower()
        if entrancewaydirection in ["north", "n"]:
            first_world.fronthousearea()
            break

        elif entrancewaydirection in ["west", "w"]:
            jacob_kitchen.startingkitchen()
            break

        elif entrancewaydirection in ["east", "e"]:
            if jacob_kitchen.jacobtalked is True and tories_cafe.cafefinished is True and sycamore_park.parklakepath is True and SashaHouse.sasha_encounter.sashatalked is True:
                #import SashaHouse
                SashaHouse.sasha_living.sashadialogue()
            else:
                print(
                    "You enter the living area and see nothing of note. Perhaps you should return here after visiting a couple places.")
                input()
            return entranceway()

        elif entrancewaydirection in ["south", "s"]:
            hallway()

        elif entrancewaydirection in ['save']:
            save_load.saving()

        else:
            print("Invalid input")
            return entranceway()

class JacobDialogue:
    def __init__(self):
        self.jacobtalked = False
        self.jacobbedroom = False

    def startingkitchen(self):
        while True:
            print(
                "You enter the kitchen, there's various kitchen appliances and a table and chairs over to the right. You see a Deer to your left and the entrance way to the east. ")
            kitchendirection = input("What do you do? ").lower()
            if kitchendirection in ["talk", "t"]:
                if self.jacobtalked is False:  # Dialogue if Jacob hasn't been talked to before
                    print(
                        "The Deer is one of your roommates, Jacob. You give him a pat on the shoulder and strike up a conversation")
                    print(
                        '"Hey {}! What’s up? Where have you been these last few days? I haven’t seen you since I went to visit my parents last week. I got back about 3 days ago and haven’t seen you since."'.format(player_info.name))
                    input()
                    print(
                        '"Sasha told me she hadn’t seen you for a minute, but she wasn\'t exactly sure how long you\'d been gone."')
                    input()
                    print("You tell Jacob that you went on a week-long vacation a bit up north.")
                    input()
                    print('"That sounds pretty nice. Seems like it was bit of a rushed vacaton though you didn’t give anyone any notice or anything."')
                    print('"Then again, maybe you just wanted to escape from everybody for a little bit. That\'s understandable."')
                    input()
                    print(
                        '"Regardless, it’s good to see you. If you ever wanna talk about that vacation a bit more in-depth just let me know, I’d been thinking of possibly going up there myself."')
                    input()
                    self.jacobtalked = True  # Marks that the player has talked to Jacob
                    player_info.player_location = 'Jacob Kitchen Dialogue'
                    return self.startingkitchen()
                elif self.jacobtalked is True:  # Dialogue for Jacob after initial conversation
                    print("'Hey buddy. I've not nothing new to say.'")
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
        print("As you look around you see how nicely decorated Jacob’s room is. You see the various landscape paintings on his walls and the house plants he has. It all meshes together great and creates a soothing atmosphere.")
        input()
        print('"What’s up?  Come to talk ‘bout that vacation?"')
        print("You tell Jacob that’s not quite what you had in mind, though the vacation will likely come up in the conversation.")
        input()
        print('"Okay then, what’d you want talk about?"')
        print('You start by telling Jacob that you wanted to talk about his past trips. He’d talked previously about going on long trips out of state, something that you might be interested in doing yourself.')
        input()
        print('"Yeah, I’ve gone on a few trips out of state, I think furthest I’ve went was about a days’ worth of driving away"')
        print('"That was when I went to Yellowstone. What a fantastic place to visit."')
        input()
        print('"Honestly I’m not a very big fan of long ass drives like that. It gets really tired after about 6 hours"')
        print('You can find yourself agreeing with Jacob, staying in a car for 24 hours doesn’t exactly seem like the greatest time.')
        input()
        print('You tell Jacob that’s part of the reason you’ve never really gone vacation anywhere too far away. The drive can really get too you.')
        input()
        print('"Yeah, I think that ends up being the case with a lot of people. You could fly, of course. In fact, that’s probably the best way to go for long distance vacations. But if you’re going only, say, 6 hours away, flying isn’t really an economical option."')
        input()
        print("You thank Jacob for shedding some light on his past trip. You’re still not sure if something like that is for you, you’ll just have to think about it.")
        input()
        print("After talking with Jacob, you take some time and finish the current contract you’re working on. The deadline was still 1 week away but of course its best to get it done early.")
        print("You are awarded $800 for the contract, you put 200 in your checking account, and the rest goes into an investment account.")
        input()
        player_info.money += 200
        print("Your bank balance is now {}".format(player_info.money))
        input()
        print("New travel area unlocked.")
        self.jacobbedroom = True
        input()
        pcbedroom()



class FirstWorld:
    def fronthousearea(self):
            print("You stand on your front porch ready for adventure! You could also return home by entering the door to your south.")
            fronthouseareadirection = input("Will you travel or return home?").lower()
            if fronthouseareadirection in ['travel', 't', 'go' 'adventure']:
                travel_system.travel_function.traveltofront()
            elif fronthouseareadirection in ['south', 's' 'home' 'door']:
                entranceway()
            else:
                print("Invalid input or area in progress")
                return self.fronthousearea()


class ToriesCafe:
    def __init__(self):
        self.cafefinished = False

    def thecafe(self):
        print("You catch a ride on the bus and end up at Tories Place, your all-time favorite place to grab lunch")
        print(
            "It’s a popular place amongst the younger crowd. The place has a modern aesthetic with colorful furniture and ample natural lighting giving the place a cheery vibe.")
        input()
        print("They’re known for their fantastic wraps, and also have some pretty good soups.")
        print(
            "Looking around you see the line to order, it’s a bit after lunch so there isn’t much of a wait. You can also see a familiar face sitting down at one of the tables")
        cafedecision = input("Will you order first or go and say hi to the familiar face? ").lower()

        if cafedecision in ['order', 'eat', ]:
            print("You decide to order some food before going to say hi.")
            print("The line moves quick and before you know it’s your turn to order.")
            input()
            print(
                "You decide to order your usual combo; a tuna wrap with a bag of chips and a drink. Not a bad deal for $4!")
            player_info.money -= 4
            print("Your bank balance is now ${}".format(player_info.money))
            print("Having ordered your food, you head over to the table of Holly, a friend of yours from high school.")
            self.hollydialoguecafe()

        elif cafedecision in ['talk', 't', 'face' 'hi']:
            print("You decide to first go over and say hi to Holly.")
            input()
            self.hollydialoguecafe()

        else:
            print("Invalid input")
            return self.thecafe()


    def hollydialoguecafe(self):
        print(
            "Holly is a vixen. No, no, not like that, in the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
        input()
        print(
            "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for proper conversation.")
        print(
            '"Hey {}! It\'s been awhile. I think the last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!"'.format(
                player_info.name))
        input()
        print(
            "You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics")
        print(
            "You ask what Holly’s been up too since then, a faint look of discomfort fills her face as she describes her falling out from college")
        input()
        print(
            '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying college. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life"')
        input()
        print(
            "You nod in agreement, remembering how many times you second guessed your choice to attend college.")
        input()
        print(
            '"And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
        input()
        print(
            '"That’s just me though. You know I’ve never been one to suck up and deal with other people’s bullshit"')
        input()
        print(
            "You can definitely see yourself understanding Holly’s decision, thinking back at all the workplace drama and rejected proposals you’ve dealt with…")
        print(
            "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer.")
        input()
        print(
            '"I draw art for a living now! I’ve always been interested in drawing before, I’m sure you remember some of my drawings from back in high school. I never really thought of it as a legitimate career path, but I’ve managed to find a niche that pays a decent amount of money through commissions."')
        print(
            '"And you know, I really enjoy it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
        input()
        print(
            '"So, what have been doing since graduating college? I know you finished with couple internships and a great GPA, so that’s had to have gotten you somewhere right?"')
        input()
        print(
            "You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons she stated, like project managers ignoring ideas.")
        print(
            "You state that you had luckily saved up enough money to live comfortably for around 2 years before quitting. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
        input()
        print(
            '"Wow, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine being able to have a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and half!"')
        print('"Still, like I said, I enjoy my work and I wouldn’t want it any other way."')
        input()
        print(
            '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around."'.format(
                player_info.name))
        print("You say goodbye to Holly and decide to head home for the day")
        input()
        player_info.player_location = 'Holly Cafe'
        self.cafefinished = True
        hallway()

class SycamorePark:
    def __init__(self):
        self.parkroommatepath = False
        self.parklakepath = False

    def lakepark(self):
        if self.parkroommatepath is False or self.parklakepath is False:
            print(
                "You arrive at Sycamore Lakeview Park after a short walk down the street. You’ve never really been too this park (or any park really) despite being close to home.")
            print(
                "You’ve never really felt like going to the park, you were always preoccupied by something else, just not up to going out, or sacred by the various flying insects that call this place home. ")
            input()
            print(
                "Well, you’re here now and ready to make the most it. As you enter the park you see two separate walking paths you could take. One to the west, the other to the east. Or you could just say forget this whole thing and head back home.")
        else:
            print(
                "You arrive at the park entrance, you see the two walking paths to your east and to your west. You could also head home.")
        pathdialog = [self.parkpathrommates,  # Used to randomize the path choice
                      self.parkpathself]  # In order to sort functions you can't call the function in this list.

        parkdecision = input("After thinking about it, you decide to go... ").lower()
        if parkdecision in ['home', 'away', ]:
            print("You decide too head home")
            first_world.fronthousearea()

        elif parkdecision in ['east', 'e']:
            print("You head down the path to your right.")
            time.sleep(3)
            if self.parkroommatepath is False and self.parklakepath is False:  # Randomly picks which path to go down
                print(
                    secrets.choice(pathdialog)())  # Instead you call the function from the randomization bit. Like this
            elif self.parkroommatepath is True and self.parklakepath is False:  # If the player has not seen the self reflection path it will play that instead of a random selection or roommate path.
                self.parkpathself()
            elif self.parkroommatepath is False and self.parklakepath is True:  # If the player has not seen the roommate path has not been seen it will play that instead of the random selection or self path
                self.parkpathrommates()

        elif parkdecision in ['west', 'w']:
            print("You head down the path to your left.")
            time.sleep(3)
            if self.parklakepath is False and self.parkroommatepath is False:  # Randomly picks which path to go down first
                print(secrets.choice(pathdialog)())
            elif self.parklakepath is True and self.parkroommatepath is False:  # If the player has seen the self reflection path the roommate path is played instead
                self.parkpathrommates()
            elif self.parklakepath is False and self.parkroommatepath is True:  # If the player has seen the roommate path then the self reflection path is played
                self.parkpathself()
        elif parkdecision in ['save']:
            save_load.saving()
        else:
            print("Invalid input")
            return self.lakepark()

    def parkpathrommates(self):
        print("This path is a slightly shorter path than the other one, as it doesn't go past the lake.")
        time.sleep(3)
        print(
            "About 25 minutes into your hour or so walk you come across a group of college aged people hanging out on a set of benches. They remind you of your more recent years spent around Sasha and Jacob.")
        input()
        print("You remember how you met both of them your 3rd year of college. At different times of course.")
        print(
            "You met Jacob in one of your upper-division elective courses, the one about environmental ethics or something of the sort. Very fitting considering Jacob has been a very outdoorsy, tree hugging type of guy ever since you’ve known him")
        input()
        print(
            "You ended up starting a study group with him since you weren’t exactly having a great time in class. As it was taught by a not so fantastic instructor. It started off as a pretty standard study group, consisting of you, Jacob and a couple other students. Eventually you started hanging out with him outside of the group and found out that he’s a really cool guy. You liked the same kind of movies, both loved pasta, and even ended up owning the same kind of car")
        input()
        print(
            "The rest is history, you’ve been good friends with him ever since. To the point that you decided to room up with him starting your 4th year at college.")
        input()
        print(
            "You ended up meeting Sasha in a similar way. You ran into her at one of the dining halls your very first year at college. You were sitting by yourself, and she came up and asked to sit with you.")
        print(
            "You started off with the usual college small talk, ‘Hey, what’s your major?’ ‘What dorm do you live in?’ She ended up living in one of the nearby dorm complexes, which shared a dining hall with your building. This led to you and her getting lunch together on a regular basis")
        input()
        print(
            "You talked quite a bit during lunch, and you eventually ended up hanging out with her outside of lunch quite a bit. You didn’t have as much in common with her as Jacob, but you still appreciated her company. As she did with you.")
        print(
            "You always kept in touch with her throughout the year, often attending various on-campus event together, and helping each other with classes. The relationship never really advanced beyond being good friends. You’ve never had very strong feelings for her, and apparently neither has she. Although... you do remember having some feelings for her when you first met, but they faded soon after that.")
        input()
        print(
            "She’s been a really great friend to you, though she can be a bit forgetful at times. You’re really glad you met her and Jacob during your time at college, who knows how different your current life would be if you didn’t!")
        input()
        print(
            "Caught up in your thoughts you find yourself at the end of your walk before you know it. You are now back at the park entrance way.")
        player_info.player_location = 'Park Walk'
        self.parkroommatepath = True
        input()
        self.lakepark()

    def parkpathself(self):
        self.parklakepath = True
        print("15 minutes into the walk you come across a familiar sight, the great Sycamore Lake. Hence the park’s name.")
        print(
            "You’ve seen this lake at least a thousand times throughout your life. In both good and bad times. You normally never give a second thought when looking out upon its seemingly never-ending horizon, but this time is different.")
        input()
        print(
            "The scenery reminded you of a past story. Memories from 15 years ago rush into your mind. It was a happier time, or at least it seems that way. Sometimes you think it might have even been the happiest you’ve ever been.")
        print(
            "Back then, you had the best friend-circle. And being a kid, you had no worries. Every summer you and your family would go to a lake house on the weekends. That's where most of your real friends were.")
        print(
            "The lake house wasn’t much, in fact it wasn’t a house at all. But rather a trailer that your parents were paying the equivalent of a car payment to own.")
        input()
        print(
            "As far as your friends go, you had your core group of friends, and then from there you’d have a best friend or two that you’d always hang out with. For you, those friends were Jane and Abbey.")
        print(
            "They were sisters, in-fact. And they were some of your best friends. You did tons of stuff together, swimming, movies, games, everything. You don't even remember how you met them, just that they were some of your closet friends ever since you did meet.")
        print(
            "It’s not an exaggeration to say that those two were some of the biggest non-family influences on your life. For both good and bad reasons")
        print(
            "The good parts have already been mentioned for the most part. They were always there for you. They supported you and you supported them. You can recall countless memories from your childhood revolving around them.")
        input()
        print(
            "Like that time their family took you to the water park. It was fantastic. You’d never been too such a wonderful place. Water rides and pools as far as your small eyes could see.")
        print(
            "It wasn’t all perfect, as they brought along another one of their friends that you weren’t really fond of. But still, it was trips like that really solidified your friendship. None of your other friends that did that kind of stuff with you. They still don’t")
        input()
        print(
            "As you look back at those memories it feels bittersweet. It’s like the saying ‘Don’t be sad that it’s over, be glad that it happened’ Though that can be hard to deal with some days.")
        print("The memories are nice but still having those people in your life would be better.")
        print(
            "Unfortunately, people drift apart, they change. You grow up, your interests change, you move away from those people… Sometimes you can get over it, but when someone has that much of an impact on your life, it’s tough. Even 7 years after its happened.")
        input()
        print(
            "As you reminisce on your memories you realize that over an hour has passed, you snap out of it and finish your walk prematurely before heading back to the park entrance way.")
        player_info.player_location = 'Park Walk'
        self.parklakepath = True
        input()
        self.lakepark()

# Global Classes


jacob_kitchen = JacobDialogue()  # Global instance of JacobKitchen

player_info = PlayerCharacter()  # Provides info for the player character

first_world = FirstWorld()

sycamore_park = SycamorePark()

tories_cafe = ToriesCafe()

player_bathroom = PCBathroom()  # Make sure to include the () when adding classes)

travel_system = TravelSystem

save_load = GameState()

# Starts the game
loadingoption = input("Do you wish to load a game? ").lower()  # Make it so this is the first question asked.
if loadingoption in ['yes', 'y', 'load', 'l']:
    save_load.loading()
elif loadingoption in ['no', 'n']:
    pass
print("Hello", player_info.name)
time.sleep(3)
print("You are about to embark on a hastily made journey involving animal people")
time.sleep(3)
print("I'm not sure of the details quite yet, since I'm basically writing this as I go.")
time.sleep(3)
print("I'm sure it will be a perfectly coded, well wrote, masterpiece")
time.sleep(2)
print("First, let's go over the character choices you've made.")
time.sleep(2)
print("Your name is", player_info.name, "you're a", player_info.sex, "and your race is a", player_info.race)
time.sleep(2)
print(
    "If you are okay with those options, then we're good. If not you'll want to restart and select the options you want.")
time.sleep(5)
print("If you input garbage or invalid options at sex, or input a race that wasn't a lion, wolf, fox, or dragon, events in the story might end up not working. So keep that in mind.")
time.sleep(4)
input("If you understand this and are happy with your name, race, and sex, hit enter to continue")
print("Excellent. This game follows typical interactive fiction rules, e.g you type north or n to go north.")
print(
    "In order to advance most dialogue in the game, you will have to press a key first. The console will print out a statement and then to get to the the next piece of dialogue you'll have to hit, say, enter.")
input("Like this. expect you won't have any text telling you too press a key to continue. Press a key to continue.")
print("With that out of the way, let's get started")
time.sleep(3)
intro()
