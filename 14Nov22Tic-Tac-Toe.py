
# board is declared as a global variable.
board = [[" "," "," "],[" "," "," "],[" "," "," "]]


# used to change the turns between the person1 and person2.
def playerShifting(times):
    # even case is for person2.
    if(times%2==0):
        print("Person1's turn..")
        person_rowno = int(input('Enter row number(0-2):'))
        
        person_colno = int(input('Enter column number(0-2):'))
        
        value = insertSymbol('O',person_rowno,person_colno)
        
        printBoard()
        
        if value=='X':
            print('person1 wins')
            return 'X'
        elif value == 'O':
            print('person2 wins')
            return 'O'
        else:
            return None
            
    # odd case is for person1.
    else:
        print("Person2's turn..")
        person_rowno = int(input('Enter row number(0-2):'))
        
        person_colno = int(input('Enter column number(0-2):'))
        
        value = insertSymbol('X',person_rowno,person_colno)
        
        printBoard()
        
        if value=='X':
            print('person1 wins')
            return 'X'
        elif value == 'O':
            print('person2 wins')
            return 'O'
        else:
            return None
        
    
# It checks whether there is any diagonal, row or column wise match of symbol 'X' or 'O'.
def checkBoard():
    if(board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X'):
        return 'X'
    elif(board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X'):
        return 'X'
    elif((board[0][0]=='X' and board[0][1] == 'X' and board[0][2]=='X') or (board[1][0]=='X' and board[1][1] == 'X' and board[1][2]=='X') or (board[2][0]=='X' and board[2][1] == 'X' and board[2][2]=='X')):
        return 'X'
    elif(board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O'):
        return 'O'
    elif(board[0][2]=='O' and board[1][1]=='O' and board[2][0]=='O'):
        return 'O'
    elif((board[0][0]=='O' and board[0][1] == 'O' and board[0][2]=='O') or (board[1][0]=='O' and board[1][1] == 'O' and board[1][2]=='O') or (board[2][0]=='O' and board[2][1] == 'O' and board[2][2]=='O')):
        return 'O'
    else:
        return None
        

# code to print the board.
def printBoard():
    for i in range(3):
        for j in range(3):
            print(board[i][j],end=" ")
        print()


# used to insert the symbol at particular position
def insertSymbol(person_symbol,person_rowno,person_colno):
    board[person_rowno][person_colno] = person_symbol
    # At this place checkBoard() function is called to check the board.
    returned_value = checkBoard()
    if(returned_value=='X'):
        return 'X'
    elif(returned_value=='O'):
        return 'O'
    else:
        return None
    

        
# It is first function which is called from the bottom if main condition.
def main():
    person1_symbol = 'X'
    person2_symbol = 'O'
    times = 7
    
    print("Person1's turn..")
    person1_rowno = int(input('Enter row number(0-2):'))
        
    person1_colno = int(input('Enter column number(0-2):'))
    
    insertSymbol(person1_symbol,person1_rowno,person1_colno)
    
    printBoard()
    
    print("Person2's turn..")
    person2_rowno = int(input('Enter row number(0-2):'))
    
    person2_colno = int(input('Enter column number(0-2):'))
    
    insertSymbol(person2_symbol,person2_rowno,person2_colno)
    
    printBoard()
    
    while(times>0):
        
        winner =playerShifting(times)
        
        if(winner == 'X' or winner=='O'):
            break
    
        times-=1
        
        
    # tie condition
    if(times==0):
        print("Game is tie.")
    
    
    
# Program execution starts from here.
if __name__ == "__main__":
    main()
