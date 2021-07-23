import sys
import hw6_ques1
import hw6_ques2

def main():
    results_file = "results.txt"
    corr_res=""
    with open(results_file, 'w') as f:
            f.write("%s" %corr_res)
    ################ Question 1 Tests ################

    q1_inputs = [ ( [50 , 20 , 10 , 15 , 5] , (60 , 40) ),
                  ( [5 , 40 , 20 , 20 , 20] , (60 , 45) ),
                  ( [30 , 20 , 20 , 15 , 5] , (60 , 40) ),
                  ( [60 , 20 , 15 , 5] , (60 , 40) ),
                  ( [30 , 20 , 20 , 15 , 5] , (60 , 40) )
                ]
    
    for inher_list , values_all in q1_inputs:
        corr_res = hw6_ques1.partition(inher_list , values_all)
        with open(results_file, 'a') as f:
            f.write("%s\n" %corr_res)
                      

    ################ Question 2 Tests ################

    board_1 = [['*' , '#'],
               ['*' , '#']
              ]
    
    board_2 = [['*' , '#' , '#' , '#'],
               ['*' , '*' , '#' , '#'],
               ['#' , '*' , '#' , '#'],
               ['*' , '*' , '*' , '*']
              ] 
               
    board_3 = [['*' , '#' , '#' , '#' , '*'],
               ['*' , '*' , '#' , '#' , '*'],
               ['#' , '*' , '#' , '#' , '#'],
               ['*' , '*' , '*' , '*' , '#']
            ]
    
    board_4 = [['*' , '#' , '#' , '#'],
               ['#' , '*' , '#' , '#'],
               ['#' , '*' , '#' , '#'],
               ['*' , '*' , '*' , '*']
              ]
               
    board_5 = [['*' , '#' , '#' , '#'],
               ['*' , '*' , '#' , '*'],
               ['#' , '*' , '#' , '*'],
               ['*' , '*' , '*' , '*']
              ]
      

    q2_inputs = [["#","*","*","*","#","*","*","#"],["#","*","#","#","#","*","#","#"],["#","#","#","*","#","*","#","#"],["*","#","#","*","*","*","#","#"],["*","*","*","*","#","#","*","*"],["#","#","#","*","#","#","#","*"],["#","#","*","*","#","#","#","*"],["#","#","#","*","#","*","*","*"],["#","*","*","*","#","#","#","*"]]
    for curr_board in q2_inputs:
        corr_res = hw6_ques2.domino_problem(curr_board)
        with open(results_file, 'a') as f:
            f.write("%s\n" %corr_res)
    sys.exit(0)

main()

