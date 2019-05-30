import Base


class ToriesCafe:
    def __init__(self):
        self.cafefinished = False

    def thecafe(self):
        print("You catch a ride on the bus and end up at Tories Place, your all-time favorite place to grab lunch")
        print(
            "It’s a popular place amongst the younger crowd. The place has a modern aesthetic with colorful furniture and ample natural lighting giving the place a cheery vibe.")
        input()
        print("They’re famous for their fantastic wraps, and also have some pretty good soups.")
        print(
            "Looking around you see the line to order, it’s a bit after lunch so there isn’t much of a wait. You also see a familiar face sitting down at one of the tables")
        cafedecision = input("Will you order first or go and say hi to the familiar face? ").lower()
        if cafedecision in ['order', 'eat', ]:
            print("You decide to order some food before going to say hi.")
            print("The line moves quick and before you know it’s your turn to order.")
            input()
            print(
                "You decide to order your usual combo; a tuna wrap with a bag of chips and a drink. Not a bad deal for $4!")
            print("Having ordered your food, you head over to the table of Holly, a friend of yours from high school.")
            print(
                "Holly is a vixen, no, not like that. In the literal sense. You’ve known her since high school and while you haven’t really been in contact much since then, you still consider her to be a friend, albeit a distant one.")
            input()
            print(
                "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that's no replacement for a proper conversation.")
            print(
                '"Hey {}, Its been a while hasn\'t it? Last time I saw you was a few years ago when we to King\'s Point with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!"'.format(
                    Base.player_info.name))  # Yes, I really did just combine the names of Cedar Point and King's Island to make King's Point
            input()
            print(
                "You fill in some details about what you’ve been up too since that trip. Detailing your current living situation with Sasha and Jacob and what you've been up too.")
            print(
                "You ask what Holly’s been up too since then, a faint look of discomfort fills her face as she describes her falling out from college")
            input()
            print(
                '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because I sucked at it, I just wasn’t enjoying it. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life"')
            print(
                '"Like I said, my grades weren’t bad enough too have them kick me out, but they weren’t great either. I was holding about a 2.5 (out of 4) GPA"')
            input()
            print(
                "You nod in agreement, remembering how many times you second guessed your major choice throughout college")
            input()
            print(
                '"And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
            input()
            print(
                "You can definitely see yourself agreeing with Holly’s decision, thinking back to all the workplace drama and rejected proposals you’ve dealt with…")
            print(
                "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer.")
            input()
            print(
                '"I draw art for a living now! I’ve always been interested in drawing; I’m sure you remember some of my art from back in high school. I never really thought of it as a legitimate career path but I’ve managed to find a niche that pays a decent amount of money through commissions."')
            print(
                '"I love it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
            input()
            print(
                '"So, what have you been doing since graduating college? I know you finished college with a couple internships under your belt and a great GPA, so that’s had to have gotten you somewhere right?"')
            input()
            print(
                "You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons that Holly has already stated, like project managers ignoring ideas.")
            print(
                "You state that you had luckily saved up enough money to live comfortably for around 2 years before you quit. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
            input()
            print(
                "'Man, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine having a savings large enough to live off of for 2 years. Let alone being able to amass that much money by only working for a year and half!'")
            print(
                "'Still, like I said, I enjoy my work and I wouldn’t want it any other way. Within reason of course.'")
            input()
            print(
                '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around."'.format(
                    Base.player_info.name))
            print("You say goodbye to Holly and decide to head home for the day")
            input()
            self.cafefinished = True
            Base.hallway()
        elif cafedecision in ['talk', 't', 'face' 'hi']:
            print("You decide to first go over and say hi to Holly.")
            print(
                "Holly is a vixen, no, not like that. In the literal sense. You’ve known her since high school and while you haven’t really been in contact much since college, you still consider her to be a friend, albeit a distant one.")
            input()
            print(
                "You exchange greetings with Holly and start conversing. There’s a lot of catching up to do, you follow each other on social media but of course that isn’t a replacement for proper conversation.")
            print(
                '"Hey {}! Last time I saw you was when we went to the amusement park your sophomore year of college with a bunch of other high school friends. And the last I saw you regularly was back before you went off to college in 2014!"'.format(
                    Base.player_info.name))
            input()
            print(
                "You fill in some details about what you’ve been up too since that amusement park trip. Detailing your current living situation with Sasha and Jacob, as well as talking about your various college antics")
            print(
                "You ask what Holly’s been up too since then, a faint look of worry and disappointment fills her face as she describes her falling out from college")
            input()
            print(
                '"Yeah, I dropped out of college at the end of 2016. Believe it or not it wasn’t because of my grades, I just wasn’t enjoying college. I know that’s a pretty shit reason to drop out, but I just couldn’t see myself doing another 2 years there. Nor could I see myself being a marketer for the rest of my life"')
            print(
                '"Like I said, my grades weren’t bad enough too have them kick me out, but they weren’t great either. I was holding about a 2.5 (out of 4) GPA"')
            input()
            print(
                "You nod in agreement, remembering how many times you second guessed your major choice throughout college")
            input()
            print(
                '"And as far as being a marketer goes, I knew I would have hated it and the corporate culture that surrounds it. Having to stick up to execs, deliver presentations on ideas that would ultimately be ignored by the project managers and higher-ups. Dealing with the petty workplace drama… That just wasn’t for me."')
            input()
            print(
                "You can definitely see yourself understanding Holly’s decision, thinking back at all the workplace drama and rejected proposals you’ve dealt with…")
            print(
                "You ask Holly what she’s doing for work since she dropped out of college, she offers a surprising answer")
            input()
            print(
                '"I draw art for a living now! I’ve always been interested in drawing before, I’m sure you remember some of my drawings from back in high school. I never really thought of it as a legitimate career path, but I’ve managed to find a niche that pays a decent amount of money through commissions."')
            print(
                '"I love it. The customer tells me what they want, I draw it, and we go on our way. There’s (typically) no bullshit, and no one else telling me what to do."')
            input()
            print(
                '"So, what have been doing since graduating college? I know you finished with couple internships and a great GPA, so that’s had to have gotten you somewhere right?"')
            input()
            print(
                "You explain that you used to work for a local big business, but eventually quit for various reasons, including reasons she stated, like project managers ignoring ideas.")
            print(
                "You state that you had luckily saved up enough money to live comfortably for around 2 years before quitting. You talk about how you now do freelance work off and on, not unlike what Holly does. It helps keep a steady flow of money coming into your bank account. And with living expenses being split between three people, you really don’t need much money to support your lifestyle.")
            input()
            print(
                '"Man, that’s fantastic. Hearing stuff like that almost makes me wish I would have stayed in college. I couldn’t imagine being able to have a savings large enough to live on for 2 years. Let alone being able to amass that much money by only working for a year and half!"')
            print('"Still, like I said, I enjoy my work and I wouldn’t want it any other way."')
            input()
            print(
                '"Well {}, it’s been fantastic talking but I’ve got a yoga class coming up in a half hour so I’ve gotta run. Hopefully I’ll see you around."'.format(
                    Base.player_info.name))
            print("You say goodbye to Holly and decide to head home for the day")
            input()
            self.cafefinished = True
            Base.hallway()
        else:
            print("Invalid input")
            return self.thecafe()
