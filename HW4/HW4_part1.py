# Garth Bates 11473063


#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []  #assuming top of the stack is the end of the list

# Now define the HELPER FUNCTIONS to push and pop values on the opstack 
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
# Recall that `pass` in Python is a no-op: replace it with your code.

def opPop():
    return opstack.pop()
    
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.

def opPush(value):
    opstack.append(value)

#-------------------------- 16% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to 
# define name, and to lookup a name

def dictPop():
    return dictstack.pop()
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    dictstack.append(d)
    #dictPush pushes the dictionary ‘d’ to the dictstack. 
    #Note that, your interpreter will call dictPush only when Postscript 
    #“begin” operator is called. “begin” should pop the empty dictionary from 
    #the opstack and push it onto the dictstack by calling dictPush.

def define(name, value):
    if len(dictstack) == 0:
        dictPush({})
    
    dictstack[-1][name] = value
    #add name:value pair to the top dictionary in the dictionary stack. 
    #Keep the '/' in the name constant. 
    #Your psDef function should pop the name and value from operand stack and 
    #call the “define” function.

def lookup(name):
    name = '/' + name
    dictstack.reverse()
    for dicts in dictstack:  #For every diction in the dictstack
        value = dicts.get(name)  #Set value for the input name
        if value is not None:
            dictstack.reverse()
            return value      #if the value exists, return it
    #else:
        #print("Name not defined")  #else print "Name not defined"
    dictstack.reverse()
    return #this will be used for error checking in other functions
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, eq, lt, gt 
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2, int)):
            opPush(op1 + op2)
        else:
            print("Error: add. Expected two numerical values. Only one input")
            opPush(op1)
            opPush(op2)
    else:
        print("Error add. Expected two operands")
        

def sub():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2, int)):
            opPush(op1 - op2)
        else:
            print("Error: sub. Expected two numerical values. Only one input")
            opPush(op1)
            opPush(op2)
    else:
        print("Error sub. Expected two operands")

def mul():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2, int)):
            opPush(op1 * op2)
        else:
            print("Error: mul. Expected two numerical values. Only one input")
            opPush(op1)
            opPush(op2)
    else:
        print("Error mul. Expected two operands")

def eq():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        result = (op1 == op2)
        opPush(result)
        '''
        if(isinstance(op1, int) and isinstance(op2, int)):
            result = (op1 == op2)
            opPush(result)
        else:
            print("Error: eq. Expected two numerical values. Only one input")
            opPush(op1)
            opPush(op2)
        '''
    else:
        print("Error eq. Expected two operands")

def lt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2, int)):
            result = (op1 < op2)
            opPush(result)
        else:
            print("Error: lt. Expected two numerical values. Only one input")
            opPush(op1)
            opPush(op2)
    else:
        print("Error lt. Expected two operands")

def gt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1, int) and isinstance(op2, int)):
            result = (op1 > op2)
            opPush(result)
        else:
            print("Error: gt. Expected two numerical values. Only one input")
            opPush(op1)
            opPush(op2)
    else:
        print("Error gt. Expected two operands")

#--------------------------- 20% -------------------------------------
# String operators: define the string operators length, get, getinterval,  putinterval, search
def length():
    if len(opstack) > 0:
        op1 = str(opPop())
        opPush(len(op1) - 2)
    else:
        print("Error length. Expected one string")
            

def get():
    if len(opstack) > 1:
        index = opPop()
        opString = str(opPop())
        opString = opString[1:-1]
        opPush(ord(opString[index]))
    else:
        print("Error get. Expected one int and one string")
        

def getinterval():
    if len(opstack) > 2:
        count = opPop()
        index = opPop()
        opString = str(opPop())
        opString = opString[1:-1]
        opString = opString[index: index + count]
        opString = '(' + opString + ')'
        opPush(opString)
    else:
        print("Error getinterval. Expected two int and one string")

def putinterval():
    if len(opstack) > 2:
        opString2 = str(opPop())
        opString2 = opString2[1:-1]
        index = opPop()
        opString1 = opPop()
        ogString = opString1

        opString1 = str(opString1)
        opString1 = opString1[1:-1]
        end = len(opString2)
        newString = '(' + opString1[:index] + opString2 + opString1[index + end:] + ')'
        #opPush(newString)

        for i in range(0, len(opstack)):
            if(opstack[i] == ogString):
                opstack[i] = newString

        for i in range(0, len(dictstack)):
            for keys in dictstack[i]:
                if dictstack[i][keys] == ogString:
                    dictstack[i][keys] = newString
        
    else:
        print("Error putinterval. Expected tow string and one int")
        

def search():
    if len(opstack) > 1:
        seek = opPop()
        seek = seek[1:-1]
        opString = opPop()
        opString = opString[1:-1]
        result = opString.split(seek, 1)
        if len(result) > 1:
            value = result[1]
            value = '(' + value + ')'
            opPush(value)
            seek = '(' + seek + ')'
            opPush(seek)
            value = result[0]
            value = '(' + value + ')'
            opPush(value)
            opPush(True)
        else:
            opString = '(' + opString + ')'
            opPush(opString)
            opPush(False)
    else:
        print("Error search. Expected two strings")
        
        

#--------------------------- 18% -------------------------------------
# Array functions and operators:
#      define the helper function evaluateArray
#      define the array operators aload, astore

# I've define a function dictionary for use in evaluation. i.e add is popped but add() is called
funcDict = {'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'length':length, 'get':get, 'getinterval':getinterval, 'putinterval':putinterval, 'search':search}

def evaluateArray(aInput):
    aOutput = []
    counter = 0
    for i in aInput:
        if (isinstance(i, str) == True):
            if funcDict.get(i) is not None:
                opPush(funcDict[i]())
                if opstack[-1] == None:
                    opPop()
            elif lookup(i) is not None:
                opPush(lookup(i))
            else:
                opPush(i) #i.e '(this is a PS string)'
        else:
            opPush(i)

    for j in range(0, len(opstack)):
        aOutput.append(opPop())
    aOutput.reverse()
    aOutput = list(filter((None).__ne__, aOutput)) #filters out all occurances of None in the list.
    return aOutput
    #should return the evaluated array

def aload():
    if len(opstack) > 0:
        opArray = opPop()
        n = len(opArray)
        for i in range(0, n):
            opPush(opArray[i])
        opPush(opArray)
    else:
        print("Error aload. Expected one array")

def astore():
    if len(opstack) > 1:
        opArray = opPop()
        entries = len(opArray)
        for i in range(0, entries):
            opArray[i] = opPop()
        opArray.reverse()
        opPush(opArray)

#--------------------------- 6% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, count, pop, clear, exch, stack
def dup():
    if len(opstack) > 0:
        value = opPop()
        opPush(value)
        opPush(value)

def copy():
    if len(opstack) > 0:
        nCopies = opPop()
        copies = []
        for i in range(0, nCopies):
            copies.append(opPop())

        copies.reverse()
        for j in range(0,2):
            for k in range(0, len(copies)):
                opPush(copies[k])
    

def count():
    value = len(opstack)
    opPush(value)

def pop():
    return opPop()

def clear():
    opstack.clear()

def exch():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)

def stack():
    print(opstack)

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.
def psDict():
    opPush({})
        
def begin():
    if len(opstack) > 0:
        curDict = opPop()
        dictPush(curDict)
    else:
        print("Error begin. Expected one dictionary value")

def end():
    if len(dictstack) > 0:
        dictPop()
    else:
        print("Error end. Expected one dictionary")

def psDef():
    if len(opstack) > 1:
        value = opPop()
        name = opPop()
        define(name, value)
    else:
        print("Error psDef. Expected one name and one value")



evaluateArray(['(aBCd)',1,2,'getinterval','(BC)','eq'])