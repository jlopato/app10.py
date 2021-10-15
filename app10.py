# Building A guesing Game:



secret_word = "coffee"

guess = ""



while guess !=secret_word:

    guess = input("Enter Guess: ")



print("congrats, you won")



--------

secret_word = "coffee"

guess = ""

guess_counter = 0

guess_limit = 3

out_guess = False



while guess !=secret_word and guess_counter < guess_limit:

    guess_counter+=1

    guess = input("Enter Guess: ")



if guess_counter == guess_limit and guess != secret_word:

    print("you lost")

else:

    print("congrats, you won")