# Garth Bates 11473063
# HW5 SSPS

opstack = []  #assuming top of the stack is the end of the list


def opPop():
    return opstack.pop()

def opPush(value):
    opstack.append(value)

dictstack = []  #assuming top of the stack is the end of the list

def dictPop():
    return dictstack.pop()

def dictPush(pvalue = None):
    if (pvalue == None):
        dictstack.append({})
    else:
        dictstack.append(pvalue)
        if ((pvalue in dictstack) == False):
            raise Exception('Cannot push pvalue')

def define(name, value):
    if len(dictstack) == 0:
        dictPush((0,{}))
    
    dictstack[-1][1][name] = value

#Old Lookup
def lookup(name, scope):
    if scope == 'static':
        try:
            return sLookupHelper((dictstack.__len__()) -1, name)
        except:
            return None
    else:
        name = '/' + name
        dictstack.reverse()
        for dicts in dictstack:  #For every diction in the dictstack
            value = dicts[1].get(name)  #Set value for the input name
            if value is not None:
                dictstack.reverse()
                return value      #if the value exists, return it

        dictstack.reverse()
        return None
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.

def sLookupHelper(last, name):
    if name in dictstack[last]:
        return (last, dictstack[last][1][name])
    elif last == dictstack[last][0]:
        return None
    else:
        nextValue = dictstack[last]
        return sLookupHelper(nextValue[0], name)

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
        '''
        for i in range(0, len(dictstack)):
            for keys in dictstack[i]:
                if dictstack[i][keys] == ogString:
                    dictstack[i][keys] = newString
        '''
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
        
        
def evaluateArray(aInput, scope):
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
            elif lookup(i, scope) is not None:
                counter += 1
                opPush(lookup(i, scope))
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
    #print(opstack)
    
    if len(opstack) > 0:
        print('==============')
        for elem in reversed(opstack):
            print(elem)
        print('==============')
        i = len(dictstack) - 1
        for entry in reversed(dictstack):
            n, d = entry
            print('----', i, '----', entry[0], '----')
            i -= 1
            for key, value in d.items():
                print(key,value)
                #print('----' + key + '----' + value + '----')

        print('==============')
    

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

#Tokenizing

import re

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s\(\)!][a-zA-Z-?0-9_\s\(\)!]*[\]]|[\()][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\)]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]",s)

def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return {'codearray':res}
        elif c=='{':
            res.append(groupMatch(it))
        elif (isInt(c) == True):
            res.append(int(c))
        elif c[0] == '[':
            res.append(arrayToList(c))
        elif c == 'true':
            res.append(True)
        elif c == 'false':
            res.append(False)
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
        elif c == 'true':
            res.append(True)
        elif c == 'False':
            res.append(bool(c)) #Append boolean False
        elif c == 'false':
            res.append(False)
        else:
            res.append(c)
    return {'codearray':res}

def psFor(scope):
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

        if (inc < 0):
            while( i >= end):
                opPush(i)
                interpretSPS(codeArray, scope)
                i += inc
        else:
            while (i <= end):
                opPush(i)
                interpretSPS(codeArray, scope)
                i = i + inc
        
    else:
        print("Error for. Expected three operands")


def psIf(scope):
    if len(opstack) > 1:
        codeArray = opPop()
        cond = opPop()
      
        if(cond == True):
            interpretSPS(codeArray, scope)
    else:
        print("Error if. Expected CodeArray and boolean")

def psIfelse(scope):
    if len(opstack) > 2:
        codeArray2 = opPop()
        codeArray1 = opPop()
        cond = opPop()

        if (cond == True):
            interpretSPS(codeArray1, scope)
        else:
            interpretSPS(codeArray2, scope)
    else:
        print('Error ifelse. Expected two CodeArrays and boolean')

# I've define a function dictionary for use in evaluation. i.e add is popped but add() is called
funcDict = {'add':add, 'sub':sub, 'mul':mul, 'eq':eq, 'lt':lt, 'gt':gt, 'length':length, 'get':get, 'getinterval':getinterval, 'putinterval':putinterval, 'search':search, 'for':psFor, 'if':psIf, 'ifelse':psIfelse
            ,'pop':pop, 'def':psDef, 'aload':aload, 'astore':astore, 'dup':dup, 'copy':copy, 'count':count, 'clear':clear, 'exch':exch, 'stack':stack, 'dict':psDict, 'begin':begin, 'end':end}

'''
Old Code from HW4
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
'''
# ------ SSPS functions -----------
# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)
def staticLink(name):
    return 0

#the main recursive interpreter function
def interpretSPS(tokenList,scope):
        for token in tokenList['codearray']:
            if (isinstance(token, int) == True or isinstance(token, bool) == True): #constant int or bool
                opPush(token)
            elif (isinstance(token, list) == True): #constant array
                opPush(evaluateArray(token, scope))
            elif(isinstance(token, dict) == True):  #codearray
                opPush(token)
            elif (isinstance(token, str) == True):
                if(len(token) >= 2 and token[0] == '(' and token[-1] == ')'):    #constant string
                    opPush(token)
                elif (len(token) >= 1 and token[0] == '/'): #name
                    opPush(token)
                elif(token in funcDict.keys()):   #built in operator
                    if (token ==  'if' or token == 'ifelse' or token == 'for'):
                        (funcDict[token](scope))
                    else:
                        (funcDict[token]())
                else:
                    #if (lookup(token) is not None):
                    v = lookup(token, scope)

                    #dictPush((staticLink, {}))

                    if v is not None:
                        if(isinstance(v, dict) == True):   #v is a function
                            dictPush((staticLink(v), {}))
                            interpretSPS(v, scope)        #codearray
                            dictPop()
                        else:
                            opPush(v)
                    else:
                        print("Error interpretSPS. Token undefined")
            else:
                print("Error interpretSPS. Not codearray")


#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clear opstack and dictstack
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():

    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """

    testinput2 = """
    /x 4 def
    (static_?) dup 7 (x) putinterval /x exch def
    /g { x stack } def
    /f { /x (dynamic_x) def g } def
    f
    """

    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """

    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput5 = """
    /x 2 def
    /n 5  def
    /A { 1  n -1 1 {pop x mul} for} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """

    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """

    testinput7 = """
    /x [1 2 3 4] def
    /A { x aload pop add add add } def
    /C { /x [10 20 30 40 50] def A stack } def
    /B { /x [6 7 8 9] def /A { x } def C } def
    B
    """

    testinput8 = """
    /x [2 3 4 5] def
    /a 10 def  
    /A { x } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x } def /a 5 def C } def
    B
    """
    myTestInput1 = """
    /var def /helper { x stack } def
    /helper1 { /var 7 def helper } def
    helper1
    """

    myTestInput2 = """
    /G { 7 14 21 } def
    /B 7 3 mul def
    /c { b g } def
    c
    """

    myTestInput3 = """
    /g (This is a test) def
    /b { exch } def
    /q (Back incrementation) def
    1 1 10 { g q b } for
    """

    interpreter(testinput1, 'static')
    
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8, myTestInput1, myTestInput2, myTestInput3]
    i = 1
    print('This is the best I got')
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, "static")
        clearBoth()
        print("Dynamic")
        interpreter(input, "dynamic")
        clearBoth()
        print('\n-----------------------------')

    
sspsTests()