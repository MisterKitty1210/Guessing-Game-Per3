import random
import time


def main():
    play = True
    print("Welcome to the Guessing Game!")
    time.sleep(1)
    while play:
        print("1. Easy \t 2. Medium \t 3. Hard\n")
        difficulty = input("What difficulty level?")
        if difficulty == 1:
            play = easy()
        elif difficulty == 2:
            play = medium()
        else:
            play = hard()


def easy():
    while play == True:
        time.sleep(1)
        p1count1 = 1
        variable1 = random.randrange(1, 11)
        print("ROUND 1")
        guess = input("Player 1: Guess a number between one and ten.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p1count1 = p1count1 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p1count1 = p1count1 + 1
        p1count1 = str(p1count1)
        print("\nYou got it!\n"
              "It took you " + p1count1 + " tries to guess the number!\n")
        time.sleep(1)
        p2count1 = 1
        variable1 = random.randrange(1, 11)
        guess = input("Player 2: Guess a number between one and ten.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p2count1 = p2count1 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p2count1 = p2count1 + 1
        p2count1 = str(p2count1)
        print("\nYou got it!\n"
              "It took you " + p2count1 + " tries to guess the number!\n")
        time.sleep(1) #END OF 1ST ROUND
        p1count2 = 1
        variable1 = random.randrange(1, 11)
        print("ROUND 2")
        guess = input("Player 1: Guess a number between one and ten.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p1count2 = p1count2 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p1count2 = p1count2 + 1
        p1count2 = str(p1count2)
        print("\nYou got it!\n"
              "It took you " + p1count2 + " tries to guess the number!\n")
        time.sleep(1)
        p2count2 = 1
        variable1 = random.randrange(1, 11)
        guess = input("Player 2: Guess a number between one and ten.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p2count2 = p2count2 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p2count2 = p2count2 + 1
        p2count2 = str(p2count2)
        print("\nYou got it!\n"
              "It took you " + p2count2 + " tries to guess the number!\n")
        time.sleep(1) #END OF 2
        p1count3 = 1
        variable1 = random.randrange(1, 11)
        print("ROUND 3")
        guess = input("Player 1: Guess a number between one and ten.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p1count3 = p1count3 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p1count3 = p1count3 + 1
        p1count3 = str(p1count3)
        print("\nYou got it!\n"
              "It took you " + p1count3 + " tries to guess the number!\n")
        time.sleep(1)
        p2count3 = 1
        variable1 = random.randrange(1, 11)
        guess = input("Player 2: Guess a number between one and ten.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p2count3 = p2count3 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and ten.")
                    p2count3 = p2count3 + 1
        p2count3 = str(p2count3)
        print("\nYou got it!\n"
              "It took you " + p2count3 + " tries to guess the number!\n")
        p1count = int(p1count1) + int(p1count2) + int(p1count3)
        p2count = int(p2count1) + int(p2count2) + int(p2count3)
        p1count = str(p1count)
        p2count = str(p2count)
        if p1count < p2count:
            print("Player 1 took " + p1count + " tries to get it three times.\n"
                  "Player 2 took " + p2count + " tries to get it three times.\n"
                  "Player 1 wins.")
        elif p1count == p2count:
            print("Both players took the same number of guesses. It is a tie.")
        else:
            print("Player 1 took " + p1count + " tries to get it three times.\n"
                  "Player 2 took " + p2count + " tries to get it three times.\n"
                  "Player 2 wins.")
        print("\nWould you like to play again?(Y/N)")
        choice = raw_input("Please enter your choice.\n")
        if choice == "Y" or choice =='y':
            return True
        else:
            print("Goodbye.")
            return False


def medium():
    while play == True:
        time.sleep(1)
        p1count1 = 1
        variable1 = random.randrange(1, 21)
        print("ROUND 1")
        guess = input("Player 1: Guess a number between one and twenty.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p1count1 = p1count1 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p1count1 = p1count1 + 1
        p1count1 = str(p1count1)
        print("\nYou got it!\n"
              "It took you " + p1count1 + " tries to guess the number!\n")
        time.sleep(1)
        p2count1 = 1
        variable1 = random.randrange(1, 21)
        guess = input("Player 2: Guess a number between one and twenty.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p2count1 = p2count1 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p2count1 = p2count1 + 1
        p2count1 = str(p2count1)
        print("\nYou got it!\n"
              "It took you " + p2count1 + " tries to guess the number!\n")
        time.sleep(1) #END OF 1ST ROUND

        p1count2 = 1
        variable1 = random.randrange(1, 21)
        print("ROUND 2")
        guess = input("Player 1: Guess a number between one and twenty.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p1count2 = p1count2 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p1count2 = p1count2 + 1
        p1count2 = str(p1count2)
        print("\nYou got it!\n"
              "It took you " + p1count2 + " tries to guess the number!\n")
        time.sleep(1)
        p2count2 = 1
        variable1 = random.randrange(1, 21)
        guess = input("Player 2: Guess a number between one and twenty.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p2count2 = p2count2 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p2count2 = p2count2 + 1
        p2count2 = str(p2count2)
        print("\nYou got it!\n"
              "It took you " + p2count2 + " tries to guess the number!\n")
        time.sleep(1) #END OF 2


        p1count3 = 1
        variable1 = random.randrange(1, 21)
        print("ROUND 3")
        guess = input("Player 1: Guess a number between one and twenty.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p1count3 = p1count3 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p1count3 = p1count3 + 1
        p1count3 = str(p1count3)
        print("\nYou got it!\n"
              "It took you " + p1count3 + " tries to guess the number!\n")
        time.sleep(1)
        p2count3 = 1
        variable1 = random.randrange(1, 21)
        guess = input("Player 2: Guess a number between one and twenty.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p2count3 = p2count3 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and twenty.")
                    p2count3 = p2count3 + 1
        p2count3 = str(p2count3)
        print("\nYou got it!\n"
              "It took you " + p2count3 + " tries to guess the number!\n")
        p1count = int(p1count1) + int(p1count2) + int(p1count3)
        p2count = int(p2count1) + int(p2count2) + int(p2count3)
        p1count = str(p1count)
        p2count = str(p2count)
        if p1count < p2count:
            print("Player 1 took " + p1count + " tries to get it three times.\n"
                  "Player 2 took " + p2count + " tries to get it three times.\n"
                  "Player 1 wins.")
        elif p1count == p2count:
            print("Both players took the same number of guesses. It is a tie.")
        else:
            print("Player 1 took " + p1count + " tries to get it three times.\n"
                  "Player 2 took " + p2count + " tries to get it three times.\n"
                  "Player 2 wins.")
        print("\nWould you like to play again?(Y/N)")
        choice = raw_input("Please enter your choice.\n")
        if choice == "Y" or choice =='y':
            return True
        else:
            print("Goodbye.")
            return False

def hard():
    while play == True:
        time.sleep(1)
        p1count1 = 1
        variable1 = random.randrange(1, 101)
        print("ROUND 1")
        guess = input("Player 1: Guess a number between one and one hundred.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p1count1 = p1count1 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p1count1 = p1count1 + 1
        p1count1 = str(p1count1)
        print("\nYou got it!\n"
              "It took you " + p1count1 + " tries to guess the number!\n")
        time.sleep(1)
        p2count1 = 1
        variable1 = random.randrange(1, 101)
        guess = input("Player 2: Guess a number between one and one hundred.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p2count1 = p2count1 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p2count1 = p2count1 + 1
        p2count1 = str(p2count1)
        print("\nYou got it!\n"
              "It took you " + p2count1 + " tries to guess the number!\n")
        time.sleep(1) #END OF 1ST ROUND
        p1count2 = 1
        variable1 = random.randrange(1, 101)
        print("ROUND 2")
        guess = input("Player 1: Guess a number between one and one hundred.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p1count2 = p1count2 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p1count2 = p1count2 + 1
        p1count2 = str(p1count2)
        print("\nYou got it!\n"
              "It took you " + p1count2 + " tries to guess the number!\n")
        time.sleep(1)
        p2count2 = 1
        variable1 = random.randrange(1, 101)
        guess = input("Player 2: Guess a number between one and one hundred.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p2count2 = p2count2 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p2count2 = p2count2 + 1
        p2count2 = str(p2count2)
        print("\nYou got it!\n"
              "It took you " + p2count2 + " tries to guess the number!\n")
        time.sleep(1) #END OF 2
        p1count3 = 1
        variable1 = random.randrange(1, 101)
        print("ROUND 3")
        guess = input("Player 1: Guess a number between one and one hundred.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p1count3 = p1count3 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p1count3 = p1count3 + 1
        p1count3 = str(p1count3)
        print("\nYou got it!\n"
              "It took you " + p1count3 + " tries to guess the number!\n")
        time.sleep(1)
        p2count3 = 1
        variable1 = random.randrange(1, 101)
        guess = input("Player 2: Guess a number between one and one hundred.")
        while guess != variable1:
            if guess < variable1:
                    print("\nHigher. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p2count3 = p2count3 + 1
            if guess > variable1:
                    print("\nLower. Guess again.")
                    guess = input("Guess a number between one and one hundred.")
                    p2count3 = p2count3 + 1
        p2count3 = str(p2count3)
        print("\nYou got it!\n"
              "It took you " + p2count3 + " tries to guess the number!\n")
        p1count = int(p1count1) + int(p1count2) + int(p1count3)
        p2count = int(p2count1) + int(p2count2) + int(p2count3)
        p1count = str(p1count)
        p2count = str(p2count)
        if p1count < p2count:
            print("Player 1 took " + p1count + " tries to get it three times.\n"
                  "Player 2 took " + p2count + " tries to get it three times.\n"
                  "Player 1 wins.")
        elif p1count == p2count:
            print("Both players took the same number of guesses. It is a tie.")
        else:
            print("Player 1 took " + p1count + " tries to get it three times.\n"
                  "Player 2 took " + p2count + " tries to get it three times.\n"
                  "Player 2 wins.")
        print("\nWould you like to play again?(Y/N)")
        choice = raw_input("Please enter your choice.\n")
        if choice == "Y" or choice =='y':
            return True
        else:
            print("Goodbye.")
            return False

play = True
main()
