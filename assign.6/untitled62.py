def domino_solution(boardlist,row,col): 
    
    if row > len(boardlist):
        return boardlist
        
    if col > len(boardlist[0]):
        domino_solution(boardlist,row+1,col)
    if len(boardlist[0]) == col:
        domino_solution(boardlist,row+1,0)
        
    if boardlist[row][col] == "*":
        boardlist[row][col] = "B"
        domino_solution(boardlist,row,col+1)
        
    else:
        domino_solution(boardlist,row,col+1)
        
    return boardlist

#def propriety(boardlist,i,j):
#    domino_solution(boardlist,0,0)
#    
#    if i > len(boardlist):
#        return 1
#    if j > len(boardlist[0]):
#        return propriety(boardlist,i+1,0)
#    
#    if boardlist[i][j] == "B":
#        if boardlist[i][j+1] == "B" or boardlist[i+1][j] == "B":
#            return propriety(boardlist,i,j+1)
#        else:
#            return "Broken board"
#    else:
#        propriety(boardlist,i,j+1)
#    
#    return boardlist
#        
#            
#    
#def a_valid_solution(boardlist):
#    propriety(boardlist)
#    domino_solution(boardlist,0,0)
#    
    

board_5 = [['*' , '#' , '#' , '#'],
               ['*' , '*' , '#' , '*'],
               ['#' , '*' , '#' , '*'],
               ['*' , '*' , '*' , '*']
              ]

print(domino_solution(board_5,0,0))
