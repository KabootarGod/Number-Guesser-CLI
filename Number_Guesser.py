import random
import json

num = random.randint(1,100)

def prnthigh():
    with open("highscores.json", 'r') as file:
        data = json.load(file)
        print(data)


print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (7 chances)
2. Medium (5 chances)
3. Hard (3 chances)

To view the leaderboard:
Type 4
      """)
diff = int(input("Enter your choice: "))
chances = int()

match diff:
    case 1:
        chances = 7
    case 2:
        chances = 5
    case 3:
        chances = 3
    case 4:
        prnthigh()
        exit()
    case _:
        print("Invalid Input")
        exit()
ini = chances

while chances != 0:
    guess = int(input("Enter your guess: "))
    if guess < num:
        print(f"Incorrect! The guess is greater than {guess}")
        chances -= 1
    elif guess > num:
        print(f"Incorrect! The guess is less than {guess}")
        chances -= 1
    else:
        print(f"Congratulations! You guessed the correct number in {ini-chances+1} attempts")
        name = input("Enter Your name: ")
        with open("highscores.json", 'r+') as file:
            data = json.load(file)
            '''
            try data[name] > ini-chances:
                data.update({name:ini-chances})
                file.close()
            except KeyError:
                pass'''
            try:
                last_score = data[name]
                if last_score > ini-chances:
                    data.update({name:ini-chances})
            except KeyError:
                data.update({name:ini-chances})
        with open("highscores.json", 'w') as f:
            json.dump(data, f, indent=4)
        break


if chances == 0:
    print("Lol! You lost, better luck next time.")
