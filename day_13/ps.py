#ps on lists 


# l=[111,222,3,4,50,6,7,-8,90,9,10,10,10]
# c=3
# l2=list(set(l.copy()))
# ##third highest value in the list
# for i in range(1,c): #  1-2
#     l2.remove(max(l2))
# print(max(l2))



# lis=[[1,2,0],[30,2,1],[5,6,7,4]]

# #[[1,2],[5,6,7],[3,40]]
# for i in range(len(lis)):
#     for j in range(len(lis)):
#         if lis[i][0]<lis[j][0]:
#             temp=lis[i]
#             lis[i]=lis[j]
#             lis[j]=temp
# print(lis)

   
# lis=[[1,2,0],[30,2,1],[5,6,7,4]]
# #[[30,2,1],[5,6,7,4],[1,2,0]]
# for i in range(len(lis)):
#     for j in range(len(lis)):
#         m1=lis[i][0]
#         for k in range(len(lis[i])):
#             if lis[i][k]>m1:
#                 m1=lis[i][k]
#         m2=lis[j][0]
#         for k in range(len(lis[j])):
#             if lis[j][k]>m2:
#                 m2=lis[j][k]
#         if m1>m2:
#             temp=lis[i]
#             lis[i]=lis[j]
#             lis[j]=temp
# print(lis)




# lis=[[1,2,0],[30,2,1],[5,6,7,4],[1,2,0]]
# for i in lis:
#     if lis.count(i)>1:
#         lis.remove(i)
# print(lis)


# num=int(input("enter the number:  "))#9848022338
num=5848022338
max=num%10  #8
# min=num%10  #8
min=0  #8
c=0
while num!=0:
    dig=num%10 # 8
    if c==0:
        min=dig
        c+=1
    if dig>max: #
        max=dig  #9
    if dig<min:
        min=dig #3 2 0
    num=num//10
if min==max:
    print("all digits are same")
else:
    print("max is ",max)
    print("min is ",min)










