#exception handling 


# l=[12,13]
# print(l[2])

# if True:
# print("hi")

# Exception handling methods:
# try 
# except 
# else 
# finally


# try:
#     print(10/0)
# except:
#     print("not possible") 


# try:
#     l=[1,2,3]
#     print(l[5])
# except IndexError as e:
#     print("code not executed")
#     print(IndexError,e)
# finally:
#     print("always executed")


# try:
#     string="123456489"
#     vowels="aeiouAEIOU"
#     c=0
#     for i in string:
#         if i in vowels:
#             c+=1
#     if c==0:
#         raise Exception("no vowels found")
#     else:
#         print(c)
# except Exception as e:
#     print("error occured: ",e)



# try:
#     age=int(input("enter the age: "))
#     if age<0:
#         raise Exception ("invalid age given")
#     else:
#         print(age)
# except Exception as e:
#     print(e)


# try:
#     name="mani"
#     mob="9848022338 "
#     sum=name+mob 
#     print(sum)
# except Exception as e:
#     print(e)


# String formatting:


# def show_name(n):
#     print(f"hi, my name is {n}")
# show_name("mani")
# show_name("ram")

##f{var name}

# def add(a,b):
#     print(f"the sum is {a+b}")
# add(2,5)
# print(f"{20+30}")


num=int(input("enter  a  number: "))
prev=0
next=0
psc=0
for i in range(1,num):
    if  i*i<num:  ##1  4   9<13
        prev=i*i #1 4 9 16 
    if i*i>=num: #16>13
        next=i*i #25
        break
if num-prev==0:
    psc+=1 
    print(psc)
# if num-prev <next-num:  #13-9  < 16-13    4<3
#     print(prev , "is the nearest")
# elif next-num<num-prev:  #16-13 < 13-9   3<4
#     print(next, "is the nearest ")


