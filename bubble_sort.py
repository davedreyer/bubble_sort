import random

# As a program below

listV = []
for value in range(0,100):
	x = random.randint(0,10000)
	listV.append(x)
print listV	
counter = True
while counter == True:
	counter = False
	for count in range(0, len(listV) - 1):
		if listV[count + 1] < listV[count]:
			holderTuple = (listV[count + 1], listV[count])
			listV[count] = holderTuple[0]
			listV[count + 1] = holderTuple[1]
			counter = True
print listV


# As a function that calculates the list

# def bubbleSort():

# 	listV = []
# 	for value in range(0,100):
# 		x = random.randint(0,10000)
# 		listV.append(x)
# 	print listV	

# 	counter = True
# 	while counter == True:
# 		counter = False
# 		for count in range(0, len(listV) - 1):
# 			if listV[count + 1] < listV[count]:
# 				holderTuple = (listV[count + 1], listV[count])
# 				listV[count] = holderTuple[0]
# 				listV[count + 1] = holderTuple[1]
# 				counter = True
# 	print listV

# bubbleSort()

# As a function where list is passed as an argument

# def bubbleSort(listV):
# 	counter = True
# 	while counter == True:
# 		counter = False
# 		for count in range(0, len(listV) - 1):
# 			if listV[count + 1] < listV[count]:
# 				holderTuple = (listV[count + 1], listV[count])
# 				listV[count] = holderTuple[0]
# 				listV[count + 1] = holderTuple[1]
# 				counter = True
# 	print listV

# listV = []
# for value in range(0,100):
# 	x = random.randint(0,10000)
# 	listV.append(x)
# print listV		

# bubbleSort(listV)

