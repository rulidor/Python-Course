
def domino_problem(board):
    "Returns game solution for valid board and appropriate message if board is not valid"
    N=len(board)
    M=len(board[0])
    if domino_help(board,N,M,0,0)==True:
        return ('Broken board')
    new_board=turn_empty_into_B(board) #else
    return new_board
    
def domino_help(board,N,M,cur_r,cur_c,flag=False):
    if cur_c==M and cur_r<N:
        return domino_help(board,N,M,cur_r+1,0,flag)
    if cur_c==M and cur_r==N:
        if flag==False:
            return False #flag=False if board is VALID, True for INVALID
        return True
    if cur_r==N:
        if flag==False:
            return False #flag=False if board is VALID, True for INVALID
        return True
    if board[cur_r][cur_c]=='#' or board[cur_r][cur_c]=='B':
        return domino_help(board,N,M,cur_r,cur_c+1,flag)     
    if board[cur_r][cur_c]=='*':
        down=is_empty(board,N,M,cur_r+1,cur_c)
        right=is_empty(board,N,M,cur_r,cur_c+1)
        if is_edge(N,M,cur_r,cur_c)==0: #0 for not edge
            if down==True and right==True:
                board[cur_r][cur_c+1]='B'
                check_right=domino_help(board,N,M,cur_r,cur_c+1,flag)
                board[cur_r][cur_c+1]='*'
                board[cur_r+1][cur_c]='B'
                check_down=domino_help(board,N,M,cur_r,cur_c+1,flag)
                board[cur_r+1][cur_c]='*'
                if check_down==True and check_right==True:
                    flag=True
                    return domino_help(board,N,M,cur_r,cur_c+1,flag)                
                if check_right==True:
                    if check_down==False:
                        board[cur_r+1][cur_c]='B'
                        return domino_help(board,N,M,cur_r,cur_c+1,flag)
                if check_down==True:
                    if check_right==False:
                        board[cur_r][cur_c+1]='B'
                        return domino_help(board,N,M,cur_r,cur_c+1,flag)
            elif right==True or down==True:
                if right==True:
                    board[cur_r][cur_c+1]='B'
                    return domino_help(board,N,M,cur_r,cur_c+1,flag)
                if down==True:
                    board[cur_r+1][cur_c]='B'
                    return domino_help(board,N,M,cur_r,cur_c+1,flag)
            else:
                flag=True
                return domino_help(board,N,M,cur_r,cur_c+1,flag) #if right=down=False
        if is_edge(N,M,cur_r,cur_c)==1: #1 for edge of lines
            if right==True:
                board[cur_r][cur_c+1]='B'
                return domino_help(board,N,M,cur_r,cur_c+1,flag)
            flag=True
            return domino_help(board,N,M,cur_r,cur_c+1,flag) #if right=False
        if is_edge(N,M,cur_r,cur_c)==2: #2 for edge of columns
            if down==True:
                board[cur_r+1][cur_c]='B'
                return domino_help(board,N,M,cur_r,cur_c+1,flag)
            flag=True
            return domino_help(board,N,M,cur_r,cur_c+1,flag) #if down=False

def is_edge(N,M,r,c):
    "Checks if cur. index is an edge of board. Returns:0-not edge, 1-edge of lines, 2-end of columns"
    if r==N-1 and c<=M-1:
        return 1
    if c==M-1 and r<=N-1:
        return 2
    return 0 #else

def is_empty(board,N,M,r,c):
    "Checks if a cell in board='*'"
    if r>=N or c>=M:
        return False
    return board[r][c]=='*'

def turn_empty_into_B(board,r=0,c=0):
    "Replaces asterisks by 'B'"
    if c==len(board[0]) and r<len(board):
        return turn_empty_into_B(board,r+1,0)
    if r==len(board):
        return board
    if board[r][c]=='*':
        board[r][c]='B'
        return turn_empty_into_B(board,r,c+1)
    return turn_empty_into_B(board,r,c+1) #else             