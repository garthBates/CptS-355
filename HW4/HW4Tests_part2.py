import unittest
from HW4_part2 import *

class HW4GradingTests(unittest.TestCase):

    def setUp(self):
        clearStacks()  #clear both stacks
        dictstack.append({})

    
    def test_input1_parse(self):
        testinput1 = """
            /square {dup mul} def
            [3 -2 1]  aload pop
            /total 0 def
            1 1 3 {pop square total add /total exch def} for
            total 14 eq stack
        """
        parseOutput = {'codearray': ['/square', {'codearray': ['dup', 'mul']}, 'def', [3, -2, 1], 'aload', 'pop', '/total', 0, 'def', 1, 1, 3, {'codearray': ['pop', 'square', 'total', 'add', '/total', 'exch', 'def']}, 'for', 'total', 14, 'eq', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput1)),parseOutput)
    
    def test_input1(self):
        testinput1 = """
            /square {dup mul} def
            [3 -2 1]  aload pop
            /total 0 def
            1 1 3 {pop square total add /total exch def} for
            total 14 eq stack
        """
        opstackOutput = [True]
        dictstackOutput = [{'/square': {'codearray': ['dup', 'mul']}, '/total': 14}]
        interpreter(testinput1)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input2_parse(self):
        testinput2 = """
            /x 1 def
            /y 2 def
            /x 10 def
            /y 20 def
            0 x 1 y {add} for
            stack
        """
        parseOutput = {'codearray': ['/x', 1, 'def', '/y', 2, 'def', '/x', 10, 'def', '/y', 20, 'def', 0, 'x', 1, 'y', {'codearray': ['add']}, 'for', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput2)),parseOutput)
    
    
    def test_input2(self):
        testinput2 = """
            /x 1 def
            /y 2 def
            /x 10 def
            /y 20 def
            0 x 1 y {add} for
            stack
        """
        opstackOutput = [165]
        dictstackOutput = [{'/x': 10, '/y': 20}]
        interpreter(testinput2)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input3_parse(self):
        testinput3 = """
            /f {dup length} def
            [1 2 (322) (451) length]
            [1 -2 4 5 add (long) length]
            (123456)  f
            stack
        """
        parseOutput = {'codearray': ['/f', {'codearray': ['dup', 'length']}, 'def', [1, 2, '(322)', '(451)', 'length'], [1, -2, 4, 5, 'add', '(long)', 'length'], '(123456)', 'f', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput3)),parseOutput)
    
    def test_input3(self):
        testinput3 = """
            /f {dup length} def
            [1 2 (322) (451) length]
            [1 -2 4 5 add (long) length]
            (123456)  f
            stack
        """
        opstackOutput = [[1, 2, '(322)', 3], [1, -2, 9, 4], '(123456)', 6]
        dictstackOutput = [{'/f': {'codearray': ['dup', 'length']}}]
        interpreter(testinput3)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input4_parse(self):
        testinput4 = """
                /x 1 def
                /y 2 def
                1 dict begin
                /x 10 def
                1 dict begin /y 3 def x y end
                /y 20 def
                x y
                end
                x y
        """
        parseOutput = {'codearray': ['/x', 1, 'def', '/y', 2, 'def', 1, 'dict', 'begin', '/x', 10, 'def', 1, 'dict', 'begin', '/y', 3, 'def', 'x', 'y', 'end', '/y', 20, 'def', 'x', 'y', 'end', 'x', 'y']}
        self.assertDictEqual(parse(tokenize(testinput4)),parseOutput)
    
    def test_input4(self):
        testinput4 = """
                /x 1 def
                /y 2 def
                1 dict begin
                /x 10 def
                1 dict begin /y 3 def x y end
                /y 20 def
                x y
                end
                x y
        """
        opstackOutput = [10, 3, 10, 20, 1, 2]
        dictstackOutput = [{'/x': 1, '/y': 2}]
        interpreter(testinput4)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input5_parse(self):
        testinput5 = """
                /sumArray
                {0 exch aload pop count n sub -1 1 {pop add} for /n n 1 add def } def
                /x 5 def
                /y 10 def
                /n 1 def
                [1 2 3 4 x] sumArray
                [x 7 8 9 y] sumArray
                [y 11 12] sumArray
                [0 0 0] astore
                stack
        """
        parseOutput = {'codearray': ['/sumArray', {'codearray': [0, 'exch', 'aload', 'pop', 'count', 'n', 'sub', -1, 1, {'codearray': ['pop', 'add']}, 'for', '/n', 'n', 1, 'add', 'def']}, 'def', '/x', 5, 'def', '/y', 10, 'def', '/n', 1, 'def', [1, 2, 3, 4, 'x'], 'sumArray', ['x', 7, 8, 9, 'y'], 'sumArray', ['y', 11, 12], 'sumArray', [0, 0, 0], 'astore', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput5)),parseOutput)
    
    def test_input5(self):
        testinput5 = """
                /sumArray
                {0 exch aload pop count n sub -1 1 {pop add} for /n n 1 add def } def
                /x 5 def
                /y 10 def
                /n 1 def
                [1 2 3 4 x] sumArray
                [x 7 8 9 y] sumArray
                [y 11 12] sumArray
                [0 0 0] astore
                stack
        """
        opstackOutput = [[15, 39, 33]]
        dictstackOutput = [{'/sumArray': {'codearray': [0, 'exch', 'aload', 'pop', 'count', 'n', 'sub', -1, 1, {'codearray': ['pop', 'add']}, 'for', '/n', 'n', 1, 'add', 'def']}, '/x': 5, '/y': 10, '/n': 4}]
        interpreter(testinput5)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input6_parse(self):
        testinput6 = """
                1 2 3 4 5 count copy 15 1 1 5 {pop exch sub} for 0 eq
                stack
        """
        parseOutput = {'codearray': [1, 2, 3, 4, 5, 'count', 'copy', 15, 1, 1, 5, {'codearray': ['pop', 'exch', 'sub']}, 'for', 0, 'eq', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput6)),parseOutput)
    
    def test_input6(self):
        testinput6 = """
                1 2 3 4 5 count copy 15 1 1 5 {pop exch sub} for 0 eq
                stack
        """
        opstackOutput = [1, 2, 3, 4, 5, True]
        dictstackOutput = [{}]
        interpreter(testinput6)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input7_parse(self):
        testinput7 = """
                (CptS322 HW1_CptS355 HW2)
                dup /myclass exch def
                myclass 16 3 getinterval /c exch def
                myclass 4 c putinterval
                myclass
                stack
        """
        parseOutput = {'codearray': ['(CptS322 HW1_CptS355 HW2)', 'dup', '/myclass', 'exch', 'def', 'myclass', 16, 3, 'getinterval', '/c', 'exch', 'def', 'myclass', 4, 'c', 'putinterval', 'myclass', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput7)),parseOutput)
    
    def test_input7(self):
        testinput7 = """
                (CptS322 HW1_CptS355 HW2)
                dup /myclass exch def
                myclass 16 3 getinterval /c exch def
                myclass 4 c putinterval
                myclass
                stack
        """
        opstackOutput = ['(CptS355 HW1_CptS355 HW2)', '(CptS355 HW1_CptS355 HW2)']
        dictstackOutput = [{'/myclass': '(CptS355 HW1_CptS355 HW2)', '/c': '(355)'}]
        interpreter(testinput7)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input8_parse(self):
        testinput8 = """
            (COVID-19 Vaccine)
                dup
                ( ) search pop exch pop
                (-19) search
                {
                    pop pop pop (Vaccine) eq
                    { (yay) }
                    { (???)  }
                    ifelse
                } if
                stack
        """
        parseOutput = {'codearray': ['(COVID-19 Vaccine)', 'dup', '( )', 'search', 'pop', 'exch', 'pop', '(-19)', 'search', {'codearray': ['pop', 'pop', 'pop', '(Vaccine)', 'eq', {'codearray': ['(yay)']}, {'codearray': ['(???)']}, 'ifelse']}, 'if', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput8)),parseOutput)
    
    def test_input8(self):
        testinput8 = """
            (COVID-19 Vaccine)
                dup
                ( ) search pop exch pop
                (-19) search
                {
                    pop pop pop (Vaccine) eq
                    { (yay) }
                    { (???)  }
                    ifelse
                } if
                stack
        """
        opstackOutput = ['(COVID-19 Vaccine)', '(yay)']
        dictstackOutput = [{}]
        interpreter(testinput8)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input9_parse(self):
        testinput9 = """
                [1 2 3 4 5] aload /myA exch def
                count copy [0 0 0 0 0] astore
                myA eq
                stack
        """
        parseOutput = {'codearray': [[1, 2, 3, 4, 5], 'aload', '/myA', 'exch', 'def', 'count', 'copy', [0, 0, 0, 0, 0], 'astore', 'myA', 'eq', 'stack']}
        self.assertDictEqual(parse(tokenize(testinput9)),parseOutput)
    
    def test_input9(self):
        testinput9 = """
                [1 2 3 4 5] aload /myA exch def
                count copy [0 0 0 0 0] astore
                myA eq
                stack
        """
        opstackOutput = [1, 2, 3, 4, 5, True]
        dictstackOutput = [{'/myA': [1, 2, 3, 4, 5]}]
        interpreter(testinput9)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input10_parse(self):
        testinput10 = """
                /n 5 def
                /fact {
                    0 dict begin
                    /n exch def
                    n 2 lt
                    { 1}
                    {n 1 sub fact n mul }
                    ifelse
                    end
                } def
                n fact
        """
        parseOutput = {'codearray': ['/n', 5, 'def', '/fact', {'codearray': [0, 'dict', 'begin', '/n', 'exch', 'def', 'n', 2, 'lt', {'codearray': [1]}, {'codearray': ['n', 1, 'sub', 'fact', 'n', 'mul']}, 'ifelse', 'end']}, 'def', 'n', 'fact']}
        self.assertDictEqual(parse(tokenize(testinput10)),parseOutput)
    
    def test_input10(self):
        testinput10 = """
                /n 5 def
                /fact {
                    0 dict begin
                    /n exch def
                    n 2 lt
                    { 1}
                    {n 1 sub fact n mul }
                    ifelse
                    end
                } def
                n fact
        """
        opstackOutput = [120]
        dictstackOutput = [{'/n': 5, '/fact': {'codearray': [0, 'dict', 'begin', '/n', 'exch', 'def', 'n', 2, 'lt', {'codearray': [1]}, {'codearray': ['n', 1, 'sub', 'fact', 'n', 'mul']}, 'ifelse', 'end']}}]
        interpreter(testinput10)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input11_parse(self):
        testinput11 = """
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
        parseOutput = {'codearray': ['/fact', {'codearray': [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1, {'codearray': ['mul', '/n', 'n', 1, 'sub', 'def']}, 'for', 'end']}, 'def', 6, 'fact']}
        self.assertDictEqual(parse(tokenize(testinput11)),parseOutput)
    
    def test_input11(self):
        testinput11 = """
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
        opstackOutput = [720]
        dictstackOutput = [{'/fact': {'codearray': [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1, {'codearray': ['mul', '/n', 'n', 1, 'sub', 'def']}, 'for', 'end']}}]
        interpreter(testinput11)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])
    
    def test_input12(self):
        testinput12 = """
            /g 14 def
            /b 7 def
            /half {g b sub} def
            half b eq
            stack
        """
        opstackOutput = [True]
        dictstackOutput = [{'/g': 14, '/b': 7, '/half': {'codearray': ['g', 'b', 'sub']}}]
        interpreter(testinput12)
        self.assertEqual(opstack,opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])

    def test_input13(self):
        testinput13 = """
            /g 0 def
            1 3 15 {2 mul} for
            stack
        """
        opstackOutput = [2, 8, 14, 20, 26]
        dictstackOutput = [{'/g':0}]
        interpreter(testinput13)
        self.assertEqual(opstack, opstackOutput)
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])

    def test_input14(self):
        testinput14 = """
            /g (This is a test) def
            /b {exch } def
            /q (Back incrementation) def
            1 1 10 {g q b} for
            stack
        """
        opstackOutput = [1, '(Back incrementation)', '(This is a test)', 2, '(Back incrementation)', '(This is a test)', 3, '(Back incrementation)', '(This is a test)', 4, '(Back incrementation)', '(This is a test)', 5, '(Back incrementation)', '(This is a test)', 6, '(Back incrementation)', '(This is a test)', 7, '(Back incrementation)', '(This is a test)', 8, '(Back incrementation)', '(This is a test)', 9, '(Back incrementation)', '(This is a test)', 10, '(Back incrementation)', '(This is a test)']
        dictstackOutput = [{}]
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])


    def test_input15(self):
        testinput15 = """
            /x 4 def 
            /g { x stack } def 
            /f { /x 7 def g } def 
            f
            """
        opstackOutput = [7]
        dictstackOutput = [{'/x': 7, '/g': {'codearray': ['x', 'stack']}, '/f': {'codearray': ['/x', 7, 'def', 'g']}}]
        dictstackOutput = [{}]
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])

    def test_input16(self):
        testinput16 = """
            /x 4 def
            /g 26 def
            /f {g x sub} def
            8 1 -1 f for
            stack
        """
        opstackOutput = ['/f', 8]
        dictstackOutput = [{}]
        self.assertEqual(len(dictstack),len(dictstackOutput))
        for i in range(0,len(dictstackOutput)):
            self.assertDictEqual(dictstack[i],dictstackOutput[i])

if __name__ == '__main__':
    unittest.main()

