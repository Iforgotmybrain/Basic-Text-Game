# Festival area
import time
import random
import os
import CharInfo
import TravelSystem
import SaveSystem

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

class FestivalStart:
    def bus_ride(self):
        if CharInfo.festival_checks.bus_ride_complete is not True:
            print(
                "You hop on a bus headed to downtown. There’s a special event today called Lake Fest, which hosts several vendors and activities.")
            input()
            print(
                "While on the bus you sit next to a man with an ‘I heart NY shirt’ on. He’s carrying a sizable backpack, and based on the apparel he’s wearing, he seems to have experience traveling.")
            print(
                "The man looks to you and asks if you’re going to Lake Fest. You say yes, and that you’ve gone to it almost every year you’ve lived here.")
            input()
            print("'So you’re a local” the Tiger says. “I’m Chris.” The Tiger reaches out to shake your hand'")
            input()
            print("You shake the Tiger’s hand and introduce yourself as {}.".format(CharInfo.player_info.name))
            print(
                "'Nice to meet you {}. I’m coming through here pretty much solely for Lake Fest. Though I wouldn’t be opposed to checking out some other places if you’ve got any recommendations. My hotel for here is booked for the day so I’ve got time.'".format(
                    CharInfo.player_info.name))
            input()
            print(
                "You can’t really think of anything else remarkable here. The town is actually quite boring. You offer a few eating recommendations, including Tories Café, stating that there really isn’t much to do here except check out the local restaurants.")
            input()
            print(
                "'Yeah, I kind of figured. This is my second time going to this event and I’ve never really seen anything else to do.” The Tiger says with a friendly tone.")

            print("'Anyway, I bet you’re probably wondering why someone would come here just for one event.'")
            input()
            print("You can’t say you were really burning your brain trying to figure that out, but you’ll humor him.")

            print(
                "'Well, I’m actually on a road trip across the country! I do it every year, in some shape or form. Last year I went by train but now I’m doing it by car.” He says with an enthusiastic tone. Clearly he’s quite interested in traveling the country.'")
            input()
            print(
                "You ask Chris for some more details, you’ve always been fascinated by the idea of traveling the country, but you’ve just never had the time or money to do so.")
            input()
            print(
                "'Well, I start off my trip on the east coast, in New York city as you might’ve guessed by my shirt.” He says while pointing to his 'I heart NY' shirt.'")

            print(
                "'I spend a varying amount of time in each place I stop. Just depends on what that city has to offer, ya know?'")

            print(
                "'The end destination changes every year. Last year I stopped at San Francisco, and this time around I’ll probably be heading to Seattle.'")
            input()
            print(
                "You tell Chris that you’ve been interested in doing something similar, you find the idea of traveling the country and seeing all it has to offer to be exciting!")
            print("It would be a nice change of pace from the predictable nature of your life at the moment.")
            input()
            print(
                "'It’s a very rewarding experience. But it’s also a significant time commitment, and too be honest, it can be a bit tiring driving for hours on end. But the experiences and sights make it worth it. There really isn’t much else like it, expect maybe traveling the world. But that’s whole different ballgame.'")
            input()
            print(
                "'If I could offer one tip, it's to plan ahead of time and check out what’s going to be going in the towns you’re passing by. Try to find the best possible time to leave so you can maximize the events you can go too'")

            print(
                "You thank Chris for advice, if you ever do decide to take on such an endeavor, you’ll definitely make sure too have a plan.")
            input()
            print(
                "'Well looks like our stop’s up here. It’s been great talking to you.” He says while extending his hand out for a farewell handshake.'")
            print("You shake his hands and say goodbye, he offers one last piece of advice before departing.")
            input()
            print(
                "'Hey, if you ever decide to go for it, hit me up on Pawbook. I’ve got a list of my favorite places to stop at it, I’d be glad to share'")

            print("You thank the Tiger as he goes on his way.")
            input()
            print("You have arrived at the festival")
            CharInfo.festival_checks.bus_ride_complete = True
            self.festival_entrance()

        elif CharInfo.festival_checks.bus_ride_complete is True:
            self.festival_entrance()

        else:
            print("Invalid input")
            return

    def festival_entrance(self):
        CharInfo.player_info.player_location = festival_area.festival_entrance
        print("You arrive at the festival and see crowds of people on the streets. Vendors as far as the eye can see.")

        print("The day is perfect for a festival, a light overcast keeps temperatures in the sun bearable, and a slight breeze keeps you cool.")
        input()
        print("You see rows of vendors directly ahead to your north, and the bus stop to travel home.")
        festivaldirection = input("What will you do? ").lower()
        if festivaldirection in ['travel', 'home', 'bus', 'stop', 'bus stop']:
            TravelSystem.travel_function.traveltofront()
        elif festivaldirection in ['north', 'vendors', 'festival', 'n']:
            print("You brave the crowd and head towards the main festival area.")
            self.festival_main()
        elif festivaldirection in ['save', 'save game']:
            SaveSystem.save_sys.saving()
        else:
            print("Invalid input")
            return self.festival_entrance()

    def festival_main(self):
        CharInfo.player_info.player_location = festival_area.festival_main
        time.sleep(1)
        print("You can see stands for everything from spices to graphic tees. The quaint downtown streets filled with folks from every part of the state, and country for that matter.")
        input()
        print("Initially you don’t see any vendors that catch your eye, though as you go walk further you do find a couple of places you wouldn’t mind checking out.")
        input()
        print("One is a painter; their stand features a host of beautiful oil paintings of various subjects and locations.")
        input()
        print("The second is a wood sculptor, he has various objects depicted in wood for sale.")
        input()
        print("And finally, the third is a novelty t-shirt and hat seller. You know, the kind that has hats with a big weed leaf and Snoop Dogg on them. You know what I’m talking about.")
        input()
        festival_vendor = input("Which one do you want to check out? ").lower()
        if festival_vendor in ['paint', 'painter', 'oil painting','painting', 'one' 'first']:
            self.vendor_painting()
        elif festival_vendor in ['hat', 'shirt', 'tshirt', 't-shirt', 'trash', 'weed', 'novelty vendor', 'snoop dogg',
                                 'novelty', '3rd', 'third']:
            self.trashy_vendor()
        elif festival_vendor in ['wood', 'wooden', 'wood sculptor', 'wooden sculptor', 'two', 'second']:
            self.wooden_vendor()
        elif festival_vendor in ['save', 'saving', 'save game']:
            SaveSystem.save_sys.saving()
        else:
            print("Invalid input")
            return self.festival_main()


    def vendor_painting(self):
        print("You walk up to the painters stand, you see works ranging from beautiful mountain landscapes to well-done portraits. He has a very diverse set of paintings.")
        input()
        print("You browse their painting selections some more; the painter eventually asks if anything catches your eye.")
        input()
        print("'I also take requests if you’re looking for something else. They are more expensive though.'")
        input()
        painter_purchase_option = input("(1). You state that you’re not really interested in any of the paintings. \
        (2). You ask the painter what the prices are for the individual pieces and the requests. ").lower()

        if painter_purchase_option in ['1']:
            print("You state that you’re not really interested in any of the paintings.")
            input()
            print("'Understandable. If you change your mind you might try looking me up online.'")
            print("He hands you a business card and you part ways.")
            return self.festival_main()

        elif painter_purchase_option in ['2']:
            print("'Well, the price for both depends on what you want'")
            print("'For example, the piece with the vixen will run you about $250. The one of the ocean beach, about $200'")
            input()
            print("'Requests are about $500 or so for a self-portrait, and around $400 or so for a specific landscape'")
            input()
            print("After browsing his selection you’ve set your eyes on 3 paintings. ")
            input()
            print("One depicts a lake surrounded by a forest, with a mountainous background.")
            print("The other is a portrait of a husky dressed in, if you were too guess, 18th century clothing. He’s holding a sword in one hand while leaning on a desk.")
            print("The third is set in a fantasy setting, showing a group of 5 furless beings traveling through the woods while being chased by wraiths with swords. The one being seems to be holding some sort of ring.")
            input()
            painting_purchased = input("After thinking about it you decide to purchase the painting with the… \
            (1): Husky \
            (2): Lake \
            (3): Wraiths \
            (4) None ".lower())

            if painting_purchased in ['1']:
                CharInfo.festival_checks.painting_purchase = 'husky'

            elif painting_purchased in ['2']:
                CharInfo.festival_checks.painting_purchase = 'lake'

            elif painting_purchased in ['3']:
                CharInfo.festival_checks.painting_purchase = 'wraiths'

            elif painting_purchased in ['4']:
                print("You tell the painter that the prices were bit more then you hoping to pay.")
                input()
                print("'Understandable. If you change your mind you might try looking me up online.'")
                print("He hands you a business card and you part ways.")
                return self.festival_main()

            else:
                print("Invalid input")
                return
            print('"Excellent! I’ll get it wrapped up and ready to go. You’ll be looking at bill of about $225."')
            input()
            print("You pay the painter and collect the painting.")
            CharInfo.festival_checks.festival_item_purchased = True
            CharInfo.player_info.money -= 225
            print("Your bank balance is now ${}".format(CharInfo.player_info.money))
            CharInfo.player_info.player_location = festival_mid.inital_concert_dialogue
            SaveSystem.save_sys.saving()
            festival_mid.inital_concert_dialogue()
        else:
            print("Invalid input")
            return self.vendor_painting()

    def wooden_vendor(self):
        print("You decide to check out the wood sculptor’s booth.")
        print("Looking at their wares, you see numerous objects made out of wood. There’s a wooden boat, dozens of boxes all in different shapes and sizes, and even a small, ‘model’ tree trunk made out of… wood.")
        input()
        print("You can see a few things you wouldn’t mind taking home, including one of the smaller boxes, and a wooden plane model depicting an SR-71.")
        print("You decide to ask the seller how much the items are.")
        input()
        print('"The box would be $45, and the plane is about $300"')
        input()
        wooden_choice = input("After thinking about it, you decide to… (1): Purchase the box (2): Purchase the plane (3): Purchase nothing ").lower()

        if wooden_choice in ['1']:
            CharInfo.festival_checks.festival_item_purchased = True
            CharInfo.festival_checks.wooden_sculpture = 'box'
            print('"Excellent choice, I’ll get that ready to go for you."')
            print("You pay the vendor $45 and receive the wooden box")
            CharInfo.player_info.money -= 45
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            CharInfo.player_info.player_location = festival_mid.inital_concert_dialogue
            SaveSystem.save_sys.saving()
            festival_mid.inital_concert_dialogue()

        elif wooden_choice in ['2']:
            CharInfo.festival_checks.festival_item_purchased = True
            CharInfo.festival_checks.wooden_sculpture = 'plane'
            print("A fantastic choice, that’s one of my favorite items I have for sale!")
            input()
            print("The vendor bags the item and you pay him $300.")
            print("You receive the model plane.")
            input()
            CharInfo.player_info.money -= 300
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            CharInfo.player_info.player_location = festival_mid.inital_concert_dialogue
            SaveSystem.save_sys.saving()
            festival_mid.inital_concert_dialogue()

        elif wooden_choice in ['3']:
            print("Okay, that's fine. If you change your mind I'll be here.")
            input()
            return self.festival_main()

        else:
            print("Invalid input")
            return self.wooden_vendor()

    def trashy_vendor(self):
        print("You decide to visit the t-shirt vendor.")
        print("This booth sells graphic tees, and the finest of bootleg snap-back hats. The shirts are $15 and the hats are $20")
        input()
        print("The T-shirts mostly have some form of meme or pop culture reference on them. You can see a T-shirt with Heath Ledger’s joker on it, with the caption ‘why so serious?’. ")
        input()
        print ("You also see a T-shirt with the oh-so popular game Fortnite on it, the shirt has picture of the game’s iconic mascot with the caption ‘eat, sleep, Fortnite, repeat’.")
        input()
        print("The hats mostly have popular sports teams on them, with the Yankees easily being the most common one. They also have a hat with weed leaf on the front, and the number 420 on the bill.")
        input()
        print("You’re not really interested in any of this vendor’s merchandize, since most of it is either trashy, of dubious quality, or will end up being outdated in a months’ time.")
        input()
        print("But, if you had to choose ''something'', you think you would pick…")
        trashy_vendor = input("(1): The shirt with Snoop Dogg and weed references on it, no way in hell are you going to wear it, but it might make a good gag gift someday. \
            (2): The bootleg NY Yankees hat. You don’t really like the Yankees, or snap-back hats, but odds are you know someone who does. It might come in handy as a gift someday.\
            (3): An absurdly outdated meme shirt that has a troll face on it. Much like the Snoop Dogg shirt, you probably aren’t going to wear, but you could give it away as a gag gift.\
            (4) Nothing").lower()

        if trashy_vendor == '1':
            print("You take the Snoop Dogg shirt and bring it to the vendor.")
            input()
            print("The vendor is a 30-something alligator. He seems to be chewing tabaco, and his shirt is stained from standing outside in the heat all day.")
            input()
            print('"Let’s see, a t-shirt? That’ll be $15."')
            print('"Hah, the Snoop Dogg one is probably of my favorites. It’s surprisingly popular as well."')
            input()
            print("You hand the alligator $15 and receive the shirt.")
            CharInfo.festival_checks.festival_item_purchased = True
            CharInfo.festival_checks.trash_vendor = 'snoop'
            CharInfo.player_info.money -= 15
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            CharInfo.player_info.player_location = festival_mid.inital_concert_dialogue
            SaveSystem.save_sys.saving()
            festival_mid.inital_concert_dialogue()

        elif trashy_vendor == '2':
            print("You grab the bootleg hat and take it to the vendor.")
            input()
            print("The vendor is a 30-something alligator. He seems to be chewing tabaco, and his shirt is stained from standing outside in the heat all day.")
            input()
            print('"Hmm, let’s see… A hat? That’ll be $20."')
            input()
            print("You hand the alligator $20 and receive the hat.")
            CharInfo.festival_checks.festival_item_purchased = True
            CharInfo.festival_checks.trash_vendor = 'hat'
            CharInfo.player_info.money -= 20
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            CharInfo.player_info.player_location = festival_mid.inital_concert_dialogue
            SaveSystem.save_sys.saving()
            festival_mid.inital_concert_dialogue()

        elif trashy_vendor == '3':
            print("You grab the troll face shirt and take it to the vendor.")
            input()
            print(
                "The vendor is a 30-something alligator. He seems to be chewing tabaco, and his shirt is stained from standing outside in the heat all day.")
            input()
            print('"Okay, a t-shirt? That’ll be $15."')
            print('"Actually, you know what, I hardly sell any of these so I’ll give to you for $8."')
            input()
            print("You hand the alligator $8 and receive the shirt.")
            CharInfo.festival_checks.festival_item_purchased = True
            CharInfo.festival_checks.trash_vendor = 'troll'
            CharInfo.player_info.money -= 8
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            CharInfo.player_info.player_location = festival_mid.inital_concert_dialogue
            SaveSystem.save_sys.saving()
            festival_mid.inital_concert_dialogue()

        elif trashy_vendor == '4':
            print("You just cannot imagine buying anything here.")
            input()
            print("You leave the booth.")
            input()
            return self.festival_main()

        else:
            print("Invalid input")
            return self.trashy_vendor()

class FestivalMid:
    def inital_concert_dialogue(self):
        print(
            "After checking out the vendors and merchants, you decide to grab something to eat from the many food trucks present.")
        input()
        print(
            "You decided to get a beef gyro, a slushy, and a funnel cake. An unhealthy meal, yes, but it’s a special event, who cares?")
        print("All together the meal cost you $15. Food trucks are damn expensive!")
        input()
        print("After eating your meal you head towards one of the many events being held here.")
        print(
            "The event you're going to is a concert, it features various local musicians and bands, with the main headliner being a band called Lioness Untamed.")
        input()
        print(
            "As you arrive at the concert stage you see one of the bands setting up, according to the schedule their name is Airplane Harness. They primarily play indie music, which helps explain their odd name choice.")
        input()
        print(
            "Your feelings on indie music differ from band to band, so you decide to stick around and see if you like their music.")
        print(
            "As you walk towards the stage you feel a tap on your shoulders. You turn around to see who’s trying to get your attention, much to your surprise, it was Holly!")
        input()
        print('"Fancy meeting you here, old friend. Never really thought of you as the festival type."')
        print(
            "You tell Holly you thought the same of her, she never seemed to like crowds of people back in high school.")
        input()
        print(
            '"Eh, it just depends on circumstances I guess. I don’t mind this kind of event too much because you can basically do whatever. Anyway, why are you here? As I was saying, I\'ve never really thought of you as the festival type."')
        input()
        print(
            "You tell Holly that going to this festival is pretty much a tradition for you, you’ve been going to it ever since you were 7. You come to it pretty much no matter what. Even if you have to go alone, that doesn’t stop you.")
        input()
        print(
            '"Huh, well good for you. I’ve only gone here, like 3 times I think. I pretty much only go If I have nothing else to do, or if someone wants me to go with them. This time it was the former."')
        input()
        print(
            "You ask Holly if she knows anything about the band playing, as they seem to be a fairly underground group")
        print(
            '"Not really, no. I figured I’d check them out since I enjoy most indie music. It’s free so it\'s not like I’m out anything but my time if I don’t like them."')
        print('"They seem to have a more lo-fi sound, which I can take or leave depending on the group."')
        input()
        print(
            '"Okay, So, a bit of an unrelated topic. But I figured since both of us are here by ourselves we could maybe hang out a bit? Maybe just until the concert ends, or until one of us loses interest whichever comes first. It’s up to you though, just thought I’d throw the idea out there."')
        input()
        print(
            "It’s been a long time since you’ve actually hung out and talked with Holly. And you are a bit a tired of wandering here alone, so her offer is definitely interesting. You can’t really think of a good reason not to at least stick together until the concert ends.")
        input()
        self.main_concert_dialogue()


    def main_concert_dialogue(self):
        print("You tell Holly that’d you be fine with her tagging along for now.")
        input()
        print('"Awesome, festivals are always better when you have likeminded people to hang out with!"')
        input()
        print("The band seems to be finished setting up and is starting their set with a song called ‘Tretter’.")
        print("Their sound is very low-fi like Holly said, it’s not really your cup of tea but you’ll stick around for a couple more songs.")
        input()
        print("About halfway into the song Holly offers her opinion on the band.")
        print('"I can’t say this is really my jam. I’ll probably still stay and listen though since there really isn’t much else going on."')
        input()
        print("You agree with Holly, even if this isn’t the greatest music you’ve ever heard there really isn’t much else to do.")
        input()
        print("With there not being much else to do, you decide to get to know Holly a bit better by asking about her career as an artist. Primarily by asking how she got started.")
        input()
        print('"Well, I’ve been drawing since… eh, around middle school I’d say. Back then it was just a hobby, of course. Just something to channel my creative ideas, and maybe show off a bit."')
        input()
        print('"When I went to college I ended up making a social media account dedicated to posting my art, I advertised it a bit and got a decent following, about 5000 people."')
        print('"At that point, it was still just a hobby, but I was definitely thinking about the money potential."')
        input()
        print('"I dropped out of college, and then after that, I got a full-time retail job and just kept working on my art and worked on getting more followers."')
        input()
        print("About what you expected to hear. You ask Holly when she started to see art as an actual career path instead of just a hobby.")
        input()
        print('"Hmm, I started taking commissions shortly after leaving college. It wasn’t a ton of money, just like beer money really. But it was something! And it was first time I’d been paid for doing art."')
        input()
        print('"About half a year into my retail job I expanded the commissions I took and also opened up a donation page. At this point, the income from my art was actually starting to rack up. Wasn’t as much as my ‘real job’ but it was enough to pay some of my utilities every month. I was really starting to see art as a legitimate career path at this point."')
        input()
        print('"From there I just sort of kept expanding my work, I started making merch, I raised the prices of commissions a bit and set up an account on one of those monthly subscription type of sites."')
        input()
        print('"The art income eventually took over my retail job’s income. I ended up working at the retail job for about 2 months saving up the income from it before I quit and worked on art full time."')
        print('"And now, here I am. I started doing art full-time 9 months ago, and it’s been surprisingly smooth sailing since."')
        input()
        print("You congratulate Holly on being able to support herself on her art. It’s not often that people are able to live off, or even achieve their ‘dream job’")
        input()
        print('"For sure. I’m definitely fortunate for being able to live off my art."')
        print('"You aren’t doing too bad either though, being able to live off of just odd jobs here and there is pretty damn nice."')
        input()
        print("You agree. You’re not sure if you would really consider contract work to be your dream job, but it's definitely a better situation than most people are in.")
        input()
        print("The band has been gone through about half of their set at this point, you’re still not feeling the music and the only thing really keeping you here is Holly.")
        input()
        print("You decide you’re going to bare the rest of the concert, or at least stay until Holly decides she’s heard enough.")
        input()
        print("The conversation between the two of you has died down a bit, there hasn’t really been an in-depth conversation since you discussed each other's careers. Just small talk amidst the compulsive checking of your smartphones and the occasional attention paid to the concert.")
        input()
        print("You grasp at straws while thinking of things to talk about. Eventually you decide to ask Holly what kind of art she draws.")
        input()
        print('"Well, I started off doing art for stuff like tv shows and movies, pop culture stuff, right? From there I just sort of expanded what I draw. Now I do commissions for a fair number of things, though I’d say I’m best at, or rather, I enjoy drawing concept art the most."')
        input()
        print('"As far as the species I’m best at drawing, I’d say Foxes (of course), Leopards, and Bears."'.format(CharInfo.player_info.race))
        input()
        print('"Alright, enough questioning me. Now it’s my turn. Why’d you leave your job at Syperion? "')
        print("I saw the Pawbook post you made when you left, but you didn't really go into why you left.")
        input()
        print('A bit of a personal question, but you’ve been bugging her about her career, so fair enough.')
        input()
        print("You explain to Holly how it all started. Initially, it all went pretty well. The job paid exceptionally well, had good benefits, and looked really good on a resume. About 5 months into the job though you started to notice some of the dysfunction abound. You grew tired of the petty office politics, your ‘superiors’ never really valued your work or your feedback, and the work you were doing just wasn’t very fulfilling.")
        input()
        print("Most workplaces will have elements of all those things, this is true, but here they were overwhelming. You knew you weren’t long for that place and started saving up a decent chunk of your paycheck each month. You put half of that chunk into an investment account, and the other half went directly into your savings.")
        input()
        print("You stayed for about 7 months after that, and by the time you put in your 2-weeks, you had saved around $40,000 total. Enough to live modestly by yourself for 1 year. Or in your case, more than enough to live with your roommates for 2+ years.")
        input()
        print("'Wow, that just amazes me. Saving 40k in only one year is just crazy. That’s almost how much I make in a year.'")
        input()
        print("'And then after that, I’m assuming you started doing that contract work you were talking about?'")
        input()
        print("Yes, you started working contracts shortly after being fired. They provide a nice in-flow of cash to help keep you going.")
        input()
        print('"Well, that was really insightful. I can totally understand quitting a job because you don’t like the culture, that’s pretty much why I took up art as my career."')
        input()
        print("At this point the band is on their last song. The evening is approaching, with only a few more hours left for the festival.")
        input()
        while True:
            print("You could ask Holly to accompany you for the rest of the day, or you could part ways. ")
            hollystayorleave = input("After thinking about it you decide too... (1): Ask Holly to tag along with you for the rest of the day \
                    (2): Go your separate ways ").lower()

            if hollystayorleave in ['1']:
                CharInfo.festival_checks.holly_stay = True
                print("You ask Holly if she wants to tag along for the rest of the day.")
                input()
                print(
                    '"Well, I wasn’t initially planning on staying after this concert, but since you’re offering… Sure, I’ll gladly tag along."')
                input()
                CharInfo.player_info.ending_points += 4
                CharInfo.player_info.player_location = festival_end.festival_hub_end
                SaveSystem.save_sys.saving()
                festival_end.festival_hub_end()
                break

            elif hollystayorleave in ["2"]:
                CharInfo.festival_checks.holly_stay = False
                print("You decide to part ways with Holly.")
                CharInfo.player_info.ending_points -= 2
                input()
                CharInfo.player_info.player_location = festival_end.festival_hub_end
                SaveSystem.save_sys.saving()
                festival_end.festival_hub_end()
                break

class FestivalEnd:
    def festival_hub_end(self):
        CharInfo.player_info.player_location = festival_end.festival_hub_end  # This keeps track of where the player is.
        print("As the band finishes their set you leave the concert and head back towards the main festival area.")
        input()

        if CharInfo.festival_checks.festival_walk is not True and CharInfo.festival_checks.holly_stay is not True:
            print("There's not much left to do here. The only other thing you could think to do is check out the bits of the festival over to the east.")

        elif CharInfo.festival_checks.festival_walk is not True and CharInfo.festival_checks.holly_stay is True:
            print("There's the festival games to the north, and the looping walk way to the east.")

        festivalhubchoice = input("You decide that you want to go... ").lower()

        if festivalhubchoice in ['e', 'east']:

            if CharInfo.festival_checks.holly_stay is True:
                self.festival_walkway_holly()

            elif CharInfo.festival_checks.holly_stay is False:
                self.festival_walkway_self()

        elif festivalhubchoice in ['n', 'north'] and CharInfo.festival_checks.holly_stay is True:  # Made it so the games are only open when you have Holly. Just too much dialogue to write otherwise.
            self.festival_games_holly()
            return self.festival_hub_end()

        elif festivalhubchoice in ['save', 'saving', 'save game']:
            SaveSystem.save_sys.saving()

        else:
            print("Invalid input")
            return self.festival_hub_end()

    def festival_games_holly(self):
        print("You head towards the many fair games set up at this festival.")
        input()
        print('"I used to always bug the hell out of my parents about playing these games. They’d always say ‘no, you’re not playing those games, they’re a rip-off. I could go to the store and buy you whatever toy it is you want for less money than it would take to win one of those games."')
        input()
        print('"Well guess what Dad, it wasn’t about the toy, it was about the experience! I don’t think Krigers has you throwing a ball into a bowl in order to get a toy, do they Dad?"')
        print('"They are terribly unfair though, of course I didn’t really understand that as a kid. I think I’ve won a grand total of once. And that was on the basketball one, it was just complete luck."')
        input()
        print("As a kid, you had a similar experience to Holly. Though your parents would occasionally give in and let you play a few.")
        input()
        print("As you walk down the path you see all the games. There’s the basketball game, which is rigged by setting the hoop higher than an official one. The ‘throw this ping pong ball into the water’ game. Which is difficult because the little ball just bounces off everything. The shooty game, which has you shooting a fragile paper target with inaccurate BB pellets. You get the idea, this place is full of unfair games and shady business practices.")
        input()
        print("Well, you came here for a reason, might as well play at least one of these games.")
        input()
        print('"I wouldn’t mind playing the one where you try to throw a baseball at a certain speed. It’s up to you though."')
        input()
        print("You could try the baseball one, you also thought about doing the BB gun one. They're all rigged in some way though, your odds are probably the same no matter which one you have a go at.")
        fairgamechoice = input('After thinking about it, you decide to... (1): Play the baseball game \
        (2): Play the BB gun game. ').lower()

        if fairgamechoice in ['1']:
            self.festival_baseball_holly()

        elif fairgamechoice in ['2']:
            self.festvial_bb_holly()

    def festvial_bb_holly(self):   # Not really happy with how this turned out. Honestly I don't consider it to be an equal to the baseball game.
        print("You decide to check out the BB gun game. Your personal preference.")
        input()
        print("This game has you shooting out all of a paper target using an automatic BB gun that looks like an old tommy gun.")
        input()
        print("The gun is incredibly inaccurate and fires so many pellets at a time that you often end up hitting the same area repeatedly.")
        input()
        print("You pay the vendor enough for 2 turns on the gun, one for each of you. The total is $12, a ridiculous price.")
        input()
        print('"It might be ridiculous, but remember, you’re paying for the "experience" "')
        input()
        print("You decide to play first since it was your idea to check this game out.")
        print("You line up at the gun. It’s quite beaten up, with most of the paint having chipped away.")
        input()
        print("The gun has sights on it but they are quite trash, so you’re really just eyeballing it. The $12 you paid will give you 300 BB rounds each. Not much considering how fast the gun fires.")
        print("You think the best way to go about this would be to shoot the outside of the target first.")
        input()
        print("You take hold of the gun and aim down its rudimentary sights, it’s bolted down to a rail which prevents you from aiming the gun with anything resembling decent accuracy.")
        print("Guess you’ll just have to make do.")
        input()
        print("You start to shoot the target, with each pull of the trigger about 10 BB pellets fly out. An unnecessary amount, no doubt it was made that way in order to reduce your chance of winning.")
        input()
        print("You start off doing a pretty decent job, you’ve shot out a decent chunk of the target, with about half it remaining.")
        print("It’s getting quite difficult at this point though since there’s less and less of the target to shoot. Instead of being able to essentially aim in the general area of the target and hit something, you have to be more careful with your shots. Which is difficult given the gun’s poor movement and sights.")
        input()
        print("You knock out some more of the target, there’s about 25% remaining, but you only have 100 pellets to get the rest of it done. At this point, your shots are missing more than they are hitting. The remaining pieces of the target aren't supported by much, which leads to the paper just giving way to pellets, dealing no damage.")
        input()
        print("You’re just about to knock out the target, you aim the gun perfectly, your finger on the trigger ready to finally win one of these silly games.")
        pc_win = random.randint(30, 100)

        if pc_win > 70:
            print("You push the trigger and the last barrage of BB pellets is unleashed. They hit the last bit of the target perfectly, destroying the last evidence of its existence.")
            input()
            print("Despite all the odds against you, you made it! You won!")
            print("The vendor begrudgingly tells that you have the pick of any cheaply made stuffed animal in stock.")
            input()
            print("Among the options are a Dragon, German Shepard, and a Fox.")
            pc_bbanimal = input("You decide to pick the... (dragon, german shepherd, fox)").lower()

            if pc_bbanimal in ['dragon']:
                print("You pick the dragon. You can never go wrong with a dragon.")

            elif pc_bbanimal in ['german shepard', 'g shep', 'german shep']:
                print("You pick the stuffed german shepard, it's color is very similar to Sasha's, being primarily black with some tan.")

            elif pc_bbanimal in ['fox']:
                print("You decide too pick the fox, foreshadowing? Probably not. You just thought the fox looked the cutest.")  # Do I keep this line? Might too heavy handed.

        elif pc_win < 70:
            print("You push the trigger, ready to decimate the last of that pain in the ass target, but as you do you hear a clicking noise, and nothing comes out. You’ve run out BB pellets.")
            input()
            print("Goddamnit! You were this close to winning! You know you would have won if the gun wasn’t such a piece of trash.")
            print("Oh well, it’s over. Maybe Holly will have some better luck. Which is really all these games are based on.")
            input()
        print("It’s Holly’s turn now, they say luck favors the Foxes, guess you’ll see.")
        input()
        print("She lines up at the gun, no doubt thinking the same things you did.")
        print('"You could have told me this thing was impossible to aim. You’d think this thing was a weapon of mass destruction with how bolted down it is."')
        input()
        print("She makes good progress at the start, chipping away a similar amount to you. She seems to have slightly better control over the rate of fire than you did.")
        input()
        print("Holly seems to be falling into the same issues you did, as she knocks more and more of target off it gets more difficult to actually hit it. Guess this is one of the main obstacles in this game.")
        print("As the game goes on it plays out very similar to your try. She ends up with about 20% of the target left but struggles to hit the rest due to its flimsy nature. ")
        input()
        holly_win = random.randint(40, 100)

        if holly_win > 60:
            print("Holly ends up at the same point you did towards the end. She’s only got about 3 more trigger pulls before she runs out of ammo.")
            input()
            print("She lines up a shot to knock out the rest of the target, she pulls the trigger, but the pellets just fly past the paper as it gives way.")
            print("Holly sighs, no doubt frustrated by this tedious game.")
            input()
            print("She lines up another shot in attempt to win this damn game.")
            print("Holly pulls the trigger and the pellets land right on target, getting rid of what was left of the target.")
            input()
            print("To your surprise, Holly actually managed to pull it off and win!")
            print("The game vendor begrudgingly offers Holly a choice of any cheaply made stuffed animal they have on display. Among those displayed are a Dragon, a German Shepard, and a {}.".format(CharInfo.player_info.race))
            input()
            print("Holly picks the {}. A funny coincidence all things considered, but that’s probably all it is, a coincidence.".format(CharInfo.player_info.race))

            if pc_win > 70:
                print("It would seem that both of you made out today. It's rare enough for one person to win these games, but two? That's almost unheard of.")
                input()

            elif pc_win < 70:
                print("It seems the sayings were right, luck does favor the foxes. At least that $12 was not spent in vain.")
                input()

        elif holly_win < 60:
            print("Holly’s nearing the end of the game, unfortunately, it seems she isn’t going to make it. There’s a good chunk of the target left, with her gun only having 40 rounds left.")
            input()
            print("She gets a few more bursts off before the gun clicks and runs out of ammo. She made a damn good effort but it just wasn’t enough.")
            input()
            if pc_win < 70:
                print("Unsurprisingly, neither of you managed too win today. That's to be expected given how rigged these games are. As Holly would say, at least you 'experienced' the games.")
                input()
            elif pc_win > 70:
                print("You are the only one to emerge victorious today, even having won you feel like you wasted your money.")
                input()
        print("With the game done and over with, you evaluate your next course of action with Holly.")

        if CharInfo.festival_checks.festival_walk is True:
            print(
                '"The day is getting pretty late, I suppose we should start heading towards the parking lot. We might be able to see the fireworks on our way out."')
            input()
            CharInfo.player_info.player_location = festival_end.festival_ending_holly
            CharInfo.festival_checks.festival_game = True
            SaveSystem.save_sys.saving()
            self.festival_ending_holly()

        elif CharInfo.festival_checks.festival_walk is not True:
            CharInfo.festival_checks.festival_game = True
            print('"The day\'s winding down, we should probably check out that other path before it gets too late."')
            input()
            CharInfo.player_info.player_location = festival_end.festival_walkway_holly
            SaveSystem.save_sys.saving()
            self.festival_walkway_holly()

    def festival_baseball_holly(self):
        print("You decide to go with Holly’s choice.")
        input()
        print("You walk up to the booth and pay for 2 shots at throwing the ball. One for each of you. It cost a total of $7. Which is ridiculous, but like Holly said you’re paying for the ‘experience’.")
        CharInfo.player_info.money -= 7
        print("You offer Holly the first pitch since this was her first choice.")
        input()
        print('"Sure, I’ll have a go at it. I actually played softball when I was in middle school so maybe I can try and channel some of that 6th-grade energy to give me an edge."')
        input()
        print("Holly lines up at the target. Her goal is to throw the ball at a speed of 60 MPH. A pretty high target for the average person. It’s made even more difficult with how inaccurate the sensor on the target is. It probably hasn’t been replaced or maintained since the thing was first made. Even if it was, there’s nothing stopping the vendor from making it read a bit slower.")
        input()
        print("She thinks about it for a minute, lining up her throw. She reels back with the ball in her hand, ready to destroy the hell out of that target.")
        input()
        print("She extends her arm and throws the ball at what seems to be a decent speed. The display takes a minute to show the speed, you both wait with mild anticipation, thinking about all the bragging opportunities if one of you were to make it while the other didn’t.")
        input()
        holly_speed = random.randint(50, 65)
        print("The display finally shows the speed. Holly threw the ball at a speed of {} MPH.".format(holly_speed))

        if holly_speed >= 60:
            print("Unbelievable! She actually made it! Quite a feat given all the factors fighting against her. Hopefully you nail it as well, else you’ll never hear the end of it.")
            input()
            print("The clerk tells Holly she can take any of the various stuffed animals they have hanging up.")
            print("Among them are a stuffed German Shepard, a stuffed Tiger, and a stuffed {}.".format(CharInfo.player_info.race))
            input()
            print("Holly chooses the stuffed {}".format(CharInfo.player_info.race))
            input()

        elif holly_speed <= 60:
            print("Holly throws the ball with all her might, but it wasn’t enough, as the speed is short of the 60 mph target.")
        print("Now it’s your turn up. You’re probably the worst possible person to try this game, as you have no experience with baseball. That is unless you count those little plastic ones you threw around with when you were 4.")
        input()
        print("Well, you’ve gotta at least make an effort. You think about the proper form to throw the ball, trying to mimic the cardboard cut-out they have standing by their booth and the way Holly threw the ball.")
        print("Eventually, you feel like you’ve got the perfect form, you bring your arm back, ready to get back some of the money you wasted on this thing.")
        input()
        print("You throw the ball, but you can tell your grip wasn’t quite right, as the ball didn’t seem to have as much oomph as you anticipated.")
        input()
        print("The ball moves at a decent speed, hitting the soft target and letting out an unsatisfying ‘plump’ sound.")
        pc_speed = random.randint(40, 70)
        print("The display shows your speed, you threw the ball at a speed of {}".format(pc_speed))

        if pc_speed > 60:
            print("You nail the target, reaching the target speed of 60MPH")
            input()

            if holly_speed >= 60:
                print("Thankfully you came through and matched Holly, It would seem nobody gained bragging rights today.")

            elif holly_speed <= 60:
                print("You emerge victorious today, gaining bragging rights against Holly for the foreseeable future.")
            print("The vendor offers you a choice of any cheaply made stuffed animal he has.")
            print("Among them are a stuffed Fox, a stuffed German Shepard, and a stuffed Dragon.")
            input()
            pc_animal_choice = input("After thinking about it, you decide too pick the... (fox, german shepard, dragon").lower()

            if pc_animal_choice in ['fox']:
                print("You decide to pick the fox. Foreshadowing? Probably not. You just thought the fox looked the cutest.")

            elif pc_animal_choice in ['german shepard', 'g shep', 'german shep', 'shepard']:
                print("You pick the stuffed german shepard, it's coat is very similar to Sasha's, it's coat is primarily black with some tan.")

            elif pc_animal_choice in ['dragon']:
                print("You pick the dragon. You can never go wrong with a dragon.")

        elif pc_speed < 60:
            print("You gave it all you got but it just wasn’t enough to hit the target speed.")
            input()
            if holly_speed > 60:
                print("It would seem Holly is the victor today, holding bragging rights against you for the foreseeable future.")

            elif holly_speed < 60:
                print("It would seem nobody emerged victorious today. Not surprising given the awful chances. At least this way you’re both on even ground as far as bragging rights goes.")

        if CharInfo.festival_checks.festival_walk is True:
            print('"Well, the day is winding down, suppose we should start heading towards the parking lot. We might be able to see the fireworks on our way out."')
            input()
            CharInfo.player_info.player_location = festival_end.festival_ending_holly
            CharInfo.festival_checks.festival_game = True
            SaveSystem.save_sys.saving()
            self.festival_ending_holly()

        elif CharInfo.festival_checks.festival_walk is not True:
            CharInfo.festival_checks.festival_game = True
            print('"It’s getting pretty late, suppose we should go check out that one path before it’s too late."')
            input()
            CharInfo.player_info.player_location = festival_end.festival_walkway_holly
            SaveSystem.save_sys.saving()
            self.festival_walkway_holly()


    def festival_walkway_holly(self):
        print('"Didn’t see much when I went this way before, but who knows maybe something changed."')
        input()
        print("Indeed, the path to the east doesn’t seem to have much going on. You walk past the small stadium where various events have been held throughout the day. None of which interested you.")
        print('"I might have been interested in the derby, of course, that went on 3 hours ago, so…"')
        input()
        print('The only thing this path seems to offer is a nice walk. It loops around the stadium and will take you back to where you started.')
        input()
        print('"Seems like this would be a good time to talk. So, what do you do for fun? What are your hobbies?"')
        input()
        print("You tell Holly about your hobbies, which you find to be pretty uninteresting. Because, well, truth is your hobbies are a bit basic and boring. You enjoy movies, music, watching TV, and maybe playing video games or watching sports here and there. Among other things.")
        input()
        print('"I mean, sure, those are pretty basic things. I won’t lie about that. That’s not necessarily a bad thing though. In some cases, I’d say it can even be a positive. Since those interests are so common, it can make it easier for other people to relate to you. So long as you don’t let those hobbies become the only thing defining you, it’s fine. That’s when you become a basic bitch, or bastard. You definitely don’t have that problem, though."')
        input()
        print('"Ya know, I like a lot of the same stuff. Music, movies, all that. You already know about my art, and I also enjoy fishing on occasion."')
        print('"Guess I’m pretty ‘basic’ as well."')
        input()
        print("You also mention to Holly that you like traveling, though you rarely do so. You also mention that you’ve been thinking about going on a road trip around the country.")
        input()
        print('"That bit about the road trip seems pretty interesting… I’ve never thought about doing something like that before."')
        print('"Has to be a pretty big commitment though, right? You’re basically putting the rest of your life on pause for the duration of the trip."')
        print('"You’d almost have to be doing contract work like us or have some damn good vacation time."')
        input()
        print('You mention to Holly that that’s part of the reason you’d never really considered it until recently. There was no way to get that much time off when working at Syperion.')
        input()
        print('"It’s definitely a cool idea. What made you think of doing that anyway?"')
        input()
        print("You mention the Tiger you met on the bus. While you’ve given the idea of a road trip a passing thought before, it’s his first-hand account that has really driven your interest.")
        input()
        print('"Taking advice from a vagabond huh? Suppose there are worst things you could do. It’s not like your going to make ‘road tripping’ a lifestyle, right?"')
        if CharInfo.festival_checks.festival_game is not True:
            CharInfo.festival_checks.festival_walk = True
            print('"Anyway, looks like we\'re almost back at the start. Guess we can go check out those games real quick."')
            input()
            CharInfo.player_info.player_location = festival_end.festival_games_holly
            SaveSystem.save_sys.saving()
            self.festival_games_holly()
        elif CharInfo.festival_checks.festival_game is True:
            CharInfo.festival_checks.festival_walk = True
            print('"Well, I guess we\'ve done just about everything here."')
            print('"It\'s getting pretty late we should probably head towards the parking lot. We should be able to see the fireworks on our there."')
            input()
            CharInfo.player_info.player_location = festival_end.festival_ending_holly
            SaveSystem.save_sys.saving()
            self.festival_ending_holly()


    def festival_walkway_self(self):
        print("This way doesn’t seem to have much going on, as the only of interest is the small stadium where various events have been held throughout the day. None of which interested you.")
        input()
        print("Indeed, the only thing this path seems to offer is a nice walk. It loops around the stadium and will take you back to where you started.")
        print("Oh well, if nothing else you can reflect on the day while walking back.")
        input()
        print("The day has gone pretty well, you think. About the same as every other year you’ve went. The only thing that was different was running into Holly. Which was nice, but ultimately you just don’t really feel a connection with her, not like you used too anyway.")
        input()
        print("Actually, thinking back too it, you never got to say goodbye to Holly. Maybe you’ll run into her again and be able to say a proper goodbye.")
        input()
        print("Other than that the day has been pretty unremarkable. Just another average day.")
        input()
        print("You walk a bit more and eventually arrive back at the place you started. With nothing left to do you decide to head home and start walking towards the bus stop.")
        input()
        CharInfo.festival_checks.festival_walk = True
        CharInfo.player_info.player_location = festival_end.festival_ending_self
        SaveSystem.save_sys.saving()
        clear()
        self.festival_hub_end()


    def festival_ending_holly(self):
        print("After checking out everything the festival has to offer, you head back towards the entrance to watch the ending fireworks show.")
        input()
        print("It’s been a long and interesting day. You came here expecting to stay for an hour or two and then go home. But after talking to Holly you decided to stay.")
        print("You really feel like the relationship between you and her has strengthened today. You got to talk really in-depth about each other, just like in the old days.")
        input()
        print("You tell Holly that you’ve appreciated her company today, it’s been a while since you’ve been able to hang out with someone like you did today.")
        input()
        print('"I really enjoyed it too. It reminded me a lot of when we, ya know, actually saw each other on a regular basis."')
        input()
        print("You both lean on Holly’s car in the parking lot, watching the fireworks as the last bit of sun falls below the horizon, giving way to the stars and planets to light the night sky.")
        input()
        print("You feel serene, this day couldn't went any better. Hanging out with a friend at the end of the day doing some simple shit, it’s nice and relaxing. You wouldn’t trade it for anything.")
        input()
        print("The lightshow ends eventually, as all things do. And now it’s time to head back home.")
        input()
        print("'Suppose this is today, then. It’s been fantastic, it really has. The festival was alright but the real highlight was just being able to… get to know you again.'")
        input()
        print('"Hey, if you ever wanna do something like this again, you can hit this number up and let me know"')
        print("Holly shows you her number on her phone, you add it to your contacts.")
        input()
        print('"I’ll be seeing you, {}. I’m sure it’ll happen one way or another."'.format(CharInfo.player_info.name))
        input()
        print("You see goodbye to Holly and head back to the bus stop. What a great day.")
        input()
        print("You hop on the bus home and head up to bed.")
        input()
        clear()
        TravelSystem.travel_points.tp.remove('Lake Fest')
        CharInfo.festival_checks.festival_ending = True
        TravelSystem.travel_function.travel_point_early_bedroom()

    def festival_ending_self(self):
        print("After checking out everything the festival has to offer, you head back towards the entrance to watch the ending fireworks show.")
        input()
        print("It’s been a long and interesting day. You came expecting to stay for an hour or two and then go home. But after talking to Holly you decided to stay a bit longer.")
        print("You had some nice discussions with her but it didn’t really go much beyond that. There just wasn’t enough interest from either party.")
        input()
        print("Still, you can’t help but feel that maybe you missed out on something. It’s not everyday you get to try and rekindle a fading friendship.")
        print("Oh well, you can’t dwell on the past too much.")
        input()
        print("Speaking of Holly, you never did see her again. Shame you never got to say goodbye.")
        input()
        print("As you head through the parking lot and towards the bus stop, you spot Holly leaning on her car, watching the fireworks. Suppose it’s not too late for farewells after all.")
        input()
        print("You walk up to the car, waving at Holly as you approach.")
        input()
        print('"Huh, I figured you’d leave Lake Fest after the concert. Guess I’m wrong again."')
        print('"So, what’s up? Come to say your farewells?"')
        input()
        print("That’s what you had in mind, yes. Though thinking about it, you could watch the rest of the fireworks with Holly if you wanted.")
        festivalselfending= input("After thinking about it you decide to... (1): Just say goodbye to Holly. It’s been nice talking to her, but that’s as far you want it to go. \
              (2): Offer to stay and watch the fireworks with her. ").lower()

        if festivalselfending in ['1']:
            print('"Well, see ya. Been nice talking. Maybe we’ll run into each other again, what a coincidence that would be."')
            input()
            print("You head to the bus stop and hop on the bus home.")
            print("Once you get home you head up to bed. The day ending like any other.")
            input()
            clear()
            CharInfo.festival_checks.festival_ending = True
            TravelSystem.travel_points.tp.remove('Lake Fest')
            TravelSystem.travel_function.travel_point_early_bedroom()

        elif festivalselfending in ['2']:
            print('"Err, appreciate the offer but you’re a bit late, as I was just getting ready to leave."')
            input()
            print('"Been nice talking, maybe we’ll run into each other again, what a coincidence that would be."')
            print('You say goodbye to Holly, a bit surprised that she brushed you off.')
            input()
            print("It makes sense though, she probably figured that if you were serious about the friendship you probably would have stuck around after the concert.")
            input()
            print("You head to the bus stop and hop on the bus home.")
            print("Once you get home you head up to bed. The day ending like any other.")
            input()
            clear()
            CharInfo.festival_checks.festival_ending = True
            TravelSystem.travel_points.tp.remove('Lake Fest')
            TravelSystem.travel_function.travel_point_early_bedroom()

        else:
            print("Invalid input")
            return self.festival_ending_self()


festival_area = FestivalStart()

festival_end = FestivalEnd()

festival_mid = FestivalMid()
