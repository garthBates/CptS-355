{-Haskell is available for Windows, Mac, and Linux. Here's the download page: http://www.haskell.org/platform/.

We will be using the HUnit unit testing package in CptS 355. -}

{- Example of using the HUnit unit test framework.  See  http://hackage.haskell.org/package/HUnit for additional documentation.
To run the tests type "runTestTT tests" at the Haskell prompt.  -}

module HW1SampleTests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW1

p1a_test1 = TestCase (assertEqual "(biggerDate (31,8,2020) (20,7,2020))" (1,8,2020)  (biggerDate (1,8,2020) (20,7,2020)) ) 
p1a_test2 = TestCase (assertEqual "(biggerDate (6,7,2020) (30,12,2019))" (6,7,2020) (biggerDate (6,7,2020) (30,12,2019)) )
p1a_test3 = TestCase (assertEqual "(biggerDate (1,1,1990) (2,1,1990))"   (2,1,1990) (biggerDate (1,1,1990) (2,1,1990))   )
p1a_test4 = TestCase (assertEqual "(biggerDate (1,1,1990) (1,1,1990))"   (1,1,1990) (biggerDate (1,1,1990) (1,1,1990))   )  

dateList = [(31,8,2020),(20,7,2020),(1,9,2020),(30,12,2019),(6,7,2018),(6,7,2020)]

p1b_test1 = TestCase (assertEqual "(maxDate dateList)" (1,9,2020)  (maxDate dateList) ) 
p1b_test2 = TestCase (assertEqual "(maxDate [(31,8,2020)])" (31,8,2020) (maxDate [(31,8,2020)]) )
p1b_test3 = TestCase (assertEqual "(maxDate [])" (error) (maxDate[]) )
p1b_test4 = TestCase (assertEqual "(maxDate [(1,1,1990),(1,1,1990)]" (1,1,1990) (maxDate[(1,1,1990),(1,1,1990)]) ) 

p2_test1 = TestCase (assertEqual "(ascending [1])"  True  (ascending [1]) ) 
p2_test2 = TestCase (assertEqual "(ascending [1,2,3,4,5,3,6,7])"  False  (ascending [1,2,3,4,5,3,6,7]) )
p2_test3 = TestCase (assertEqual "(ascending [1,3,4,5,6,7,10,100,200])"  True  (ascending [1,3,4,5,6,7,10,100,200]) )
p2_test4 = TestCase (assertEqual "(ascending []" True  (ascending[]) )
p2_test5 = TestCase (assertEqual "(ascending [10,20,3]"  False (ascending[10,20,3])  )

p3a_test1 = TestCase (assertEqual "(insert 3 100 [1,2,3,4,5,6,7,8])" [1,2,3,100,4,5,6,7,8] (insert 3 100 [1,2,3,4,5,6,7,8]) ) 
p3a_test2 = TestCase (assertEqual "(insert 8 100 [1,2,3,4,5,6,7,8])" [1,2,3,4,5,6,7,8,100] (insert 8 100 [1,2,3,4,5,6,7,8]))
p3a_test3 = TestCase (assertEqual "(insert 9 100 [1,2,3,4,5,6,7,8])" [1,2,3,4,5,6,7,8] (insert 9 100 [1,2,3,4,5,6,7,8]))
p3a_test4 = TestCase (assertEqual "(insert 3 100 [])" [] (insert 3 100 []))
p3a_test5 = TestCase (assertEqual "(insert 0 100 [1,2,3]" [100,1,2,3] (insert 0 100 [1,2,3]) )
p3a_test6 = TestCase (assertEqual "(insert 0 0 []" [0] (insert 0 0 []) )

p3b_test1 = TestCase (assertEqual "(insertEvery 3 100 [1,2,3,4,5,6,7,8,9,10])" [1,2,3,100,4,5,6,100,7,8,9,100,10] (insertEvery 3 100 [1,2,3,4,5,6,7,8,9,10]) ) 
p3b_test2 = TestCase (assertEqual "(insertEvery 8 100 [1,2,3,4,5,6,7,8])" [1,2,3,4,5,6,7,8,100] (insertEvery 8 100 [1,2,3,4,5,6,7,8]))
p3b_test3 = TestCase (assertEqual "(insertEvery 9 100 [1,2,3,4,5,6,7,8])" [1,2,3,4,5,6,7,8] (insertEvery 9 100 [1,2,3,4,5,6,7,8]))
p3b_test4 = TestCase (assertEqual "(insertEvery 3 100 [])" [] (insertEvery 3 100 []))
p3b_test5 = TestCase (assertEqual "(insertEvery 1 100 [1,2,3])" [1,100,2,100,3,100] (insertEvery 1 100 [1,2,3]) )
p3b_test6 = TestCase (assertEqual "(insert 0 0 []" [] (insert 0 0 []) )

storelog = [("Mon",50),("Fri",20), ("Tue",20),("Fri",10),("Wed",25),("Fri",30)]

p4a_test1 = TestCase (assertEqual "(getSales \"Fri\" storelog)" 60  (getSales "Fri" storelog) ) 
p4a_test2 = TestCase (assertEqual "(getSales \"Mon\" storelog)" 50  (getSales "Mon" storelog) ) 
p4a_test3 = TestCase (assertEqual "(getSales \"Sat\" storelog)" 0  (getSales "Sat" storelog) )
p4a_test4 = TestCase (assertEqual "(getSales \"Mon\" [(\"Mon\",20)]" 20 (getSales "Mon" [("Mon",20)]) )
p4a_test5 = TestCase (assertEqual "(getSales \"Mon\" []" 0 (getSales "Mon" []) ) 

sales = [("Amazon",[("Mon",30),("Wed",100),("Sat",200)]),("Etsy",[("Mon",50),("Tue",20),("Wed",25),("Fri",30)]),
         ("Ebay",[("Tue",60),("Wed",100),("Thu",30)]),("Etsy",[("Tue",100),("Thu",50),("Sat",20),("Tue",10)])]

p4b_test1 = TestCase (assertEqual "(sumSales \"Etsy\" \"Tue\" sales)" 130  (sumSales "Etsy" "Tue" sales) ) 
p4b_test2 = TestCase (assertEqual "(sumSales \"Etsy\" \"Sun\" sales)" 0  (sumSales "Etsy" "Sun" sales) ) 
p4b_test3 = TestCase (assertEqual "(sumSales \"Amazon\" \"Mon\" sales)" 30  (sumSales "Amazon" "Mon" sales) )
p4b_test4 = TestCase (assertEqual "(sumSales \"Amazon\" \"Mon\" [])" 0 (sumSales "Amazon" "Mon" []) )
p4b_test5 = TEstCase (assertEqual "(sumSales \"CraigsList\" \"Mon\" sales)" 0 (sumSales "CraigsList" "Mon" sales) ) 

p5a_test1 = TestCase (assertEqual "(split ',' \"Courses:,CptS355,CptS322,CptS451,CptS321\")" ["Courses:","CptS355","CptS322","CptS451","CptS321"] (split ',' "Courses:,CptS355,CptS322,CptS451,CptS321")) 
p5a_test2 = TestCase (assertEqual "(split 0  [1,2,3,0,4,0,5,0,0,6,7,8,9,10])" [[1,2,3],[4],[5],[],[6,7,8,9,10]] (split 0  [1,2,3,0,4,0,5,0,0,6,7,8,9,10])) 
p5a_test3 = TestCase (assertEqual "(split 1 [2,3,1,5,6,1,8])" [[2,3],[5,6],[8]] (split 1 [2,3,1,5,6,1,8]) )
p5a_test4 = TestCase (assertEqual "(split 1 [])" [] (split 1 []) )


p5b_test1 = TestCase (assertEqual "(nSplit ',' 1 \"Courses:,CptS355,CptS322,CptS451,CptS321\")" (["Courses:","CptS355,CptS322,CptS451,CptS321"]) (nSplit ',' 1 "Courses:,CptS355,CptS322,CptS451,CptS321") ) 
p5b_test2 = TestCase (assertEqual "(nSplit ',' 2 \"Courses:,CptS355,CptS322,CptS451,CptS321\")" (["Courses:","CptS355","CptS322,CptS451,CptS321"]) (nSplit ',' 2 "Courses:,CptS355,CptS322,CptS451,CptS321") ) 
p5b_test3 = TestCase (assertEqual "(nSplit ',' 4 \"Courses:,CptS355,CptS322,CptS451,CptS321\")" (["Courses:","CptS355","CptS322","CptS451","CptS321"]) (nSplit ',' 4 "Courses:,CptS355,CptS322,CptS451,CptS321") ) 
p5b_test4 = TestCase (assertEqual "(nSplit ',' 5 \"Courses:,CptS355,CptS322,CptS451,CptS321\")" (["Courses:","CptS355","CptS322","CptS451","CptS321"]) (nSplit ',' 5 "Courses:,CptS355,CptS322,CptS451,CptS321") ) 
p5b_test5 = TestCase (assertEqual "(nSplit 0 3 [1,2,3,0,4,0,5,0,0,6,7,8,9,10])" ([[1,2,3],[4],[5],[0,6,7,8,9,10]]) (nSplit 0 3 [1,2,3,0,4,0,5,0,0,6,7,8,9,10]) ) 
p5b_test6 = TestCase (assertEqual "(nSplit 1 1 [2,3,1,5,6,1,8])" [[2,3],[5,6,1,8]] (nSplit 1 1 [2,3,1,5,6,1,8]) )
p5b_test7 = TestCase (assertEqual "(nSplit 1 1 [])" [] (nSplit 1 1 []) )

-- assertEqual can't resolve the type of [] ; so the following test gives a type error. 
--p2_test4 = TestCase (assertEqual "ascending []" (True)   (ascending []) ) 

tests = TestList [ TestLabel "Problem 1a- test1 " p1a_test1,
                   TestLabel "Problem 1a- test2 " p1a_test2,
                   TestLabel "Problem 1a- test3 " p1a_test3,
                   TestLabel "Problem 1a- test4 " p1a_test4,
                   TestLabel "Problem 1b- test1 " p1b_test1,
                   TestLabel "Problem 1b- test2 " p1b_test2,
                   TestLabel "Problem 1b- test3 " p1b_test3,
                   TestLabel "Problem 1b- test4 " p1b_test4,
                   TestLabel "Problem 2- test1 " p2_test1, 
                   TestLabel "Problem 2- test2 " p2_test2, 
                   TestLabel "Problem 2- test3 " p2_test3,
                   TestLabel "Problem 2- test4 " p2_test4,
                   TestLabel "Problem 2- test5 " p2_test5,
                   TestLabel "Problem 3a- test1 " p3a_test1, 
                   TestLabel "Problem 3a- test2 " p3a_test2, 
                   TestLabel "Problem 3a- test3 " p3a_test3,
                   TestLabel "Problem 3a- test4 " p3a_test4,
                   TestLabel "Problem 3a- test5 " p3a_test5,
                   TestLabel "Problem 3a- test6 " p3a_test6,                   
                   TestLabel "Problem 3b- test1 " p3b_test1, 
                   TestLabel "Problem 3b- test2 " p3b_test2, 
                   TestLabel "Problem 3b- test3 " p3b_test3,
                   TestLabel "Problem 3b- test4 " p3b_test4,
                   TestLabel "Problem 3b- test5 " p3b_test5,
                   TestLabel "Problem 3b- test6 " p3b_test6,                                     
                   TestLabel "Problem 4a- test1 " p4a_test1, 
                   TestLabel "Problem 4a- test2 " p4a_test2, 
                   TestLabel "Problem 4a- test3 " p4a_test3,
                   TestLabel "Problem 4a- test4 " p4a_test4,
                   TestLabel "Problem 4a- test5 " p4a_test5,
                   TestLabel "Problem 4b- test1 " p4b_test1, 
                   TestLabel "Problem 4b- test2 " p4b_test2, 
                   TestLabel "Problem 4b- test3 " p4b_test3,
                   TestLabel "Problem 4b- test4 " p4b_test4,
                   TestLabel "Problem 4b- test5 " p4b_test5, 
                   TestLabel "Problem 5a- test1 " p5a_test1, 
                   TestLabel "Problem 5a- test2 " p5a_test2,
                   TestLabel "Problem 5a- test3 " p5a_test3,
                   TestLabel "Problem 5a- test4 " p5a_test4, 
                   TestLabel "Problem 5b- test1 " p5b_test1, 
                   TestLabel "Problem 5b- test2 " p5b_test2,                    
                   TestLabel "Problem 5b- test3 " p5b_test3,
                   TestLabel "Problem 5b- test4 " p5b_test4, 
                   TestLabel "Problem 5b- test5 " p5b_test5,
                   TestLabel "Problem 5b- test6 " p5b_test6,
                   TestLabel "Problem 5b- test7 " p5b_test7
                 ] 
                  
-- shortcut to run the tests
run = runTestTT  tests