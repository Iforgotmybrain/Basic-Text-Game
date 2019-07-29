

def testingstuff():
    while True:
        print("These are the options:")
        print("(1)")
        print("(2)")
        test = input("Pick one")

        if test in ['1']:
            print("Redirecting")
            input()
            print("Test stuff to see if this works")
            print("test test")
            return

        elif test in ['2']:
            print("Testing test test")
            print("Does this work as intended?")
            print("Guess I'll see")
            input()


testingstuff()