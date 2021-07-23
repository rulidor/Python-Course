# *************** EXERCISE 1 ***************

# **************************************************************
# ************************ QUESTION 1 **************************
def question1(a1, an, n):
    "Prints sum of a series"
    if n==0:
        print("0")
    elif n==1:
        print(a1)
    else:
        print(n*(a1+an)/2)


# **************************************************************
# ************************ QUESTION 2 **************************
def question2(x):
    "Prints 'SHOKO','BO' or 'GUMIGAM' if divisible by 3,5,15. Else-prints number itself"
    for i in range(1,x+1):
        if i%15==0: #if divisible by 15
            print("GUMIGAM")
            continue
        if i%3==0: #only if not divisible by 15
            print("SHOKO")
        elif i%5==0: #if divisible ny 5 but not by 3
            print("BO")
        else: #if neither divisible by 3 nor by 5
            print(i)
    print("**********")


# **************************************************************
# ************************ QUESTION 3 **************************
def is_palindrome(s, left, right):
    "Checks if a string is a palindrome between 2 indexes"
    while left<right:
        if s[left] != s[right]: #a mismatch - no palindrome
            return False
        left+=1
        right-=1
    return True #no mismatches

def question3(s):
    "Checks and prints if a string is 'almost' a palindrome"
    pal=0 #0 means pal., 1 means almost pal., 2 means not almost pal.
    left=0 #left iterator
    right=len(s)-1 #right iterator
    while left<right:
        if s[left]==s[right]: #both char. are equal
            left+=1
            right-=1
        else:
            #checking if removing s[left] makes palindrome
            if is_palindrome(s, left+1, right):
                print("TRUE")
                pal=1
                break
            #checking if removing s[right] makes palindrome
            elif is_palindrome(s, left, right-1):
                print("TRUE")
                pal=1
                break
            else:
                pal=2 #not a palindrome
                break
    if pal==2:
        print("FALSE")
    elif pal==0: #exactly a pal. Note: if almost pal., "TRUE" ALREADY printed
        print("TRUE")


# **************************************************************
# ************************ QUESTION 4 **************************
def question4(input_list):
    "Prints the average of the 2 largest even numbers and 2 largest odd numbers in a list"
    even1=-1 #largest even number in list
    even2=-1 #2nd largest even number in list
    odd1=-1 #largest odd number in list
    odd2=-1 #2nd largest odd number in list
    for i in input_list:
        if i==0:
            break
        if i%2==0: #number is even
            if i>even1:
                even2=even1
                even1=i
            elif i>even2: #number is not larger than even1 but larger than even2
                even2=i
        else: #number is odd
            if i>odd1:
                odd2=odd1
                odd1=i
            elif i>odd2: #number is not larger than odd1 but larger than odd2
                odd2=i
    print((even1+even2+odd1+odd2)/4)
