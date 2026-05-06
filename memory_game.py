import random

cards = ['A','A','B','B','C','C','D','D']
random.shuffle(cards)

board = ["*"] * 8
moves = 0

while "*" in board:
    print("\nBoard:", board)

    try:
        first = int(input("First card (0-7): "))
        second = int(input("Second card (0-7): "))

        # kontrol 1: aralık kontrolü
        if first < 0 or first > 7 or second < 0 or second > 7:
            print("Invalid index! Choose between 0-7.")
            continue

        # kontrol 2: aynı kart seçimi
        if first == second:
            print("You cannot pick the same card!")
            continue

        # kontrol 3: açık kart seçimi
        if board[first] != "*" or board[second] != "*":
            print("Card already opened!")
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
        print("Please enter a valid number!")

print("\nYou finished the game!")
print(f"Total moves: {moves}")