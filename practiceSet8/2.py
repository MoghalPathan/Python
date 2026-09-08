# the game function in computer lets user play game and returs the score as an integer.
# You need to read a file "hiscore.txt" which is either blank or contains the previous hiscore. 
# you need to write a program to update the hiscore whenever the function game() breaks the high score.

import random

def get_high_score():
    try:
        with open("highscore.txt") as f:
            content = f.read().strip()
            return int(content) if content else 0

    except FileNotFoundError:
        return 0

def update_high_score(new_score):
    with open("highscore.txt", "w") as f:
        f.write(str(new_score))

def game():
    """Placeholder: simulates a game and returns a score."""
    score = random.randint(0, 100)
    print(f"You scored: {score}")
    return score

def main():
    high_score = get_high_score()
    score = game()   

    if(score>high_score):
        print(f"New high score!{score} beats old score of {high_score}.")
    else:
        print(f"score: {score}. High Score reamins {high_score} ")   


if __name__ == "__main__":
    main()                  
    