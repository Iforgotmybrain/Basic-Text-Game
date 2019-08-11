import os
import sys
import CharInfo
import SaveSystem

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class ValeryPark:
    def park_start(self):  # Give the park more detail.
        CharInfo.valery_checks.valery_true_ending = False  # Add save points
        print("You and Valery arrive at the park after a short walk. It’s fairly early into the evening and the park is pretty empty at the moment. Guess most people are probably still at work or at home at this point in the day.")
        input()
        print("It would seem that this is more of urban park as it lacks dedicated walking trails, and instead just seems to have a set of paths that go all throughout the park.")
        print("While this park might not be as nice for just going on a walk, it seems perfect if you just want to sit down and relax or talk with someone.")
        input()
        print("“Never been to this park before. I usually go to the one on Gorge street when I wanna go for a quick walk.”")
        input()
        print("“So, you wanna just sit down and chill for a bit? Because honestly, that sounds like the best time to me”")
        input()
        print("You decide to follow Valery’s lead and just sit down at a bench and talk for a bit.")
        input()
        print(" ""Man, it has been a long time since I've been able to just sit down with someone and talk about - just whatever really."" Valery says as seems to relax a bit.")
        print("""You've been asking me all this questions so I think its my turn to ask you some.""")
        print("""Let's start off with a an easy one, did you into this intending to try and date me?""")
        input()
        print("(1): I had considered it a possibility, but I didn’t know you well enough to say if I’d even enjoy your company. No offense.")
        print("(2): I hadn’t really given it any thought. I just saw it as an opportunity to get to know someone new.")
        print("(3): I’d be lying if I said I wasn’t banking on something sparking between us.")
        val_first_question = input("Pick a response ")

        if val_first_question in ['1']:
            print("“Hah, no offense taken. Honestly, I went into this just expecting to maaaybe make a new friend, definitely did not expect to mesh so well with ya.”")
            print("“I’m glad it’s worked out so well though. It’s uh, been a while since I’ve had such a great time just talking with someone.” Valery says while his face blushes.")
            input()

        elif val_first_question in ['2']:
            print("“That’s pretty much what I was expecting. Just based off our brief conversations I never expected to get along so well with you.”")
            print("“I’m not complaining though, it’s uh, been a while since I’ve had such a great time just talking with someone.” Valery says while his face blushes.")
            input()

        elif val_first_question in ['3']:
            if CharInfo.player_info.sex in ['Male']:
                print("“Can’t say that was the case for me. I was just expecting to eat some good food and get to know a cool dude.”")

            elif CharInfo.player_info.sex in ['Female']:
                print("“Can’t say that was the case for me. I was just expecting to eat some good food and get to know a cool gal.”")

            print("“I’m not complaining though, it’s uh, been a while since I’ve had such a great time just talking with someone.” Valery says while his face blushes.")
            input()

        print("“Okay, next question: Were you at this year’s lake festival? I’ll explain why I’m asking this once you answer.”")
        input()
        print("(1): I was! Went there pretty much all day and even got to meet an old friend.")
        print("(2): I was there. In fact I’ve gone to pretty much every lake festival since the mid-2000s.")
        print("(3): Uh, nope. Never set foot there this year ")
        val_second_question = input("Pick an answer ")

        if val_second_question in ['1']:
            print("“I knew it! I swore I remembered seeing you there, you were at the concert talking to some vixen.” Valery says with an excited look on his face “I didn’t know who you were at the festival, but when you were introducing yourself a couple of days later I couldn’t help but think I remembered seeing you before.”")
            input()
            print("“I’m guessing the Fox was your old friend?”")
            print("You confirm Val’s suspicions and state that the Fox’s name is Holly.")
            input()
            if CharInfo.festival_checks.holly_stay is True:
                print("“Holly, huh? Well you two seemed to be getting along pretty well. Though I’m guessing you didn’t take that anywhere, else we probably wouldn’t be talking right now.”")
                input()

            elif CharInfo.festival_checks.holly_stay is not True:
                print("“Holly, huh? You two seemed already pretty familiar with each other so that seems right.”")
                input()

        elif val_second_question in ['2']:
            print("“I knew it! I swore I remembered seeing you there, you were at the concert talking to some vixen.” Valery says with an excited look on his face “I didn’t know who you were at the festival, but when you were introducing yourself a couple of days later I couldn’t help but think I remembered seeing you before.”")
            input()
            print("“And damn, every festival since the mid-2000s is some real dedication. Must be a tradition for you at this point.”")
            print("You tell Val that’s pretty much what is, just a tradition you started when you were a teenager.")
            input()
            print("“Cool, if this whole relationship thing works out we’ll have to go there together next year.” Val says with a smile.")
            input()

        elif val_second_question in ['3']:
            print("“Well I guess you must have a doppelganger because there was this {} that looked just like you at the concert. When I met you a few days after the festival I was thinking that I remembered seeing you there, guess not.”".format(CharInfo.player_info.race.name.upper()))
            input()

        print("“Alright, I think this my last question for you: how long have you lived in Iridium City?")
        input()
        print("")
        print("You tell Valery that you’ve been living here for around 3 years. Before that you were in college and then during your childhood your family lived in Sprucetown, which is about 2 hours east from where you live now.")  # Grammar?
        input()
        print("“Alright so you’ve been living by the lake most of your life.”")
        print("“I’ve lived in-state my whole life but never by the lake, until recent of course.”")
        input()
        print("(1): Where’d you live before coming here?")
        print("(2): I sat by the ocean and put in a place holder to remember to write this and make it work.")
        val_living_question = input("Choose a response ")

        if val_living_question in ['1']:
            print("“Just before moving here? Nagysburg. Lived there for 3 years until I got that job offer. Before that I lived in Fulton, which is where I grew up and went to college. Ended up Staying there a year after graduating since I got a job at a local company.”")
            input()
            print("(1): How’d your time in Nagysburg and Fulton compare to here?")
            print("(2): I’m guessing there was some reason you left those places to come here.")
            val_moving_question = input("Choose a response ")

            if val_moving_question in ['1']:
                print("“My time in Nagysburg was pretty similar to here. Main difference is that in Nagysburg I had something resembling a friend group, while here I know you and that’s pretty much it.”")
                print("“The job I had in Nagysburg wasn’t the great though. Hardly any paid time off and the insurance was trash. I’ve had it a lot better here in that regard.”")
                input()
                print("“Fulton’s a bit more complex. I had a great social life there, after all that’s where pretty every friend I made up until graduation lived.”")
                print("“But I couldn’t help but feel unfulfilled. I’d lived my whole life there and it was really starting to drag on. You see the same people, drive the same roads to the same place your parents worked at when you were growing up.”")
                input()
                print("“It got mundane, and honestly a little depressing. Life wasn’t really exciting anymore, I felt like I was just running off a script doing the same thing week after week.”")
                print("“So I started looking for jobs a fair ways away from home. Applied to a bunch of them but of course only a few asked me to interview. The company in Nagysburg ended up offering me the best salary and was in a pretty nice city so I figured that was probably my best bet.”")
                input()
                print("“Ended up being a pretty nice experience. Got along really well with my coworkers and one of my neighbors as well, they ended up being part of the friend group I was talking about.”")
                input()
                if CharInfo.valery_checks.valery_heart_to_heart is True:
                    print("“And of course we’ve already talked a bit about my time here so far. Still pretty early into the move so I’m sure things will get better.”")
                    input()

            elif val_moving_question in ['2']:
                print("“Yup. For Nagysburg it was the job. I ended up getting completely burnt out because they gave me shit for time off. Plus, the insurance was basically useless so when I did get burnt out, I couldn’t even afford to go and see a therapist to help me sort my stuff out.”")
                input()
                print("“And then for Fulton; I just got bored of living there. I’d lived my whole life there and it was really starting to drag on. You see the same people, drive the same roads to the same place your parents worked at when you were growing up.”")
                print("“It just got to be too much for me. So I started looking for jobs that were a decent distance away from Fulton. Applied to a bunch of jobs and got a couple of interviews, the company in Nagysburg ended up having the best salary and location.”")
                input()
                print("“I jumped on the job offer and moved there shortly after. Ended up being a pretty nice experience all things considered. I got along really well with my coworkers and even got to know one of my neighbor’s pretty well. That turned out to be a pretty nice group of friends.”")
                input()

            print("(1): Seems like you did pretty well in the last new place you moved too. So I’m sure it’ll end up working out here, too.")
            print("(2): Well hopefully you don’t run off too soon from here, I’d probably end up missing ya.")
            print("(3): It’s good to get outside of your comfort zone and explore a bit. I’m actually planning on going on a cross-country road trip here pretty soon.")
            val_deeper_move_question = input("Choose a response")

            if val_deeper_move_question in ['1']:
                print("“I didn’t do terrible in Nagysburg and Fulton I’ll say that. I don’t know if I’d say I did ‘pretty well’ though. After all there’s reason I moved away from those towns.”")
                input()
                print("“I’ve already explained my issues with Fulton pretty well, but there’s some other stuff that went on during my time in Nagysburg that I didn’t talk much about.”")
                if CharInfo.valery_checks.valery_date_points >= 15 and CharInfo.valery_checks.valery_heart_to_heart is True:
                    print("Valery seems to take a moment to think, he sighs before eventually talking again. “We’ve talked about some pretty deep stuff today, so I guess it’s alright if I talk to you about those issues.”")
                    input()
                    CharInfo.player_info.player_location = val_park.park_end
                    SaveSystem.save_sys.saving()
                    clear()
                    self.park_end()
                else:
                    print("“And if I’m being honest, I just don’t feel comfortable talking about those issues right now. It’s nothing against you, just a personal thing.”")
                    input()

            elif val_deeper_move_question in ['2']:
                print("“Hah, I’d probably end up missing you too. Or at least be left wondering what could have been.”")
                input()
                print("“Ya know, I kind of ran into that when I moved from Fulton and Nagysburg. Constantly thinking about how things could have gone if I had stayed instead of moved.”")
                print("““It’s was a fairly deep-rooted problem for me in Nagysburg, I’ve gotten over it for the most part now. That and the lack of people to talk too in Nagysburg were really taking their toll on me.””")
                input()
                print("(1): Lack of people to talk too? Wanna talk a bit more about that?")
                print("(2): I've given up, I'm sick of waiting, this is a placeholder until I get later into the game.")
                val_talking_issue = input("Choose a response")

                if val_talking_issue in ['1']:
                    if CharInfo.valery_checks.valery_date_points >= 15 and CharInfo.valery_checks.valery_heart_to_heart is True:  # Dialogue can only be unlocked with a high date point score and the more in-depth dialogue scene at the restaurant.
                        print("Valery seems to take a moment to think, he sighs before eventually talking again. “We’ve talked about some pretty deep stuff today, so I guess it’s alright if I talk to you about it.")
                        input()
                        CharInfo.player_info.player_location = val_park.park_end
                        SaveSystem.save_sys.saving()
                        clear()
                        self.park_end()
                    else:
                        print("“And if I’m being honest, I just don’t feel comfortable talking about that issue right now. It’s nothing against you, just a personal thing.”")
                        input()
                        #  Put to end of game when I get there
                elif val_talking_issue in ['2']:
                    print("Placeholder.")
                    CharInfo.valery_checks.valery_true_ending = False
                    input()

            elif val_deeper_move_question in ['3']:
                print("“A road trip, huh? Didn’t think you’d be the kind of person to go out and do something like that.”")
                input()
                print("You take some time to explain the whole concept to Valery. You tell him what your exact travel plans are and how long you plan on it taking.")
                input()
                print("“I won’t lie, it sounds really interesting. Be a great way to build our relationship, too. Maybe keep me in mind when your picking people to go, yeah?”")
                print("You tell Val you'll keep him mind when you start picking your travel mates.")
                input()
                print("""I get what your saying about moving outside of your comfort zone. I did enjoy being in a new city and experience all the new thing that had to offer.""")
                print("""What really got me down was just the complete lack of people I had to talk too about more serious stuff.""")
                input()
                print("(1): A lack of people to talk too? Wanna talk about that a bit more?")
                print("(2): That's unfortunate. At least you seem to be having better luck with that this time around.")
                val_talking_issue_1 = input("Choose a response ")

                if val_talking_issue_1 in ['1']:
                    if CharInfo.valery_checks.valery_date_points >= 15 and CharInfo.valery_checks.valery_heart_to_heart is True:
                        print("Valery seems to take a moment to think, he sighs before eventually talking again. “We’ve talked about some pretty deep stuff today, so I guess it’s alright if I talk to you about it.")
                        input()
                        CharInfo.player_info.player_location = val_park.park_end
                        SaveSystem.save_sys.saving()
                        clear()
                        self.park_end()
                    else:
                        print("“And if I’m being honest, I just don’t feel comfortable talking about that issue right now. It’s nothing against you, just a personal thing.”")
                        input()
                        #  Put to end of game when I get there

                elif val_talking_issue_1 in ['2']:
                    print("Placeholder")
                    input()



    def park_end(self):
        if CharInfo.valery_checks.valery_heart_to_heart is True and CharInfo.valery_checks.valery_date_points >= 15:
            print("“It’s not anything horrifying, don’t get the wrong idea. But it’s a pretty depressing and disappointing thing for me to look back on, so I don’t like talking about it too much.")
            input()
            print("“Towards the end of my time in Nagysburg I was in a pretty bad place. I was lonely, and as I might have mentioned, I started getting pretty burnt out on my job because they were practically working me to death.”")
            input()
            print("“Now, I know you might be thinking “How could you be lonely? You said you had a pretty solid group of friends, right?” I had friends, yes. But most of those friends weren’t really the kind you’d spill your heart out too. We never talked about anything too serious, mostly just kept it centered around work or our hobbies.”")
            input()
            print("“That meant I didn’t really have anybody to talk too about serious, in-depth stuff. Things like how I was feeling emotional, my future, job burn out, and numerous other things.”")
            print("“Back in Fulton I’d have a couple of friends that’d be down for listening to whatever bullshit I want, but that wasn’t the case in Nagysburg.”")
            input()
            print("“And of course, I couldn’t afford to see a therapist to help with that issue since my health insurance, which I paid $300 a month for by the way, wouldn’t cover any of the cost for therapy. I would have been paying close to $200 per session to just talk to somebody about my problems. Even with my decent paying job I couldn’t afford that.”")  # Realest talk here. I've dealt with this exact situation before.
            input()
            print("“It was a pretty rough patch for me. I had no real friends to talk too, no family members, and no significant other to talk about it either. I felt so isolated from everybody else, I was dealing with all my challenges and issues myself, there was no one else to help me deal with them.”")
            print("“I was just keeping all these feelings to myself and it wasn’t working. I didn’t know what to do. I didn’t feel like going to work, I didn’t feel like going out, I just wanted to stay at home and hide.”")
            input()
            print("(1): How’d you get out of that emotional pit?")
            print("(2): And that’s part of the reason you wanted to move here, right?")
            print("(3): I think I’ve heard enough.")
            val_lonely_question = input("Choose a response ")

            if val_lonely_question in ['1']:
                print("“Honestly? I still haven’t 100% gotten out of that funk. I did start talking to some of my old friends towards the end of time at Nagysburg, which helped.”")
                input()
                print("“And then I’ve just been telling myself I have to really make an effort to try and meet new people, like you. That’s helped quite bit, even if I don’t end up connecting, I can at least feel good about the fact that I’m trying.”")
                input()
                CharInfo.valery_checks.valery_true_ending = True

            elif val_lonely_question in ['2']:
                print("“Kind of. I moved here because I really enjoyed the city, plus the job offer I got here was a lot less work intensive and had a lot better benefits.”")
                input()
                print("“Of course I did go into the move thinking about how well everything could work out for me. Thinking about how I’m going to meet all these awesome people, find my soulmate. So, I guess it was a mix of searching for a more satisfying life plus wanting a better job.”")
                input()
                print("“It’s worked out alright so far. Like I said the job is a lot better than my old one. And I’ve been keeping in contact with some of my old friends which has helped me a bit.”")
                print("“And since I’ve gotten here I’ve been telling myself that I need to be more active in getting to know new people, which has help quite a bit as well. Even if I don’t end up connecting with someone I can at least feel good about the fact that I’m trying.”")
                input()
                CharInfo.valery_checks.valery_true_ending = True

            elif val_lonely_question in ['3']:
                print("“Ok. I understand. Not everyone wants to hear me complain about my problems.”")
                input()
                CharInfo.valery_checks.valery_true_ending = False
                CharInfo.valery_checks.valery_date_points -= 8
                #  Send to end later

        print("“And those failures make it even better when I find someone like you.” He says while jabbing your shoulder and giving you a slight grin.”")
        input()
        print("“Oh, and I’m sure you knew this by now, but I know you brought me here because you were interested in me. I figured you probably worked that out given how personal our talks have gotten.”")
        input()

        if CharInfo.valery_checks.valery_heart_to_heart is True and CharInfo.valery_checks.valery_true_ending is not True:  # If the player choose the secret dialogue option in the restaurant but didn't finish all of Vals dialogue here
            print("“It’s been great getting to know you, and honestly, I’d say I’m pretty into you as well. When we were talking in the restaurant I couldn’t help but feel like I was back in Fulton hanging out with an old friend. It was great”")
            input()
            print("“I’d be lying if I said I wasn’t already thinking about what’s next for us. Better be another date, at least.”")
            input()
            print("(1): I was already thinking about that. I’ve got a couple of ideas I was in mind, including a road trip.")
            print("(2): There’s still plenty of time to figure that out. Since we live in the same neighborhood, I’m sure we’ll be seeing each other quite often.")
            print("(3): Yeah… we’ll see about that. I’m gonna be pretty busy so any date will have to be postponed a bit.")
            val_ending_1_response = input("Choose a response")

        elif CharInfo.valery_checks.valery_heart_to_heart is True and CharInfo.valery_checks.valery_true_ending is True:  # If player choose the secret dialogue option and finished all of Vals dialogue.
            print("“Don’t worry, the interest goes both ways, like me. Honestly wasn’t sure if I wanted our relationship to go any further than friends at the start, but after our talks here and at the restaurant, I kind of fell for you.”")
            input()
            print("“The last time I enjoyed talking with someone this much was, uh, let’s just say awhile ago.”")
            print("“I really like you, {}. And I can’t wait to spend even more time with you.”".format(CharInfo.player_info.name))
            input()


        elif CharInfo.valery_checks.valery_heart_to_heart is not True and CharInfo.valery_checks.valery_date_points >= 15:  # If the player didn't choose the secret dialogue option but did get along well with Val
            print("“The feeling is mutual. I wasn’t sure about taking our relationship any further than friends when we were talking in the restaurant, but when we got here and started talking a bit more in-depth I really started to enjoy my time with you.”")
            input()
            print("“It’s been great getting to know you, never would have expected coming into this that I’d be leaving with a romantic interest in you.”")
            input()


        elif CharInfo.valery_checks.valery_date_points <= 10:  # If the player didn't really talk with Valery much.
            print("“I’ll be honest, I like you. But I just don’t know if I can see us being a couple, you know? At least, not right now. I just don’t know you well enough.”")
            print("“I just don’t think we’d get along that well. Maybe we can go on another date sometime, but for now though, no, I don’t feel the same way. I don’t see us being any more than friends.”")
            input()






val_park = ValeryPark()