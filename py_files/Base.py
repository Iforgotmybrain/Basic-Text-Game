# Tales from the Road
# -*- coding: utf-8 -*-

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


def bank_money():
    print("You fire up your smartphone and check your bank balance")
    print("Your current balance is ${}".format(CharInfo.player_info.money))
    return pcbedroom()


def intro():
    print("As you finish the 5th and final season of Barking Bad you feel a sense of satisfaction, but also a feeling of sadness. The culmination of 5 years work is over in the span of an hour.")
    input()
    print("While you’re satisfied with the ending of the show, you can’t help but feel disappointed that there won’t be any more episodes to look forward too. You find that it’s a common feeling when it comes to finishing excellent media.")
    print("It has been a familiar feeling as of recent, as you’ve binge watched 3 different shows this past week while staying at Teuton Resorts. The vacation has given yourself a break from your obligations, and from your housemates.")
    input()
    print("Unfortunately, this is your last day here, as your reservation is up tomorrow. It feels like your long-awaited vacation is over almost as soon as it began.")
    input()
    print("You spent the rest of the day packing and cleaning the room. The next day you grab breakfast and head off for home.")
    input()
    print("You eventually arrive at home in the evening, with none of your housemates to be seen. You bring your stuff inside and unpack it before getting something to eat. Afterwards you watch a short movie in your room and go to bed. Another day in paradise.")
    input()
    pcbedroom()


def pcbedroom():
    if CharInfo.misc_checks.bathroom_bd is not True:
        print(
            "You wake up the next morning, your bedroom is dimly lit with the only source of light being the sun as it sneaks through the blinds.")
    elif CharInfo.sasha_checks.sasha_living is True and CharInfo.jacob_checks.jacob_bedroom is not True:  # Makes it so the dialogue doesn't repeat
        print("You wake up the next day feeling better. Your conversation with Sasha helped ease your mind, and made you realize just how great of friends you have now.")
        print("You think about possibly asking Jacob about some of his past trips. He should be in his bedroom.")
        input()

    elif CharInfo.festival_checks.festival_ending is True and CharInfo.chris_checks.chris_computer_list is not True: # Same thing.
        print("You wake up the next morning still a bit surprised by the events of last night.")
        input()
        print("You think that now would be a good time to plan out the road trip, maybe try and figure out who you’d want to bring along, where you’d want to go, stuff like that.")
        input()
        print("You can think of a couple of things you could do; you might try asking your roommates for suggestions on where to go, and ask them rather they’d want to go on the road trip with you.")
        input()
        print("You could also check out Chris the Tiger’s Pawbook account and see what he suggests checking out. You could do that on your computer in the bedroom.")
        input()

        if CharInfo.festival_checks.holly_stay is True:  # Only brings up this dialogue is the player stuck around with Holly.
            print("Maybe not strictly related to the road trip, but you could look into maybe going on another date with Holly as well. You might try and Call Holly to see if she’d be up for that.")
            input()
        print("It’s quite a nice day out as well, you might go on a walk just for the hell of it.")
        input()
    print("You are standing in your bedroom. You see the door to the bathroom to your east, and the doorway to the hallway directly ahead to the north.")

    if CharInfo.festival_checks.festival_ending is True:  # Makes it so the player cannot access the phone or computer before they complete the festival. Which is when they become functional.
        print("There is also your computer to the south of the room.")
        if CharInfo.jacob_checks.jacob_post_fest is True and CharInfo.sasha_checks.sasha_post_fest is True:
            print("You could also use your Phone to check up on Holly.")

    print("You could also check your bank balance.")
    pcbedroomdirection = input('Which do you do? ').lower()
    CharInfo.player_info.player_location = pcbedroom
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

    elif pcbedroomdirection in ['phone', 'smartphone', 'cellphone', 'call', 'text', 'cell']:
        Phone.smart_phone_placement.phone_placeing()

    else:
        print("Invalid input")
        return pcbedroom()


def pccomputer():
    if CharInfo.chris_checks.chris_computer_list is not True:
        print("You turn on the computer and log in, opening Firefox and hitting up Pawbook.")
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
        print('"I\'m guessing you’ll be starting off where you are now, in Idenberg."')
        print(
            '"I’ll have to look up some routes you might go and get back to you on points of interest. Shouldn’t take me to long, I’ll probably have you a nice list by the end of the day."')
        input()
        print(
            "You reply to Chris and thank him for helping you out, you tell him that you’ll be awaiting his list.")
        CharInfo.chris_checks.chris_computer_list = True
        SaveSystem.save_sys.saving()
        pcbedroom()

    elif CharInfo.chris_checks.chris_computer_list is True and CharInfo.chris_checks.chris_computer_list_completed is not True:
        print("You check your Pawbook messages and don’t see anything from Chris. He’s probably still working on it")
        pcbedroom()




class PCBathroom:
    def bathroompc(self):
        while True:
            if CharInfo.misc_checks.bathroom_bd is True:
                print("You see the opened trunk on the floor and the doorway you entered to your west")

            elif CharInfo.misc_checks.bathroom_bd is not True:
                print("You enter a bathroom, you see a trunk on the floor and the doorway you entered to your west")

            bathroomoption = input("What do you do? ").lower()

            if bathroomoption in ["trunk", "chest"] and CharInfo.misc_checks.bathroom_bd is not True:  # Prevents user from opening trunk more than once
                print("You open the trunk and find a mysterious sculpture")  # Might make this a trigger in the future
                CharInfo.misc_checks.bathroom_bd = True
                input()
                return self.bathroompc()

            elif bathroomoption in ['trunk', 'chest'] and CharInfo.misc_checks.bathroom_bd is True:
                print("There's nothing more in the trunk.")
                input()

            elif bathroomoption in ["west", "w", "West"]:
                print("You return to your bedroom.")
                return pcbedroom()


def hallway():
    while True:
        print("You enter a hallway. You can enter your bedroom to the south. There's also a doorway to your west, a staircase to your east, and another doorway to the north.")
        hallwaydirection = input("Which direction do you go? ").lower()
        if hallwaydirection in ["west", "w"]:

            if CharInfo.sasha_checks.sasha_talk is not True:  # Checks to see if player has talked to sasha before
                sasha_encounter.bedroom()
                break

            elif CharInfo.sasha_checks.sasha_talk is True and CharInfo.festival_checks.festival_ending is not True:
                sasha_encounter.sashabedroom()
                break

            elif CharInfo.festival_checks.festival_ending is True:
                sasha_encounter.sasha_post_fest_dialogue()
                break

        elif hallwaydirection in ["east", "e"]:
            entranceway()
            break

        elif hallwaydirection in ['save']:
            SaveSystem.save_sys.saving()

        elif hallwaydirection in ['north', 'n']:
            if CharInfo.sasha_checks.sasha_living is not True:
                print("The door is locked. Maybe you should come back later.")
                input()
                return hallway()

            elif CharInfo.sasha_checks.sasha_living is True:
                jacob_kitchen.bedroomdialogue()

        elif hallwaydirection in ['south', 's']:
            pcbedroom()

        elif hallwaydirection in ['phone', 'smartphone', 'cellphone', 'call', 'text', 'cell']:
            Phone.smart_phone_placement.phone_placeing()

        else:
            print("Invalid input")
            return hallway()

class SashaEncounter:

    def bedroom(self):
        while True:
            print(
                "You enter your roommates bedroom, it's your typical bedroom with nothing out of the ordinary expect for the Shepard sitting at the desk")
            print(
                "To your left you see a German Shepard sitting at a desk, to the south you see the doorway to the hallway")
            bedroomoption = input("What do you do? ").lower()

            if bedroomoption in ["talk", "t", 'left', 'l', 'german shepard', 'shepard'] and CharInfo.festival_checks.festival_ending is not True:
                self.sashabedroomdialog()

            elif bedroomoption in ["south", "s"]:
                hallway()
            else:
                print("Invalid input")
                return self.bedroom()

    def sashabedroomdialog(self):
        if CharInfo.sasha_checks.sasha_talk is not True:
            print("You approach the German Shepard and exchange greetings.")
            print(
                "The German Shepard is one of your roommates, Sasha. She's a trustworthy sort, but can be a bit absent-minded at times")
            input()
            print(
                """ "{}! Where have you been all this time! I haven't seen you in over a week! You weren't in your room so I was thinking you most have went on an unannounced vacation." """.format(
                    CharInfo.player_info.name))
            input()
            print('You explain to Sasha that you did indeed go on a week-long vacation up north, about 5 hours away.')
            input()
            print('"Hah, I was right for once!"')
            print(
                '"Hey, you know, I’ve kept on top of all your chores while you were gone. You’re gonna owe me for the weeks’ time you decided to disappear. I was thinking you could take of my work for 2 or so weeks."')
            input()
            print("You nod in agreement with Sasha, it only seems fair considering you didn’t give either of your roommates a heads up before leaving.")
            input()
            print("You say goodbye to Sasha and head back to the hallway.")
            input()
            CharInfo.sasha_checks.sasha_talk = True
            CharInfo.player_info.player_location = hallway # Indicates that the player has talked to Sasha allowing for more dialog
            hallway()
        elif CharInfo.sasha_checks.sasha_talk is True:
            print(""" "You know, I actually had a friend once that basically disappeared for 2 weeks." """)
            input()
            print(
                """ "Turns out she was hiding out in her apartment. She didn't leave it for 2 weeks and only answered text messages to tell people she was ‘ok’" """)
            input()
            print(
                """ "It was quite sad hearing about that for the first time, my friend was basically tearing herself apart, and by the time I knew something was up it was too late to intervene." """)
            print(""" "She did end up getting help thankfully, and last time I heard from her she was doing pretty good." """)
            input()
            print(
                """ "It makes me think of how I simply dismissed your disappearance as nothing to worry about. Who knows where you could have been or what you could have been up too!" """)
            input()
            print(
                """ "Anyway, you're fine now and that's all that matters. You might want to check in with Jacob, he was gone for half the week so he wasn't entirely sure how long you were gone for." """)
            input()
            print("You exit Sasha's room and enter the hallway")
            CharInfo.player_info.player_location = hallway
            hallway()
        elif CharInfo.sasha_checks.sasha_talk is True and CharInfo.sasha_checks.sasha_living is True:
            print('"Hey, {}. Can\'t think of anything new going on"'.format(CharInfo.player_info.name))

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
        print("“So what brings you to me today? More confiding? Wanna talk about someone?”")
        input()
        print("You tell Sasha, that, despite her snarky remarks, you were actually here to talk about something else for once.")
        input()
        print("“Alright, I was just messing with you. Just seems like you always come to me when you need to talk about something, which is fine, just wanted to poke some fun at it.”")
        input()
        print("You mention to Sasha that the main reason you came here was to discuss destinations for the road trip.")
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
        print("You decide to ask Sasha how she would feel about going on the road trip with you, telling her that it likely be a month trip, and that you’d be taking a total of 3 people.")
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
            CharInfo.sasha_checks.sasha_post_fest = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()

        elif CharInfo.jacob_checks.jacob_post_fest is not True:
            print("You exit Sasha’s room. You should probably go talk to Jacob about the road trip.")
            input()
            CharInfo.sasha_checks.sasha_post_fest = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()

        elif CharInfo.jacob_checks.jacob_post_fest is True and CharInfo.festival_checks.holly_stay is not True:
            print("You exit Holly’s room. Chris probably has his list posted on Pawbook by now.")
            CharInfo.sasha_checks.sasha_post_fest = True
            CharInfo.player_info.player_location = hallway
            SaveSystem.save_sys.saving()
            hallway()





def entranceway():
    CharInfo.player_info.player_location = entranceway
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
    def sashadialogue(self):
        CharInfo.sasha_checks.sasha_living = False
        if CharInfo.sasha_checks.sasha_living is False:
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
            '"Like the movie? It’s called Revengers: Titan Attack. One of the last movies in the Lightning Maus Movie Universe. There’s one more that comes after this, but it isn’t out on disc yet"')
        input()
        print(
            '"Actually, do you even like superhero movies? I won’t say anymore about it just In-case you want to watch it at some point."')
        input()
        print(
            "You state your preference for superhero movies, saying that you haven’t really kept up with the Revengers movies since the first one")
        input()
        print(
            '"Oh boy, you are in for a treat if you ever decide to catch up on them. Definitely let me know before you do, I’d love to re-watch all of them with you."')
        print('"Anyway, you want anything or just here to chat?"')
        input()
        sashatalkorconfess = input("(1): Tell Sasha you wanted to talk about your walk in the park. (2:) Just keep chatting.")

        if sashatalkorconfess in ['1']:
            print(
                "You tell Sasha that you wanted to talk about your recent walk in the park.")  # Maybe implement a choice later? Don't really have the story options to make this optional yet.
            input()                                                                            # Surprisingly I did actually implement a choice later.
            print('"A walk in the park, huh? What about it did you want to talk about?"')
            input()
            print(
                "You take some time to explain what exactly is on your mind. That you're bothered by how you left your friends.")
            input()
            print(
                '"So, what happened to these friends? Did they move away? Lose interest in the relationship? Give me some more info."')
            input()
            print(
                "You start to provide some background information to Sasha, explaining the friends’ role in your life, how they affected you, and then eventually how it all broke down ")
            print(
                "You can remember exactly how it started, it was mid-September during your teen years. Your parents had just told you that they couldn’t afford to stay at the lake anymore and that they would be packing up and leaving by the end of the month.")
            input()
            print(
                "This was a huge change. By the end of the month, you’d be moving away from the place of your childhood, the place where you spent almost all your summer days. The place where you met your best-friends.")
            input()
            print(
                "You were gone a week after that. You didn’t have time to mention it to most of your friends since they weren’t even there at the time. In an age without smartphones and social media, those friendships essentially ended that day")
            input()
            print(
                "As you tell Sasha about the move, you remember another ordeal before the move. It involved some of your best-friends, Abbey and Jane. The move ended your friendships completely, yes, but you remember that you were on surprisingly shaky terms with both of them months before moving.")
            input()
            print(
                "You started to drift apart. Your interests were changing, and as you got older you has less and less common ground. To the point where Jane said that she ‘barely knew you’. It was actually a similar case with you, you didn’t know what they were interested in anymore. It’s hard to stay friends with someone when you have no idea what they want to talk about. Regardless, hearing that took you down a notch. Were you ignoring them and not even realizing it? Did they just not feel like you were friends anymore?")
            input()
            print(
                "You never got to ask them why they felt that way, so you can only assume. You feel it was a combination of both parties changing their ideas and interests, as well as Jane and Abbey hanging out with a different friend group. Both parties just slowly lost interest in each other.")
            print(
                "Looking back at it, you feel that the break down of the friendship was inevitable. Even if you hadn’t moved away, it's likely the friendship would have deteriorated further and further. The move simply accelerated things")
            input()
            print(
                "You connected with Abbey and Jane on social media 3 years after moving away, but of course it wasn’t the same. There just wasn’t anything to talk about. Both groups were almost completely different people from the ones 3-4 years ago. Any connections you might have had were gone.")
            input()
            print("You should have let go at that point, but 7 years in the future and you still cling to the past.")
            print(
                "You look to Sasha after rambling on, she seems surprised to hear this from you, considering you’d never mentioned anything about it before.")
            input()
            print(
                '"That’s quite the story. Can’t say I would have expected something like this from you. You always seemed like the kind of person to live in the present."')
            print('"Then again perhaps I just suck at reading people."')
            input()
            print(
                '"I think most of us have experienced something similar to you. A friendship breaking down for whatever reason"')
            input()
            print(
                '"I think the reason you still look back at that time with such regret is because of the way your relationship broke down. You watched your relationship with Abbey and Jane slowly drift away. With it being the fault of no one. Apparently, you didn’t even really get to discuss it with them, that lack of closure has no doubt helped lead to your current feelings"')
            input()
            print('"People change, and in the case of Abbey and Jane, there just isn\'t much you can do about it."')
            input()
            print(
                '"I’ve dealt with a kind of similar situation before. I’m sure you remember me talking about one of my roommates in college dropping out because of depression, well that wasn’t the first time something like that happened."')
            input()
            print(
                '"One of my friends in high school was dealing with some serious shit. Depression, anxiety, and he never told anyone about it. He’d hid it from everyone else, there was no way to know what was going with him. He always cracked jokes, would hang out with you and do whatever, he seemed like one of the most carefree, happy guys I knew."')
            print(
                '"You probably know where this is going by now. He was dealing with serious clinical depression, didn’t want anyone to know because he didn’t want to burden them. He didn’t want people to feel sorry for him."')
            input()
            print(
                '"He ended up committing suicide by overdosing during his junior year of high school. The last guy you would have expected to have that kind of stuff going on "')
            print(
                '"It was extremely difficult dealing with that for the first few months, hell, the first year even. Everybody at the school had trouble dealing with it."')
            input()
            print(
                '"It took me a long time to come to terms with it. And then after that, I still dealt with a mix of guilt and sadness. I felt like I should have picked up on him being depressed. I should have been able to help him in some way. I tried numerous things to try and get past it, stuff as simple as trying new hobbies or traveling, and even went to therapy."')
            input()
            print(
                '"Ultimately, what helped me the most was focusing on the friends that were still there, and on forming new friendships. It helps keep your mind off the past, and helps fill the void that was left. Instead of worrying about what happened in the past, you just try and focus on the now, and how you can make the most of it."')
            input()
            print(
                '"Of course, that’s not always easy to do. Stuff like this never is. And even if you succeed, it doesn’t completely erase the past. You’ll still have moments of weakness, you’ll still think about what could have been"')
            input()
            print(
                '"All you can do is try, and if that fails, ya know, you’ve gotta reach out to people. Family, friends, somebody. Just letting your thoughts simmer isn’t going to help, it just puts you further down the rabbit hole."')
            print(
                '"There’s no easy way out of these kinds of situations, and odds are, it\'s not going to be the first time you’re going to deal with it"')
            input()
            print(
                'You find yourself resonating with Sasha’s advice and past experiences, though you feel like you’re left with more questions for yourself then before having this conversation. You’re not sure if that’s a good thing or a bad thing.')
            input()
            print('You ask Sasha if she still thinks about those memories very often.')
            input()
            print(
                '"Yes, I still look back at those memories on occasion. Though I’ve found myself looking at the positives of those times rather the negatives. I’m at a point in my life where I feel I’ve moved on from that. I’m happy with how everything has worked out at this point, and that’s in no small part to my friends\' group and support group."')
            input()
            print(
                'You thank Sasha for entertaining your thoughts and helping you out, it helped clear your mind a bit.')
            input()
            print(
                '"Of course! That’s what friends are for. I’ll see you around; oh, and make sure you tell me if you want to catch up on the Revenger’s movies! I’ll be pissed if you don’t!"')
            input()
            print(
                'You say goodbye to Sasha and head up to the room for the night, your mind full of thoughts to process')
            input()
            CharInfo.player_info.player_location = pcbedroom
            CharInfo.sasha_checks.sasha_living = True
            CharInfo.player_info.ending_points += 2
            SaveSystem.save_sys.saving()
            pcbedroom()

        elif sashatalkorconfess in ['2']:
            print("Placeholder")
            return


class JacobDialogue:
    def startingkitchen(self):
        while True:
            print(
                "You enter the kitchen, there's various kitchen appliances and a table and chairs over to the right. You see a Deer to your left and the entrance way to the east. ")
            kitchendirection = input("What do you do? ").lower()
            if kitchendirection in ["talk", "t"]:
                if CharInfo.jacob_checks.jacob_kitchen is not True:  # Dialogue if Jacob hasn't been talked to before
                    print(
                        "The Deer is one of your roommates, Jacob. You give him a pat on the shoulder and strike up a conversation")
                    print(
                        '"Hey {}! What’s up? Where have you been these last few days? I haven’t seen you since I went to visit my parents last week. I got back about 3 days ago and haven’t seen you since."'.format(CharInfo.player_info.name))
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
                    CharInfo.jacob_checks.jacob_kitchen = True  # Marks that the player has talked to Jacob
                    CharInfo.player_info.player_location = jacob_kitchen.startingkitchen
                    return self.startingkitchen()
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
        print("As you enter Jacob's room you see how nicely decorated it is. You see the various landscape paintings on his walls and the house plants he has. It all meshes together great and creates a soothing atmosphere.")
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
        print('You can find yourself agreeing with Jacob, staying in a car for most of the day doesn’t exactly seem like the greatest time.')
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
        CharInfo.player_info.money += 200
        print("Your bank balance is now {}".format(CharInfo.player_info.money))
        input()
        print("New travel area unlocked.")
        CharInfo.jacob_checks.jacob_bedroom = True
        TravelSystem.tp.append('Lake Fest')
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
            if CharInfo.festival_checks.painting_purchase is True:
                print(
                    '"A piece of artwork, huh? Never had you figured as that type, probably because I’ve never seen you hang so much as a picture on your walls."')
                input()
            elif CharInfo.festival_checks.wooden_sculpture is True:
                print(
                    '"Wood sculptures are pretty cool, I tried taking wood carving up as hobby but didn’t have much luck with it. Just didn’t have the ‘artistic vision’ I suppose."')
                input()
            elif CharInfo.festival_checks.trash_vendor is True:
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
                '"Man, there’s a handful of places I can think of. There’s an awesome museum in Jonstown, which is along I-23 heading west. Should be right on the route you’d take."')
            input()
            print(
                '"There’s also a beautiful state park in Loba, which is in the next state over. Place is called Occidentale State Park, they’ve got camping sites near by if you’re up for that as well. I went there about 3 years ago for spring break with an ex."')
            input()
            print(
                '"Another place to check out is the Ragniti pop factory, it’s on Interstate 65 in Loba, which you’ll probably be taking in order to take on I-23. They give tours everyday, might be a nice little thing to check so you can give yourself a break from driving."')
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
            print("Although, this might limit who you can take on the road trip. As you’re thinking of taking no more then 3 people. Anymore and it would get a bit crowded in the car.")
            input()
            print("Still, it might not hurt to ask him anyway. It would give you a good idea on if he would be willing to go.")
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
                '"A bit short notice too put in vacation time for work, I’ll have to discuss it with Joe and see if we can work something out. Probably be a about 3 or so weeks, yeah?"')
            input()
            print("You tell Jacob that you were planning on the road trip being no more than 4 weeks.")
            input()
            print(
                '"Alright, I’ll check it out with my work and get back to you then, if I get the time off I’ll let you know and we can work it out."')
            input()

            if CharInfo.sasha_checks.sasha_post_fest is not True:
                print("You tell Jacob you’re looking forward too it. Now to see what Sasha has to say.")
                input()
                CharInfo.jacob_checks.jacob_post_fest = True
                SaveSystem.save_sys.saving()
                entranceway()

            elif CharInfo.sasha_checks.sasha_post_fest is True and CharInfo.festival_checks.holly_stay is True:
                print("You tell Jacob you’re looking forward to it. Maybe now you should see what Holly's up to using your phone in the bedroom.")  # (This is placeholder. I want to make it so the player can use the phone at all locations)
                input()
                CharInfo.jacob_checks.jacob_post_fest = True
                SaveSystem.save_sys.saving()
                entranceway()

            elif CharInfo.sasha_checks.sasha_post_fest is True and CharInfo.festival_checks.holly_stay is not True:
                print(
                    "You tell Jacob you’re looking forward to it. By now Chris should have gotten his list together, you should probably check the computer and see what he said.")
                input()
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
            fronthouseareadirection = input("Will you travel or return home?").lower()
            if fronthouseareadirection in ['travel', 't', 'go', 'adventure']:
                TravelSystem.travel_function.traveltofront()
            elif fronthouseareadirection in ['south', 's', 'home', 'door']:
                entranceway()
            else:
                print("Invalid input or area in progress")
                return self.fronthousearea()


class ToriesCafe:
    def thecafe(self):
        print("You catch a ride on the bus and end up at Tories Place, your all-time favorite place to grab lunch")
        print(
            "It’s a popular place amongst the younger crowd. The place has a modern aesthetic with colorful furniture and ample natural lighting giving the place a cheery vibe.")
        input()
        print("They’re known for their fantastic wraps, and also have some pretty good soups.")
        print(
            "Looking around you see the line to order, it’s a bit after lunch so there isn’t much of a wait. You can also see a familiar face sitting down at one of the tables")
        input()
        cafedecision = input("(1): Order food and then go over say hi to Holly.(2): Go over and say hi to Holly right away. (3): Just order some food and go home.").lower()

        if cafedecision in ['1', '3']:
            print("You decide to order some food real quick before going to say hi.")
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
                print("She's sitting all alone and doesn't seem to be particularly engaged in anything.")
                print("It would have been interesting to hear what she's been up to since you last met.")
                input()
                print("Oh well, you might end up meeting her some other time. You were never that close to her anyway.")
                input()
                print("You finish up your meal and throw your trash away before hopping on the bus to go back home for the day.")
                input()
                CharInfo.misc_checks.cafe_finished = True
                CharInfo.player_info.player_location = entranceway
                CharInfo.player_info.ending_points -= 1
                SaveSystem.save_sys.saving()
                entranceway()

            print("Having ordered your food, you head over to the table of Holly, a friend of yours from high school.")
            self.hollydialoguecafe()

        elif cafedecision in ['3']:
            print("You decide to first go over and say hi to Holly.")
            input()
            self.hollydialoguecafe()

        else:
            print("Invalid input")
            return self.thecafe()


    def hollydialoguecafe(self):
        print(
            "Holly is a vixen. No, not like that, in the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
        input()
        print(
            "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for a proper conversation.")
        print(
            '"Hey {}! It\'s been awhile. I think the last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends.'.format(
                CharInfo.player_info.name))
        print('"And the last time I saw you regularly was back before you went off to college in 2014!"')
        input()
        print(
            "You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics")
        print(
            "You ask what Holly’s been up too since then, a faint look of discomfort fills her face as she describes her falling out from college")
        input()
        print(
            '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying college. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there."')
        print('"I couldn\'t see myself working as a marketer for the rest of my life either."')
        input()
        print(
            "You nod in agreement, remembering how many times you second guessed your choice to attend college.")
        input()
        print(
            '"More on the marketer thing, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
        input()
        print(
            '"That’s just me though. You know I\'ve never been one to suck up and deal with other people’s bullshit"')
        input()
        print(
            "You can definitely see yourself understanding Holly’s decision, thinking back to all the workplace drama and rejected proposals you’ve dealt with…")
        print(
            "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer.")
        input()
        print(
            '"I draw art for a living now! I was always interested in art, I’m sure you remember some of my drawings from back in high school."')
        print('"I never really thought of it as a legitimate career path, but I’ve managed to find a niche that pays a decent amount of money through commissions."')
        input()
        print(
            '"And you know, I really enjoy it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
        input()
        print(
            '"So, what have you been doing since graduating college? I know you finished with a couple internships and a great GPA, so that’s had to have gotten you somewhere right?"')
        input()
        print(
            "You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons she stated, like project managers ignoring ideas.")
        print(
            "You state that you had luckily saved up enough money to live comfortably for around 2 years before quitting. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
        input()
        print(
            '"Wow, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine having a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and a half!"')
        print('"Still, like I said, I enjoy my work and I wouldn’t want it any other way."')
        input()
        print(
            '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Maybe I’ll see you around some other time."'.format(
                CharInfo.player_info.name))
        print("You say goodbye to Holly and decide to head home for the day.")
        input()
        CharInfo.player_info.ending_points += 1
        CharInfo.player_info.player_location = hallway
        CharInfo.misc_checks.cafe_finished = True
        SaveSystem.save_sys.saving()
        hallway()


class SycamorePark:
    def lakepark(self):
        if CharInfo.park_checks.park_roommate_path is not True and CharInfo.park_checks.park_lake_path is not True:
            print(
                "You arrive at Sycamore Lakeview Park after a short walk down the street. You’ve never really been too this park despite being close to home.")
            print(
                "That's mainly because you've never really felt like going to the park. You were always preoccupied by something else, just not up to going out, or sacred by the various insects that call this place home. ")
            input()
            print(
                "Well, you’re here now and ready to make the most it. As you enter the park you see two separate walking paths you could take. One to the west, the other to the east. Or you could just say 'forget this' and head back home.")
        else:
            print(
                "You arrive at the park entrance, you see the two walking paths to your east and to your west. You could also head home.")
        pathdialog = [self.parkpathrommates,  # Used to randomize the path choice
                      self.parkpathself]  # In order to sort functions you can't call the function in this list.

        parkdecision = input("After thinking about it, you decide to go... ").lower()
        if parkdecision in ['home', 'away', ]:
            print("You decide to head home")
            first_world.fronthousearea()

        elif parkdecision in ['east', 'e']:
            print("You head down the path to your east.")
            if CharInfo.park_checks.park_roommate_path is not True and CharInfo.park_checks.park_lake_path is not True:  # Randomly picks which path to go down
                print(
                    secrets.choice(pathdialog)())  # Instead you call the function from the randomization bit. Like this
            elif CharInfo.park_checks.park_roommate_path is True and CharInfo.park_checks.park_lake_path is not True:  # If the player has not seen the self reflection path it will play that instead of a random selection or roommate path.
                self.parkpathself()
            elif CharInfo.park_checks.park_roommate_path is not True and CharInfo.park_checks.park_lake_path is not True:  # If the player has not seen the roommate path has not been seen it will play that instead of the random selection or self path
                self.parkpathrommates()

        elif parkdecision in ['west', 'w']:
            print("You head down the path to your west.")
            time.sleep(3)
            if CharInfo.park_checks.park_lake_path is not True and CharInfo.park_checks.park_roommate_path is not True:  # Randomly picks which path to go down first
                print(secrets.choice(pathdialog)())
            elif CharInfo.park_checks.park_lake_path is True and CharInfo.park_checks.park_roommate_path is not True:  # If the player has seen the self reflection path the roommate path is played instead
                self.parkpathrommates()
            elif CharInfo.park_checks.park_lake_path is not True and CharInfo.park_checks.park_roommate_path is True:  # If the player has seen the roommate path then the self reflection path is played
                self.parkpathself()
        elif parkdecision in ['save']:
            SaveSystem.save_sys.saving()
        else:
            print("Invalid input")
            return self.lakepark()

    def parkpathrommates(self):
        print("This path is slightly shorter than the other one, as it doesn't go past the lake.")
        input()
        print(
            "About 25 minutes into your hour or so walk you come across a group of college aged people hanging out on a set of benches. They remind you of your more recent years spent around Sasha and Jacob.")
        input()
        print("You remember how you met both of them in college. At different times of course.")
        print(
            "You met Jacob in one of your upper-division elective courses, the one about environmental ethics or something like that. Very fitting considering Jacob has been a very outdoorsy type of guy ever since you’ve known him")
        input()
        print(
            "You ended up starting a study group with him since you weren’t exactly having a great time in class. Mainly because it was taught by a not so fantastic professor.")
        input()
        print("It started off as a pretty standard study group, consisting of you, Jacob, and a couple other students. Eventually you started hanging out with him outside of the group and found out that he’s a really cool guy. You liked the same kind of movies, liked the same kinds of food, and even ended up owning the same brand of car.")
        input()
        print(
            "The rest is history, you’ve been good friends with him ever since. To the point that you decided to roommate up with him starting your 4th year at college.")
        input()
        print(
            "You ended up meeting Sasha in a similar way. You ran into her at one of the dining halls your very first year at college. You were sitting by yourself, and she came up and asked to sit with you.")
        print(
            "You started off with the usual college small talk, ‘Hey, what’s your major?’ ‘What dorm do you live in?’ She ended up living in one of the nearby dorm complexes, which shared a dining hall with your building. This led to you and her getting lunch together on a fairly regular basis.")
        input()
        print(
            "You talked quite a bit during lunch, and you eventually ended up hanging out with her outside of lunch quite a bit. You didn’t have as much in common with her as Jacob, but you still appreciated her company. As she did with you.")
        print(
            "You always kept in touch with her throughout the year, often attending various on-campus event together, and helping each other with classes. The relationship never really advanced beyond being good friends, as you’ve never had very strong feelings for her, and apparently neither has she. Although... you do remember having some feelings for her when you first met, but they faded soon after that.")
        input()
        print(
            "She’s been a really great friend to you, though she can be a bit forgetful at times. You’re really glad you met her and Jacob during your time at college, who knows how different your current life would be if you didn’t!")
        input()
        print(
            "Caught up in your thoughts you find yourself at the end of your walk before you know it. You are now back at the park entrance way.")
        CharInfo.player_info.player_location = sycamore_park.lakepark
        CharInfo.park_checks.park_roommate_path = True
        SaveSystem.save_sys.saving()
        input()
        self.lakepark()

    def parkpathself(self):
        print("15 minutes into the walk you come across a familiar sight, the great Sycamore Lake. Hence the park’s name.")
        input()
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
            "They were sisters, in-fact. You did tons of stuff together, swimming, movies, games, everything. You don't even remember how you met them, just that they were some of your closet friends ever since.")
        print(
            "It’s not an exaggeration to say that those two were some of the biggest non-family influences on your life.")
        print(
            "Mainly bcauser they were always there for you. They supported you and you supported them. You can recall countless memories from your childhood revolving around them.")
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
        CharInfo.player_info.player_location = sycamore_park.lakepark
        CharInfo.park_checks.park_lake_path = True
        input()
        self.lakepark()

# Global Classes


jacob_kitchen = JacobDialogue()  # Global instance of JacobKitchen  # Provides info for the player character

first_world = FirstWorld()

sycamore_park = SycamorePark()

tories_cafe = ToriesCafe()

player_bathroom = PCBathroom() # Make sure to include the () when adding classes)

sasha_living = LivingRoom()

sasha_encounter = SashaEncounter()

# Starts the game


TravelSystem.travel_function.travel_point_cafe = tories_cafe.thecafe  # Sets travel points
TravelSystem.travel_function.travel_point_park = sycamore_park.lakepark
TravelSystem.travel_function.travel_point_festival_one = Festival.festival_area.bus_ride
TravelSystem.travel_function.travel_point_bedroom = pcbedroom
TravelSystem.travel_function.travel_point_hallway = hallway


loadingoption = input("Do you wish to load a game? ").lower()  # Make it so this is the first question asked.
if loadingoption in ['yes', 'y', 'load', 'l']:
    SaveSystem.save_sys.loading()
elif loadingoption in ['no', 'n']:
    pass

print("Hello", CharInfo.player_info.name)
time.sleep(3)
print("Welcome to Tales from the Road. A slice of life text game about furry characters")
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
print("Excellent. This game follows typical interactive fiction rules, e.g you type north or n to go north. If you want to interact with an object you can type in it's name and interact with it.")
print(
    "In order to advance most dialogue in the game, you will have to press a key first. The console will print out a statement and then to get to the the next piece of dialogue you'll have to hit, say, enter.")
input("Like this. expect you won't have any text telling you too press a key to continue. Press a key to continue.")
print("Sometimes you'll able to choose the next dialogue option. The options will numbered which allows you to type in the corresponding number and select that dialogue option.")
input()
print("It will look like this:")
input('(1): You now understand how dialogue prompts work. (2): Choose any number listed to continue.')
print("With that out of the way, let's get started")
time.sleep(3)
intro()
