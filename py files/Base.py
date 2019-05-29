# Text game
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import secrets
import sys
from Travel_locations import Traveling

class PlayerStats:
    def __init__(self, race, sex, name):
        self.name = name
        self.sex = sex
        self.race = race


class PlayerCharacter(PlayerStats):  # Grabs and stores info about player
    def __init__(self):
        super().__init__(name=input("What is your name? "), sex=input("Do you wish to play as male or female? "),
                         race=input(
                             "Which race do you want to play as? Wolf, Lion, Fox or Dragon? (This is simply for role playing) "))


def startingroomlightswitch():
    lightswitch = ""
    while lightswitch != "north" and lightswitch != "east":
        lightswitch = input("Which way do you go? ")
        if lightswitch == "north":
            hallway()
        elif lightswitch == "east":
            player_bathroom.bathroompc()
    return lightswitch

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
                print("You return to the dim room, you see a doorway to your north and the bathroom to your east")
                return startingroomlightswitch()


def hallway():
    while True:
        if tories_cafe.cafefinished is True:
            print("After returning from the cafe you do work on one of your current contracts before going to bed")
        print("You enter a hallway with a doorway to your east and a staircase to your west")
        hallwaydirection = input("Which direction do you go? ").lower()
        if hallwaydirection in ["west", "w"]:
            entranceway()
            break
        elif hallwaydirection in ["east", "e"]:
            if sasha_encounter.sashatalked is False:  # Checks to see if player has talked to sasha before
                sasha_encounter.bedroom()
                break
            elif sasha_encounter.sashatalked is True:
                sasha_encounter.sashabedroom()
                break
        else:
            print("Invalid input")
            return hallway()


class SashaEncounter:
    def __init__(self):
        self.sashatalked = False

    def bedroom(self):
        while True:
            print(
                "You enter your roommates bedroom, it's your typical bedroom with nothing out of the ordinary expect for the Shepard sitting at the desk")
            print(
                "To your left you see a German Shepard sitting at a desk, to the south you see the doorway to the hallway")
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
            print(
                "The German Shepard is one of your roommates, Sasha. She's a trustworthy sort. But a bit absent-minded at times")
            input()
            print(
                """ "{}! Where have you been all this time! I haven't seen you in over a week! I figured you most have went on an unannounced vacation." """.format(
                    player_info.name))
            input()
            print(
                """ "I’ve kept on top of all your chores, you’re gonna owe me for the weeks’ time you decided to disappear. I was thinking you could take of my work for 2 or so weeks." """)
            input()
            self.sashatalked = True  # Indicates that the player has talked to Sasha allowing for more dialog
            self.sashabedroom()
        elif self.sashatalked == True:
            print(""" "You know, I actually had a friend in college once that disappeared for like 2 weeks" """)
            print(
                """ "Turns out she basically gave up and wasn't leaving her dorm. She was in a pretty bad place mentally, and ended up dropping all her classes and leaving college." """)
            input()
            print(
                """ "It was depressing watching my friend essentially fall apart. And by the time I knew something was up with her it was too late to intervene." """)
            input()
            print(
                """ "Makes me think of how I simply dismissed your disappearance as nothing to worry about. Who knows where you could have been or what you could have been up too!" """)
            input()
            print(
                """ "Anyway, you're fine now and that's all that matters. You might want to check in with Jacob, he was gone for half the week so he wasn't entirely sure how long you missing." """)
            print(""" "He should be somewhere downstairs." """)
            input()
            print("You exit Sasha's room and enter the hallway")
            hallway()
        elif self.sashatalked is True and sasha_living.sashalivingroomdialogue is True:
            print('"Hey, {}. Can\'t think of anything new going on"'.format(player_info.name))

    def sashabedroom(self):
        while True:
            print("You see Sasha, your roommate, and the doorway to the hallway to your south")
            direction = input("What do you wish to do? ")
            if direction in ["south", "s"]:
                hallway()
                break
            elif direction == "talk":
                self.sashabedroomdialog()
                break
            else:
                print("Invalid input")
                return self.sashabedroom


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
            if jacob_kitchen.jacobtalked is True and tories_cafe.cafefinished is True and sycamore_park.parklakepath is True and sasha_encounter.sashatalked is True:
                sasha_living.sashadialogue()
            else:
                print(
                    "You enter the living area and see nothing of note. Perhaps you should return here after visiting a couple places.")
                input()
            return entranceway()

        elif entrancewaydirection in ["south", "s"]:
            hallway()

        else:
            print("Invalid input")
            return entranceway()


class LivingRoom:
    def __init__(self):
        self.sashalivingroomdialogue = False

    def sashadialogue(self):
        if self.sashalivingroomdialogue is False:
            print("You return to the living room once again, Sasha is sitting on the couch watching something on the television. You can talk to her or return to the entrance way to your south.")
        elif self.sashalivingroomdialogue is True:
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
            '"Like the movie? It’s called Revengers: Titan Attack. One of the last movies in the Merkel universe. There’s one more that comes after this, but it isn’t out on disc yet"')
        input()
        print(
            '"Do you like superhero movies? I won’t say anym ore about it just In-case you want to watch it at some point."')
        input()
        print(
            "You state your preference for superhero movies, saying that you haven’t really kept up with the Revengers movies since the first one")
        input()
        print(
            '"Oh boy, you are in for a treat if you ever decide to catch up on them. Definitely let me know before you do, I’d love to re-watch all of them with you."')
        print('"Anyway, you want anything or just here to chat?"')
        input()
        print(
            "You tell Sasha that you wanted to talk to her about past friends. Your recent walk in the park weighing on your mind, you’re hoping that one of your best friends can give you some advice.")  # Maybe implement a choice later? Don't really have the story options to make this optional yet.
        input()
        print('"Well… I’m gonna be honest, that’s a pretty loaded question."')
        print('"First of all, what happened to these friends? Did they move away? Lose interest in the relationship?"')
        input()
        print(
            "You start to provide some background information to Sasha, explaining the friends’ role in your life, how they affected you, and then eventually how it all broke down ")
        print(
            "You can remember exactly how it started, it was mid-September during your teen years. Your parents told you that they couldn’t afford to stay at the lake anymore and that they would be packing up and leaving by the end of the month.")
        input()
        print(
            "This was a huge change. By the end of the month, you’d be moving away from the place of your childhood, the place where you spent almost all your summer days. The place where you met your best-friends.")
        input()
        print(
            "You were gone a week after that. You didn’t have time to mention it to most of your friends since they weren’t even there at the time. In an age without smartphones and social media, those friendships essentially ended that day")
        input()
        print(
            "As you tell Sasha about the move, you remember another ordeal before the move. It involved some of your best-friends Abbey and Jane. The move ended your friendships completely, yes, but you remember that you were on surprisingly shaking terms with both of them months before moving.")
        input()
        print(
            "You started to drift apart. Your interests were changing, and as you got older you found less and less common ground. To the point where Jane said that she ‘barely knew you’. It was actually a similar case with you, you didn’t know what they were really interested in anymore. It’s hard to stay friends with someone when you have no idea what to do with them. Regardless, hearing that took you down a notch. We’re you ignoring them and not even realizing it? Did they just not feel like you were friends anymore?")
        input()
        print(
            "You never got to ask them why they felt that way, so you can only assume. You feel it was a combination of both parties changing their ideas and interests, as well as Jane and Abbey hanging out with a different friend group. Both parties just slowly lost interest in each other.")
        print(
            "Looking back at it, you feel that the break down of the friendship was inevitable. Even if you hadn’t moved away, it's likely the friendship would have deteriorated further and further. The move simply accelerated things")
        input()
        print(
            "You connected with Abbey and Jane on social media 3 years after moving away, but of course it wasn’t the same. There just wasn’t anything to talk about. Both groups were almost completely different people from the ones 3-4 years ago. Any connections you might have had were gone.")
        input()
        print("You should have let go at that point, but 8 years in the future and you still cling to the past.")
        print(
            "You look to Sasha after rambling on, she seems surprised to hear this from you, considering you’d never mentioned anything about it before.")
        input()
        print(
            '"“That’s quite the story. Can’t say I would have expected something like this from you. You always seemed like the kind of person to live in the present."')
        print('"Then again perhaps I just suck at reading people."')
        input()
        print(
            '"I think most people have experienced something similar to you. A friendship breaking down for whatever reason"')
        input()
        print(
            '"I think the reason you still look back at that time with such regret is because of the way your relationship broke down. You watched your relationship with Abbey and Jane slowly drift away. With it being the fault of no one. You didn’t have anyone to deflect the blame to for this failing. And apparently, you didn’t even really get to discuss it with them, that lack of closure has no doubt helped lead to your current feelings"')
        input()
        print('"People change, and in the case of Abbey and Jane, there just wasn’t much you can do about it."')
        input()
        print(
            '"I’ve dealt with a somewhat similar situation before. I’m sure you remember me talking about one of my roommates in college dropping out because of depression, well that wasn’t the first time something like that happened."')
        input()
        print(
            '"One of my friends in high school was dealing with some serious shit. Depression, anxiety, and he never told anyone about it. He’d hid it from everyone else, there was no way to know what was going with him. He always cracked jokes, would hang out with you and do whatever, he seemed like one of the most carefree, happy guys I knew."')
        print(
            '"You probably know where this is going by now. He was dealing with serious clinical depression, didn’t want anyone to know because he didn’t want to burden them. He didn’t want people to feel sorry for him."')
        input()
        print(
            '"He ended up committing suicide by overdosing on Tylenol his junior year of high school. The last guy you would have expected to have that kind of stuff going on "')
        print('"It was extremely difficult dealing with that for the first few months, hell, the first year even."')
        input()
        print(
            '"It took me a long time to come to terms with it. And then after that, I still dealt with a mix of guilt and sadness. I felt like I should have picked up on him being depressed. I should have been able to help him in some way. I tried numerous things to try and get past it, stuff as simple as trying new hobbies or traveling, as well as going to therapy."')
        input()
        print(
            '"Ultimately, what helped me the most was focusing on the friends that were still there, and on forming new friendships. It helps keep your mind off the past, and it helps fill the void that was left. Instead of worrying about what happened in the past, you just try and focus on the now, and how you can make the most of it."')
        input()
        print(
            '"Of course, that’s not always easy to do. Stuff like this never is. And even if you succeed, it doesn’t completely erase the past. You’ll still have moments of weakness, you’ll still think about what could have been"')
        input()
        print(
            '"All you can do is try, and if that fails, ya know, you’ve gotta reach out to people. Family, friends, Somebody. Just letting your thoughts simmer isn’t going to help, it just puts you further down the hole."')
        input()
        print(
            '"One of my favorite bands actually has a quite a few songs dealing with this kind of topic. Off the top of my head, I think of their songs has a verse that goes kind like:"')
        time.sleep(2)
        print('"There\'s no magic bullet, no cure for pain"')
        print('"What\'s done is done, \'til you do it again"')
        input()
        print(
            '"Basically he’s saying there’s no easy way out of these kinds of situations, and odds are, it\'s not going to be the first time you’re going to deal with it"')
        input()
        print(
            'You find yourself resonating with Sasha’s advice and past experiences, though you feel like you’re left with more questions for yourself then before having this conversation. You’re sure if that’s a good thing or a bad thing.')
        input()
        print('You ask Sasha if she still thinks about those memories very often.')
        input()
        print(
            '"Yes, I still look back at those memories on occasion. Though I’ve found myself looking at the positives of those times rather the negatives. I’m at a point in my life where I feel I’ve moved on from that. I’m happy with how everything has worked out at this point, and that’s in no small part to my friends\' group and support group."')
        input()
        print('You thank Sasha for entertaining your thoughts and helping you out, it helped clear your mind a bit.')
        input()
        print(
            '"Of course! That’s what friends are for. I’ll see you around; oh, and make sure you tell me if you want to catch up on the Revenger’s movies! I’ll be pissed if you don’t!"')
        input()
        print('You say goodbye to Sasha and head up to the room for the night, your mind full of thoughts to process')
        input()
        self.sashalivingroomdialogue = True
        hallway()


class JacobKitchen:
    def __init__(self):
        self.jacobtalked = False

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
                        '"Hey {}! Where have you been these last few days? I haven’t seen you since I left for vacation last week. I got back about 3 days ago and haven’t seen you since."'.format(
                        player_info.name))
                    input()
                    print(
                        "Sasha told me she hadn’t seen you for a minute, but she wasn't exactly sure how long you'd been gone.")
                    input()
                    print(
                        '"Regardless, it’s good to see you. If you ever wanna talk about where you went off too, you know where to find me."')  # Feels kind of unnatural?
                    input()
                    self.jacobtalked = True  # Marks that the player has talked to Jacob
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


class FirstWorld:
    def fronthousearea(self):
        while True:
            print("You stand on your front porch ready for adventure! You could also return home by entering the door to your south.")
            fronthouseareadirection = input("Will you travel or return home?").lower()
            if fronthouseareadirection in ['travel']:
                travel_system.traveltofront()
                break
            if fronthouseareadirection in ['south', 's']:
                entranceway()
                break
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
        print("They’re famous for their fantastic wraps, and also have some pretty good soups.")
        print(
            "Looking around you see the line to order, it’s a bit after lunch so there isn’t much of a wait. You also see a familiar face sitting down at one of the tables")
        cafedecision = input("Will you order first or go and say hi to the familiar face? ").lower()
        if cafedecision in ['order', 'eat', ]:
            print("You decide to order some food before going to say hi.")
            print("The line moves quick and before you know it’s your turn to order.")
            input()
            print(
                "You decide to order your usual combo; a tuna wrap with a bag of chips and a drink. Not a bad deal for $4!")
            print("Having ordered your food, you head over to the table of Holly, a friend of yours from high school.")
            print(
                "Holly is a vixen, no, not like that. In the literal sense. You’ve known her since high school and while you haven’t really been in contact much since then, you still consider her to be a friend, albeit a distant one.")
            input()
            print(
                "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that's no replacement for a proper conversation.")
            print(
                '"Hey {}, Its been a while hasn\'t it? Last time I saw you was a few years ago when we to King\'s Point with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!"'.format(
                    player_info.name))  # Yes, I really did just combine the names of Cedar Point and King's Island to make King's Point
            input()
            print(
                "You fill in some details about what you’ve been up too since that trip. Detailing your current living situation with Sasha and Jacob and what you've been up too.")
            print(
                "You ask what Holly’s been up too since then, a faint look of discomfort fills her face as she describes her falling out from college")
            input()
            print(
                '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because I sucked at it, I just wasn’t enjoying it. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life"')
            print(
                '"Like I said, my grades weren’t bad enough too have them kick me out, but they weren’t great either. I was holding about a 2.5 (out of 4) GPA"')
            input()
            print(
                "You nod in agreement, remembering how many times you second guessed your major choice throughout college")
            input()
            print(
                '"And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
            input()
            print(
                "You can definitely see yourself agreeing with Holly’s decision, thinking back to all the workplace drama and rejected proposals you’ve dealt with…")
            print(
                "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer.")
            input()
            print(
                '"I draw art for a living now! I’ve always been interested in drawing; I’m sure you remember some of my art from back in high school. I never really thought of it as a legitimate career path but I’ve managed to find a niche that pays a decent amount of money through commissions."')
            print(
                '"I love it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
            input()
            print(
                '"So, what have you been doing since graduating college? I know you finished college with a couple internships under your belt and a great GPA, so that’s had to have gotten you somewhere right?"')
            input()
            print(
                "You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons that Holly has already stated, like project managers ignoring ideas.")
            print(
                "You state that you had luckily saved up enough money to live comfortably for around 2 years before you quit. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
            input()
            print(
                "'Man, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine having a savings large enough to live off of for 2 years. Let alone being able to amass that much money by only working for a year and half!'")
            print(
                "'Still, like I said, I enjoy my work and I wouldn’t want it any other way. Within reason of course.'")
            input()
            print(
                '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around."'.format(
                    player_info.name))
            print("You say goodbye to Holly and decide to head home for the day")
            input()
            self.cafefinished = True
            hallway()
        elif cafedecision in ['talk', 't', 'face' 'hi']:
            print("You decide to first go over and say hi to Holly.")
            print(
                "Holly is a vixen, no, not like that. In the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
            input()
            print(
                "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for proper conversation.")
            print(
                '"Hey {}! Last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!"'.format(
                    player_info.name))
            input()
            print(
                "You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics")
            print(
                "You ask what Holly’s been up too since then, a faint look of worry and disappointment fills her face as she describes her falling out from college")
            input()
            print(
                '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying college. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life"')
            print(
                '"Like I said, my grades weren’t bad enough too have them kick me out, but they weren’t great either. I was holding about a 2.5 (out of 4) GPA"')
            input()
            print(
                "You nod in agreement, remembering how many times you second guessed your major choice throughout college")
            input()
            print(
                '"And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
            input()
            print(
                "You can definitely see yourself understanding Holly’s decision, thinking back at all the workplace drama and rejected proposals you’ve dealt with…")
            print(
                "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer")
            input()
            print(
                '"I draw art for a living now! I’ve always been interested in drawing before, I’m sure you remember some of my drawings from back in high school. I never really thought of it as a legitimate career path, but I’ve managed to find a niche that pays a decent amount of money through commissions."')
            print(
                '"I love it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
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
                '"Man, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine being able to have a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and half!"')
            print('"Still, like I said, I enjoy my work and I wouldn’t want it any other way."')
            input()
            print(
                '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around."'.format(
                    player_info.name))
            print("You say goodbye to Holly and decide to head home for the day")
            input()
            self.cafefinished = True
            hallway()
        else:
            print("Invalid input")
            return self.thecafe()


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
            print("You decide you still aren’t feeling up to a walk in the park and head home")
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
        input()
        self.parkroommatepath = True
        self.lakepark()

    def parkpathself(self):
        print("15 minutes into the walk you come across a familiar sight, the great Sycamore Lake. Hence the park’s name.")
        print(
            "You’ve seen this lake at least a thousand times throughout your life. In both good and bad times. You normally never give a second thought when looking out upon its seemingly never-ending horizon, but this time was different.")
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
            "As you look back at those memories it feels bittersweet. It’s like the saying ‘Don’t be sad that it’s over, be glad that it happened’ Though that can be hard to live with some days.")
        print("The memories are nice but still having those people in your life would be better.")
        print(
            "Unfortunately, people drift apart, they change. You grow up, your interests change, you move away from those people… Sometimes you can get over it, but when someone has that much of an impact on your life, it’s tough. Even 7 years after its happened.")
        input()
        print(
            "As you reminisce on your memories you realize that over an hour has passed, you snap out of it and finish your walk prematurely before heading back to the park entrance way.")
        input()
        self.parklakepath = True
        self.lakepark()


# Global Classes

sasha_encounter = SashaEncounter()  # Global instance of class SashaEncounter,very useful.

jacob_kitchen = JacobKitchen()  # Global instance of JacobKitchen

player_info = PlayerCharacter()  # Provides info for the player character

first_world = FirstWorld()

sycamore_park = SycamorePark()

tories_cafe = ToriesCafe()

sasha_living = LivingRoom()

player_bathroom = PCBathroom()  # Make sure to include the () when adding classes)

travel_system = Traveling
# Starts the game

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
print("With that out of the way, let's get started", flush=True)
time.sleep(5)
print("You are in a dimly-lit room, you see a doorway to your north and to your east")
time.sleep(3)
startingroomlightswitch()

