# Author: Barath Srinivasan

# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
# The integer division should truncate toward zero.
# Make sure to follow order of operations!

# Notes:
# you may not assume that the given expression is always valid. (Return 0 if not valid)

# Explanation of Code:
"""
I first iterate through the given string s to compute all the division and multiplication operators. Because these are of the same level in OOP, they can be computed from left to right without worrying about order. 
So, while I iterate through string, I keep track of the left and right operand, named first and second, to compute using the appropriate operation. After computing, if the next operation is either division or multiplication
I use the total from my current calculations to continue; however, if the next operation is not either, then I store the current total with the next operation. Now I continue this until all my division and multiplication 
operations are completed. Then, I add the same thing, but for addition and subtraction. As last time, I can compute left to right since they are of the same level in OOP. Only exception is this time, I don't have to check for the next operation because I removed all other operations before. So, I use the current total as the left operand and continue with my computations. At the end, I return the total, for the user to use as he/she pleases.
"""

# Analysis of Code:
"""
My code has a time complexity of O(n). This is because none of the loops are nested and all characters in the string are visited. Even the replace function I use to remove spaces, iterates through the string once, visiting all the characters. Space complexity if also of O(n) because the variables I intialize are of constant size. They don't change depending of the given input. However, string s can be n characters long and, therefore, requires space for all n of its characters. 
"""

def calculate(s):
    if s is None: # checks to see if arg s is null
        return 0

    # intialize variables I use
    first = ""
    second = ""
    total = 0
    remaining = ""
    lastOper = ""

    s.replace(" ","") # remove any spaces in the str
    s = s + "\n" # add a null byte in the end as a marker
    
    for c in s: # iterate through each letter of my string
        if c.isdigit(): # checks until operator has been spotted
            if not lastOper: # to see if left or right operand needs to be filled
                first += c
            else:
                second += c
        elif c.isalpha(): # if a letter, then return 0
            return 0
        else: # operator has been found
            if lastOper is "/": # checks last operator to see what needs to be done
                try: # incase int func throws an error
                    total = int(first) // int(second) # divides left and right operand
                except: # return 0 if expection thrown
                    return 0
                
                if c is "/" or c is "*": # if division or multiplication, can continue by using total as first value
                    first = str(total) # passes total to first
                    second = "" # needs to find new second operand
                    lastOper = c # current operator will be used for future calculations
                else: # if not division or multiplication, then need to store current total
                    remaining += str(total) + c # stores current total and next operator
                    first = "" # resets variable
                    second = ""
                    lastOper = ""
            elif lastOper is "*": # same as division case, but for multiplication
                try:
                    total = int(first) * int(second)
                except:
                    return 0
                
                if c is "/" or c is "*":
                    first = str(total)
                    second = ""
                    lastOper = c
                else:
                    remaining += str(total) + c
                    first = ""
                    second = ""
                    lastOper = ""
            else: # not operator has been found
                if c is "/" or c is "*": # if division or multiplication, then store it
                    lastOper = c
                else: # else processed string to remaining
                    remaining += first + c
                    first = "" # reseat variable
    
    # reset necessary variables
    first = ""
    second = ""
    total = 0
    lastOper = ""

    # should have completed all division and multiplication operators by now
    
    for c in remaining: # iterate through the remaining characters
        if c.isdigit(): # check to see if a digit
            if not lastOper: # check to see if operation has been found, to decide whether to store to left or right operand
                first += c
            else:
                second += c
        
        else: # operator found
            if lastOper is "+": # if addition
                try: # incase int throws and exception
                    total = int(first) + int(second) # compute total and store value
                except:
                    return 0
                
                first = str(total) # use current total to continue computation
                second = "" # reset variable
                lastOper = c # store current operator for future operations
            elif lastOper is "-": # same as addition case, but for subtraction
                try:
                    total = int(first) - int(second)
                except:
                    return 0
                
                first = str(total)
                second = ""
                lastOper = c
            else: # neither addition or subtraction operators found so far
               try: # incase int func throws an exception
                   total = int(first) # convert string to int
               except:
                   return 0
               
               lastOper = c # stores operator
                   
    return total # returns total
