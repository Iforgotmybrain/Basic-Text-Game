import CharInfo


class ValeryPark:
    def park_start(self):
        print("You and Valery arrive at the park after a short walk. It’s fairly early into the evening and the park is fairly empty at the moment. Guess most people are probably still at work or at home at this point in the day.")
        input()
        print("“Never been to this park before. I usually go to the one on Gorge street if I want just chill or go for a quick walk.”")
        print("“So you wanna just sit down and chill for a bit? Because honestly, that sounds like the best time to me”")
        input()
        print("You decide to follow Valery’s lead and just sit down at a bench and talk for a bit.")
        input()
        print("“So…” Valery says, giving a serious look and a short pause between his next sentence.")
        input()
        print("“When was the last time you really spent time with someone, and really got to know them?”")
        input()
        print("(1): Well, not too long ago I got to spend some time with this old friend named Holly...")
        print("(2): It's been a long time since I've truly connected with someone.")
        print("(3): I suppose it was today, with you.")
        val_getting_know_response = input("Pick a response")

        if val_getting_know_response in ['1']:
            print("Yeah? Tell me some more about your time with her. You've been asking me questions all day, so now it's my turn.")
            input()
            print("You oblige Val and start to talk about your time spent at the festival with Holly.")
            input()
            print("The story starts with you meeting Holly at the lake festival concert, she surprised you quite a bit when she tapped on your shoulder and said hello.")  # Let's try first person dialogue. Breaks the rules but flip it.
            input()
            print("After that the two of you caught up a bit and talked about each other’s careers. That went on for around half an hour.")  # On second thought, let's not use first person that way. It's silly.
            if CharInfo.festival_checks.holly_stay is True:
                print("Towards the end of the bands set you asked Holly if she wanted to tag along with you for the rest of the night, lucky enough she said “sure”.")
                input()
                print("After the concert you and her checked out the rest of the festival.")
                print("You talked a bit about hobbies and played one of those rigged fair games as well. Towards the end of the day the two of you sat on the hood of Holly’s car and watched the fireworks.")
                input()
                if CharInfo.holly_checks.holly_relationship_status in ['dating']:
                    print("It was a great night, it reminded you of when the two of you used to hang out in high school. You wouldn’t have traded that night for anything.")
                    input()
                    print("“I’m guessing you met up with her again after that and it didn’t work out.”")
                    input()
                    print("(1): We haven't gone on any other dates after that. Although we were thinking of going on one this Sunday.")
                    print("(2): I actually didn’t setup another date. Didn’t want my options to be limited.")
                    val_dating_holly = input("Pick a response ")

                    if val_dating_holly in ['1']:
                        print("“I see. Well if anything happens between us I guess that’ll complicate things a bit, huh?’")
                        input()

                    elif val_dating_holly in ['2']:
                        print("“Sure, you had such a great time but didn’t set up another date with her. There’s gotta be a lie somewhere in there.”")
                        input()
                        CharInfo.valery_checks.valery_date_points -= 4

                elif CharInfo.holly_checks.holly_relationship_status in ['hold']:
                    print("It was a decent night, although ultimately you didn’t feel the same connection to her you used too.")
                    input()
                    print('"Yeah I\'ve found that tends to happen quite a bit. No point in continuing to date someone you don\'t think you\'ll get along with."')
                    input()

                elif CharInfo.holly_checks.holly_relationship_status in ['rejected']:
                    print("You can’t say it was the greatest night, in fact you’d say you were a bit disappointed. Holly just seemed like an entirely different person from who she used to be. You barely felt like friends, let alone anything more serious.")
                    input()
                    print('"That\'s too bad. I\'m guessing our time spent together today has gone a bit better than that if you wanted to talk with me some more."')
                    input()

                elif CharInfo.holly_checks.holly_relationship_status in ['ignored']:
                    print("While the night might have sounded nice, it was – in your mind, awful. Holly was as uninteresting as always and seemed to struggle to connect with you. The festival itself was just alright, but It ended up being a waste of time all things considered.")
                    input()
                    print('"Wow, that sounds terrible. I\'m guessing our time spent together today has gone a bit better than that if you wanted to talk with me some more."')
                    input()

            elif CharInfo.festival_checks.holly_stay is not True:
                print("Towards the end of the bands set you considered asking Holly if she wanted to tag along with for the rest of the night, but you decided to just go your separate ways.")
                print("You just weren’t feeling that strong of a connection to her, so you figured it was best to just let it be.")
                input()
                print("“So you knew towards the end that it just wasn’t going to work out, huh?”")
                print("“I’ve had that happen on quite a few dates myself. It’s a bit disappointing when you spend a couple of hours getting to know someone and then realizing they’re not really a good fit for you.”")
                input()
                print("“Can’t say that’s happened today, at least for me. And given that you wanted to talk to me some more, you probably feel the same way.”")
                input()

        elif val_getting_know_response in ['2']:
            print("“I can relate to that, unfortunately. I think the last time I truly felt intertwined with somebody was 4 years ago. And that only lasted for a few months.”")
            print("“I’ve had hookups here and there since then, of course. But none of them were people I wanted to spend the rest of my life with.”")
            input()

        elif val_getting_know_response in ['3']:
            print("“Honestly, I’d say the same thing. The last time I enjoyed being with someone this much was 4 years ago, if that tells you anything.”")
            input()




