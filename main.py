from player import Player
import random
import time

game = True
player = Player()
turns = 0

while game:
    player_turn = True
    player.show_board()
    user_response = list(input("Choose a position:\n>"))
    user_attempt = player.fill_box(user_response, player_turn)

    while not user_attempt:
        print("That Position is already filled or does not exist.")
        user_response = list(input("Choose a position:\n>"))
        user_attempt = player.fill_box(user_response, player_turn)

    player.show_board()
    if player.check_for_user_win():
        print("You Win!")
        break

    turns += 1
    if turns == 5:
        print("It's a tie.")
        break

    print("\nComputer's Turn...\n")
    time.sleep(1)

    player_turn = False
    cp_response = player.computer_turn()
    attempt = player.fill_box(cp_response, player_turn)
    while not attempt:
        cp_response = player.computer_turn()
        attempt = player.fill_box(cp_response, player_turn)

    if player.check_for_computer_win():
        player.show_board()
        print("You Lose")
        break

