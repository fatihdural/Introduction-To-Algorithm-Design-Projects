########## Part1 ##########
def optimalPlan(NyCost, SfCost, MonthsNum, MovingCost):	
	currentPathNY=NyCost[0]
	currentPathSF=SfCost[0]
	tempNy, tempSf = 0, 0
	optimalPath = []
	for i in range(MonthsNum):
		tempNy = currentPathNY
		tempSf = currentPathSF

		if( (tempSf + MovingCost + NyCost[i]) <  (tempNy + NyCost[i]) ):
			currentPathNY = tempSf + MovingCost + NyCost[i]
		else:
			currentPathNY = tempNy + NyCost[i]
		
		if( (tempNy + MovingCost + SfCost[i]) <  (tempSf + SfCost[i]) ):
			currentPathSF = tempNy + MovingCost + SfCost[i]
		else:
			currentPathSF = tempSf + SfCost[i]
		
		if( currentPathNY < currentPathSF ):
			optimalPath.append("NY")
		else:
			optimalPath.append("SF")
	return(optimalPath ) 

########## Part2 ##########
class Symposium (object):
	def __init__(self, symposiumName, startTime, finishTime):
		self.symposiumName = symposiumName
		self.startTime = startTime
		self.finishTime = finishTime
	def printSymposiumInformation(self):
		print("The", self.symposiumName, "symposium start at", self.startTime, "and finish at", self.finishTime)

def findOptimalList(symposiumList):
	optimalList = []
	currentTime = 00.00
	temp = 0
	for i in range(len(symposiumList)):
		minimum = 25
		for j in range(len(symposiumList)):
			if( (symposiumList[j].finishTime < minimum) and (symposiumList[j].startTime >= currentTime) ):
				currentTime = symposiumList[j].finishTime
				minimum = currentTime
				temp = symposiumList[j]
		if( minimum == 25 ):
			return optimalList
		optimalList.append(temp)
	return optimalList

########## Part3 ##########
def findSumZeroSubArray(set): 
    allSums = []
    currentSum = 0
    if(set[0] == 0):
    	print("First element is zero, so subset with the total sum of elements zero would be : [0]")
    	return
    for i in range(len(set)): 
        currentSum += set[i] 
        if(currentSum == 0 or currentSum in allSums): 	
        	startIndex =  allSums.index(currentSum) + 1
        	lastIndex = i+1
        	print("Subset with the total sum of elements zero is :", set[startIndex:lastIndex]) 
        	return
        allSums.append(currentSum) 
    print("There is no subset with the total sum of elements zero!!")

########## Part5 ##########
def sumOfIntegers(integerList):
	operationList = []
	print(integerList)
	for i in range(len(integerList)):
		first = min(integerList)
		integerList.remove(first)
		second = min(integerList)
		integerList.remove(second)
		result =  first + second
		operationList.append(result)
		if( len(integerList) ==  0):
			return result, sum(operationList)
		integerList.append(result)

def main():
	#########################################################
	print("\n-------PART1-------")
	NYCostList = [1, 3, 20, 30, 5, 9]
	SFCostList = [2, 20, 2, 4, 3, 20]
	MovingCost = 10
	MonthsNum = 6
	print("NY Cost List :", NYCostList)
	print("SF Cost List :", SFCostList)
	print("Moving Cost :", MovingCost)
	print("Number of months :", MonthsNum)
	print("The plan of minimum cost :", optimalPlan(NYCostList, SFCostList, MonthsNum, MovingCost))
	print("-----------------")
	NYCostList = [1, 3, 20, 30]
	SFCostList = [50, 20, 2, 4]
	MovingCost = 10
	MonthsNum = 4
	print("NY Cost List :", NYCostList)
	print("SF Cost List :", SFCostList)
	print("Moving Cost :", MovingCost)
	print("Number of months :", MonthsNum)
	print("The plan of minimum cost :", optimalPlan(NYCostList, SFCostList, MonthsNum, MovingCost))

	#########################################################
	print("\n-------PART2-------")
	s1 = Symposium("S1", 09.00, 10.00)
	s2 = Symposium("S2", 09.00, 11.00)
	s3 = Symposium("S3", 10.00, 10.30)
	s4 = Symposium("S4", 10.00, 12.00)
	s5 = Symposium("S5", 10.00, 10.30)
	s6 = Symposium("S6", 12.00, 12.30)
	s7 = Symposium("S7", 13.00, 16.00)
	s8 = Symposium("S8", 13.00, 14.00)
	s9 = Symposium("S9", 14.00, 14.45)
	s10 = Symposium("S10", 14.30, 15.30)
	symposiums = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
	optimalList = findOptimalList(symposiums)
	print("The optimal list of sessions :")
	for i in range(len(optimalList)):
		optimalList[i].printSymposiumInformation()
	print("-----------------")
	s1 = Symposium("S1", 09.00, 10.15)
	s2 = Symposium("S2", 10.00, 11.00)
	s3 = Symposium("S3", 10.15, 10.30)
	s4 = Symposium("S4", 11.00, 12.00)
	s5 = Symposium("S5", 11.00, 11.30)
	s6 = Symposium("S6", 12.00, 14.00)
	s7 = Symposium("S7", 13.00, 13.30)
	s8 = Symposium("S8", 13.00, 14.00)
	s9 = Symposium("S9", 14.00, 14.45)
	s10 = Symposium("S10", 15.30, 16.30)
	symposiums = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
	optimalList = findOptimalList(symposiums)
	print("The optimal list of sessions :")
	for i in range(len(optimalList)):
		optimalList[i].printSymposiumInformation()
  
	#########################################################
	print("\n-------PART3-------")
	set = [4, 2, -3, 1, 6]
	print("Set of integers :", set)
	findSumZeroSubArray(set)
	print("-----------------")
	set = [1, 3, 5, -8, 1, 6, 11]
	print("Set of integers :", set)
	findSumZeroSubArray(set)

	#########################################################
	print("\n-------PART5-------")
	integerList = [1, 2, 3, 4]
	sum, numberOfOp =  sumOfIntegers(integerList)
	print("Sum of integers in list is:", sum)
	print("Number of operations is :", numberOfOp )
	print("-----------------")
	integerList = [5, 8, 31, 1]
	sum, numberOfOp =  sumOfIntegers(integerList)
	print("Sum of integers in list is:", sum)
	print("Number of operations is :", numberOfOp )

main()


