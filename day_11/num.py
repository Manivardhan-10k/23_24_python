# list 
# dict 
# set /frozen set 
# tuple 
# strings
# boolean   

# numbers
int 
float 
complex

# int: 
# -infi  infi 
# -999999 1321654541354

# print(type(111))
# print(type(-1213111))


# Float 
# print(type(-3.5))
# print(type(5.0))



#complex
# print(type(2+3j))

num=9848022338 
#it is not having any indexes
#it is immutable 

# print(len(num))


# abs
# print(abs(-987.00))


# pow 
# print(pow(5,2))
# print(pow(2,8))

#round
# print(round(3.1412,3))


#divmod
# 5/2  2.5 
# 5%2   1
# print(divmod(6,2))


# print(min(1,2))
# print(max(1,2))

# num=9848022338 
# print(len(str(num)))
# n2=123
# print(len(n2))

#mod  div// 



#we need to divide the number with 10 

# print(98480%10) 9848  984.8     98.4 9.8   .9  0
# num=9848022338
# count=0
# while num!=0:#9848 984 98 9 0
#     digit=num%10   #8 4 8 9
#     num=num//10    #98  9 0
#     count=count+1 
# print(count)



#armstrong number 
#8+1+8  =17
#153     1+125+27   153 

# num=153
# copy=num #212
# sec_copy=num
# length=0

# while num!=0: ##212 21 1 0
#     num=num//10  #21 2 0
#     length+=1 #1 2 3
# sum=0
# while copy!=0: #212 21 2 0
#     digit=copy%10 # 2  1 2
#     sum=sum + digit**length #  2**3  8 8+1**3  9  9+2**3 +   9+ 8 17
#     copy=copy//10   #21 2 0
# if sum==sec_copy:  #17==212
#     print("armstrong")
# else:
#     print("not armstrong")


num=1234567890# 7
copy=num
pos=1
count=0
while num!=0:
    num=num//10
    count+=1
if count>=pos:
    while copy!=0:
        digit=copy%10 
        copy=copy//10
        if count==pos:   
            print(digit)
        count=count-1   



    