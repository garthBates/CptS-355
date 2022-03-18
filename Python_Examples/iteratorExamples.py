# Additional Iterator Examples

class Naturals(object):
    def __init__(self,init):
        self.current = init
    def __next__(self):
        result = self.current
        self.current += 1
        return result
    def __iter__(self):
        return self

class NaturalsUptoN(object):
    def __init__(self,init,N):
        self.current = init
        self.N = N
    def __next__(self):
        if self.current > self.N: 
            raise StopIteration
        result = self.current
        self.current += 1
        return result
    def __iter__(self):
        return self
    
class copyIter(object):
    def __init__(self,it):
        self.input1 = it         
    def __next__(self):
        try:
            self.current = self.input1.__next__()
        except:
            raise StopIteration
        return self.current
    def __iter__(self):
        return self


class copyIter2(object):
    def __init__(self,it):
        self.input1 = it
        try:
            self.current = self.input1.__next__()
        except:
            self.current = None
    def __next__(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        try:
            self.current = self.input1.__next__()
        except:
            raise StopIteration
        return result
    def __iter__(self):
        return self


it = copyIter2(iter([1,2,3,4,5,6]))
print("First:", it.__next__())
print("Second", it.__next__())
for item in it:
    print(item)


#generator example
def letters(start, finish):
   current = start
   while current <= finish:
      yield current
      current = chr(ord(current)+1)

gLetters = letters("a","d")
gLetters.__next__()

for a in letters("a","f"):
    print(a)
list(gLetters)


#use of iterators
def getCourse(it):
    course = ""
    for c in it:
        if c=='-':
            return course
        else:
            course += c
    return course

i = iter("CptS355-CptS322-CptS321")
course1 = getCourse(i)
course2 = getCourse(i)
course3 = getCourse(i)