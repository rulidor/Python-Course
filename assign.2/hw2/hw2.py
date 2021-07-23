# *************** EXERCISE 2 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def print_digits_frame(digit):
    "Prints a frame according to the received digit"
    print('#' * (digit+2))
    for i in range(digit):
        s="|"
        for j in range(i+1):
            s=s+str(j+1)
        print(s+(' ')*(digit+2-len(s)-1)+'|')
    print('#' * (digit+2))


# **************************************************************
# ************************ QUESTION 2 **************************
def compress_text(to_compress):
    "Returns a list with char counts of received string"
    s=to_compress
    list=[] #compressed
    count=1 #sequential charts counter
    last_char=s[0]
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            list.append([s[i],count])
            count=1
        last_char=s[i]
    if s[i+1]==last_char:
        list.append([s[i],count])
    else:
        list.append([s[i+1],1]) 
    return list

def evaluate_compression(original_text, compressed_text):
    "Calculates and returns compression ratio"
    return (len(original_text)) / (len(compressed_text)*2)        
    

# **************************************************************
# ************************ QUESTION 3 **************************
def calculate_average_grade(students, feedback):
    "Calculates and prints average grade"
    sum=0
    for i in students:
        sum=sum+i[1]
    average_grade=sum/len(students) 
    print("Average grade: "+str(average_grade))
    if feedback==True:
        print_feedbacks(students, average_grade)
        

def print_feedbacks(students, average_grade):
    "Prints a feedback for every student"
    for i in students:
        if i[1]>=average_grade:
            print("Good job, "+i[0]+"!")
        else:
            print("You can do better, "+i[0]+"!")

    
    
    
    
    
    
    
    
    
