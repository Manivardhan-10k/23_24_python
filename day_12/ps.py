# l=[1,3,1,9,1,3,12,5]
# #peak number  
# #the element must be greater than its neighbours

# peak=l[0] 
# for i in range(len(l)-1):   ##
#     if l[i]>l[i-1] and l[i]>l[i+1] :
#         if l[i]>peak:
#           peak=l[i]  #3  9   3
# print(peak)




#magical number 

# num=8   #1 2 4 
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if num==sum:
#     print("magical")
# else:
#     print("not magical")




# name="ganesh"   #a e         g b n f s h
# res=""
# vowels="aeiouAEIOU"
# for i in range(len(name)):
#     if name[i] in vowels:  #membership operator
#         code=ord(name[i])   ##97 101
#         char=chr(code+1)  ##b  102
#         res+=char  ## gb gbnf
#     else:
#         res+=name[i]  #gbnfsh
# print(res)


# details={
#     'marks':{ "tel":65,"hin":56,"eng":93},  #'highest':93
# }
# sub=""
# mark=0
# for i in details:
#     if i =="marks":
#         for j in details[i]:
#             if details[i][j]>mark:
#                 mark=details[i][j]
#                 sub=j
# print(sub,mark)



# 10  
# 2
# 0   5 
# 1   2 
# 0   1
# 1

# string="1.3,12,133,155.55"
# string=string.split(",")
# only_num=True
# for i in string:  #list
#     for j in i:
#         code=ord(j)
#         if (code<48 or code>57 ) and code!=46:
#             only_num=False
#             print("other than number",j)
#             break
# if only_num:
#     print("numbers")
# else:
#     print("not number")
