import random

def play_game():
    cards = ['A','A','B','B','C','C','D','D']
    random.shuffle(cards)

    board = ["*"] * 8
    moves = 0

    while "*" in board:
        print("\nBoard:", board)

        try:
            first = int(input("First card (0-7): "))
            second = int(input("Second card (0-7): "))

            if first < 0 or first > 7 or second < 0 or second > 7:
                print("Invalid index!")
                continue

            if first == second:
                print("Same card!")
                continue

            if board[first] != "*" or board[second] != "*":
                print("Already opened!")
                continue

            board[first] = cards[first]
            board[second] = cards[second]

            print("Revealed:", board)

            if cards[first] == cards[second]:
                print("Match!")
            else:
                print("No match!")
                board[first] = "*"
                board[second] = "*"

            moves += 1

        except:
            print("Invalid input!")

    print("\nYou finished the game!")
    print(f"Total moves: {moves}")


# 🔁 RESTART SYSTEM
while True:
    play_game()
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Goodbye!")
        break