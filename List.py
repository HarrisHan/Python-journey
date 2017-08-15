list1 = []
list2 = list()

numList = [8,6,5,7,2]
mixList = [1,"one",1.0]

nestList = [numList, mixList]

print(mixList + numList)

mixList.extend(numList)

numList.append([9,10])

numList = [8,3,4,2,1]

numList.sort()

numList1 = numList
numList.sort()

numList = numList.copy()

numList[0]
numList[0:3] == numList[0:-2]

# -1 表示最后一个元素 -2表示倒数第二个

numList.insert(1, 9)

numList.insert(100, 9)
print(numList)
# [8, 6, 5, 7, 2，9]

print(len(numList))

print(numList.index(2))

