# Festival area
import time
import CharInfo
import pickle
import teststoring
#  What if each file had it's own save system.


class GameState:  # Might have to put this in base because the import is causing all kinds of issues.
    def saving(self):
        print("Saving game")
        pickle_out = open('gamestate.pickle', 'wb')
        pickle.dump([teststoring.vinf], pickle_out)
        pickle_out.close()
        print("Game Saved!")
        self.playerlocation()

    def loading(self):
        print("Loading game")
        pickle_in = open('gamestate.pickle', 'rb')
        [teststoring.vinf] = pickle.load(pickle_in)
        pickle_in.close()
        print("Game Loaded!")
        self.playerlocation()

    def playerlocation(self):
        if CharInfo.player_info.player_location in ['Festival Start']:
            festival_area.festival_entrance()

class FestivalStart:
    def __init__(self):
        self.bus_ride_completed = False
        self.painting_purchase = ''

    def bus_ride(self):
        print("You hop on a bus headed to downtown. There’s a a special event today called Lake Fest, which hosts several vendors and activities.")
        input()
        print("While on the bus you sit next to a man with an ‘I heart NY shirt’ on. He’s carrying a sizable backpack and based on the apparel he’s wearing seems to be well-traveled.")
        print("The man looks to you and asks if you’re going to Lake Fest. You say yes, and that you’ve gone to it almost every year you’ve lived here.")
        input()
        print("'So you’re a local” the Tiger says. “I’m Chris.” The Tiger reaches out to shake your hand'")
        input()
        print("You shake the Tiger’s hand and introduce yourself as {}.".format(CharInfo.player_info.name))
        print("'Nice to meet you {}. I’m coming through here pretty much solely for Lake Fest. Though I wouldn’t be opposed to checking out some other places if you’ve got any recommendations. My hotel for here is booked for the day so I’ve got time.'".format(CharInfo.player_info.name))
        input()
        print("You can’t really think of anything else remarkable here. The town is actually quite boring. You offer a few eating recommendations, including Tories Café, stating that there really isn’t much to do here except check out the local restaurants.")
        input()
        print("'Yeah, I kind of figured. This is my second time going to this event and I’ve never really seen anything else to do.” The Tiger says with friendly tone.'")

        print("'Anyway, I bet you’re probably wondering why someone would come here just for one event.'")
        input()
        print("You can’t say you were really burning your brain trying to figure that out, but you’ll humor him.")

        print("'Well, I’m actually road tripping across the country! I do it every year, in some shape or form. Last year I went by train but this time I’m doing it by car.” He says with an enthusiastic tone. Clearly he’s quite interested in traveling the country.'")
        input()
        print("You ask Chris for some more details, you’ve always been fascinated by the idea of traveling the country, but you’ve just never had the time or money to do so.")
        input()
        print("'Well, I start off my trip on the east coast, in New York city as you might’ve guessed by my shirt.” He says while pointing to his 'I heart NY' shirt.'")

        print("'I spend a varying amount of time in each place I stop. Just depends on what that city has to offer, ya know?'")

        print("'The end destination changes every year. Last year I stopped at San Francisco, and this time around I’ll probably be heading to Seattle.'")
        input()
        print("You tell Chris that you’ve always been interested in doing something similar, you find the idea of traveling the country and seeing all it has to offer to be exciting!")
        input()
        print("'It’s a very rewarding experience. But it’s also a significant time commitment, and too be honest, it can be a bit tiring driving for hours on end. But the experiences and sights make it worth it. There really isn’t much else like it, expect maybe traveling the world. But that’s whole different ballgame.'")
        input()
        print("'If I could offer one tip, it's too plan ahead of time and check out what’s going to be going in the towns you’re passing by. Try to find the best possible time to leave so you can maximize the events you can go too'")

        print("You thank Chris for advice, if you ever do decide to take on such an endeavor, you’ll definitely make sure too have a plan.")
        input()
        print("'Well looks like our stop’s up here. It’s been great talking to you.” He says while extending his hand out for a farewell handshake.'")
        print("You shake his hands and say goodbye, he offers one last piece of advice before departing.")
        input()
        print("'Hey, if you ever decide to go for it, hit me up on Facebook. I’ve got a list of my favorite places to stop that I’d be glad to share'")

        print("You thank the Tiger as he goes on his way.")
        input()
        print("You have arrived at the festival")
        self.bus_ride_completed = True
        self.festival_entrance()

    def festival_entrance(self):
        CharInfo.player_info.player_location = 'Festival Start'
        print("You arrive at the festival and see crowds of people on the streets. Vendors as far as the eye can see.")

        print("The day is perfect for a festival, a light overcast keeps temperatures in the sun bearable, and a slight breeze keeps you cool.")
        input()
        print("You see rows of vendors directly ahead to your north, and the bus stop to travel home.")
        festivaldirection = input("What will you do? ")
        if festivaldirection in ['travel', 'home', 'bus', 'stop', 'bus stop']:
            #import TravelSystem
            #TravelSystem.travel_function.traveltofront()
        elif festivaldirection in ['north', 'vendors', 'festival', 'n']:
            print("You brave the crowd and head towards the main festival area.")
            self.festival_main()
        elif festivaldirection in ['save', 'save game']:
            save_sys.saving()




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
            # stuff here to check off painter
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
                self.painting_purchase = 'husky'
            elif painting_purchased in ['2']:
                self.painting_purchase = 'lake'
            elif painting_purchased in ['3']:
                self.painting_purchase = 'wraiths'
            elif painting_purchased in ['4']:
                print("You tell the painter that the prices were bit more then you hoping to pay.")
                input()
                print("'Understandable. If you change your mind you might try looking me up online.'")
                print("He hands you a business card and you part ways.")
                # Return somehow
            print('"Excellent! I’ll get it wrapped up and ready to go. You’ll be looking at bill of about $225."')
            input()
            print("You pay the painter and collect the painting.")
            CharInfo.player_info.money -= 225
            print("Your bank balance is now {}".format(CharInfo.player_info.money))











festival_area = FestivalStart()

save_sys = GameState()




