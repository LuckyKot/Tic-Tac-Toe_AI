import copy
import random

#Main building blocks of the program, class to build and work with the tic tac toe board and win detection function
#Initializes a list 3x3 filled with *s
#Print board just prints the current board according the format
#Score function just counts the scores the agents act on
#get_available_moves places an agent (X or O) in empty spots and returns the 'move' list. X coordinate Y coordinate and X/O
#get_new_state places the X/O to the spot based on list from previous function
#game_over detects if all spots has been filled, meaning a game over
#game_win used to be a fancy small function that would return 'X' or 'O' based on who won but it was wrong, so I just decided to
#hardcode every possible winning state to avoid further extensive debugging
class Board:
    def __init__(self):
        self.board=[]
        for i in range(3):
            self.board.append([])
            for j in range (3):
                self.board[i].append('*')
                
    def print_board(self): 
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                print(self.board[i][j],sep='',end='')
            print('\n',sep='',end='')
        print('\n')
            
    def score(self,depth):
        if self.game_win()=='X':
            return 10 - depth
        elif self.game_win()=='O':
            return depth - 10
        else:
            return 0
        
    def get_available_moves(self,agent):
        aMoves=[]
        for i in range(3):
            for j in range (3):
                if self.board[i][j]=='*':
                    aMoves.append([i,j,agent])
        return aMoves
                    
    def get_new_state(self,indexes):
        temp=copy.deepcopy(self.board)
        temp[indexes[0]][indexes[1]]=indexes[2]
        return temp
    
    def game_over(self):
        if self.game_win()=='X' or self.game_win()=='O':
            return True
        for i in range(3):
            for j in range (3):
                if self.board[i][j]=='*':
                    return False
        return True

    def game_win(self):   
        if self.board[0][0] == self.board[1][1]== self.board[2][2] == 'X':
            return 'X'
        elif self.board[0][0] == self.board[1][1]== self.board[2][2] == 'O':
            return 'O'

        if self.board[0][2] == self.board[1][1]== self.board[2][0] == 'X':
            return 'X'
        elif self.board[0][2] == self.board[1][1]== self.board[2][0] == 'O':
            return 'O'

        if self.board[0][0] == self.board[0][1]== self.board[0][2] == 'X':
            return 'X'
        elif self.board[0][0] == self.board[0][1]== self.board[0][2] == 'O':
            return 'O'

        if self.board[0][0] == self.board[1][0]== self.board[2][0] == 'X':
            return 'X'
        elif self.board[0][0] == self.board[1][0]== self.board[2][0] == 'O':
            return 'O'

        if self.board[1][0] == self.board[1][1]== self.board[1][2] == 'X':
            return 'X'
        elif self.board[1][0] == self.board[1][1]== self.board[1][2] == 'O':
            return 'O'

        if self.board[0][1] == self.board[1][1]== self.board[2][1] == 'X':
            return 'X'
        elif self.board[0][1] == self.board[1][1]== self.board[2][1] == 'O':
            return 'O'

        if self.board[0][2] == self.board[1][2]== self.board[2][2] == 'X':
            return 'X'
        elif self.board[0][2] == self.board[1][2]== self.board[2][2] == 'O':
            return 'O'

        if self.board[2][0] == self.board[2][1]== self.board[2][2] == 'X':
            return 'X'
        elif self.board[2][0] == self.board[2][1]== self.board[2][2] == 'O':
            return 'O'

        return 0

#main minimax function, mostly a modified version of the minimax function from the article provided with the assignment
def minimax(game,depth):
    
    if depth%2==0:
        agent='X'
    else:
        agent='O'
          
    if game.game_over():
        return game.score(depth),game
    depth=depth+1
    scores = [] 
    moves = []
    
    for move in game.get_available_moves(agent):
        possible_game = Board()
        possible_game.board = copy.deepcopy(game.get_new_state(move))
        temp,temp2=minimax(possible_game,depth)
        
#        if depth==6:
#            print('Score:',possible_game.score(depth))
#            print('temp:',temp)
#            print('Board:')
#            possible_game.print_board()
        
        scores.append(temp)
        moves.append(move)
    
    if agent=='X':
        max_score_index = scores.index(max(scores))
#        print('score list:',print(scores),'min:',min(scores))
        choice = moves[max_score_index]
        return scores[max_score_index],choice
    else:
        min_score_index = scores.index(min(scores))
#        print('score list:',print(scores),'min:',min(scores))
        choice = moves[min_score_index]
        return scores[min_score_index],choice

print('0x 1x 2x')
print('3x 4x 5x')
print('6x 7x 8x')
test = Board()
depth=0
while not test.game_over():
    j = int(input('Enter your turn:'))
    
    y=j//3
    x=j%3



    test.board[y][x]='X'

    test.print_board()
    
    depth=depth+1
    if (test.game_win())=='X':
        print('X win!\n')
        break
    elif (test.game_win())=='O':
        print('O win!\n')
        break
    elif test.game_over():
        print('Draw!\n')
        break

    score,move=minimax(test,depth)
    test.board=copy.deepcopy(test.get_new_state(move))
    test.print_board()
    if (test.game_win())=='X':
        print('X win!\n')
        break
    elif (test.game_win())=='O':
        print('O win!\n')
        break
    elif test.game_over():
        print('Draw!\n')
        break
    depth=depth+1
