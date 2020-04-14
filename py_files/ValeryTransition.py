import os
import TravelSystem
import SaveSystem
import CharInfo
import MidChapBase

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class ValeryNeighborhoodWalk:
    def valery_first_walk(self):
        print("After a day of working on your road trip itinerary you decide to get some fresh air and go on a walk around the neighborhood.")
        input()
        print("It’s a beautiful day outside, the temperature is a refreshing 78 and there’s a slight breeze off the lake making this pretty much a perfect day.")
        input()
        print("You start your walk off by going your usual route, the road you take loops around so it doesn’t really matter which way you take.")
        input()
        print("The walk starts off pretty well, with nothing of note really happening.")
        print("As you walk you wave and say hi to the people you usually see walking a bout.")
        input()
        print("As you walk around the neighborhood you recall one of the houses near you being put up for rent recently, as you walk past it you see that the for rent sign has been taken out. Seems somebody’s renting it now.")
        input()
        print("You were somewhat familiar with the last person that lived there, you wouldn’t have considered yourselves friends, but you talked on occasion.")
        print("He moved away on pretty good terms fortunately, as he had recently gotten a job promotion that required him to relocate.")
        input()
        print("You’ll have to say hi to whoever moved in there if you see them around them neighborhood. You’re pretty familiar with everybody else in the nearby area so it shouldn’t be too difficult to spot them.")
        input()
        print("You’re about 75% down with your walk at this point, nothing spectacular has happened so far, it’s just your typical walk in the neighborhood.")
        input()
        print("As you walk down the hill that leads towards your house you see who you assume to be the person now renting the house down the street. Based off the fact that you’ve never seen him in the neighborhood until now.")
        input()
        print("You think about going over to introduce yourself, it seems a bit weird though, and if it turns he’s just some guy walking through the neighborhood you’ll have made a bit of ass of yourself.")
        input()
        print("You could also just ignore him. Then you wouldn’t have to worry about embarrassing yourself by waving down a random bloke on the street.")
        input()
        print("You think about it for a moment, deciding too...")
        valery_talk_or_ignore = input("(1): Introduce yourself and see where the conversation leads. \
                                       (2): Just go on your way and ignore him.  ")
        if valery_talk_or_ignore in ['1']:
            print("You say fuck it and decide to go over and say hi to who you presume to be neighbor. You figure that you aren’t really out anything if it ends up just being some guy off the street.")
            input()
            print("You wave him down from across the street and walk over to introduce yourself. This seems a bit odd in your mind, but if the roles were reversed you probably wouldn’t think too much of it.")
            print("You walk up to the slim-built hyena and ask him if he’s the new occupant of the house down the street.")
            input()
            print("“I am. Just moved in around 5 days ago.” the Hyena says in a somewhat surprised or perhaps confused tone.")
            input()
            print("You reach out to shake his hand and introduce yourself as {}. You tell him that you live just a few houses down the street from where his house is.".format(CharInfo.player_info.name))
            input()
            print("“I’m Valery, nice to meet you {}. You’re actually the first neighbor that I’ve met so far. Seems like nobody else had the same spunk that you did when it comes to meeting new neighbors”".format(CharInfo.player_info.name))
            input()
            print("“I do appreciate the initiative, it can be a bit unnerving moving somewhere and knowing absolutely no one. Just getting to know the names of the people around me helps me feel a bit more at ease.”")
            input()
            print("You tell Valery that you’re quite glad you could help him feel more at home.")
            print("You also tell Valery that if he needs anything to just let you know. You tell him which house yours is before saying goodbye.")
            input()
            print("“I’ll make sure to keep that in mind. Hopefully I’ll be seeing you around!”")
            input()
            print("You wave goodbye to the Hyena and continue on your walk.")
            print("As you finish your walk and return home nothing else happens. It was a fairly uneventful walk except for meeting Valery.")
            CharInfo.valery_checks.valery_first_walk = 'met'
            CharInfo.player_info.ending_points += 4
            TravelSystem.travel_points.tp.remove('A quick walk')
            input()
            clear()
            self.chapter_3_halfway_transistion()

        elif valery_talk_or_ignore in ['2']:
            print("You decide to just keep to yourself and leave him be. It would be a weird going over and bugging a stranger that’s just minding their own business.")
            input()
            print("You continue on your walk with nothing else happening. The walk was pretty uneventful.")
            CharInfo.valery_checks.valery_first_walk = 'ignore'
            CharInfo.player_info.ending_points -= 2
            TravelSystem.travel_points.tp.remove('A quick walk')
            input()
            clear()
            self.chapter_3_halfway_transistion()

        else:
            print("Invalid input.")
            return self.valery_first_walk()

    def chapter_3_halfway_transistion(self):
        if CharInfo.valery_checks.valery_first_walk in ['ignore', 'met']:
            print("After having went on a walk you can’t think of anything else that you needed to do today.")
            input()

        elif CharInfo.valery_checks.valery_first_walk not in ['ignore', 'met']:
            CharInfo.valery_checks.valery_first_walk = 'no walk'
            TravelSystem.travel_points.tp.remove('A quick walk')
            print("It's getting fairly late so you decide to just skip the walk and stay in for the rest of the day.")
            input()

        print("You've gotten the basic plan for your road trip down, now you've just gotta figure out who you're bringing.")
        input()

        if CharInfo.holly_checks.holly_relationship_status in ['dating']:
            print("You've also got that date with Holly to look forward to.")
            print("You're quite excited for it given how well the last one went.")
            input()

        elif CharInfo.holly_checks.holly_relationship_status in ['hold', 'rejected', 'ignored']:
            print("You also cleared things up in regards to Holly.")
            input()

            if CharInfo.holly_checks.holly_relationship_status in ['rejected']:
                print("She was probably taken back a bit by the rejection, but it's better to be upfront with your feelings rather than just ghosting her.")
                input()

            elif CharInfo.holly_checks.holly_relationship_status in ['hold']:
                print("Telling Holly you weren't interested in a relationship at the moment leaves things bit open. It wasn't an outright rejection so you could always try to rekindle things if you change your mind.")
                input()
                print("And it frees you up in regards to dating other people. But of course there's also no reason she can't go on other dates as well.")
                input()

            elif CharInfo.holly_checks.holly_relationship_status in ['ignored']:
                print("Just ignoring Holly probably wasn't the best way to deal with her, but it was definitely the easiest.")

        elif CharInfo.holly_checks.holly_relationship_status not in ['rejected', 'dating', 'hold'] and CharInfo.festival_checks.holly_stay is True:
            CharInfo.holly_checks.holly_relationship_status = 'ignored'
            print("You didn't really clear things up with Holly as much as you just ignored her.")
            input()
            print("Being ignored will upset her a bit. If you weren't interested in pursuing a relationship you probably would have been better off just saying so upfront.")
            input()
            CharInfo.player_info.ending_points -= 2

        if CharInfo.valery_checks.valery_first_walk in ['met']:
            print("You got to meet your new neighbor today as well. You'll have to go down to his apartment or meet up sometime and get to know him a bit better.")
            input()

        print("Well, You've still got plenty of time to figure everything out.")
        print("That's likely what you'll be doing for the next couple of weeks, just figuring out all the fine details of the trip.")
        input()
        print("Stuff like the finances and dealing with any plans you might have.")
        print("For now, you're just going to relax for a bit while you take everything in.")
        input()
        CharInfo.misc_checks.halfway_chap3 = True
        clear()
        print("It's been about 4 days since you started getting ready for your big road trip.")
        input()
        print("Since then you haven’t done anything too taxing. You spent about a day to just relax, and then worked on clearing any appointments or obligations you might have had during or leading up to the road trip.")
        input()
        print("Today you were thinking of sorting out the budget for the road trip. The money you have in your bank account now won’t be nearly enough for the whole road trip.")
        print("That means having to dip into your investments and savings. Not something you take lightly, but you feel that the experiences this trip will give you will be worth it.")
        input()
        print("Besides, you’ll probably be able to make up the difference by working on more contracts once you’re done with the road trip.")
        input()

        if CharInfo.valery_checks.valery_first_walk in ['met'] and CharInfo.player_info.ending_points <= -4:
            print("You were considering going to see Valery as well. Though you have to wonder if he would even welcome your company. You hardly know him, after all.")
            input()

        elif CharInfo.valery_checks.valery_first_walk in ['met'] and CharInfo.player_info.ending_points >= -4:
            print("You also thought of going to see if Valery needed help with anything. Might as well try and get to know your new neighbor some more.")
            input()

        if CharInfo.valery_checks.valery_first_walk in ['no walk'] and CharInfo.player_info.ending_points >= -2:
            print("You recently got a new neighbor as well. You could go down and meet him, see if he needs help with anything.")
            input()

        if CharInfo.valery_checks.valery_first_walk in ['ignored'] and CharInfo.player_info.ending_points >= -4:
            print("You could always go and introduce yourself to the new neighbor as well. Its not too late.")
            input()

        if CharInfo.valery_checks.valery_first_walk in ['met'] or CharInfo.valery_checks.valery_first_walk in ['ignored'] \
            and CharInfo.player_info.ending_points >= -4 or CharInfo.valery_checks.valery_first_walk in ['no walk'] \
            and CharInfo.player_info.ending_points >= -2:
            TravelSystem.travel_points.tp.append('Valery\'s House')
            CharInfo.misc_checks.valery_open = True
            CharInfo.valery_checks.valery_lunch = ''
            CharInfo.misc_checks.money_scene = ''
            print("Valery's House unlocked as travel option.")
            input()
        CharInfo.player_info.player_location = TravelSystem.travel_function.travel_point_mid_bedroom
        clear()
        SaveSystem.save_sys.saving()


class ValeryLunch:
    def valery_house(self):  # Is this enough content? If not how would I expand it?
        print("You decide to go and see how your new neighbor, Valery, is doing.")
        if CharInfo.valery_checks.valery_first_walk in ['met']:
            print("He seemed pretty nice when you met him on the walk.")
            input()
        else:
            print("Sasha already met him, which is how you found out he just moved in.")
            input()
        print("You walk down the street to his house. You have to knock on his door as he doesn’t seem to have a doorbell.")
        input()
        print("Valery answers the door; he seems to be a bit surprised by you visiting.")
        input()
        if CharInfo.valery_checks.valery_first_walk in ['met']:
            print("“Hey, {}. I was wondering if you were really going to come down or not.".format(
                CharInfo.player_info.name))
            input()
            print("“Unfortunately, you’ve come down at a pretty bad time, as I’ve got work in about half an hour.”")
            print(
                "“Maybe we can meet up for lunch or something in a couple of days? I’ve got the weekend off and no commitments so I’m pretty much free.”")
            input()

        else:
            print("“Uh, hello there. You are?”")
            input()
            print("You introduce yourself as {}, you tell him that you live in the house down the road, and that you’re Sasha’s roommate.".format(CharInfo.player_info.name))
            input()
            print("“Ah, well hello {}. I’m Valery but you probably already knew that from Sasha.”".format(CharInfo.player_info.name))
            print("“Nice of you to come down and say hello, but unfortunately, you’ve caught me at a bit of a bad time. As I’ve gotta go to work in about half an hour.”")
            print("“I’d love to get talk with you sometime though, maybe we can get lunch this weekend?”")
            input()

        if CharInfo.player_info.ending_points >= -4:
            print("Going out for lunch doesn’t sound too bad. It would probably be a better way to learn more about him anyway.")
            input()

        elif CharInfo.player_info.ending_points <= -4:
            print("You’re not quite sure how you feel about going out for lunch with someone you hardly know.")
            input()
            print("It feels like a bit of a rush to go from barely knowing your neighbor to going out and getting lunch.")
            input()

        print("You tell Valery that you…")
        if CharInfo.player_info.ending_points >= -4:
            print("(1): Would be down for getting lunch sometime this weekend.")

        elif CharInfo.player_info.ending_points <= -4:
            print("(1): Would be alright with going to get lunch. It wasn't exactly what you had in mind but you'll work with it.")

        if CharInfo.player_info.ending_points <= -4:
            print("(2): Don't really see the point in going to get lunch with someone you hardly know")

        elif CharInfo.player_info.ending_points >= -4:
            print("(2): Appreciate the offer but have other plans for this weekend.")

        valery_lunch_decision = input("")

        if valery_lunch_decision in ['1']:
            print("You tell Valery that getting lunch this weekend sounds good.")
            input()
            print("“Great! How about The Rat’s Place on Saturday?”")

            if CharInfo.holly_checks.holly_relationship_status in ['dating']:
                print("You don’t really have anything going on except for that date with Holly on Sunday. So that time should work well.")
                input()

            elif CharInfo.holly_checks.holly_relationship_status not in ['dating']:
                print("You don't have anything going on this weekend so that date should work well.")
                input()

            print("You tell Valery that The Rat's Place on Saturday will work great. You'll see him there around 12 PM.")
            input()
            print("“Awesome, see you Saturday!”")
            input()

            if CharInfo.holly_checks.holly_relationship_status not in ['dating']:
                print("You say goodbye to Valery and head back home.")
                input()

            elif CharInfo.holly_checks.holly_relationship_status in ['dating']:
                print("You say goodbye to Valery and head back home. Guess your weekend is pretty busy.")
                input()

            CharInfo.valery_checks.valery_lunch = True
            CharInfo.player_info.ending_points += 2
            clear()
            TravelSystem.travel_points.tp.remove('Valery\'s House')

            if CharInfo.misc_checks.money_scene in ['no investment', 'investments']:
                CharInfo.player_info.player_location = MidChapBase.last_of_chapter_3_transfer
                SaveSystem.save_sys.saving()
                MidChapBase.last_of_chapter_3_transfer()

            else:
                CharInfo.player_info.player_location = TravelSystem.travel_function.travel_point_mid_entranceway
                SaveSystem.save_sys.saving()
                TravelSystem.travel_function.travel_point_mid_entranceway()

        elif valery_lunch_decision in ['2']:

            if CharInfo.player_info.ending_points <= -4:
                print("You make up an excuse and tell Valery that you already have stuff going on this weekend. In reality you have plenty on time to go out this weekend, but you just don’t feel comfortable doing so.")
                input()

            elif CharInfo.player_info.ending_points >= -4 and CharInfo.holly_checks.holly_relationship_status in ['dating']:
                print("You tell Valery that you have some other stuff going on this weekend and that you won't able to go out for lunch.")
                input()
                print("Which isn't a total lie since you are going on a date with Holly this Sunday.")
                input()

            elif CharInfo.player_info.ending_points >= -4 and CharInfo.holly_checks.holly_relationship_status not in ['dating']:
                print("You tell Valery that you had some other plans for the weekend. Those plans may or may not be just sitting around the house and doing nothing, but he doesn’t need to know that.")
                input()

            print("“Aw, well that’s too bad. Maybe we can get lunch some other time.”")
            print("“Well, I better get moving, see you around.”")
            input()
            print("You say bye to Valery and head home.")
            input()
            CharInfo.valery_checks.valery_lunch = False
            CharInfo.player_info.ending_points -= 2
            clear()
            TravelSystem.travel_points.tp.remove('Valery\'s House')

            if CharInfo.misc_checks.money_scene in ['no investment', 'investment']:
                CharInfo.player_info.player_location = MidChapBase.last_of_chapter_3_transfer
                SaveSystem.save_sys.saving()
                MidChapBase.last_of_chapter_3_transfer()
            else:
                CharInfo.player_info.player_location = TravelSystem.travel_function.travel_point_mid_entranceway
                SaveSystem.save_sys.saving()
                TravelSystem.travel_function.travel_point_mid_entranceway()
        else:
            print("Invalid input")
            self.valery_house()





quick_walk = ValeryNeighborhoodWalk()

valery_lunch = ValeryLunch()