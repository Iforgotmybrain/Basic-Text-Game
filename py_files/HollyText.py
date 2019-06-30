import SaveSystem
import CharInfo
import TravelSystem


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
        holly_relationship_option = input("(1): Ask Holly if she’d like to go another date sometime. \
        (2): Tell Holly that while you enjoyed last night you aren’t really interested in a relationship at the moment.\
        (3): Tell Holly that you just aren’t really interested in taking the relationship any further, as you didn’t really feel a strong connection with her.").lower()
        if holly_relationship_option in ['1']:
            print("You write up a message to Holly telling her that you really enjoyed your time spent together last night, and that you’d be interested in going on another date if she would be up for it.")
            input()
            print("You hesitate for a moment before sending the message, if she says yes who knows how far this relationship might end up going. It could end up limiting your options in the future.")
            input()
            print("But at the same time if you spent to much time waiting around she’ll probably think you aren’t interested in her. You’ve gotta capture the feeling before it’s gone.")
            input()
            print("You contemplate for a moment, eventually deciding to…")
            holly_one_option = input("(1): Sent the text (2): Erase the message and go back to the drawing board")

            if holly_one_option in ['1']:
                print("It’s been a long time since you’ve gotten along with someone as well as you did with Holly yesterday. You sent the text message and eagerly await her response.")

            elif holly_one_option in ['2']:
                return self.holly_text_decision()

        elif holly_relationship_option in ['2']:
            print("You write up a message to Holly, stating that while you enjoyed your time together last night, you aren’t really interested in pursuing a relationship right now.")
            input()
            print("You think about the message for a minute, this likely won’t completely erase any future relationship potential with Holly, but it will certainly put it on hold indefinitely.")
            input()
            print("After thinking about it, you decide to…")
            holly_two_option = input("(1): Sent the message (2): Go back to the drawing board")

            if holly_two_option in ['1']:
                print("You sent the message, you appreciated Holly’s company but you just aren’t down for a relationship at the moment, you want to keep your options open.")

            elif holly_two_option in ['2']:
                return self.holly_text_decision()

        elif holly_relationship_option in ['3']:
            print("You write up a text to Holly, you say in the message that you just didn’t feel connection with her yesterday, and that you aren’t interested in a relationship.")
            input()
            print("After deliberating for a moment, you think about the possible ramifications of this message. This will for certain end any possibility of a romantic relationship with Holly, though your regular relationship will still be intact. It might be a bit more awkward though.")
            input()
            print("You decide to…")
            holly_three_option = input("(1): Sent the message (2): Go back to the drawing board")

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

                if CharInfo.jacob_checks.jacob_post_fest is True and CharInfo.sasha_checks.sasha_post_fest is True and \
                        CharInfo.chris_checks.chris_computer_list_completed is True:
                    print("You put your phone back in your pocket, after dealing with Holly there's still plenty of time for that walk you were thinking about.")
                    input()
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_hallway()

                elif CharInfo.chris_checks.chris_computer_list_completed is not True:
                    print("You put your back in your pocket, you should probably check to see if you Chris has that list completed.")
                    input()
                    SaveSystem.save_sys.saving()
                    TravelSystem.travel_function.travel_point_hallway()

            elif holly_three_option in ['2']:
                return self.holly_text_decision()


holly_text_dialogue = HollyTextDialogue()

