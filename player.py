import random


class Player:
    def __init__(self):
        self.board = [
            ["    ", "A    ", "B    ", "C    "],
            ["1 ", "___", " | ", "___", " | ", "___"],
            ["2 ", "___", " | ", "___", " | ", "___"],
            ["3 ", "   ", " | ", "   ", " | ", "   "],
        ]
        self.current_board = f"{''.join(self.board[0])}\n{''.join(self.board[1])}\n{''.join(self.board[2])}\n{''.join(self.board[3])}"

    def fill_box(self, response, player_turn):
        letter = response[0]
        number = response[1]
        if player_turn:
            cp = "_X_"
        elif not player_turn:
            cp = "_O_"
        if letter == "A":
            if number == "1":
                if self.board[1][1] == "___":
                    self.board[1][1] = cp
                    return True
                else:
                    return False
            elif number == "2":
                if self.board[2][1] == "___":
                    self.board[2][1] = cp
                    return True
                else:
                    return False
            elif number == "3":
                if self.board[3][1] == "   ":
                    self.board[3][1] = cp
                    return True
                else:
                    return False

        elif letter == "B":
            if number == "1":
                if self.board[1][3] == "___":
                    self.board[1][3] = cp
                    return True
                else:
                    return False
            elif number == "2":
                if self.board[2][3] == "___":
                    self.board[2][3] = cp
                    return True
                else:
                    return False
            elif number == "3":
                if self.board[3][3] == "   ":
                    self.board[3][3] = cp
                    return True
                else:
                    return False

        elif letter == "C":
            if number == "1":
                if self.board[1][5] == "___":
                    self.board[1][5] = cp
                    return True
                else:
                    return False
            elif number == "2":
                if self.board[2][5] == "___":
                    self.board[2][5] = cp
                    return True
                else:
                    return False
            elif number == "3":
                if self.board[3][5] == "   ":
                    self.board[3][5] = cp
                    return True
                else:
                    return False
            else:
                return False


    def check_for_user_win(self):
        if "_X_" in self.board[1][1] and "_X_" in self.board[1][3] and "_X_" in self.board[1][5]:
            return True
        elif "_X_" in self.board[2][1] and "_X_" in self.board[2][3] and "_X_" in self.board[2][5]:
            return True
        elif "_X_" in self.board[3][1] and "_X_" in self.board[3][3] and "_X_" in self.board[3][5]:
            return True
        elif "_X_" in self.board[1][1] and "_X_" in self.board[2][1] and "_X_" in self.board[3][1]:
            return True
        elif "_X_" in self.board[1][3] and "_X_" in self.board[2][3] and "_X_" in self.board[3][3]:
            return True
        elif "_X_" in self.board[1][5] and "_X_" in self.board[2][5] and "_X_" in self.board[3][5]:
            return True
        elif "_X_" in self.board[1][1] and "_X_" in self.board[2][3] and "_X_" in self.board[3][5]:
            return True
        elif "_X_" in self.board[1][5] and "_X_" in self.board[2][3] and "_X_" in self.board[3][1]:
            return True
        else:
            return False

    def check_for_computer_win(self):
        if "_O_" in self.board[1][1] and "_O_" in self.board[1][3] and "_O_" in self.board[1][5]:
            return True
        elif "_O_" in self.board[2][1] and "_O_" in self.board[2][3] and "_O_" in self.board[2][5]:
            return True
        elif "_O_" in self.board[3][1] and "_O_" in self.board[3][3] and "_O_" in self.board[3][5]:
            return True
        elif "_O_" in self.board[1][1] and "_O_" in self.board[2][1] and "_O_" in self.board[3][1]:
            return True
        elif "_O_" in self.board[1][3] and "_O_" in self.board[2][3] and "_O_" in self.board[3][3]:
            return True
        elif "_O_" in self.board[1][5] and "_O_" in self.board[2][5] and "_O_" in self.board[3][5]:
            return True
        elif "_O_" in self.board[1][1] and "_O_" in self.board[2][3] and "_O_" in self.board[3][5]:
            return True
        elif "_O_" in self.board[1][5] and "_O_" in self.board[2][3] and "_O_" in self.board[3][1]:
            return True
        else:
            return False

    def show_board(self):
        print(f"{''.join(self.board[0])}\n{''.join(self.board[1])}\n{''.join(self.board[2])}\n{''.join(self.board[3])}")

    def computer_turn(self):
        choice = [random.choice(["A", "B", "C"]), str(random.randint(1, 3))]
        return choice
