module HW2
     where

-- 1
{- (a) merge2 5%-}
merge2 :: [a] -> [a] -> [a]
merge2 l1 [] = l1 
merge2 [] l2 = l2
merge2 (x:xs) (y:ys) = x : y :merge2 xs ys

{- (b) merge2Tail 10% -}
merge2Tail :: [a] -> [a] -> [a]
merge2Tail l1 [] = l1
merge2Tail [] l2 = l2
merge2Tail (x:xs) (y:ys) = x : y : merge2Tail xs ys



fastReverse ::[a] ->[a]
fastReverse xs = revAppend xs []
	where 
		revAppend::[a] ->[a] ->[a]
		revAppend[]acc = acc
		revAppend(x:xs) acc = revAppend xs (x:acc)



{- (c) mergeN 5%-}
mergeN :: [[a]] -> [a]
mergeN [[]] = []
mergeN (x:xs) = foldl merge2 x xs





-- 2
{- (a) removDuplicates 10% -}
{-
removDuplicates:: Eq a => [a] -> [a]
removDuplicates [] = []
removDuplicates list = removDuplicatesHelper list []


removDuplicatesHelper:: Eq a => [a] -> [a] -> [a]
removDuplicatesHelper [] _ = []
removDuplicatesHelper (x:xs) list2
					| x `elem` list2 = removDuplicatesHelper xs list2
					| otherwise = x : removDuplicatesHelper xs (x:list2)
-}

removDuplicates:: Eq a => [a] -> [a]
removDuplicates = foldl uniq []
			where uniq acc x
				| x `elem` acc = acc
				| otherwise = acc ++ [x]

--Unneeded
removDuplicatesHelper:: (Ord a, Num a) => a -> a -> Bool
removDuplicatesHelper x y = if x == y then True else False


{- (b) count 5% -}
count::Eq a => a -> [a]-> Int
count _ [] = 0
count x list = sum(map (\a ->1) (filter (== x) list))



{- (c) histogram 10% -}
histogram::Eq a => [a] -> [(a,Int)]
histogram [] = []
--histogram list = histogram list []
histogram (x:xs) = map histogramHelper [x:xs]-- map wont run histrogramHelper on whole list, dont know why
--histogram (x:xs) = histogramHelper (x:xs) : []


histogramHelper:: Eq a => [a] -> (a,Int)
histogramHelper (x:xs) = (x, count x (x:xs))

-- 3                
{- (a) concatAll 4% -}
concatAll:: [[String]] -> String
concatAll [] = []
concatAll(x:xs) = concatHelper(concatOtherHelper (x:xs))

concatOtherHelper:: [[String]] -> [String]
concatOtherHelper [] = []
concatOtherHelper xs = foldl (++) [] xs

concatHelper:: [String] -> String
concatHelper [] = ""
concatHelper xs = foldl (++) "" xs

{- (b) concat2Either 9% -}         
data AnEither  = AString String | AnInt Int
    deriving (Show, Read, Eq)


concat2Either::[[AnEither]] -> AnEither
concat2Either [] = AString ""
concat2Either (x:xs) = concat2EitherHelper(concat2EitherOtherHelper(x:xs))


concat2EitherOtherHelper::[[AnEither]] -> [AnEither]
concat2EitherOtherHelper [] = []
concat2EitherOtherHelper xs = foldl (++) [] xs


concat2EitherHelper:: [AnEither] -> AnEither
concat2EitherHelper [] = AString ""
concat2EitherHelper xs = foldl (toAString) (AString "") xs


toAString:: AnEither -> AnEither -> AnEither
toAString (AString x) (AnInt y)   =  AString (x ++ (show y))
toAString (AString x) (AString y) = AString (x ++ y)
toAString (AnInt x) (AnInt y) = AString ((show x) ++ (show y))
toAString (AnInt x) (AString y) = AString ((show x) ++ y)


{- (b) concat2Str 6% -}               
concat2Str:: [[AnEither]] -> String
concat2Str [] = ""
concat2Str (x:xs) = anEitherToString(concat2Either(x:xs)) "" --I realized I'd just have to take [[AnEither]] to AnEither then to String

anEitherToString:: AnEither -> String -> String
anEitherToString (AString x) y =  (x ++ y)
anEitherToString (AnInt x) y = ((show x) ++ y)


-- 4 

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

{- (a) evaluateTree - 10% -}

evaluateTree:: ExprTree Int -> Int
evaluateTree (ELEAF x) = x
evaluateTree (ENODE x e1 e2) = (evaluate x) (evaluateTree (e1)) (evaluateTree (e2))




{- (b) printInfix - 10% -}
printInfix:: Show a => ExprTree a -> String
printInfix (ELEAF x) = show x
printInfix (ENODE x e1 e2) = "(" ++ printInfix (e1) ++ " `" ++ show x ++ "` " ++ printInfix (e2) ++ ")"




{- (c) createRTree 12% -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)


createRTree:: ExprTree Int -> ResultTree Int
createRTree (ELEAF x) = RLEAF x
createRTree (ENODE x e1 e2) = RNODE (evaluate x (evaluateTree e1) (evaluateTree e2)) (createRTree e1) (createRTree e2)  



-- 5
{-Sample trees 4% -}
tree1 = (ENODE Sub (ENODE Sub(ENODE Mul(ELEAF 5)(ELEAF 5))(ELEAF 6))(ENODE Add(ELEAF 12)(ELEAF 7)))
tree2 = (ENODE Add (ENODE Add(ENODE Add(ELEAF 1)(ELEAF 1))(ELEAF 1))(ENODE Add(ENODE Add(ELEAF 1)(ELEAF 1))(ELEAF 1)))





