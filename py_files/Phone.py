import SaveSystem
import CharInfo
import TravelSystem


class PhonePlacement:
    def phone_placing(self):
        if CharInfo.festival_checks.holly_stay is True and CharInfo.holly_checks.holly_relationship_status not in ['rejected', 'dating', 'hold']:
            holly_text_dialogue.holly_text_one()

        elif CharInfo.holly_checks.holly_relationship_status in ['rejected', 'dating', 'hold']:
            print("You can't think of anyone to text or call right now.")
            input()
            return TravelSystem.travel_function.travel_point_bedroom()


class HollyTextDialogue:
    def holly_text_one(self):
        print("You hold your smartphone and pull up your contacts app, scrolling down until you hit the H column and find “Holly”.")
        input()
        print("You’ve never really been fond of calling people, so you decide to text her instead of calling.")
        print("You spent the next 20 minutes writing the perfect text, after much deliberation you decide to just keep it simple. You type up a simple greeting and tell Holly who it is that’s texting her, asking her what’s been going on since yesterday.")
        input()
        print("The next couple of minutes are spent browsing social media on your phone while you wait for a reply, soon your phone buzzes and a text message notification pops up on your screen")
        input()
        print("The contents of the message read: “Hey. Haven’t really been doing much, just doing stuff around my apartment")
        input()
        self.holly_text_decision()

    def holly_text_decision(self):
        print("You think a bit about what to write up next, eventually deciding too:")
        holly_relationship_option = input("(1): Ask Holly if she’d like to go on another date sometime. \
        (2): Tell Holly that while you enjoyed last night you aren’t really interested in a relationship at the moment.\
        (3): Tell Holly that you just aren’t really interested in taking the relationship any further, as you didn’t really feel a strong connection with her. ").lower()

        if holly_relationship_option in ['1']:
            print("You write up a message to Holly telling her that you really enjoyed your time spent together last night, and that you’d be interested in going on another date if she would be up for it.")
            input()
            print("You hesitate for a moment before sending the message, if she says yes who knows how far this relationship might end up going. It could end up limiting your options in the future.")
            input()
            print("But at the same time if you spent to much time waiting around she’ll probably think you aren’t interested in her. It's like thar Airplane Harness song went, 'You’ve only got so long to capture the feeling before it’s gone.'")
            input()
            print("You contemplate for a moment, eventually deciding to…")
            holly_one_option = input("(1): Sent the text (2): Erase the message and go back to the drawing board ").lower()

            if holly_one_option in ['1']:
                print("It’s been a long time since you’ve gotten along with someone as well as you did with Holly yesterday. You sent the text message and eagerly await her response.")
                input()
                print("She sends a reply quite quickly, you read the message with great anticipation, it says the following:")
                input()
                print('"I’d totally be down for another date. I had a fantastic time last night, we had some really good chemistry going on, I felt."')
                print('"I was thinking we could just get dinner together sometime next week. See where this thing goes from there."')
                input()
                print("You sent back a message saying that you’d be fine with getting dinner sometime. You also ask if she has any place in mind for dinner.")
                input()
                print("“I don’t know. I didn’t really think I’d get this far if I’m being honest.”")
                print("“Maybe a steakhouse? I dunno, but I’d be fine with going somewhere you want.”")
                input()
                print("You’ve been feeling like Mexican food recently, but you also wouldn’t mind going to the Firefly Tavern.")
                print("No better time then the present to pick a place to eat, you text Holly and tell her that you want to eat at…")
                holly_restaurant = input("(1). El Presidente’s Palace, the Mexican restaurant. \
                (2). Polo’s Steakhouse \
                (3). Firefly Tavern ").lower()

                if holly_restaurant in ['1']:
                    print('"Mexican food sounds good, I’m down for that."')
                    CharInfo.holly_checks.holly_date_restaurant = 'mexican'
                    input()

                elif holly_restaurant in ['2']:
                    print('"Aw, you’re just going there because I mentioned it aren’t you?"')
                    print('"It’s fine though, I mentioned it for a reason."')
                    input()
                    CharInfo.holly_checks.holly_date_restaurant = 'steakhouse'
                    input()

                elif holly_restaurant in ['3']:
                    print('"Never been there, guess I’ll just have to trust your judgement in food."')
                    CharInfo.holly_checks.holly_date_restaurant = 'tavern'
                    input()

                else:
                    print("Invalid input")
                    return self.holly_text_decision()

                print('"Now we’ve just gotta figure out a time and date, Lemme just make sure I don’t have anything coming up real quick."')
                input()
                print("You know for a fact that you don’t have anything upcoming, so pretty much anytime would work.")
                input()
                print('"How about next Thursday at around 6 PM? Should give us some extra time after dinner, and we should be able to avoid a long wait time."')
                input()
                print("You tell Holly that the time will work great and that you’re looking forward to it.")
                input()
                print('"Same, if it’s anything like yesterday I’m sure it will be great."')
                input()
                print("The texts slow down shortly after that, with just some back and forth conversation throughout the rest of the day.")
                input()
                CharInfo.holly_checks.holly_relationship_status = 'dating'
                CharInfo.player_info.ending_points += 2

                if CharInfo.chris_checks.chris_computer_list_completed is True:
                    print(
                        "You put your phone back in your pocket, after setting up your date with Holly there's still plenty of time for that walk you were thinking about.")
                    input()
                    print("Of course you could also just call it a day and forget the walk if you wanted.")
                    print("If you want to call it a day you should probably head to your bedroom and Sleep.")
                    input()
                    TravelSystem.travel_points.tp.append('A quick walk')
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_bedroom()

                elif CharInfo.chris_checks.chris_computer_list_completed is not True:
                    print(
                        "You put your back in your pocket, you should probably check to see if you Chris has that list completed.")
                    input()
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_bedroom()

            elif holly_one_option in ['2']:
                return self.holly_text_decision()

            else:
                print("Invalid input")
                return self.holly_text_decision()

        elif holly_relationship_option in ['2']:
            print("You write up a message to Holly, stating that while you enjoyed your time together last night, you aren’t really interested in pursuing a relationship right now.")
            input()
            print("You think about the message for a minute, this likely won’t completely erase any future relationship potential with Holly, but it will certainly put it on hold indefinitely.")
            input()
            print("After thinking about it, you decide to…")
            holly_two_option = input("(1): Sent the message (2): Go back to the drawing board ").lower()

            if holly_two_option in ['1']:
                print("You sent the message, you appreciated Holly’s company but you just aren’t down for a relationship at the moment, you want to keep your options open.")
                input()
                print("She quickly replies, her message says: “That’s fine, I understand completely.”")
                print("“I appreciate you saying that up front rather than just stringing me along.”")
                input()
                print("You tell Holly that you wouldn’t’ think of just leaving her out in the air. Even if your relationship doesn’t go anywhere else you still want to remain friends, after all.")
                input()
                print('"I get it, I’m fine with just being friends. If circumstances change I wouldn’t say no to another date, though."')
                input()
                print("You reply and tell Holly that you’ll keep it in mind, the grass isn’t always greener on the other side.")
                print("The conversation ends fairly quickly after that message.")
                input()
                CharInfo.holly_checks.holly_relationship_status = 'hold'

                if CharInfo.chris_checks.chris_computer_list_completed is not True:
                    print(
                        "You put your back in your pocket, you should probably check to see if Chris has that list completed.")
                    input()
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_bedroom()

                elif CharInfo.chris_checks.chris_computer_list_completed is True:
                    print(
                        "You put your phone back in your pocket, after dealing with Holly there's still plenty of time for that walk you were thinking about.")
                    input()
                    print("Of course you could also just call it a day and forget the walk if you wanted.")
                    print("If you want to call it a day you should probably head to your bedroom and Sleep.")
                    input()
                    TravelSystem.travel_points.tp.append('A quick walk')
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_bedroom()

            elif holly_two_option in ['2']:
                return self.holly_text_decision()

            else:
                print("Invalid input")
                return self.holly_text_decision()

        elif holly_relationship_option in ['3']:
            print("You write up a text to Holly, you say in the message that you just didn’t feel connection with her yesterday, and that you aren’t interested in a relationship.")
            input()
            print("After deliberating for a moment, you think about the possible ramifications of this message. This will for certain end any possibility of a romantic relationship with Holly, though your regular relationship will still be intact. It might be a bit more awkward though.")
            input()
            print("You decide to…")
            holly_three_option = input("(1): Sent the message (2): Go back to the drawing board ").lower()

            if holly_three_option in ['1']:
                print("You sent the message. It’s nothing against her as a person, she just wasn’t a good match for you.")
                input()
                print("She sends a reply fairly quickly; “Wow, I’m a bit surprised to hear that. I understand though, no point in going any further if there’s in no interest.")
                input()
                print("“I appreciate you telling me that though, better than just ghosting me.”")
                input()
                print("You thank Holly for understanding. You send her a text telling her that you’re still fine with being friends, so long as doesn’t find that too awkward.")
                input()
                print("“No, I’m fine with just being friends. It’s not like we broke up or anything. We basically only went on one ‘date’ after all.”")
                input()
                print("You sent a text thanking Holly again for understanding, telling her to have good rest of the day.")
                input()
                print("“Of course, same to you.”")
                CharInfo.holly_checks.holly_relationship_status = 'rejected'
                input()

                if CharInfo.chris_checks.chris_computer_list_completed is True:
                    print("You put your phone back in your pocket, after dealing with Holly there's still plenty of time for that walk you were thinking about.")
                    input()
                    print("Of course you could also just call it a day and forget the walk if you wanted.")
                    print("If you want to call it a day you should probably head to your bedroom and Sleep.")
                    input()
                    TravelSystem.travel_points.tp.append('A quick walk')
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_bedroom()

                elif CharInfo.chris_checks.chris_computer_list_completed is not True:
                    print("You put your back in your pocket, you should probably check to see if you Chris has that list completed.")
                    input()
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_bedroom()

            elif holly_three_option in ['2']:
                return self.holly_text_decision()

            else:
                return self.holly_text_decision()
        else:
            print("Invalid input")
            return self.holly_text_decision()


smart_phone_placement = PhonePlacement()

holly_text_dialogue = HollyTextDialogue()

