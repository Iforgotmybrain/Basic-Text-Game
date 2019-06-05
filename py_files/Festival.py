# Festival area
import time
import CharInfo
import TravelSystem
import SaveSystem


class FestivalStart:
    def __init__(self):
        self.bus_ride_completed = False
        self.painting_purchase = ''

    def bus_ride(self):
        if CharInfo.festival_checks.bus_ride_complete is not True:
            print(
                "You hop on a bus headed to downtown. There’s a a special event today called Lake Fest, which hosts several vendors and activities.")
            input()
            print(
                "While on the bus you sit next to a man with an ‘I heart NY shirt’ on. He’s carrying a sizable backpack and based on the apparel he’s wearing seems to be well-traveled.")
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
                "'Yeah, I kind of figured. This is my second time going to this event and I’ve never really seen anything else to do.” The Tiger says with friendly tone.'")

            print("'Anyway, I bet you’re probably wondering why someone would come here just for one event.'")
            input()
            print("You can’t say you were really burning your brain trying to figure that out, but you’ll humor him.")

            print(
                "'Well, I’m actually road tripping across the country! I do it every year, in some shape or form. Last year I went by train but this time I’m doing it by car.” He says with an enthusiastic tone. Clearly he’s quite interested in traveling the country.'")
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
                "You tell Chris that you’ve always been interested in doing something similar, you find the idea of traveling the country and seeing all it has to offer to be exciting!")
            input()
            print(
                "'It’s a very rewarding experience. But it’s also a significant time commitment, and too be honest, it can be a bit tiring driving for hours on end. But the experiences and sights make it worth it. There really isn’t much else like it, expect maybe traveling the world. But that’s whole different ballgame.'")
            input()
            print(
                "'If I could offer one tip, it's too plan ahead of time and check out what’s going to be going in the towns you’re passing by. Try to find the best possible time to leave so you can maximize the events you can go too'")

            print(
                "You thank Chris for advice, if you ever do decide to take on such an endeavor, you’ll definitely make sure too have a plan.")
            input()
            print(
                "'Well looks like our stop’s up here. It’s been great talking to you.” He says while extending his hand out for a farewell handshake.'")
            print("You shake his hands and say goodbye, he offers one last piece of advice before departing.")
            input()
            print(
                "'Hey, if you ever decide to go for it, hit me up on Facebook. I’ve got a list of my favorite places to stop that I’d be glad to share'")

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
        festivaldirection = input("What will you do? ")
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
        time.sleep(1)
        print("You can see stands for everything from spices to graphic tees. The quaint downtown streets filled with folks from every part of the state, and country for that matter.")
        input()
        print("Initially you don’t see any vendors that catch your eye, though as you go walk further you do find a couple of places you wouldn’t mind checking out.")
        input()
        print("One is a painter; their stand features a host of beautiful oil paintings of various subjects and locations.")
        time.sleep(1)
        print("The second is a wood sculptor, he has various objects depicted in wood for sale.")
        time.sleep(1)
        print("And finally, the third is a novelty t-shirt and hat seller. You know, the kind that has hats with a big ass weed leaf and Snoop Dogg on them. You know what I’m talking about.")
        festival_vendor = input("Which one do you want to check out? ")
        if festival_vendor in ['paint', 'painter', 'oil painting','painting']:
            self.vendor_painting()


    def vendor_painting(self):
        print("You walk up to the painters stand, you see works ranging from beautiful mountain landscapes to tasteful nude works, separately featuring a horse and a vixen. He has a very diverse set of paintings.")
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

            print("''For example, the piece with the vixen will run you about $250. The one of the ocean beach, about $200")
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
            (4) None".lower())
            if painting_purchased in ['1']:
                CharInfo.GlobalCheckFestival.painting_purchase = 'husky'
            elif painting_purchased in ['2']:
                CharInfo.GlobalCheckFestival.painting_purchase = 'lake'
            elif painting_purchased in ['3']:
                CharInfo.GlobalCheckFestival.painting_purchase = 'wraiths'
            elif painting_purchased in ['4']:
                print("You tell the painter that the prices were bit more then you hoping to pay.")
                input()
                print("'Understandable. If you change your mind you might try looking me up online.'")
                print("He hands you a business card and you part ways.")
                return self.festival_main()
            print('"Excellent! I’ll get it wrapped up and ready to go. You’ll be looking at bill of about $225."')
            input()
            print("You pay the painter and collect the painting.")
            CharInfo.GlobalCheckFestival.festival_item_purchased = True
            CharInfo.player_info.money -= 225
            print("Your bank balance is now {}".format(CharInfo.player_info.money))

    def wooden_vendor(self):
        print("You decide to check out the wood sculptor’s booth.")
        print("Looking at their wares, you see numerous objects made out of wood. There’s a wooden boat, dozens of boxes all in different shapes and sizes, and even a small, ‘model’ tree trunk made out of… wood.")
        input()
        print("You can see a few things you wouldn’t mind taking home, including one of the smaller boxes, and a wooden plane model depicting an SR-71.")
        print("You decide to ask the seller how much the items are.")
        input()
        print('"The box would be $45, and the plane is about $300"')
        input()
        wooden_choice = input("After thinking about it, you decide to… (1): Purchase the box (2): Purchase the plane \
              (3): Purchase nothing")
        if wooden_choice in ['1']:
            CharInfo.GlobalCheckFestival.festival_item_purchased = True
            CharInfo.GlobalCheckFestival.wooden_sculpture = 'box'
            print('"Excellent choice, I’ll get that ready to go for you."')
            print("You pay the vendor $45 and receive the wooden box")
            CharInfo.player_info.money -= 45
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            #return
        elif wooden_choice in ['2']:
            CharInfo.GlobalCheckFestival.festival_item_purchased = True
            CharInfo.GlobalCheckFestival.wooden_sculpture = 'plane'
            print("A fantastic choice, that’s one of my favorite items I have for sale!")
            input()
            print("The vendor bags the item and you pay him $300.")
            print("You receive the model plane.")
            input()
            CharInfo.player_info.money -= 300
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            #return
        elif wooden_choice in ['3']:
            print("Okay, that's fine. If you change your mind I'll be here.")
            input()
            return self.festival_main()

    def trashy_vendor(self):
        print("You decide to visit the t-shirt vendor.")
        print("This booth sells graphic tees, and the finest of bootleg snap-back hats. The shirts are $15 and the hats are $20")
        input()
        print("The T-shirts mostly have some form of meme or pop culture reference on them. You can see a T-shirt with Heath Ledger’s joker on it, with the caption ‘why so serious?’. You also see a T-shirt with the oh-so popular game Fortnite on it, the shirt has picture of the game’s iconic llama with the caption ‘eat, sleep, Fortnite, repeat’.")
        input()
        print("The hats mostly have popular sports teams on them, with the Yankees easily being the most common one. They also have a hat with weed leaf on the front, and the number 420 on the bill.")
        input()
        print("You’re not really interested in any of this vendor’s merchandize, since most of it is either trashy, of dubious quality, or will end up being outdated in a months’ time.")
        input()
        print("But, if you had to choose ''something'', you think you would pick…")
        trashy_vendor = input("(1): The shirt with Snoop Dogg and weed references on it, no way in hell are you going to wear it, but it might make a good gag gift someday. \
            (2): The bootleg NY Yankees hat. You don’t really like the Yankees, or snap-back hats, but odds are you know someone who does. It might come in handy as a gift someday.\
            (3): An absurdly outdated meme shirt that has the troll face on it. Much like the Snoop Dogg shirt, you probably aren’t going to wear, but you might wear it in jest, or give it away as a gag gift.\
            (4) Nothing")
        if trashy_vendor == '1':
            print("You take the Snoop Dogg shirt and bring it to the vendor.")
            input()
            print("The vendor is a 30-something alligator. He seems to be chewing tabaco, and his shirt is stained from standing outside in the heat all day.")
            input()
            print('"Let’s see, a t-shirt? That’ll be $15."')
            print('"Hah, the Snoop Dogg one is probably of my favorites. It’s surprisingly popular as well."')
            input()
            print("You hand the alligator $15 and receive the shirt.")
            CharInfo.GlobalCheckFestival.festival_item_purchased = True
            CharInfo.GlobalCheckFestival.trash_vendor = 'snoop'
            CharInfo.player_info.money -= 15
            print("Your bank balance is now {}".format(CharInfo.player_info.money))
            #return

        elif trashy_vendor == '2':
            print("You grab the bootleg hat and take it to the vendor.")
            input()
            print("The vendor is a 30-something alligator. He seems to be chewing tabaco, and his shirt is stained from standing outside in the heat all day.")
            input()
            print('"Hmm, let’s see… A hat? That’ll be $20."')
            input()
            print("You hand the alligator $20 and receive the hat.")
            CharInfo.GlobalCheckFestival.festival_item_purchased = True
            CharInfo.GlobalCheckFestival.trash_vendor = 'hat'
            CharInfo.player_info.money -= 20
            print("Your bank balance is now {}".format(CharInfo.player_info.money))

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
            CharInfo.GlobalCheckFestival.festival_item_purchased = True
            CharInfo.GlobalCheckFestival.trash_vendor = 'troll'
            CharInfo.player_info.money -= 8
            print("Your bank balance is now {}".format(CharInfo.player_info.money))

        elif trashy_vendor == '4':
            print("You just cannot imagine buying anything here.")
            input()
            print("You leave the booth.")
            input()
            return self.festival_main()

class FestivalMid:


festival_area = FestivalStart()



