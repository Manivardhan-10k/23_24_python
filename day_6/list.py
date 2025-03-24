# list:
# it is a ordered collection of elements
# it is mutable 

# []
# print(type([]))

#homogenous

#heterogenous
# my_list=[1,2,3,4,5,61,7,8,9,1,55,6,8,86,8,8,9,46,56,5,7,56,587,6,45,458,4]  #0 1 2 3 4 5

# lists are accessed using indexes
#index startn from 0 

# print(my_list[15])

#len()
# last=len(my_list)-1 #5
# print(my_list[last])


# lt=[11213245,2,3]
# lt[0]=10
# print(lt)


# lt=[1,"hello",True,"hey"]

# for i in range(0,len(lt),1):##0 1 2 3
#     print(lt[i])



# lt=[1,2,3]
# lt[3]=4

#append()
# lt.append(4)
# lt.append(5)
# lt.append([5,8,9])
# lt.append(True)

# print(lt)


#copy()
# new=lt.copy()
# print(new)


#clear( )
# lt.clear()
# print(lt)

#count()
# lt=[1,2,3,1,1,1,1,1,11,1,1]
# print(lt.count(15))

#extend
# lt=[1,2,3,1,1,1,1,1,11,1,1]
# lt.extend([1,2,3,4,5])
# print(lt)



#index
# lt=[1,2,3,4,5]
# print(lt.index(50))


#insert
# lt=[1,2,3,5,6]
# lt.insert(3,4)
# print(lt)


#pop
# lt=[1,2,3,4,5,9]
# lt.pop(30)
# print(lt)

#remove
# lt=[1,2,3,4,5,9]
# lt.remove(1)
# print(lt)



#reverse

# lt=[1,2,3,4,5,6]
# lt.reverse()
# print(lt)


#sort
# lt=["hi","hill","a","b"]
# lt.sort(reverse=True)
# print(lt)



#min 
# lt=[1,2,3,5,9,-9,12,3,45,-98,-99]
# print(min(lt))

# #max
# print(max(lt))


# lt=[1,1,1,1,1,12]
# print(lt.index(1))


#task

lt=[1,2,3,5,9,-9,12,3,45,-98,-99]
even=[]
odd=[]
