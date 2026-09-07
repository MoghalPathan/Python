#write a program to create a mini project on snake, water, gun



def game(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

def main():
    import random
    print("Comp Turn: Snake(s), Water(w), Gun(g)")
    randNo = random.randint(0, 2)
    if randNo == 0:
        comp = 's'
    elif randNo == 1:
        comp = 'w'
    elif randNo == 2:
        comp = 'g'

    you = input("Your Turn: Snake(s), Water(w), Gun(g): ")
    result = game(comp, you)

    print(f"Computer chose: {comp}")
    print(f"You chose: {you}")

    if result is None:
        print("It's a tie!")
    elif result:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()

