import pickle


class GameState:

    #def saving(self):
     #   pickle_out = open('testing.pickle', 'wb')
      #  pickle.dump(testing_test.mysalsa, pickle_out)
    #    pickle_out.close()
      #  print("File Saved!")

    def loading(self):
        pickle_in = open('testing.pickle', 'rb')
        testing_test.mysalsa = pickle.load(pickle_in)
        print(testing_test.mysalsa)

class testing:
   def __init__(self):
       self.uknow = False

testing_test = testing()
game_test = GameState()

#gameyes = input("Enter save")
#if gameyes == "yes":
  #  game_test.saving()

gameno = input("Enter Load")
if gameno == "yes":
    game_test.loading()





