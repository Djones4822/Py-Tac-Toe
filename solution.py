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
    main_list.append([board[0][0],board[1][1],board[2][2]])
    main_list.append([board[0][2],board[1][1],board[2][0]])

    
    #Get Cols and Rows
    cols = zip(board[0],board[1],board[2])
    rows = board

    #Merge lists
    main_list += cols + rows

    full = True
    for lst in main_list:
        combo = ''.join(lst)
        if combo == 'XXX':
            return True, 'X'
        elif combo == 'OOO':
            return True, 'O'
        elif '.' in combo:
            full = False
    if full == True:
        return True, 'Draw'
    else:
        return False, 0
    
        
def display_board(board):
    for i in board:
        print str(i) + '\n'
        
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
                break
            except ValueError:
                print 'Please enter a number 1-3'
                
        if board[row-1][columns_dict[col]] == '.':
            return [row-1,  columns_dict[col]]
        else:
            print 'That space has already been taken!'
    
def main():
    #Initialize game
    player1_turn = True
    player2_turn = False
    print 'Py-Tac-Toe!!\n\n'
    
    board = init_board()

    while True:         #Main Game Loop
        
        #Player 1 Turn
        display_board(board)
        if player1_turn:
            print 'Player 1!'
            answer = get_next_move(board)
            board[answer[0]][answer[1]] = 'X'
            player1_turn = False
            Player2_turn = True
            
            results = win_test(board)
            
            if results[0] == True:
                if results[1] == 'X': 
                    print '\n\nPlayer 1 is the winner!!!!!!!'
                    display_board(board)
                    return None
                elif results[1] == 'Draw':
                    print '\n\nDRAW!'
                    display_board(board)
                    return None
        
        #Player 2 Turn
        else:
            print 'Player 2!'
            answer = get_next_move(board)
            board[answer[0]][answer[1]] = 'O'
            player1_turn = True
            Player2_turn = False
            if results[0] == True:
                if results[1] == 'O': 
                    print '\n\nPlayer 2 is the winner!!!!!!!'
                    display_board(board)
                    return None
                elif results[1] == 'Draw':
                    print '\n\nDRAW!'
                    display_board(board)
                    return None
        
        
if __name__ == '__main__':
    main()
