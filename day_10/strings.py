# '' ""  """"""  ''''''

# print('this is "python"')
# index 
# immutable


# lower 
# upper 
# swapcase 
# strip 
# lstrip 
# rstrip
# replace 
# startswith 
# endswith 
# .isalpha() 
# .isdigit() 
# isalnum 
# find 
# .zfill()
# center


# .isspace()
# word=" @*"
# print(word.isspace()) 


# string="this is python"  #3
# split
# print(string.split("")) #seperator

# word="python"
# word=list(word)
# print(word)
# l=[]
# for i in range(0,len(word),1):
#     l.append(word[i])
# print(l)


#join 

# print("#".join(l))



# ASCII values ---> American Standard Code for information Interchange 


# hi 

# 0-127


# 48 -57   - -0  -9
# 65 - 90    A -Z 
# 97 - 122  a-z


#ord 
# print(ord("9"))
# print(ord("A"))
# print(ord("z"))
# print(ord(" "))
# print(ord("/"))


#chr 
# print(chr(42))
# print(chr(105))



# problem solving:

# string="malayalam"  #nohtyp
# rev=""
# for i in range(len(string)-1,-1,-1):
#     rev= rev+(string[i])
# #palindromre or not 
# #mom malayalam racecar
# if rev==string:
#     print("palindrome")
# else:
#     print("not palindrome")


# string="this is python class"  #most   s  cc c  dd dd
# most=""
# c=0
# for i in range(len(string)):
#     if string.count(string[i])>c:  ##t 2 >0 2>2 4>2
#         most=string[i] #t s
#         c=string.count(string[i]) ##2 4
# print(most,c)


#anagram 
#silent listen  polo loop   pot top

# s1="silent"
# s2="listen"
# if len(s1)!=len(s2):
#     print("not anagrams")
# else:
#     ana=True
#     for i in range(len(s1)):
#         if s1.count(s1[i])!=s2.count(s1[i]):  #1
#             ana=False
#             break
# if ana:
#     print(s1,s2,"are anagrams")
# else:
#     print("not anagrams")


# string="this is python" 
# print(string[0:4:1])
# print(string[:4:])
# print(string[4::])
# print(string[::-1])
# print(string[::-1])


# word="racecars"
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


##return most repeated word in the sentence



# para="the is the most used word in the english"# is most used word in english
# para=para.split(" ")
# # print(para)
# for i in range(len(para)):
#     if para.count(para[i])==1:
#         print(para[i])


s1="abc d"
s2="dabc"
mat=False
for i in range(len(s1)): ## 0 1 2
    s=s1[i+1::]+s1[:i+1:]   ##bcd a bcda          cd ab   cdab     d abc dabc
    if s==s2:
        mat=True
        break
if mat:
    print(True)
else:
    print(False)

# djikstra's algo