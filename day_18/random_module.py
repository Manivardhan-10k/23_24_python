##random 

# import random 
# import math

#random()   it is returning a float value
# num=math.floor(random.random()*10000)
# if num >= 1000   and num<=9999:
#     print(num)



# a<=n<=b


#random.randint(a,b)
# print(random.randint(1000,9999))

#randrange(start stop step)
# print(random.randrange(1,20,5))  #1 6 11 16 
 

# print(random.choice(("mani","ravi","sagar")))


# print(random.choices([1,2,3,5,4,3,5,86,5,8,9965,4],k=5))



# print(random.shuffle([1,2,3,4,5,6]))



# random()
# randint()
# randrange()
# choice ()
# choices()


num=random.randint(1,10)
turns=3
for i in range(1,4):
    user_input=int(input("enter the number: "))
    if user_input==num:
        print("correct guess!!")
        break
    else:
        print("try again!!")
        turns-=1
if turns==0:
    print(f"the corrent num is {num}")

target=25
player_1=0+4   
player_2=0
##(1-6)


