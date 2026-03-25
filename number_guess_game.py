import random

def game(range):
    num = random.randint(0,range)
    attempts = 0

    while True :
        try:
            guess = int(input(f"Enter your guess (0-{range}) : "))
            attempts +=1

            if guess > num:
                print(f"Lower than {guess}")
            elif guess < num : 
                print(f"Higher than {guess}")
            else :
                print(f'Correct! Hurray , You guessed the right number {num} in {attempts} attempts.')
                break
                
        except:
            print("Please enter a valid number!")

    play()


def play_game():
    level = int(input('''Which difficulty level you like to play 
              1. Easy (1-100)
              2. Medium (1-500)
              3. Hard (1-1000)
              Enter the difficulty no: ''' ))

    if  0 < level < 4:
        match level: 
            case 1 : 
                game(100)
            case 2: 
                game(500)
            case 3:
                game(1000)
    else:
        print("Invalid Input")
        play_game()

def play():
    play = input("Play Again! ( Yes / No) : ")
    match play.lower():
        case 'yes' : 
            play_game()
        case 'no':
            print("Thank You, For trying this game. 👋")
            exit()
        case _:
            print("Thank you, to visit my game. 👋")
            exit()
    
play_game()
