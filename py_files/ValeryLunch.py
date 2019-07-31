import os
import sys
import CharInfo
import TravelSystem
import SaveSystem
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class ValeryLunchStart:
    def __init__(self):
        self.pc_meal_choice = ''
        self.val_question_complete = ''


    def valery_lunch_intro(self):
        CharInfo.valery_checks.valery_date_points = 0
        CharInfo.valery_checks.valery_heart_to_heart = False
        print("The weekend is finally here, and with it comes the various outings that you’ve been expecting.")
        input()
        if CharInfo.player_info.ending_points <= -4:
            print("Today you’ll be going to get lunch with Valery, you’re a bit nervous about the whole thing but it’ll probably work out fine.")
            input()

        elif CharInfo.player_info.ending_points >= -4:
            print("Today you’ll be going to get lunch with Valery. It should be nice to get to know him a bit better.")
            input()

        if CharInfo.holly_checks.holly_relationship_status in ['dating']:
            print("You also have a date with Holly tomorrow, guess this weekend is quite busy.")
            input()

        print("Pretty much the only thing you have going on today is the lunch with Valery, so you’ll probably just end up hanging around the house until lunch.")
        input()
        clear()
        print("A couple of hours pass and before you know It it’s time to head out to The Rat’s Place for lunch. You finish up the video you were watching on the computer and head to your car to drive to the restaurant.")
        input()
        CharInfo.player_info.player_location = val_lunch.valery_lunch_rats_start
        clear()
        SaveSystem.save_sys.saving()

    def valery_lunch_rats_start(self):
        print("You arrive about 10 minutes before 12, you always like to give yourself some extra time.")
        input()
        print("Seems like Valery hasn’t gotten here yet; you’ll have to wait around a bit and see if he shows up. If not you’ll just head in and get a table.")
        print("It takes a couple more minutes for Valery to finally arrive, as he pulls into the parking lot you exit your car and head towards the entrance of the restaurant.")
        input()
        print("The Rat’s Place is situated just off the lake, the building itself is painted in a light blue color, with white accents. The side facing the lake is made almost entirely of glass, offering a spectacular view.")
        print("And according to a plaque mounted near the seating area, the restaurant is named after a set of critically acclaimed movies, called “The Rat Movies”.")
        input()
        print("You enter the restaurant and wait for Valery to make his way in, he ends up arriving very shortly after you.")
        print("“Hello there, {}. I’ve been looking forward to this lunch all week!”".format(CharInfo.player_info.name))
        input()
        print("You tell Valery you have as well, it’s always good to try and get to know new people.")
        input()
        print("“This place just lets you pick your own seat, so we can just head over here and sit at one of these tables.”")
        print("You follow Valery to the table, it would seem that the table he picked is on the lakeside of the restaurant, the mostly glass wall lets you as far out as the horizon!")
        input()
        print("“We got pretty lucky, these are some of the best seats here. Most of the time they’re taken.”")
        input()
        print("(1): You’ve been here before?")
        print("(2): It’s a damn nice view for sure.")
        print("(3): Not bad, but nothing I haven’t seen 100 times.")
        view_dialogue = input("Select a dialogue choice, 1, 2, or 3 ")

        if view_dialogue in ['1']:
            print("“Yup! Quite a few times actually. I might have just moved into the area, but I’ve been traveling up here for quite some time.”")
            print("“But that’s a story for another time. We should probably focus on just getting our food and drinks ordered for now.”")
            input()
            CharInfo.valery_checks.valery_date_points += 2

        elif view_dialogue in ['2']:
            print("“There’s pretty much nothing like it. Like an ocean of freshwater.”")
            input()
            CharInfo.valery_checks.valery_date_points += 2

        elif view_dialogue in ['3']:
            print("“Doesn’t make it any less impressive. At least to me, anyway.”")
            input()
            CharInfo.valery_checks.valery_date_points -= 2

        else:
            print("Invalid input")
            self.valery_lunch_rats_start()

        print("You and Valery sit down at your table and await the waiter to take your order.")
        input()
        print("“Y'know, this restaurant is probably one of the more unique ones along the lake. Had to have cost a fair bit of money to make this monster of a glass wall.”")
        print("""Just think of the engineering they had to do get it to work, you have to make sure the glass is tempered and fairly thick, or else it’ll be destroyed in one hailstorm.""")
        print("""And you've gotta factor in the fact that its probably going to have to be cleaned pretty often...""")
        input()
        print("“Sorry, was starting to go on a bit of tangent there. I’m an engineer so stuff like that kind of makes me geek out a bit.”")
        input()
        while True:
            print("(1): I can definitely understand rambling on about stuff you're passionate about")
            print("(2): How long have you been an engineer?")
            print("(3): Cool, I get it, you’re an engineer.")
            val_glass = input("Pick a dialogue choice ")

            if val_glass in ['1']:
                print(
                    "“Sure, but I have tendency to take it a bit too far. Guess that’s just how it is with most people’s passion”")
                input()
                break

            elif val_glass in ['2']:
                print(
                    "“4 years! That’s how long I’ve been out of college as well. Went to Redding State University and got my bachelor’s degree there.“")
                input()
                print(
                    "I was actually lucky enough to get a job right out the gate, so yeah, I've been working as an engineer for 4 years.")
                input()
                break

            elif val_glass in ['3']:
                print(
                    "“Oh. Uh, sorry if it came off as bragging. Was just trying to explain why I was so interested in that particular wall…”")
                input()
                CharInfo.valery_checks.valery_date_points -= 6
                break

            else:
                print("Invalid input")

        print("“Anyway, don’t know if you’ve been here before, but the BBQ here is fantastic. I got the pulled pork sandwich last time I was here, and it was perfect”")
        input()
        print("You tell Valery you appreciate the recommendation, although ultimately, it’s up to you to decide what you want.")
        print("The waitress arrives shortly after the two of you sit down, giving you your menus and asking what the two of you want to drink. You order a soft drink and Valery orders iced tea.")
        input()
        print("She seemed to be familiar with Valery, as she remarked how he finally brought someone with him to eat.")
        print("“Heh, guess I come here a bit too often if the staff are recognizing me.”")
        input()
        print("(1): Bit sad, isn’t it?")
        print("(2): Guess it’s a pretty good restaurant if you come here that often")
        print("(3): How often do you actually come here?")
        print("(4): I wonder what they think of you, given how often you’re here.")
        val_restaurant_freq = input("Pick a dialogue option ")

        if val_restaurant_freq in ['1']:
            print("“Makes me worry a bit about how much time I waste here, I don’t really see it as ‘sad’ though”")
            print("“I mean come on, people have favorite restaurants, they have places they like to go too. There’s nothing wrong with that.”")
            CharInfo.valery_checks.valery_date_points -= 2
            CharInfo.player_info.ending_points -= 2
            input()

        elif val_restaurant_freq in ['2']:
            print("“Hah, I think it’s more of the atmosphere that I enjoy here rather than the food. But the food is actually pretty good.”")
            print("“I do come here pretty often though, almost every lunch break I either carry-out, or stay here and eat if I have the time”")
            input()
            print("“Since moving here I’ve been pretty lonely. So going to this place and having lunch just sort of me makes feel more… Connected? I guess you would say.”")
            print("“Makes me feel less isolated, at least.”")
            CharInfo.valery_checks.valery_date_points += 4
            CharInfo.player_info.ending_points += 2
            input()

        elif val_restaurant_freq in ['3']:
            print("“Ehh, probably 5 times a week? A decent amount for sure, but it’s not like I spent all my time here.”")
            print("“I enjoy the atmosphere and the feeling of familiarity. I also like that it gives me the opportunity to just be around people.”")
            input()
            print("“I don’t really know anyone else here, so it’s not like I can get together with someone. No significant other, and none of coworkers really get along with me.”")
            print("“So yeah, it can get a bit a lonely. Going here just sort of, helps me feel connected.”")
            CharInfo.valery_checks.valery_date_points += 4
            CharInfo.player_info.ending_points += 2
            input()

        elif val_restaurant_freq in ['4']:
            print("“The hell are you talking about? Come on dude just because they recognize me doesn’t mean they think I’m some sort of no-life loser.”")
            input()
            if CharInfo.valery_checks.valery_date_points == -8:
                print("“Honestly feels like you’re just being a prick for no reason.”")
                print("“Come on dude if you didn’t want to come you could have just said no. If you keep going after me, I’m out.”")
                CharInfo.valery_checks.valery_date_points -= 8
                CharInfo.player_info.ending_points -= 6
                input()

            elif CharInfo.valery_checks.valery_date_points != -8:
                print("No need to be a prick.")
                CharInfo.valery_checks.valery_date_points -= 8
                CharInfo.player_info.ending_points -= 6
                input()
        else:
            print("Invalid input")
            self.valery_lunch_rats_start()

        print("You and Valery look over the menu, most of the items are seafood or barbecue related.")
        input()
        print("You see a few things that catch your eye, including the ribs and the grilled salmon.")
        print("You’ve still got time to choose so you’ll look over the menu some more.")
        input()
        if CharInfo.valery_checks.valery_date_points >= 2:
            print("“Think I’ll go for something I haven’t had yet, the perch sandwich. “")
            input()
            print("“Y’know, looking over this menu gave a thought. Imagine how different society would be if things like ribs were made from actual pig?")
            print("“Obviously that was kind of a thing back in the dark ages, but nowadays we can just make these crazy synthetic ribs out of plants and stuff.”")
            input()
            print("“If nothing else, we’d have one fucked up class structure that’s for sure.”")
            input()
            print("You’ve never really given that topic much thought, though now that Valery brings it up, the entire world would likely be radically different if the eating of sapient species weren’t outlawed back in the 1700s.")
            input()
        CharInfo.player_info.player_location = val_lunch.valery_lunch_rats_mid
        clear()
        SaveSystem.save_sys.saving()
        self.valery_lunch_rats_mid()

    def valery_lunch_rats_mid(self):
        print("Well, the waitress should be here anytime to take your order, guess you better decide what you want.")
        input()
        print("You decide to pick the...")
        print("(1): The ribs")
        print("(2): The grilled salmon")
        print("(3): The pulled pork sandwich")
        player_meal_choice = input("Pick your meal, 1, 2, or 3 ")

        if player_meal_choice in ['1']:
            print("You decide to go with the ribs, according to Valery they should be pretty good.")
            self.pc_meal_choice = 'ribs'
            input()

        elif player_meal_choice in ['2']:
            print("You pick the grilled salmon. You’ve had salmon before, but never grilled. Might as well try it out now.")
            self.pc_meal_choice = 'grilled salmon'
            input()

        elif player_meal_choice in ['3']:
            print("With how good Valery says their barbeque is, the pulled pork sandwich should be great.")
            self.pc_meal_choice = 'pulled pork sandwich'
            input()

        else:
            print("Invalid input")
            self.valery_lunch_rats_mid()

        print("Sure enough, shortly after picking your meal the waitress comes to your table asks’ if you’re ready to order.")
        input()
        print("“I’ll have the perch sandwich” Valery says to waitress.")
        print("“And I’ll just take the fries that come with it.”")
        input()
        print("You tell the waitress you’ll take the {}. And that you’re fine with the sides that come with it.".format(self.pc_meal_choice))
        input()
        print("“Alright I’ll get these order right in, just let me know If you need anything else.” The waitress says as she finishes taking your orders.")
        input()
        print(
            "While you wait for your food to arrive, you should have plenty of time to get to know Valery a bit better.")
        input()
        clear()
        CharInfo.player_info.player_location = val_lunch.val_questions_rats
        self.val_questions_rats()

    def val_questions_rats(self):
        print("You decide to ask Valery...")
        print("(1): About his fairly unusual name (For a dude)")
        print("(2): Why he decided to move here.")
        print("(3): How long he’s been coming to iridium City")
        print("(4): What his hobbies are.")
        print("(5): Just ignore him until dinner arrives.")
        if self.val_question_complete is True:
            print("(6) That's enough questions for now. ")
        val_get_to_know = input("What will you ask Valery? (You can come back and ask other questions.) ")

        if val_get_to_know in ['1']:
            print("You ask Valery about his name, stating that Valery is a fairly unusual name for a guy.")
            input()
            print("“You're right, it is quite a different name. I actually hated it through my adolescence, but with time I started to like it a bit more.”")
            input()
            print("“I believe my parents told me they named me after a scientist or something.”")
            print("“It’s been awhile since I asked them though so I could be misremembering.”")
            input()
            print("(1): Well I think it’s a very fitting name for you!")
            print("(2): So long as you’re happy with your name I guess that’s all that matters.")
            print("(3): If I were you, I’d have probably already changed my name by now.")
            val_name_choice = input("Pick your response ")

            if val_name_choice in ['1']:
                print("“Aw, thanks. It’s not often I get a compliment on my name.”")
                print("“Most people just think it’s weird. Sometimes they’ll come right out and say it, but usually you can just infer what they’re thinking.”")
                input()
                print("“Weird looks are pretty much all I have to deal with nowadays, thankfully. Back in high school and middle school I’d always get picked on because of my more feminine name…”")
                input()
                print("“But thankfully most people I meet now are decent enough to not hate me just based off of my name.”")
                CharInfo.valery_checks.valery_date_points += 8
                CharInfo.player_info.ending_points += 4
                self.val_question_complete = True
                input()
                SaveSystem.save_sys.saving()
                clear()
                self.val_questions_rats()

            elif val_name_choice in ['2']:
                print("“I suppose so. The weird looks I get from people when I tell them my name is Valery can be a bit harsh at times, but I can deal with it.”")
                input()
                print("“People just outright disliking me because of my more feminine name hurts though, thankfully that hasn’t really been a problem since my high school and middle school years.”")
                print("“Most people are decent enough to not dislike me just because of my name, thankfully.”")
                CharInfo.valery_checks.valery_date_points += 2
                CharInfo.player_info.ending_points += 2
                self.val_question_complete = True
                input()
                SaveSystem.save_sys.saving()
                clear()
                self.val_questions_rats()

            elif val_name_choice in ['3']:
                print("“Can’t change your name until your 18. And at that point my name was just part of who I was.”")
                print("“Besides, at 18 my worst years were behind me. I was done with high school, and middle school was becoming a distant memory.”")
                input()
                print("“Just didn’t make sense to change my name because a few people I didn't even care about hated it.”")
                CharInfo.valery_checks.valery_date_points -= 2
                self.val_question_complete = True
                input()
                SaveSystem.save_sys.saving()
                clear()
                self.val_questions_rats()

            else:
                print("Invalid input")
                self.val_questions_rats()

        elif val_get_to_know in ["2"]:
            print("You ask Val about why he decided to move to Iridium City.")
            input()
            print("“Well that’s pretty simple, I moved here for work”")
            print("“It was a pretty easy choice, I loved the area, and the pay and benefits for job were good, so I jumped on it.”")
            input()
            while True:
                print("(1): So where do you work?")
                print("(2): What do you love so much about Iridium City? You seem to be quite attached to it.")

                if CharInfo.player_info.ending_points <= -4 or CharInfo.valery_checks.valery_date_points <= -4:
                    print("(3): Cool, that’s enough. I don’t want to hear your whole life story.")

                else:
                    print("(3): Cool story, let's change the subject.")

                    val_work_question = input("Pick a response ")

                    if val_work_question in ['1']:
                        print(
                            "“I actually work for the city! Might not be the most prestigious work, but it’s good enough for me.”")
                        print(
                            "“Plus, it’s really cool having a job where you can make a big impact on the community. You don’t get that at a lot of places.”")
                        input()
                        print(
                            "You can definitely appreciate Valery’s comments on having satisfying work. The mundane and unimpactful nature of your previous job at Syperion was a big reason why you left.")
                        CharInfo.valery_checks.valery_date_points += 2
                        self.val_question_complete = True
                        input()

                    elif val_work_question in ["2"]:
                        print(
                            "“I guess I just really like being by the lake. Just the whole atmosphere of the town is great, there's nothing else like it.”")
                        self.val_question_complete = True
                        input()


                    elif val_work_question in ['3']:
                        if CharInfo.valery_checks.valery_date_points <= -16:
                            print(
                                "“Okay, I’ve had it. You’ve been a total asshole this whole time for no damn reason.”")
                            print(
                                "“If you didn’t want to come out for lunch you could have just said no, but instead you come out here and purposely fuck around.”")
                            input()
                            print(
                                "“I’m finished here, I’m not letting you push me around. Have fun paying for the bill, fucking dick.”")
                            input()
                            print("This scene can't be finished until I get towards the end.")
                            input()
                            break  # Fix this later

                        elif CharInfo.player_info.ending_points <= -4 or CharInfo.valery_checks.valery_date_points <= -4:
                            print("“No need to be a dick about it. Could have just changed the subject…”")
                            input()
                            CharInfo.valery_checks.valery_date_points -= 4
                            self.val_question_complete = True
                            self.val_questions_rats()
                            break

                        else:
                            pass

                        self.val_question_complete = True
                        self.val_questions_rats()
                        break


        elif val_get_to_know in ["3"]:
            print("“I’ve been coming up here for around 7 years! Of course, I haven’t lived here until very recent.”")
            input()
            while True:
                print("(1): What made you start visiting the city?")
                print("(2): How do you feel about living in the city so far?")
                if CharInfo.player_info.ending_points <= -6 or CharInfo.valery_checks.valery_date_points <= -6:
                    print(
                        "(3): I’m gonna stop you right there. I don’t want to hear your whole story leading up to this day.")
                    input()
                else:
                    print("(3): Interesting, but I wanna ask you about something else.")
                val_city_question = input("Pick a response ")

                if val_city_question in ['1']:
                    print(
                        "“The Lake Festival! One of friends was going and asked if I wanted to go. I said sure and ended up loving the festival and the city.”")
                    print("“Since then I’ve been to just about every festival here. And I make… well, made, a couple of my own trips every year.”")
                    input()
                    print("“Don't really need to make trips to here since I moved, right?”")
                    input()
                    self.val_question_complete = True

                elif val_city_question in ['2']:
                    print("“I’m gonna be honest, it’s been a bit underwhelming. Not the city itself so much, but just… the overall experience.”")
                    input()
                    print("“You know how it can be. Before you even start doing something you think about how everything’s going to go.”")
                    print("“You plan it all out, think about how great things are going to be. Then you actually get to the real thing and… it just doesn’t go the way you were expecting.”")
                    input()
                    print("(1): What exactly hasn't gone to plan?")
                    if CharInfo.player_info.ending_points <= -6 or CharInfo.valery_checks.valery_date_points <= -6:
                        print("(2): That’s just how it goes, too bad. Let’s move onto something else.")
                    else:
                        print("(2): I get it. Let’s talk about something else.")

                    val_moving_dialogue = input("Pick a response")

                    if val_moving_dialogue in ['1']:
                        print("“I don’t know If I’d say, “hasn’t gone to plan” it’s more not having expectations met.”")
                        print("“Really I’ve just been a bit underwhelmed with my social life here.”")
                        input()
                        print("“Guess that’s to be expected with moving into a town where you don’t know anybody. Doesn’t really make it any easier though.”")
                        input()
                        print("(1): Well, you’ve got me to lean on, at least.")
                        print("(2): It can be a hard adjustment, you’ve gotta do your best to put yourself out there and meet new people.")
                        if CharInfo.player_info.ending_points <= -6 or CharInfo.valery_checks.valery_date_points <= -6:
                            print("(3): Reality is often disappointing. It’s not my problem so let’s talk about something else.")
                        else:
                            print("(3): Not everything goes to plan. You’ll just have to figure out a way to deal with it.")
                        val_social_response = input("Pick a response")

                        if val_social_response in ['1']:
                            print("“Heh, I uh, didn’t expect you to say something like that.”")
                            input()
                            if CharInfo.valery_checks.valery_date_points >= 12:
                                print(
                                    "“You’re right, though. Might seem a bit sad, but you’re the closest thing I have to a friend in this town.”")
                                print(
                                    "“I really do appreciate how welcoming you’ve been to me. As you've probably guessed not everyone has been so gun-ho about getting to know me.”")
                                input()
                                print(
                                    "“And with how well I’ve gotten along with you, it’s really helped me feel at home. "
                                    "So thank you, it's been a long time since I've felt this way when hanging out with someone.”")
                                input()
                                print(
                                    "“Anyway, that’s enough feely stuff for now, let’s talk about something else before I choke up.”")
                                input()
                                CharInfo.valery_checks.valery_date_points += 4
                                CharInfo.player_info.ending_points += 2
                                CharInfo.valery_checks.valery_heart_to_heart = True
                                self.val_questions_rats()

                            else:
                                print("“I do appreciate you saying that, though. I suppose you are the closest thing I’ve got to a friend here.”")
                                input()
                                print("Just, uh, I probably won’t actually be leaning on you. No offence.")
                                input()
                                CharInfo.valery_checks.valery_date_points += 4
                                CharInfo.player_info.ending_points += 2
                                CharInfo.valery_checks.valery_heart_to_heart = False
                                self.val_questions_rats()

                        elif val_social_response in ['2']:
                            print("“I know, and I’ve been trying. It’s the main reason I invited you out to lunch, after all.”")
                            print("“The hardest part is just finding those people. You see someone at work, on the street or wherever, and you don’t anything about them. You don’t know how they’re going to react when you talk to them.”")
                            input()
                            print("“You don’t know if you even have any shared interests, we might end up being complete opposites. It can be really intimidating.”")
                            input()
                            print("You ask Valery if he has tried finding friends in groups or clubs he's be interested in.")
                            input()
                            print("“I’ve definitely thought about it, but I usually end up not checking them out for similar reasons. It’s intimidating going to those meetups when you don’t know anyone.”")
                            print("“Those groups or clubs probably already have their own cliques set up, and I’d just end up feeling like the odd one out.”")
                            input()
                            print("“Anyway, I think that’s enough talking about my problems. Let’s talk about something less depressing.”")
                            input()
                            CharInfo.valery_checks.valery_date_points += 6
                            CharInfo.player_info.ending_points += 4
                            self.val_question_complete = True
                            self.val_questions_rats()

                        elif val_social_response in ['3']:

                            if CharInfo.player_info.ending_points <= -6 or CharInfo.valery_checks.valery_date_points <= -6:
                                CharInfo.valery_checks.valery_date_points -= 8
                                CharInfo.player_info.ending_points -= 6

                                if CharInfo.valery_checks.valery_date_points <= -16:
                                    print("It might not be your problem but showing a little kindness wouldn't kill you, asshole.")
                                    input()
                                    print("Honestly, you've been a real fucking prick this whole time, but this is probably the most upset I've been over it.")
                                    print("I open my heart to you and you just tell me you don't care. If you didn't give a shit about me you could have just declined to come to lunch.")
                                    input()
                                    print("But instead you decide to come here and insult me over and over again. You're a real piece of work, {}.")
                                    print("I'm out of here. Enjoy paying for the whole meal, dick.")
                                    input()
                                    self.val_question_complete = True
                                    break

                                elif CharInfo.valery_checks.valery_date_points <= -8:
                                    print("Okay dude, I like you but if you keep pushing me around I'm not sticking around.")
                                    input()
                                    self.val_question_complete = True
                                    self.val_questions_rats()
                                    break

                                else:
                                    print("Fine. It's not like I wanted to talk about my feelings or anything.")
                                    self.val_question_complete = True
                                    self.val_questions_rats()
                                    break
                            else:
                                print("“I guess so. Hopefully I’ll figure everything out with time.”")
                                self.val_question_complete = True
                                self.val_questions_rats()


                    elif val_moving_dialogue in ['2']:
                        self.val_question_complete = True
                        pass

                elif val_city_question in ['3']:
                    print("")

        elif val_get_to_know in ["4"]:
            print("You ask Val what some of his hobbies are.")
            print("“My hobbies? Well, I enjoy playing video games quite bit, I’ve also been messing around with the piano recently.”")
            input()
            print("“I’m not any good at it, but it’s been fun learning. I’m also pretty big into cars.”")
            input()
            while True:
                print("(1): Video games? Have a favorite game or system?")
                print("(2): How long have you been trying to play the piano?")
                print("(3): Cars, huh? Do you track?")
                if CharInfo.player_info.ending_points <= -4:
                    print("(4): Could you be any less interesting?")
                else:
                    print("(4): Cool, let's talk about something else.")
                val_hobbies_response = input("Pick a response")

                if val_hobbies_response in ['1']:
                    print("“Well I mostly play on PC and asking what my favorite game is… that’s a bit of a difficult question.”")
                    input()
                    print("“Let’s see… I loved New Vegas, but Fallout 3 was one of my first introductions to open world games, there’s a lot of nostalgia there.”")
                    print("“And then you have games I loved as a kid, like Hot Pursuit 2 and Animal Crossing…”")
                    input()
                    print("“Damn dude this is a loaded question. I guess I’ll go with animal Crossing. I’m gonna have to think on this a bit more later though…”")
                    input()
                    self.val_question_complete = True
                    CharInfo.valery_checks.valery_date_points += 2

                elif val_hobbies_response in ['2']:
                    print("“Only a couple of months. Up until that point I'd never played an instrument before and decided I was finally going to take a swing at it.”")
                    input()
                    print("“It’s gone pretty well. I’m still a long way off from being decent, but I’m improving every month.”")
                    print("“Maybe someday I’ll be good enough to form a band and quit being an engineer, hah.”")
                    input()
                    self.val_question_complete = True
                    CharInfo.valery_checks.valery_date_points += 2
                      # Should I clear before returning?

                elif val_hobbies_response in ['3']:
                    print("“No, haven’t really thought about doing that. I think the nearest track is like 2 hours away so it’d be a bit out of the way.")
                    print(" “I mainly just follow stuff online, gawk at any cool cars I see on the street. Stuff like that.”")
                    input()
                    print("Guess that kind of makes me a casual car enthusiast. Oh well.")
                    input()
                    self.val_question_complete = True


                elif val_hobbies_response in ['4']:

                    if CharInfo.player_info.ending_points <= -4:
                        print("“Could you be any more of a dick?”")
                        CharInfo.valery_checks.valery_date_points -= 6

                        if CharInfo.valery_checks.valery_date_points <= -16:
                            print(
                                "“Okay, I’ve had it. You’ve been a total asshole this whole time for no damn reason.”")
                            print(
                                "“If you didn’t want to come out for lunch you could have just said no, but instead you came here and purposely fucked around with me.”")
                            input()
                            print(
                                "“I’m finished here, I’m not letting you push me around. Have fun paying for the bill, fucking dick.”")
                            input()
                            print("This scene can't be finished until I get towards the end.")
                            input()
                            self.val_question_complete = True
                            break  # Fix this later
                        else:
                            self.val_question_complete = True
                            self.val_questions_rats()
                            break
                    else:
                        self.val_question_complete = True
                        self.val_questions_rats()
                        break



        elif val_get_to_know in ['5']:
            pass

        elif val_get_to_know in ['6']:
            pass

        else:
            print("Invalid input.")
            self.val_questions_rats()










val_lunch = ValeryLunchStart()