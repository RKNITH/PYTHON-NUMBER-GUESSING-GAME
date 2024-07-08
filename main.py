import random
print("welcome to number guessing game")

print("I think a number between 1 to 100, guess waht is it")

num = random.randint(1, 100)
print(num)
HARD_LEVEL_TURNS =5
EASY_LEVEL_TURNS =10

def setDifficultyLevel():
    turns =input("enter the difficulty level ").lower()
    if turns == "easy":
        return EASY_LEVEL_TURNS
    elif turns =="hard":
        return HARD_LEVEL_TURNS

def compareNumber(guess, num, turn):
    if guess > num:
        print("Too High")
        return turn -1
    elif guess < num:
        print("Too Low")
        return turn -1
    elif guess == num:
        return "correct"  

tur =setDifficultyLevel()

is_game_on =True
while is_game_on:
    print(f" you have {tur} turns to guess the number")

    guess =int(input("guess the number "))

    result =compareNumber(guess, num, tur)

    if result =="correct":
        is_game_on =False
        print("You Got It")
    else:
        tur -=1
        if tur ==0:
            is_game_on =False
            print("you loose the game")    

            
        


