
-- CptS 355 - Fall 2020  : 09/06/2020

module HW1
     where


-- 1.a. biggerDate and maxDate
biggerDate::(Ord a1,Ord a2, Ord a3)=>(a3,a2,a1)->(a3,a2,a1)->(a3,a2,a1)
biggerDate(day1, month1, year1)(day2, month2, year2)
	| year1 > year2 = (day1,month1,year1)
	| year2 > year1 = (day2, month2, year2)
	| month1 > month2 = (day1, month1, year1)
	| month2 > month1 = (day2, month2, year2)
	| day1 > day2 = (day1, month1, year1)
	| day2 > day1 = (day2, month2, year2)
	| otherwise = (day1, month1, year1)

-- 1.b. maxDate
maxDate::(Ord a1, Ord a2, Ord a3)=>[(a3, a2, a1)]->(a3,a2,a1)
maxDate [] = error "maxDate, Input list is empty"
maxDate [x] = x
maxDate(x:xs) = biggerDate(x)(maxDate(xs))

-- 2. ascending
ascending :: Ord t => [t] -> Bool
ascending [] = True
ascending [x] = True
ascending(x:xs) | x <= head xs = ascending(xs)
				| otherwise = False

-- 3.a. insert 
insert:: (Ord t1, Num t1)=>t1 -> t2 -> [t2] -> [t2]
insert 0 item iL = item : iL
insert n item [] = []
insert n item (x:xs) = x : insert (n-1) item xs

-- 3.b. insertEvery
{-
insertEvery::(Eq t, Num t) => t-> a-> [a] -> [a]
insertEvery n item xs = backtrace n xs where
	backtrace 0 xs = item:backtrace n xs
	backtrace _[] = []
	backtrace z (x:xs) = x:backtrace(z-1)xs            
-}
{-
insertEvery n item xs = backtrace n xs where backtrace
backtrace 0 xs = y:backtrace n xs
backtrace _[] = []
backtrace z (x:xs) = x:backtrace (z-1) xs
-}

{-
insertEvery 0 item iL = item : iL
insertEvery n item [] = []
insertEvery n item (x:xs) = insertEvery(n-1) item (x : insertEvery(n-1) item xs)
-}

-- 4.a. getSales
getSales:: (Num p, Eq t) => t -> [(t,p)] -> p
getSales day [] = 0
getSales day (x:xs) | day == fst(x) = (snd(x) + getSales(day)(xs))
					| day /= fst(x) = getSales(day)(xs)
					| otherwise = getSales(day)(xs)
                         
-- 4.b. sumSales
sumSales:: (Num p) => String -> String -> [(String,[(String,p)])] -> p
sumSales store day [] = 0
sumSales store day (x:xs) | store == fst(x) = getSales(day)(snd(x)) + sumSales(store)(day)(xs)
						  | otherwise = sumSales store day xs


-- 5.a. split
split :: Eq a => a -> [a] -> [[a]]
split dil [] = []

split dil (x:xs) | x == dil = split(dil)(xs)
				 | otherwise = [x] : split(dil)(xs)
{-
split dil (x:xs) | x /= dil = [x] : split(dil)(xs)
				 | x == dil = xs : split(dil)(xs)
				 | otherwise = split(dil)(xs)
-}
{-
split dil (x:xs) | x == dil =  [] : rest
				 | otherwise = (x : head rest) : tail rest
				 where
				 	rest = split dil xs
-}
-- 5.a. nSplit

