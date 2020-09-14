def sortBlackWhite(boxList):
	for i in range(1, int (len(boxList) / 2) ):
		if (i % 2 == 1):				# replacement
			temp = boxList[i]
			boxList[i] =  boxList[-(i+1)]
			boxList[-(i+1)] = temp

def findFakeCoin(coins):	# fake coin algorithm
	if( len(coins) == 1 ):
		return coins[0]
	else:
		if( len(coins) % 2 != 0 ):	
			singleItem = coins[0]	# if lenght of list is odd, take first item and give 2 part of remaining list.
			coins.pop(0)
			fake = 0;
			firstWeight =  weightOfPart(coins[:int(len(coins) / 2) ])	# seperate 2 part and iterate with smallest one
			secondWeight = weightOfPart(coins[int(len(coins) / 2):])
			if( firstWeight < secondWeight ):
				fake =  findFakeCoin(coins[:int(len(coins) / 2)])
			else:
				fake = findFakeCoin(coins[int(len(coins) / 2):])
			if( fake < singleItem ):
				return fake
			else:
				return singleItem
		else:
			firstWeight =  weightOfPart(coins[:int(len(coins) / 2) ])
			secondWeight = weightOfPart(coins[int(len(coins) / 2):])
			if( firstWeight < secondWeight ):
				return findFakeCoin(coins[:int(len(coins) / 2)])
			else:
				return findFakeCoin(coins[int(len(coins) / 2):])

def weightOfPart(coinsPart):	# total weight of given part of list
	totalWeight = 0
	for i in range(len(coinsPart)):
		totalWeight += coinsPart[i]
	return totalWeight

def quicksort(x):
    if len(x) == 1 or len(x) == 0:      # if there are not elements, return the last element
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):       # less than pivol should be leftside and others should be rightside, this loop provides it.
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])    # send parts to quicksort recursive call.
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]        # Move elements of arr[0..i-1], that are greater than key 
        j = i-1                 # to one position ahead of their current position
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def findMedian(arr):
	arr = sorted(arr) # First we sort the array with sorted function
	print("Sorted array is ", arr)
	sizeArr = len(arr)	# take size of list

	if sizeArr % 2 == 0: 	# if size is even
		return float((arr[int((sizeArr-1)/2)] + arr[int(sizeArr/2)])/2.0)
	else:	# if size is odd
		return arr[int(sizeArr/2)] 


def findSubsequences(arr, index, subarr, result, criter): # find possible subsequences for given array with recursion
    if index == len(arr):
        if len(subarr) != 0:
            if( sumElements(subarr) >= criter ):
                result.append(sorted(subarr, reverse=True))
    else: 
        findSubsequences(arr, index + 1, subarr, result, criter) # Subsequence without including the element at current index 
        findSubsequences(arr, index + 1, subarr+[arr[index]], result, criter) # Subsequence including the element at current index 
    return

def sumElements(arr):   # sum of given list element
    totalSum = 0
    for i in range(len(arr)):
        totalSum += arr[i]
    return totalSum
def multElements(arr):  # multiply of given list elements
    totalSum = 1
    for i in range(len(arr)):
        totalSum *= arr[i]
    return totalSum
def minimumSubsequence(arr):    # find minimum sublist through all sublists
    result = multElements(arr[0]);
    resultArr = []
    for i in range(len(arr)):
        if( multElements(arr[i]) < result ):
            result = multElements(arr[i])
            resultArr = arr[i].copy()
    return resultArr

import random
		
def main():
	#########################################################
	print("-------PART1-------")
	boxNumber = 10		# choose number of total elements (2n)
	boxList = []
	for i in range(int(boxNumber/2)):	# create list first half of list as black and remaining list as white
		boxList.append("black")
	for i in range(int(boxNumber/2)):
		boxList.append("white")
	sortBlackWhite(boxList)				# sort as black-white-black-white
	for i in range(0, boxNumber):
		print(boxList[i])				# print 

	#########################################################
	print("\n","-------PART2-------")
	coinNumber = 12			# choose number of coin including fake coin.
	fakeIndex = random.randint(0,coinNumber-1)	# push fake coin to list with random index
	coins = []
	print("All coins : ")
	for i in range(coinNumber):
		if( i == fakeIndex ):
			coins.append(90)	# fake coin weight
		else:
			coins.append(100)	# real coin weight
		print(coins[i])
	fakeCoin = findFakeCoin(coins)	# find fake coin
	print("And ", fakeCoin, " is fake coin.")

	#########################################################
	print("\n","-------PART3-------")
	arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print("Unsorted array is ", arr)
	print("Sorted array with Quick Sort is ", quicksort(arr.copy()) )
	print("Sorted array with Insertion Sort is ", insertionSort(arr))

	#########################################################
	print("\n","-------PART4-------")
	arr = [1, 3, 2, 15, 28, 13, 19, 51, 41, 10]
	print("Unsorted Array is ", arr)
	print("Median of the array is ", findMedian(arr)) 

	#########################################################
	print("\n","-------PART5-------")
	arr = [2, 4, 7, 5, 22, 11]
	criter = float(( ( max(arr) + min(arr) ) * len(arr) ) / 4.0 )
	result = []
	print("Array is ", arr)
	print("Criteria is ", criter, "(all sub-arrays are bigger or equal than criteria)")
	findSubsequences(arr, 0, [], result, criter)
	print("Sub-arrays that satisfy the condition: ")
	for i in result:
		print(i)
	print("The optimal sub-array is : ", minimumSubsequence(result))

main()