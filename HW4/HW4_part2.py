# Garth Bates 11473063
# HW4 part2

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
            #return None #this will be used for error checking in other functions
    dictstack.reverse()
    return None
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
    #print(dictstack)
    #print(opstack)
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
#funcDict = {'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'length':length, 'get':get, 'getinterval':getinterval, 'putinterval':putinterval, 'search':search}

def evaluateArray(aInput):
    aOutput = []
    opPush('MARKER')
    counter = 0
    for i in aInput:
        if (isinstance(i, str) == True):
            if funcDict.get(i) is not None:
                counter += 1
                opPush(funcDict[i]())
                if opstack[-1] == None:
                    counter -= 1
                    opPop()
            elif lookup(i) is not None:
                counter += 1
                opPush(lookup(i))
            else:
                counter +=1
                opPush(i) #i.e '(this is a PS string)'
        else:
            counter +=1
            opPush(i)

    for j in range(0, len(opstack)):
        value = opPop()
        if value == 'MARKER':
            break
        else:    
            aOutput.append(value)
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
    opPop()
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

#----------------------------Part 2 --------------------------------------
#Tokenizing

import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s\(\)!][a-zA-Z-?0-9_\s\(\)!]*[\]]|[\()][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\)]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]",s)

#Token list to code array

# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner
            # parenthesis, it will be appended to the list we are constructing
            # as a whole.
            res.append(groupMatch(it))
        elif (isInt(c) == True):
            res.append(int(c))
        else:
            res.append(c)
    return False

#Helper function to determine if token is an integer
def isInt(inStr):
    try:
        out = int(inStr)
    except:
        return False
    return True

#Helper function to conver an array to a list
def arrayToList(inArray):
    output = []

    #temp = tokenize(inArray)
    temp = inArray.split()
    
    #removes the first [ and appends the first value
    if (isInt(temp[0][1]) == True):
        output.append(int(temp[0][1]))
    else:
        output.append(temp[0][1])

    #loops through the middle of the array, appending values

    for i in range (len(temp) - 2):
        if (isInt(temp[i+1]) == True):
            output.append(int(temp[i+1]))
        else:
            output.append(temp[i+1])

    #removes the last ] and appends the value
    if (isInt(temp[-1][:-1]) == True):
        output.append(int(temp[-1][:-1]))
    else:
        output.append(temp[-1][:-1])
    
    return output
    
# Function to parse a list of tokens and arrange the tokens between { and } braces
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}': #non matching closing parenthesis; return false since there is a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(groupMatch(it))
        elif (isInt(c) == True):  #calls isInt to check token if is an integer value
            res.append(int(c))
        elif c[0] == '[': #calls arrayToList if an array is found
            res.append(arrayToList(c))
        elif c == 'True':
            res.append(bool(c)) #Append boolean True
        elif c == 'False':
            res.append(bool(c)) #Append boolean False
        else:
            res.append(c)
    return {'codearray':res}

def psFor():
    if len(opstack) > 3:
        codeArray = opPop()
        end = opPop()
        if (isinstance(end, str)):
            end = lookup(end)
        
        inc = opPop()
        if (isinstance(inc, str)):
            inc = lookup(inc)
            
        start = opPop()
        if (isinstance(start, str)):
            start = lookup(start)
        
        i = start
        '''
        for x in range(start, (inc + end), end):
            opPush(x)
            interpretSPS(codeArray)

        '''
        if (inc < 0):
            while( i >= end):
                opPush(i)
                interpretSPS(codeArray)
                i += inc
        else:
            while (i <= end):
                #print("Inside for", opstack)
                opPush(i)
                interpretSPS(codeArray)
                i = i + inc
        
    else:
        print("Error for. Expected three operands")


def psIf():
    if len(opstack) > 1:
        codeArray = opPop()
        cond = opPop()
      
        if(cond == True):
            interpretSPS(codeArray)
    else:
        print("Error if. Expected CodeArray and boolean")

def psIfelse():
    if len(opstack) > 2:
        codeArray2 = opPop()
        codeArray1 = opPop()
        cond = opPop()

        if (cond == True):
            interpretSPS(codeArray1)
        else:
            interpretSPS(codeArray2)
    else:
        print('Error ifelse. Expected two CodeArrays and boolean')

# I've define a function dictionary for use in evaluation. i.e add is popped but add() is called
funcDict = {'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'length':length, 'get':get, 'getinterval':getinterval, 'putinterval':putinterval, 'search':search, 'for':psFor, 'if':psIf, 'ifelse':psIfelse
            ,'pop':pop, 'def':psDef, 'aload':aload, 'astore':astore, 'dup':dup, 'copy':copy, 'count':count, 'clear':clear, 'exch':exch, 'stack':stack, 'dict':psDict, 'begin':begin, 'end':end}


# This will probably be the largest function of the whole project,
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them.
def interpretSPS(code): # code is a code array
    #dictPush({})
    for token in code['codearray']:
        if (isinstance(token, int) == True or isinstance(token, bool) == True): #constant int or bool
            opPush(token)
        elif (isinstance(token, list) == True): #constant array
            opPush(evaluateArray(token))
        elif(isinstance(token, dict) == True):  #codearray
            opPush(token)
        elif (isinstance(token, str) == True):
            if(len(token) >= 2 and token[0] == '(' and token[-1] == ')'):    #constant string
                opPush(token)
            elif (len(token) >= 1 and token[0] == '/'): #name
                opPush(token)
            elif(token in funcDict.keys()):   #built in operator
                (funcDict[token]())
            else:
                #if (lookup(token) is not None):
                 v = lookup(token)
                 if v is not None:
                    if(isinstance(v, dict) == True):   #v is a function
                         interpretSPS(v)        #codearray
                    else:
                        opPush(v)
                 else:
                    print("Error interpretSPS. Token undefined")
        else:
            print("Error interpretSPS. Not codearray")

def interpreter(s):
    interpretSPS(parse(tokenize(s)))

#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []


testinput1 = """
    /fact{
        0 dict
        begin
            /n exch def
            1
            n -1 1 {mul /n n 1 sub def} for 
        end
    } def
    6 fact

    """

#print(parse(tokenize(testinput1)))
#interpreter(testinput1)