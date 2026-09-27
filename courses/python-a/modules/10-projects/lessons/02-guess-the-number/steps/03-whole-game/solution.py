secret = 7
guesses = [3, 10, 6, 7, 2]
tries = 0
while True:
    guess = guesses[tries]
    tries = tries + 1
    if guess > secret:
        print("Too big")
    elif guess < secret:
        print("Too small")
    else:
        print("You got it!")
        break
