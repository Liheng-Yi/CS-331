from Players import *
import sys
import OthelloBoard



play1 = 0
play2 = 0

class GameDriver:
    def __init__(self, p1type="human", p2type="alphabeta", num_rows=4, num_cols=4, p1_eval_type=0, p1_prune=False, p2_eval_type=0, p2_prune=False, p1_depth=8, p2_depth=8, results =[]):
        if p1type.lower() in "human":
            self.p1 = HumanPlayer('X')

        elif p1type.lower() in "alphabeta":
            self.p1 = AlphaBetaPlayer('X', p1_eval_type, p1_prune, p1_depth)

        else:
            print("Invalid player 1 type!")
            exit(-1)

        if p2type.lower() in "human":
            self.p2 = HumanPlayer('O')

        elif p2type.lower() in "alphabeta":
            self.p2 = AlphaBetaPlayer('O', p2_eval_type, p2_prune, p2_depth)

        else:
            print("Invalid player 2 type!")
            exit(-1)

        self.board = OthelloBoard.OthelloBoard(num_rows, num_cols, self.p1.symbol, self.p2.symbol)
        self.board.initialize()
        self.results = results

    def display(self):
        print("Player 1 (", self.p1.symbol, ") score: ", \
                self.board.count_score(self.p1.symbol))

    def process_move(self, curr_player, opponent):
        invalid_move = True
        while(invalid_move):

            tem = curr_player.get_move(self.board)

            # if( not self.board.is_legal_move(col, row, curr_player.symbol)):
            #     print("Invalid move")
            if(tem is None):
                print("Invalid move")
                return
            else:
                (col, row) = tem
                # print("Move:", [col,row], "\n")
                self.board.play_move(col,row,curr_player.symbol)
                return


    def run(self):
        current = self.p1
        opponent = self.p2
        # self.board.display()

        cant_move_counter, toggle = 0, 0

        # main execution of game
        # print("Player 1(", self.p1.symbol, ") move:")
        # Get a move, then display it in a while loop
        turn_count = 0
        while True:
            if self.board.has_legal_moves_remaining(current.symbol):
                turn_count += 1
                cant_move_counter = 0
                self.process_move(current, opponent)
                # self.board.display()
            else:
                # print("Can't move")
                if(cant_move_counter == 1):
                    break
                else:
                    cant_move_counter +=1
            toggle = (toggle + 1) % 2
            if toggle == 0:
                current, opponent = self.p1, self.p2
                # print("Player 1(", self.p1.symbol, ") move:")
            else:
                current, opponent = self.p2, self.p1
                # print("Player 2(", self.p2.symbol, ") move:")

        #decide win/lose/tie state
        state = self.board.count_score(self.p1.symbol) - self.board.count_score(self.p2.symbol)
        print("alphabeta"," against ", "alphabeta")
        # self.board.display()
        tem = 1
        if( state == 0):
            print("Tie game!!")
        elif state >0:
            print("Player 1 Wins!")

        else:
            print("Player 2 Wins!")


        
        # print("depth: ", self.p2_depth, "player ", tem,"won the game")
        # print("total nodes seen by p1", self.p1.total_nodes_seen)

        # self.results.append((self.p1.total_nodes_seen, self.p2.total_nodes_seen))
        # print(self.results)
        

def main():
    board_size = 5


    depths = [2, 4, 6, 8]

    # Perform the searches and record the number of nodes seen
    results = []



    for depth in depths:
        # Create a player for each heuristic
        game = GameDriver("alphabeta", "alphabeta", board_size, board_size, 2,
                0, 1, 0, depth, depth, results)
        
        game.run()
    print(game.results)



    # debbuggin main function
    # game = GameDriver("alphabeta", "alphabeta", board_size, board_size, 
    # # p1_eval_type,
    #         2,
    # # p1_prune,
    #         0, 
    # # p2_eval_type
    #         2,
    # # p2_prune=False
    #         0, 
        
    #         8, 8)
    # game.run()

main()
