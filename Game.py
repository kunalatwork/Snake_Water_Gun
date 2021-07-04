from random import choice

print("Hello User,\nWelcome to Snake Water gun Game. You are going to play with computer and its a\ngame of 10 rounds. "
      "Who will win more no. of games from opponent. He will be the winner.\n")
choicenum = int(input("Let's get started\nTo continue - Press 1\nCancel = Press 2 \nChoose : "))

if choicenum == 1:
    Tround = 10
    CWin = 0
    UWin = 0
    while True:
        list = ["Snake", "Water", "Gun"]
        get = choice(list)
        Choice = get.lower()
        num = input("\nChoose one from Snake, Water, Gun\nChoose : ")
        UChoice = num.lower()
        # Snake
        if Choice == "snake" and UChoice == "water":
            print("You lose! Computer win")
            CWin = CWin + 1
        elif Choice == "snake" and UChoice == "gun":
            print("You Win! Computer Lose")
            UWin = UWin + 1
        elif Choice == "snake" and UChoice == "snake":
            print("Oops ! Match Tie")

        # Water
        elif Choice == "water" and UChoice == "water":
            print("Oops ! Match Tie")
        elif Choice == "water" and UChoice == "gun":
            print("You lose! Computer win")
            CWin = CWin + 1
        elif Choice == "water" and UChoice == "snake":
            print("You Win! Computer Lose")
            UWin = UWin + 1

        # Gun
        elif Choice == "gun" and UChoice == "water":
            print("You Win! Computer Lose")
            UWin = UWin + 1
        elif Choice == "gun" and UChoice == "gun":
            print("Oops ! Match Tie")
        elif Choice == "gun" and UChoice == "snake":
            print("You lose! Computer win")
            CWin = CWin + 1
        else:
            print("Invalid input")

        Tround = Tround - 1
        print(f"{Tround} rounds left out of 10")
        print(f"You {UWin} : Computer {CWin}\n")
        if Tround == 0:
            break
    print(f"Final Score \nYou {UWin} : Computer {CWin}")

    if UWin > CWin:
        print(f"You win! {UWin} : {CWin}")
    elif UWin < CWin:
        print(f"Computer win! {UWin} : {CWin}")


elif choicenum == 2:
    print("Thank you ! Please visit again")
else:
    print("Sorry!")
