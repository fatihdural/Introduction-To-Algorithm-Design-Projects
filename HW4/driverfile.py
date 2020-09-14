########## Part2 ##########
def kth(firstarr, secondarr, k):
	if( len(firstarr) + len(secondarr)  < k ):
		print("List index out of range. k must be smaller or equal (m + n)")
		return
	firstIndex = 0
	secondIndex = 0
	for i in range(1, len(firstarr) * len(secondarr)):
		if( firstarr[firstIndex] < secondarr[secondIndex] ):
			firstIndex += 1
			if( i == k):
				return firstarr[firstIndex-1]
		else:
			secondIndex += 1
			if( i == k):
				return secondarr[secondIndex-1]

########## Part3 ##########
def maxSubsequence(seq): 
	tempSum = maxSum = k = 0
	firstIndex, lastIndex = 0, -1
	for i in range( len(seq) ):
		tempSum += seq[i]
		if tempSum > maxSum:
			maxSum = tempSum
			firstIndex = k
			lastIndex   = i
		elif tempSum < 0:
			tempSum = 0
			k = i + 1
	return (seq[firstIndex : lastIndex + 1], maxSum)

########## Part4 ##########
class Graph(): 
	def __init__(init, V): 
		init.V = V 
		init.graph = [[0 for column in range(V)] 
						for row in range(V)] 
		init.colorArr = [-1 for i in range(init.V)] 
	def printGraph(init):
		for i in range(init.V):
			print(init.graph[i])
	def isBipartiteUtil(init, src): 
		queue = [] 
		queue.append(src) 
		while queue: 
			U = queue.pop() 
			if init.graph[U][U] == 1: 
				return False; 
			for v in range(init.V): 
				if (init.graph[U][v] == 1 and
					init.colorArr[v] == -1): 
					init.colorArr[v] = 1 - init.colorArr[U] 
					queue.append(v) 
				elif (init.graph[U][v] == 1 and
					init.colorArr[v] == init.colorArr[U]): 
					return False
		return True
	def isBipartite(init): 
		init.colorArr = [-1 for i in range(init.V)] 
		for i in range(init.V): 
			if init.colorArr[i] == -1: 
				if not init.isBipartiteUtil(i): 
					return False
		return True
					
########## Part5 ##########
def findBestDay(costArr, priceArr):
	gain = [0]
	for i in range(0, len(costArr)-1):
		gain.append((priceArr[i+1] - costArr[i]))
	print("Gain : ", gain)
	if( all(i <= 0 for i in gain) ):
		print("There is no day to make money")
	else:
		print("The best day to buy goods is ", gain.index(max(gain))) 

def main():
	#########################################################
	print("\n-------PART2-------")
	firstarr = [2, 3, 6, 7, 9]
	secondarr = [1, 4, 8, 10] 
	k = 5
	print("First sorted array : ", firstarr)
	print("Second sorted array : ", secondarr)
	print("k : ", k)
	print("kth element is ", kth(firstarr, secondarr, k) ) 	
	print("-----------------")
	firstarr = [10, 20, 30, 60, 90]
	secondarr = [5, 10, 10, 40] 
	k = 3
	print("First sorted array : ", firstarr)
	print("Second sorted array : ", secondarr)
	print("k : ", k)
	print("kth element is ", kth(firstarr, secondarr, k) ) 	
	kth(firstarr, secondarr, k)	

	#########################################################
	print("\n-------PART3-------")
	seq = [5, -6, 6, 7, -6, 7, -4, 3]
	print("Given array : ", seq)
	Subsequence, sumSubsequence =  maxSubsequence(seq)
	print("The contiguous subsequence is ", Subsequence)
	print("And sum of subsequence is ", sumSubsequence)
	print("-----------------")
	seq = [-2, -3, 4, -1, -2, 1, 5, -3]
	print("Given array : ", seq)
	Subsequence, sumSubsequence =  maxSubsequence(seq)
	print("The contiguous subsequence is ", Subsequence)
	print("And sum of subsequence is ", sumSubsequence)

	#########################################################
	print("\n-------PART4-------")
	g = Graph(4) 
	g.graph = [[0, 1, 1, 1],
				[1, 0, 0, 1],
				[1, 0, 0, 1],
				[0, 1, 1, 0]]
	print("Graph is ↓")
	g.printGraph()
	if( g.isBipartite() ):
		print("Is graph bipartite? YES")
	else:
		print("Is graph bipartite? NO")
	print("-----------------")
	g = Graph(4) 
	g.graph = [[0, 1, 0, 1], 
            [1, 0, 1, 0], 
            [0, 1, 0, 1], 
            [1, 0, 1, 0]] 
	print("Graph is ↓")
	g.printGraph()
	if( g.isBipartite() ):
		print("Is graph bipartite? YES")
	else:
		print("Is graph bipartite? NO")

	#########################################################
	print("\n-------PART5-------")
	costArr = [5, 11, 2, 21, 5, 7, 8, 12, 13, 0]
	priceArr = [0, 7, 9, 5, 21, 7, 13, 10, 14, 20]
	print("Costs : ", costArr)
	print("Prices : ", priceArr)
	findBestDay(costArr, priceArr)
	print("-----------------")
	costArr = [5, 2, 1, 2, 5, 7, 8, 1, 3, 0]
	priceArr = [0, 3, 1, 0, 1, 0, 1, 1, 1, 2]
	print("Costs : ", costArr)
	print("Prices : ", priceArr)
	findBestDay(costArr, priceArr)

main()


