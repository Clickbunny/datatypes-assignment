import copy
li1 = [1, 2, [3,5], 4]
li2 = copy.deepcopy(li1)
li2[0][1]=6
print(li2)

li1 = [1, 2, [3,5], 4]
li2 = copy.copy(li1) #shallow copy
li2[0][1]=6
print(li2)


#deep copy cretes a copy of ther object and the element of the object.
#sshalow copy creates a copy of the object but references each element of the object.