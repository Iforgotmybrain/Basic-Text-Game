# Text game
import time
def rollintro ():
    print("In the beginning, there was nothing but this line of text")
    time.sleep(2)
    print ("But soon that changed, and the program began to develop")

def startingroom ():
    print("You are in a dimly-lit room, you see a light switch to your north")
    time.sleep(2)



rollintro()

playername = input("What is your name? >")

print("Hello {}" .format(playername))
time.sleep(3)
print("You are about to embark on a hastily made journey involving animal people")
time.sleep(3)
print("I'm not sure of the details quite yet, since I'm basically writing this as I go.")
time.sleep(3)
print("I'm sure it will be a perfectly coded, well wrote, masterpiece")
time.sleep(3)

print("But first, you must create your character")
time.sleep(3)
print("Your options are a Wolf, Fox, Lion, or Dragon")
time.sleep(2)
playerclass = input("Which do you choose?")
if playerclass in ['Wolf', 'wolf']:
    print("You have choose to be a Wolf")
elif playerclass in ['Fox', 'fox']:
    print("You have choose to be a Fox")
elif playerclass in ['Lion', 'lion']:
    print("You have choose to be a Lion")
elif playerclass in ['Dragon', 'dragon']:
    print("You have choose to be a Dragon")
time.sleep(2)
print("With that out of the way, let's get started")
