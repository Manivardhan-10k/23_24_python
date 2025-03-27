# dict:
# collection of key value pairs
#mutable
 

# get()
# update()
# pop()
# clear
# keys
# values 
# items 
# del 




# SET:
#it will store only the unique values
#it mutable
# print(type({1,2,3,4,4,4,3}))

# my_set={1,2,3,4,5,1,2,3,4,5,6}
# print(my_set)

# my_set=set([1.2,2,5,6,8,9,4,8,"hello",True])
# for i in my_set:
#     print(i)



# my_set={1,2,3,4,5,6,"values",0}

#add
# my_set.add(7)
# my_set.add("hello")
# print(my_set)

#remove
# my_set.remove()
# print(my_set)

#discard
# my_set.discard(0)
# my_set.discard(10)
# print(my_set)


#pop
# my_set.pop()
# my_set.pop()
# my_set.pop()
# my_set.pop()
# my_set.pop()
# print(my_set)


#clear
# my_set.clear()
# print(my_set)



# s1={1,2,3,4,5,6,7,8,"hi",False}
# s2={0,6,7,'8','9',10,True}

#union
# print(s1.union(s2))
# print(s2.union(s1))

#intersection 
# print(s1.intersection(s2))
# print(s2.intersection(s1))

#difference
# print(s1.difference(s2))
# print(s2.difference(s1))

#symmetric difference

# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1))

#copy
# new=s1.copy()
# print(new)


# set1=frozenset([2,3,4,0,1,5])
# set2=frozenset([0,1,2,3,4,5])
# set1.add(9)
# print(type(set1))
# new=set1.copy()
# print(new)

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))


#isdisjoint
# print(set1.isdisjoint(set2))

#issubset
# print(set2.issubset(set1))

#issuperset
# print(set1.issuperset(set2))


# set1={1,100,202,22,33,3003,4}
# print(set1)