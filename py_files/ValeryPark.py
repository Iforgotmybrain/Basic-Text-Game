import os
import sys
import CharInfo
import SaveSystem

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class ValeryPark:
    def __init__(self):
        self.val_deeper_move_question = ''

    def park_start(self):  # Give the park more detail.
        CharInfo.valery_checks.valery_true_ending = False  # Remember to add save points
        CharInfo.valery_checks.valery_ending_path = ''
        print("You and Valery arrive at the park after a short walk. It’s fairly early into the evening and the park is pretty empty at the moment. Guess most people are probably still at work or at home at this point in the day.")
        input()
        print("It's late summer so the trees are still quite green, though the grass is looking a bit dry. Walking through the entrance you can see the map of the park and a few fountains.")
        print("Looking at the map, it would seem that this is more of an urban park as it lacks dedicated walking trails, and instead just seems to have a set of paths that go all throughout the park.")
        print("While this park might not be as nice for just going on a walk, it seems perfect if you just want to sit down and relax or talk with someone.")
        input()
        print("“Never been to this park before. I usually go to the one on Gorge street when I wanna go for a quick walk.”")
        input()
        print("“So, you wanna just sit down and chill for a bit? Because honestly, that sounds like a good time to me”")
        input()
        print("You decide to follow Valery’s lead and just sit down at a bench and talk for a bit.")
        input()
        print(' "Man, it has been a long time since I\'ve been able to just sit down with someone and talk about - just whatever really." Valery says as he seems to relax a bit.')
        print('"You\'ve been asking me all these questions so I think it\'s my turn to ask you some."')
        print('"Let\'s start off with a an easy one, what kind of music do you like to listen to?"')
        input()
        print(
            "(1): Metal and harder rock is usually what I listen too.")
        print(
            "(2): Indie rock is my main jam, though I'm not opposed to other genres")
        print("(3): Rap and hip-hop is typically what I'll listen too.")
        print("(4): I like jazz quite a bit")
        print("(5): Classical is what I enjoy listening to the most")
        print("(6): Honestly I listen to a lot of different genres, they all have something I enjoy listening to.")
        val_first_question = input("Pick a response ")

        if val_first_question in ['1']:
            print(
                "“Interesting, wouldn't have taken you as someone who enjoyed heavier music.”")
            print(
                "“I could never get into metal myself, there's some heavier rock bands I like but I definitely wouldn't consider it my favorite genre.”")
            input()
            print('"That would go to alt-rock. I used to listen to just regular rock music quite a bit as well but I got kind of bored of it."')
            print('"Mainly because mainstream rock hasn\'t changed that much since the 2000s. I was actually listening to whatever the top rock song of last year was and I seriously thought I was listening to a song from 2004."')
            print('"It had the same exact sound as a rock song from around 2004, only thing that gave away the fact it was a song made in 2018 was the fact that it mentioned the actual year. Shame to see such a storied and formerly great genre turn into a boring and stagnant mess."')
            input()
            print('"Alt-rock and indie rock have sort of gone the way I would have expected rock too, lot more experimentation and different sound styles. But that\'s enough about music, let\'s talk more about you."')
            input()

        elif val_first_question in ['2']:
            print(
                "“Nice taste, I like quite a bit of indie music myself. Mainly some of the more psychedelic bands like Manhunter and Kings.”")
            print(
                '"My primary genre I listen to alt-rock though, I used to listen to just regular rock music quite a bit as well but I got kind of bored of it."')
            input()
            print('"Mainly because mainstream rock hasn\'t changed that much since the 2000s. I was actually listening to whatever the top rock song of last year was and I seriously thought I was listening to a song from 2004."')
            print('"It had the same exact sound as a rock song from around 2004, only thing that gave away the fact it was a song made in 2018 was the fact that it mentioned the actual year. Shame to see such a storied and formerly great genre turn into a boring and stagnant mess."')
            input()
            print('"Alt-rock and indie rock have sort of gone the way I would have expected rock too, lot more experimentation and different sound styles. But that\'s enough about music, let\'s talk more about you."')
            input()

        elif val_first_question in ['3']:
            print('"Nice, I used to listen to a lot of rap when I was a bit younger, sort got out of it a bit now though."')
            print('"Mainly it was Trap I listened to, now if I listen to any its more mainstream and vanilla stuff."')
            print('"Now I mainly listen to alt-rock, used to listen to regular rock quite a bit as well but got kind of bored of it."')
            input()
            print('"Mainly because mainstream rock hasn\'t changed that much since the 2000s. I was actually listening to whatever the top rock song of last year was and I seriously thought I was listening to a song from 2004."')
            print('"It had the same exact sound as a rock song from around 2004, only thing that gave away the fact it was a song made in 2018 was the fact that it mentioned the actual year. Shame to see such a storied and formerly great genre turn into a boring and stagnant mess."')
            input()
            print('"Alt-rock and indie rock have sort of gone the way I would have expected rock too, lot more experimentation and different sound styles. But that\'s enough about music, let\'s talk more about you."')
            input()



        elif val_first_question in ['4']:
            print('"Could never get into jazz myself. I can see why people like it through."')
            print('"It\'s a pretty broad genre though, I\'m sure I could find something I like if I searched long enough."')
            input()
            print('"Most of the time I listen to alt-rock though, I liked rock quite a bit as well but I\'ve gotten a bit bored of it."')
            input()
            print('"Mainly because mainstream rock hasn\'t changed that much since the 2000s. I was actually listening to whatever the top rock song of last year was and I seriously thought I was listening to a song from 2004."')
            print('"It had the same exact sound as a rock song from around 2004, only thing that gave away the fact it was a song made in 2018 was the fact that it mentioned the actual year. Shame to see such a storied and formerly great genre turn into a boring and stagnant mess."')
            input()
            print('"Alt-rock and indie rock have sort of gone the way I would have expected rock too, lot more experimentation and different sound styles. But that\'s enough about music, let\'s talk more about you."')
            input()

        elif val_first_question in ['5']:
            print('"Interesting choice, can\'t say I enjoy listening to it myself but I appreciate how much of an impact its had on music as a whole."')
            print('"I\'m more of an alt-rock guy myself, used to just listen to regular rock but I got kind of bored of it."')
            input()
            print('"Mainly because mainstream rock hasn\'t changed that much since the 2000s. I was actually listening to whatever the top rock song of last year was and I seriously thought I was listening to a song from 2004."')
            print('"It had the same exact sound as a rock song from around 2004, only thing that gave away the fact it was a song made in 2018 was the fact that it mentioned the actual year. Shame to see such a storied and formerly great genre turn into a boring and stagnant mess."')
            input()
            print('"Alt-rock and indie rock have sort of gone the way I would have expected rock too, lot more experimentation and different sound styles. But that\'s enough about music, let\'s talk more about you."')
            input()

        elif val_first_question in ['6']:
            print('"Nice, I totally get that. There\'s a ton of great music out there, and with streaming services its easy to find a bunch of stuff you like."')
            print('"That\'s how I\'ve found a bunch of my favorite bands recently. Just browsing the suggested artists and listening to streaming radio."')
            print('"My main genre is probably alt-rock though. Used to listen to a bunch of regular rock music as well, but I got bored of the genre."')
            input()
            print('"Mainly because mainstream rock hasn\'t changed that much since the 2000s. I was actually listening to whatever the top rock song of last year was and I seriously thought I was listening to a song from 2004."')
            print('"It had the same exact sound as a rock song from around 2004, only thing that gave away the fact it was a song made in 2018 was the fact that it mentioned the actual year. Shame to see such a storied and formerly great genre turn into a boring and stagnant mess."')
            input()
            print('"Alt-rock and indie rock have sort of gone the way I would have expected rock too, lot more experimentation and different sound styles. But that\'s enough about music, let\'s talk more about you."')
            input()

        print("“Okay, next question: Were you at this year’s lake festival? I’ll explain why I’m asking this once you answer.”")
        input()
        print("(1): I was! Went there pretty much all day and even got to meet an old friend.")  # Maybe expand this?
        print("(2): I was there. In fact I’ve gone to pretty much every lake festival since the mid-2000s.")
        print("(3): Uh, nope. Never set foot there this year ")
        val_second_question = input("Pick an answer ")

        if val_second_question in ['1']:
            print(
                "“I knew it! I swore I remembered seeing you there, you were at the concert talking to some vixen.” Valery says with an excited look on his face “I didn’t know who you were at the festival, of course, but when you were introducing yourself a couple of days later I couldn’t help but think I remembered seeing you before.”")
            input()
            print("“I’m guessing the Fox was your old friend?”")
            print("You confirm Val’s suspicions and state that the Fox’s name is Holly.")
            input()
            if CharInfo.festival_checks.holly_stay is True:
                print(
                    "“Holly, huh? Well you two seemed to be getting along pretty well. Though I’m guessing you didn’t take that anywhere, else we probably wouldn’t be talking right now.”")
                input()

            elif CharInfo.festival_checks.holly_stay is not True:
                print("“Holly, huh? You two seemed already pretty familiar with each other so that seems right.”")
                input()

        elif val_second_question in ['2']:
            print(
                "“I knew it! I swore I remembered seeing you there, you were at the concert talking to some vixen.” Valery says with an excited look on his face “I didn’t know who you were at the festival, of course, but when you were introducing yourself a couple of days later I couldn’t help but think I remembered seeing you before.”")
            input()
            print(
                "“And damn, every festival since the mid-2000s is some real dedication. Must be a tradition for you at this point.”")
            print(
                "You tell Val that’s pretty much what it is, just a tradition you started when you were a teenager.")
            input()
            print(
                "“Cool, if this whole relationship thing works out we’ll have to go there together next year.” Val says with a smile.")
            input()

        elif val_second_question in ['3']:
            print(
                "“Well I guess you must have a doppelganger because there was this {} that looked just like you at the concert. When I met you a few days after the festival I was thinking that I remembered seeing you there, guess not.”".format(
                    CharInfo.player_info.race.title()))
            input()

        print("“Alright, I think this is my last question for you: how long have you lived in Iridium City?")
        input()
        print("")
        print("You tell Valery that you’ve been living here for around 3 years. Before that you were in college and then during your childhood your family lived in Sprucetown, which is about 2 hours east from where you live now.")  # Grammar?
        input()
        print("“Alright so you’ve been living in a city by the lake for most of your life.”")
        print("“I’ve lived in-state my whole life as well but never by the lake, until recent of course.”")
        input()
        print("(1): Where’d you live before coming here?")
        print("(2): I sat by the ocean and put in a place holder to remember to write this and make it work.")
        val_living_question = input("Choose a response ")

        if val_living_question in ['1']:
            print("“Just before moving here? Nagysburg. Lived there for 3 years until I got my job here. Before that I lived in Fulton, which is where I grew up and went to college. Ended up staying there a year after graduating since I got a job at a local company.”")
            input()
            print("(1): How’d your time in Nagysburg and Fulton compare to here?")
            print("(2): I’m guessing there was some reason you left those places to come here.")
            val_moving_question = input("Choose a response ")

            if val_moving_question in ['1']:
                print("“My time in Nagysburg was pretty similar to here. Main difference is that in Nagysburg I had something resembling a friend group, while here I know you and that’s pretty much it.”")
                print("“The job I had in Nagysburg wasn’t that great though. Hardly any paid time off and the insurance was trash. I’ve had it a lot better here in that regard.”")
                input()
                print("“Fulton’s a bit more complex. I had a great social life there, after all that’s where pretty every friend I made up until graduation lived.”")
                print("“But I couldn’t help but feel unfulfilled. I’d lived my whole life there and it was really starting to drag on. You see the same people, drive the same roads to the same place your parents worked at when you were growing up.”")
                input()
                print("“It got mundane, and honestly a little depressing. Life wasn’t really exciting anymore, I felt like I was just running off a script doing the same thing week after week.”")
                print("“So I started looking for jobs a fair ways away from home. Applied to a bunch of them but of course only a few asked me to interview. The company in Nagysburg ended up offering me the best salary and was in a pretty nice city so I figured that was probably my best bet.”")
                input()
                print("“Ended up being a pretty nice experience. Got along really well with my coworkers and one of my neighbors as well, they ended up being part of that friend group I was talking about.”")
                input()
                if CharInfo.valery_checks.valery_heart_to_heart is True:
                    print("“And of course we’ve already talked a bit about my time here so far. Still pretty early into the move so I’m sure things will get better.”")
                    input()

            elif val_moving_question in ['2']:
                print("“Yup. For Nagysburg it was the job. I ended up getting completely burnt out because they gave me shit for time off. Plus, the insurance was basically useless so when I did get burnt out, I couldn’t even afford to go and see a therapist to help me get through it.”")
                input()
                print("“And then for Fulton; I just got bored of living there. I’d lived my whole life there and it was really starting to drag on. You see the same people, drive the same roads to the same place your parents worked at when you were growing up.”")
                print("“It just got to be too much for me. So I started looking for jobs that were a decent distance away from Fulton. Applied to a bunch of jobs and got a couple of interviews, the company in Nagysburg ended up having the best salary and location.”")
                input()
                print("“I jumped on the job offer and moved there shortly after. Ended up being a pretty nice experience all things considered. I got along really well with my coworkers and even got to know one of my neighbor’s pretty well. That turned out to be a pretty nice group of friends.”")
                input()

            print("(1): Seems like you did pretty well in the last new place you moved too. So I’m sure it’ll end up working out here, too.")
            print("(2): Well hopefully you don’t run off too soon from here, I’d probably end up missing ya.")
            print("(3): It’s good to get outside of your comfort zone and explore a bit. I’m actually planning on going on a cross-country road trip here pretty soon.")
            self.val_deeper_move_question = input("Choose a response ")

            if self.val_deeper_move_question in ['1']:
                print("“I didn’t do terrible in Nagysburg and Fulton I’ll say that. I don’t know if I’d say I did ‘pretty well’ though. After all there’s reason I moved away from those towns.”")
                input()
                print("“I’ve already explained my issues with Fulton pretty well, but there’s some other stuff that went on during my time in Nagysburg that I didn’t talk much about.”")
                if CharInfo.valery_checks.valery_date_points >= 15 and CharInfo.valery_checks.valery_heart_to_heart is True:
                    print("Valery seems to take a moment to think, he sighs before eventually talking again. “We’ve talked about some pretty personal stuff already, so I guess it’s alright if I talk to you about those issues.”")
                    input()
                    CharInfo.player_info.player_location = val_park.park_end
                    clear()
                    SaveSystem.save_sys.saving()
                    self.park_end()
                else:
                    print("“And if I’m being honest, I just don’t feel comfortable talking about those issues right now. It’s nothing against you, just a personal thing.”")
                    input()

            elif self.val_deeper_move_question in ['2']:
                print("“Hah, I’d probably end up missing you too. Or at least be left wondering what could have been.”")
                input()
                print("“Ya know, I kind of ran into that when I moved from Fulton and Nagysburg. Constantly thinking about how things could have gone if I had stayed instead of moved.”")
                print("“It was a fairly deep-rooted problem for me in Nagysburg, I’ve gotten over it now for the most part now. That and the lack of people to talk too in Nagysburg were really taking their toll on me.”")
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

            elif self.val_deeper_move_question in ['3']:
                print("“A road trip, huh? Didn’t think you’d be the kind of person to go out and do something like that.”")
                input()
                print("You take some time to explain the whole concept to Valery. You tell him what your exact travel plans are and how long you plan on it taking.")
                input()
                print("“I won’t lie, it sounds really interesting. Be a great way to build our relationship, too. Maybe keep me in mind when you're picking people to go, yeah?”")
                print("You tell Val you'll keep him in mind when you start picking your travel mates.")
                input()
                print('"I get what your saying about moving outside of your comfort zone. I did enjoy being in a new city and experiencing all the new things that had to offer."')
                print('"What really got me down was just the complete lack of people I had to talk too about more serious stuff."')
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
                        print("“If I’m being honest, I just don’t feel comfortable talking about that issue right now. It’s nothing against you, just a personal thing.”")
                        input()
                        #  Put to end of game when I get there

                elif val_talking_issue_1 in ['2']:
                    print("Placeholder")
                    input()




    def park_end(self):
        if CharInfo.valery_checks.valery_heart_to_heart is True and CharInfo.valery_checks.valery_date_points >= 15:
            print("“It’s not anything horrifying, don’t get the wrong idea. But it’s a bit depressing for me to look back on, so I don’t like talking about it too much.")
            input()
            print("“Towards the end of my time in Nagysburg I was in a pretty bad place. I was lonely, and as I might have mentioned, I started getting pretty burnt out on my job because they were practically working me to death.”")
            input()
            print("“Now, I know you might be thinking “How could you be lonely? You said you had a pretty solid group of friends, right?” I had friends, yes. But most of those friends weren’t really the kind you’d spill your heart out too. We never talked about anything too serious, mostly just kept it centered around work or our hobbies.”")
            input()
            print("“That meant I didn’t really have anybody to talk to about more serious stuff. Things like how I was feeling emotional, my future, job burn out, and numerous other things.”")
            print("“Back in Fulton I’d have a couple of friends that’d be down for listening to whatever bullshit I wanted to talk about, but that wasn’t the case in Nagysburg.”")
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
                print('"Moving here has helped a bit. Or at least it\'s made me a bit more optimistic. New place, new opportunities and people."')
                print('"Of course having too high of expectations can be a dangerous thing too. Like telling yourself that you\'re going to meet all these awesome people and then you actually get there for real and it\'s nothing like you imagined."')
                input()
                print('"Wouldn\'t say that exact scenario has happened for me, but I did kind of expect that moving here would help sovle some of my problems."')
                input()
                print("“And then I’ve also been telling myself I have to really make an effort to try and meet new people, like you. That’s helped quite bit too. Even if I don’t end up connecting, I can at least feel good about the fact that I’m trying.”")
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
                print("“Really? You couldn't take 10 minutes out of your life to just listen to what I have to say?”")
                input()
                CharInfo.valery_checks.valery_true_ending = False
                CharInfo.valery_checks.valery_date_points -= 8
                print('"You must not care about me too much if you don\'t want to hear me out. Suppose were done here then."')
                print('"No point in continuing this pseudo-date when you can\'t even spare the time to listen to my story."')
                input()
                print("Valery gets up and walks to us car without even saying goodbye. Seems you really struck a nerve with him.")
                input()
                print("Placeholder")
                input()

        print("“And of course those failures make it even better when I do actually connect with someone. Like with you.” He says while jabbing your shoulder and giving you a slight grin.”")
        input()
        print("“Alright, I don't like to talk my sad shit for too long, makes me too emotional. Let's talk about something a bit more upbeat.”")  # Need to word this better I think
        print('"Namely, our relationship. Which is the reason you brought me. You didn\'t say it outright, but I know you\'re interested in me, why else would you have brought me here?"')
        input()

        if CharInfo.valery_checks.valery_heart_to_heart is True and CharInfo.valery_checks.valery_true_ending is not True:  # If the player choose the secret dialogue option in the restaurant but didn't finish all of Vals dialogue here
            val_endings.ending_one()  # Putting the endings in a separate class and giving them their own function works so much better. Looks much neater.

        elif CharInfo.valery_checks.valery_heart_to_heart is True and CharInfo.valery_checks.valery_true_ending is True:  # If player choose the secret dialogue option and finished all of Vals dialogue.
            val_endings.ending_two_true()

        elif CharInfo.valery_checks.valery_heart_to_heart is not True and CharInfo.valery_checks.valery_date_points >= 15:  # If the player didn't choose the secret dialogue option but did get along well with Val
            val_endings.ending_three()

        elif CharInfo.valery_checks.valery_date_points <= 10:  # If the player didn't really talk with Valery much.
            val_endings.ending_four_bad()


class ValeryEndings:
    def ending_one(self):
        print(
            "“Honestly, I’d say I’m pretty into you as well. When we were talking in the restaurant I couldn’t help but feel like I was back in Fulton hanging out with an old friend. It was great”")
        input()
        print(
            "“I’d be lying if I said I wasn’t already thinking about what’s next for us. Better be another date, at least.”")
        input()

        if val_park.val_deeper_move_question in ['3']:
            print(
                "(1): I was already thinking about that. I’ve got a couple of ideas in mind, including that road trip I mentioned.")

        elif val_park.val_deeper_move_question not in ['3']:
            print(
                "(1): I was already thinking about that. I've a got a couple of ideas in mind, including a road trip.")

        print(
            "(2): There’s still plenty of time to figure that out. Since we live in the same neighborhood, I’m sure we’ll be seeing each other quite often.")
        print("(3): Yeah… we’ll see about that. I’m gonna be pretty busy so any date will have to be postponed a bit.")
        val_ending_1_response = input("Choose a response")

        if val_ending_1_response in ['1']:

            if val_park.val_deeper_move_question in ['3']:
                print(
                    """Hell yeah, like I said I'm down for that. Just gotta let me know if you're committing so I can get my work stuff taken care of.""")
                input()
            else:
                print("""A road trip, huh? Mind filling me in on the details?""")
                input()
                print(
                    "You take some time to explain the whole concept to Valery. You tell him what your exact travel plans are and how long you plan on it taking.")
                input()
                print(
                    "“I won’t lie, it sounds really interesting. Be a great way to build our relationship, too. Maybe keep me in mind when you're picking people to go, yeah?”")
                print("You tell Val you'll keep him in mind when you start picking your travel mates.")
                input()
            self.ending_one_common()

        elif val_ending_1_response in ['2']:
            print(
                "Yeah, no point in worrying about it too much. Might be going on a few more walks around the neighborhood though heh.")
            input()
            self.ending_one_common()

        elif val_ending_1_response in ['3']:
            print(
                "I'm sure you'll find time. From my experience people always end up over thinking how busy they'll end up being,")
            input()
            self.ending_one_common()

    def ending_one_common(self):
        print(
            "Well, I guess our day is about done here. It's been a joy talking with you, can't say I expected today to end with us figuring out when our next date will be.")
        print(
            "But I'll take it, Gods know it's been a long time since I've been in a serious relationship.")

        if CharInfo.player_info.race in ['wolf', 'Wolf'] and CharInfo.player_info.sex in ['Female', 'female']:
            print(
                "(1): *Give Valery a kiss on the cheek* Sometimes you have days where life's a bitch, guess today was one where you got kissed by one instead. See you around, Val.")
        else:
            print(
                "(1): *Give Valery a kiss on the cheek* We don't expect a lot of things, Valery. Most of time it's unpleasantness we don't expect, not today, though. See you around, Val.")

        print(
            "(2): Never know what you're gonna get when you wake up in the morning. Most of time the day goes on as usual, but sometimes you get unforgettable days like this. They make those mundane days worth it.")

        val_ending_1_last = input("Choose a response ")

        if val_ending_1_last in ['1']:
            print("End")

        elif val_ending_1_last in ['2']:
            print("""You're right, {}. That's why I'll be looking forward to our next date so much.""")
            print("""Bah, that's enough rambling on. See you round the neighborhood, {}.""".format(
                CharInfo.player_info.name))
            input()
            print("You say goodbye to Valery and watch as he walks back to his car.")

    def ending_two_true(self):
        print(
            "“Don’t worry, the interest goes both ways, like me. Honestly wasn’t sure if I wanted our relationship to go any further than friends at the start, but after our talks here and at the restaurant, I kind of fell for you.”")
        input()
        print("“The last time I enjoyed being around someone this much was, uh, let’s just say awhile ago.”")
        print("“I really like you, {}. And I can’t wait to spend even more time with you.”".format(
            CharInfo.player_info.name))
        input()
        print("(1): ")
        if val_park.val_deeper_move_question in ['3']:
            print("(2): I feel the same, Valery. Don't know when our next date will be but I do have that road trip coming up...")
        else:
            print("(2):I feel the same. That said, I’m planning on going on a road trip pretty soon, might be a good opportunity for us to spend some more time together…")
        print("(3): Same here, Valery. Although I’d be lying if I said I wasn’t at least a little bit interested in you coming into lunch.")
        valery_ending_two_prompt = input("Choose a response ")

        if valery_ending_two_prompt in ['1']:
            pass

        elif valery_ending_two_prompt in ['2']:
            if val_park.val_deeper_move_question in ['3']:
                print("“Exactly what I was thinking! Bit of a jump to go from a single date to spending a whole month together, be a good way to see if we can stand living with each other though.”")
                print("“Like I said keep me in mind when you're asking people to tag along. I’m down for that 100%.”")
                input()
                print("""Well I have to say it's getting pretty late. It's 5 PM now and we've been talking since 12, sure didn't feel like that much time passed.""")
                print("""Guess we better start heading home, we keep talking any longer and we'll be getting bit by mosquitoes.""")
                input()
                print('Valery stands up before resuming the conversation "Come give me a hug before we head back home."')
                input()
                print("(1): I was thinking of more than just a hug")
                print("(2): *Hug Valery* ")
                val_ending_two_prompt_two = input("Choose a response ")

                if val_ending_two_prompt_two in ['1']:
                    print("Placeholder")

                elif val_ending_two_prompt_two in ['2']:
                    print("You and Valery share a fairly long hug before saying your goodbyes.")
                    print(' "I\'m sure I\'ll be seeing you around the neighborhood quite a bit now. Might even have to stop down at your house sometime." Valery says with a somewhat suggestive look.')
                    print("See ya round then, {}".format(CharInfo.player_info.name))
                    input()
                    print("You say goodbye to Valery and watch as he heads back towards his car. Today was a good day.")
                    input()

        elif valery_ending_two_prompt in ['3']:
            print("“Man, I didn’t think I was that attractive. Guess I just hit a nerve with ya.”")
            print("""Cause I know it wasn't my personality that got you hooked, we had barely talked at that point.""")
            input()
            print("""You certainly aren't bad to look at either, although I generally weigh personality higher than looks, at least when it comes to serious relationships""")
            input()
            print("""Well, it's getting pretty late. Think we've been talking for a little over 5 hours, sure didn't feel like it though.""")
            print("""Guess we better think about heading out, we keep talking any longer we'll end up getting devoured by mosquitoes.""")
            input()
            print('Valery stands up before continuing to talk "Come here and give me a hug before we head back home."')
            input()
            print("(1): I was thinking of more than just a hug")
            print("(2): *Hug Valery* ")
            val_ending_two_prompt_two = input("Choose a response ")

            if val_ending_two_prompt_two in ['1']:
                print("Placeholder")

            elif val_ending_two_prompt_two in ['2']:
                print("You and Valery share a fairly long hug before saying your goodbyes.")
                print(
                    ' "I\'m sure I\'ll be seeing you around the neighborhood quite a bit now. Might even have to stop down at your house sometime." Valery says with a somewhat suggestive look.')
                print("See ya round then, {}".format(CharInfo.player_info.name))
                input()
                print("You say goodbye to Valery and watch as he heads back towards his car. Today was a good day.")
                input()

    def ending_three(self):
        print(
            "“The feeling is mutual. I wasn’t sure about taking our relationship any further than friends when we were talking in the restaurant, but when we got here and started talking a bit more in-depth I really started to enjoy my time with you.”")
        input()
        print(
            "“It’s been great getting to know you, never would have expected coming into this that I’d be leaving with a romantic interest in you.”")
        input()
        print("(1): It was a bit of a surprise for me as well. I figured that, at most, we'd part our lunch today as friends.")
        print("(2): Sometimes the best things in life come unexpectedly. Usually they just end up being the worst things in life, though. Like your employer firing you unexpectedly.")
        val_ending_three_prompt = input("Choose a response ")

        if val_ending_three_prompt in ['1']:
            print("""Yeah I guess that's just how life can be sometimes. Keeps you on your toes, I guess.""")
            input()
            print("""Well it's 5 PM now and we've been talking since we got at the restaurant at 12. It's been a great day but I suppose it's about time for us to head home.""")
            print("""Can't remember the last I was actually disappointed about having to go home. Now come here and give me a hug before we leave.""")
            input()
            print("You and Valery both stand up before hugging each other good bye.")
            print("""See ya round, {}. I'm sure I'll see you around the neighborhood. Plus we've still gotta talk about our next date.""".format(CharInfo.player_info.name))
            input()
            print("You say good bye to Valery and watch as he walks to his car. Blah blah more fluff later.")

        elif val_ending_three_prompt in ['2']:
            print("""Oh hell yeah. This is probably the best 'unexpected' thing to happen to me. Everything else? Trash. Nothing but pain and suffering.""")
            print("""It's hard for me to say that this one good thing outweighs the bad though, there's some real shit I've dealt with suddenly.""")
            input()
            print("Anyway, I think we've probably yakked on enough. It's 5 PM and we got at the restaurant at 12. We talk much longer and we'll be getting bit by mosquitoes.")
            input()
            print("""Can't remember the last I was actually disappointed about having to go home. Now come here and give me a hug before we leave.""")
            input()
            print("You and Valery both stand up before hugging each other goodbye.")
            print("""See ya round, {}. I'll be looking for you around the neighborhood. Plus we've still gotta talk about our next date.""".format(CharInfo.player_info.name))
            input()
            print("You say goodbye to Valery and watch as he walks to his car. Blah blah more fluff later.")

    def ending_four_bad(self):
        print(
            "“I’ll be honest, I like you. But I just don’t know if I can see us being a couple, you know? At least, not right now. I just don’t know you well enough.”")
        print(
            "“Maybe we can go on another date sometime, but for now though, no, I don’t feel the same you seem too. I don’t really see us being any more than friends.”")
        input()
        print("(1): I have to say, I'm a bit disappointed. But I understand, if you're not comfortable with dating me, that's fine.")  # Could take this to a weird end. Get into some real nice guy kind of stuff. Kind of makes me uncomfortable putting that kind of stuff into the game, though.
        print("(2): Really? If you weren't interested in me you could have just declined my invitation to come here...")  # I Feel like it might normalize that kind of behavior, nice guys and their like are not good people. Also doesn't really fit the character so let's not do that actually.
        val_ending_four_prompt = input("Choose a response ")

        if val_ending_four_prompt in ['1']:
            print("""I'm glad you took that as well as you did. I know there's some real pieces of work out there that go insane as soon as you deny them. I'm happy you're not one of them.""")
            print("""I wouldn't say this is a complete denial but... yeah honestly I just don't see us working out. So I guess it kind of is.""")
            input()
            print("Well I suppose we should head home, we've wasted enough time talking here. I hope we can at least part as friends.")
            input()
            print("(1): *Get up and reach out to shake his hand* Friends it is.")
            print("(2): I respect your choice, but I feel like it would just be awkward for us to keep hanging out.")
            val_denied_four_prompt = input("Choose a response ")

            if val_denied_four_prompt in ['1']:
                print("Valery reaches out and shakes your hand 'I'm glad you feel the same, {}. Hopefully I'll see you round the neighborhood!'".format(CharInfo.player_info.name))
                print("You say your goodbyes to Valery and tell him you're always glad to have another friend to count on.")
                input()
                print("More???")

            elif val_denied_four_prompt in ['2']:
                print("""I understand completely, there'd probably always be that thought in the back of our minds saying 'what if'.""")
                print("""Well suppose that's it. I'll be seeing you, {}.""".format(CharInfo.player_info.name))
                input()
                print("You say your goodbyes to Valery and head back to your car.")
                print("More???")

        elif val_ending_four_prompt in ['2']:
            print("""I thought that maybe I'd see something different in you here, but I didn't. It's not your fault, we just weren't made for each other.""")
            print("""Don't get me wrong, I don't hate you or anything. I just... don't really see a serious relationship between the two of us going anywhere.""")
            input()
            print("Valery reaches out his hand to you 'I hope we can stay friends, though.'")
            input()
            print("(1): *Get up and reach out to shake his hand* Friends it is.")
            print("(2): No. I don't think so. I doubt an ordinary relationship would work out either. Plus it would just be awkward.")
            val_hard_denied_four_prompt = input("Choose a response ")

            if val_hard_denied_four_prompt in ['1']:
                print(
                    "Valery reaches out and shakes your hand 'I'm glad you feel the same, {}. Hopefully I'll see you round the neighborhood!'".format(
                        CharInfo.player_info.name))
                print(
                    "You say your goodbyes to Valery and tell him you're always glad to have another friend to count on.")
                input()
                print("More???")

            elif val_hard_denied_four_prompt in ['2']:
                print("""That's unfortunate but I understand your choice. If you feel that way it's definitely best for both of us if we just stopped hanging out.""")
                print("""Suppose that's it then. Goodbye, {}""".format(CharInfo.player_info.name))
                input()
                print("You say bye to Valery and head back to your car.")
                input()
                print("More???")


class ValeryDateEndingTransistion:
    def ending_transition(self):
        pass






val_park = ValeryPark()
val_endings = ValeryEndings()