columns_dict = {'A':0, 'B':1, 'C':2}

def init_board():
    return [
            ['.','.','.'], 
            ['.','.','.'], 
            ['.','.','.']
        ]
        

def win_test(board):
    main_list = []
    
    #Get Diags
    main_list.append([board[i][j] for i,j in zip(range(len(board)),range(len(board))[::-1])]) #left diag
    main_list.append([board[i][i] for i in range(len(board))]) #right diag
    
    #Get Cols and Rows
    main_list += zip(board[0],board[1],board[2]) #columns
    main_list += board #rows

    combo = [''.join(lst) for lst in main_list]
    
    if 'XXX' in combo or 'OOO' in combo:
        return 1
    elif '.' not in ''.join(combo):
        return -1
    else:
        return None
    
        
def display_board(board):
    board = [[i+1] + board[i] for i in range(len(board))]
    board = [['', 'A','B','C']] + board
    
    for row in board:
        print ''.join([str(space).rjust(5, " ") for space in row])
        
def get_next_move(board):
    while True:
        while True:
            col = raw_input("What column would you like to place?\n\n-> ").upper()
            if col == 'A' or col == 'B' or col == 'C':
                break      
            else: print "Please type A B or C"
        
        while True:
            row = raw_input("What row?\n\n-> ")
            try:
                row = int(row)
                if row == 1 or row == 2 or row == 3:
                    break
                else:
                    print 'Please enter a number 1-3'
            except ValueError:
                print 'Please enter a number 1-3'
                
        if board[row-1][columns_dict[col]] == '.':
            return [row-1,  columns_dict[col]]
        else:
            print 'That space has already been taken!'
    
def main():
    
    #Initialize game
    player1_turn = True
    board = init_board()

    print """
_______________.___.       ________________  _________         ___________________  ___________
\______   \__  |   |       \__    ___/  _  \ \_   ___ \        \__    ___/\_____  \ \_   _____/
 |     ___//   |   |  ______ |    | /  /_\  \/    \  \/   ______ |    |    /   |   \ |    __)_ 
 |    |    \____   | /_____/ |    |/    |    \     \____ /_____/ |    |   /    |    \|        \\
 |____|    / ______|         |____|\____|__  /\______  /         |____|   \_______  /_______  /
           \/                              \/        \/                           \/        \/
          
          by David Jones
          and Farhan Samani
------------------------------------------------------------------------------------------------

          """
    
    #Main Game Loop
    while True:
        
        #Begin Turn
        display_board(board)
        
        if player1_turn:
            num, char = (1, 'X')
        else:
            num, char = (2,'O')
        
        print '\nPlayer %i!' %num
        
        answer = get_next_move(board)
        
        board[answer[0]][answer[1]] = char
        
        player1_turn = not player1_turn
            
        results = win_test(board)
            
        if results == 1:
            print '\n\nPlayer %i is the winner!!!!!!!' % (num)
            display_board(board)
            return None
        elif results == -1:
            print '\n\nDRAW!'
            display_board(board)
            return None

        
if __name__ == '__main__':
    main()
