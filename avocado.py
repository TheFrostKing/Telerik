# from rlcompleter import Completer


# def main():
#     options = [1, 2]
#     base_case = 3 - player
#     4, 5 - computer
#     6 - player
#     7 - computer
#     8 - computer
#     9 - player
#     10 - computer
#     11- computer
#     12 - player
#     13 - ...
#  (14 - 1) % 3  == 0  = False 


#     current_avocados_in_bucket = 14
#     if (current_avocados_in_bucket - 1) % 3 == 0:
#         current_avocados_in_bucket -= 1
#         return 1
#     current_avocados_in_bucket -= 2
#     return 2 
 

class Game():

    def __init__(self, number_of_avocados):
        self.number_of_avocados = number_of_avocados

    def start_game(self):
        print("Let the game begin!")
        current_turn = ""

        if self.number_of_avocados % 3 == 0:
            current_turn = 'player'
        else:
            current_turn = 'pc'

        while self.number_of_avocados > 0:
            if current_turn == 'player':
                print("It's player's turn.\n Please choose a number:\n")
                player_input = int(input())
                self.validate_user_input(player_input)
                print("Player has picked: %s" % player_input)
                self.number_of_avocados -= player_input
                print("Remaining number of avocados in bucket: %s" % self.number_of_avocados)
                if self.number_of_avocados == 0:
                    print("The winner is: %s" % current_turn)
                    return
                current_turn = 'pc'
                continue

            if current_turn == 'pc':
                print("It's computer's turn.")
                self.computers_turn()
                if self.number_of_avocados == 0:
                    print("The winner is: %s" % current_turn)
                    return
                current_turn = "player"


    def computers_turn(self):
        if (self.number_of_avocados - 1) % 3 == 0:
            print("Computer has picked: %s" % "1")
            self.number_of_avocados -= 1
            print("Remaining number of avocados in bucket: %s" % self.number_of_avocados)
            return

        print("Computer has picked: %s" % "2")
        self.number_of_avocados -= 2
        print("Remaining number of avocados in bucket: %s" % self.number_of_avocados)


    def validate_user_input(self, number_to_validate):
        if number_to_validate > 2 or number_to_validate < 1:
            raise ValueError("You must pick a value between 1 and 2.")


if __name__ == "__main__":
    avocados = int(input("Please choose number of avocados to add to the bucket: "))
    Game(avocados).start_game()
