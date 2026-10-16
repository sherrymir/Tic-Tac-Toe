from random import choice

class tictactoe:
    def __init__(self):
        self.positions = [
        "TopL", "TopC", "TopR",
        "MidL", "MidC", "MidR",
        "BotL", "BotC", "BotR"]

        self.table ={
        "TopL": " ","TopC": " ","TopR": " ",
        "MidL": " ","MidC": " ","MidR": " ",
        "BotL": " ","BotC": " ","BotR": " "}

        self.win_conditions = [ 
        ["TopL", "TopC", "TopR"], ["MidL", "MidC", "MidR"], ["BotL", "BotC", "BotR"],
        ["TopL", "MidL", "BotL"], ["TopC", "MidC", "BotC"], ["TopR", "MidR", "BotR"],  
        ["TopL", "MidC", "BotR"], ["TopR", "MidC", "BotL"]]
    

    def The_Table(self,board):
        """Generates the table for the game"""

        print(board["TopL"]+"|"+board["TopC"]+"|"+board["TopR"])
        print("-+-+-")
        print(board["MidL"]+"|"+board["MidC"]+"|"+board["MidR"])
        print("-+-+-")
        print(board["BotL"]+"|"+board["BotC"]+"|"+board["BotR"])

    def Check_Winner(self,table: dict,turn: str) -> bool:
        """decides winner by checking the current position with the given win_conditions"""

        for condition in self.win_conditions:
            if all(table[pos] == turn for pos in condition):
                return True
        return False

    def Basic_ai(self,turn) -> str:
        """
        first priority: attempts finishing move.
        second priority: Blocks the opponent's winning move."""

        for position in self.positions:
            if self.table[position] != " ":
                continue
            
            self.table[position] = turn

            result = self.Check_Winner(self.table,turn)

            self.table[position] = " "

            if result:
                return position

        opponent = "X" if turn == "O" else "O"
        block = False
        for position in self.positions:
            if self.table[position] != " ":
                continue

            self.table[position] = opponent
            block = self.Check_Winner(self.table,opponent)

            self.table[position] = " "

            if block:
                return position
        return None

    def Intermediate_ai(self,turn) -> str:
        """Avoids potential threats that could lead to a loss by looking two moves ahead"""

        opponent = "X" if turn == "O" else "O"
        for position in self.positions:
            if self.table[position] != " ":
                continue

            self.table[position] = turn

            result = self.Basic_ai(opponent)

            self.table[position] = " "

            if result:
                continue

            self.table[position] = turn
            result = self.Basic_ai(turn)
            self.table[position] = " " 

            if result: 
                return position

        return None

    # def Strategic_ai(self,turn):
    #     """""" 
    #     pass

    def computer_move(self) -> str:
        while True:
            random_move = choice(self.positions)
            if self.table[random_move] != " ":
                continue
            if self.table[random_move] == " ":
                return random_move
        return None

def Main():

    game = tictactoe()

    game.The_Table(game.table)
    turn = "X"

    while " " in game.table.values(): 
        if turn == "X":
            choice = input(f"Where do you wanna put {turn} e.g(TopL,MidC,BotR): ")

            if choice not in game.table:
                print("Please enter the Valid position.")
                continue

            if game.table[choice] != " ":
                print("The square is already occupied.")
                continue

            game.table[choice] = turn
            print()

            if game.Check_Winner(game.table,turn):
                print(f"\n{turn} is the winner!")
                return
            
            print("Computer's turn".center(50,"-"))

        if turn == "O":
            ai = game.Basic_ai(turn)
            if not ai:
                ai = game.Intermediate_ai(turn)
            if not ai:
                ai = game.computer_move()
            if ai:
                game.table[ai] = turn
                game.The_Table(game.table)
                
                if game.Check_Winner(game.table,turn):
                    print(f"\n{turn} is the winner!")
                    return

        turn = "X" if turn == "O" else "O"

    print("\nIts a draw")

if __name__ == "__main__":
    Main()
