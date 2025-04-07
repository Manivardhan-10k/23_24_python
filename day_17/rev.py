# datatypes:
# list 
# dict 
# tuple 
# set 
# string 
# number 
# boolean 

# loops 
# conditional
# functions 

# comprehensions: 
# it is easy way of writing or looping over the iterables


num=[1,2,3,4,5,6,7,8,9,10]

# even=[]
# for i in range(0,len(num)):
#     if num[i]%2==0:
#         even.append(num[i])
# print(even)

# even=[num[x] for x in range(0,len(num)) if num[x]%2==0]  #0  2 4  6 8 10
# print(even)


# num=[0,1,2,3,4,5,6,7,8,9,10,11,12]

# third=(num[x] for x in range(0,len(num),3))
# print(list(third))


# str_list=["hi","hello","how","fine","world"]

# out=[ some for some in str_list  if len(some)==5]
# print(out)


# mat=[[1,2,3],[4,5,6],[7,8,9]]
# final=[ j  for i  in mat  for j in i if j%2==0]
# print(final)

# num_list=[1,2,3,4,5,6,7,8,9,10] 
# out={x:num[x]    for x in range(0,len(num_list))}
# print(out)


# num={
#     "0":1,
#     "1":2,
#     "2":3
# }

# print(num.items())
# final={x:y  for x,y in num.items() if y%2==0}
# print(final)




# names={
#      "1":"sankar",
#      "2":"Saikrishna",
#      "3":"mani",
#      "4":"akash"   
# }
# sorted={x:y  for x,y in names.items() if len(y)==5}
# print(sorted)



# slicing:
num=[1,2,3,4,5,6,7,8,9,10] 

# new1=[]
# for i in range(2,20):
#     new1.append(num[i])
# print(new1)
# new=num[2:6:1]
# new=num[2:6:]
# new=num[2::]
# print(new)

# for i in range(len(num)-1,-1,-1):
#     print(num[i])
# new=num[::-1]
# print(new)


# string="malayalam"
# if string[::-1]==string:
#     print("palindrome")
# else:
#     print("not palindrome")
# t=(12,13,14,15,16,17)
# print(t[::-1])



string="malayalam"    #1  2 3 4 5 6