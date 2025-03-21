#function 
# it is a reusable block of code with acertain functionality

#functions in python are defined with 'def' keyword

# i have a username and i have to pass it to function
#arguments
#parameters
# def greet(someone):  ##someone is a parameter to store the argument
#     print("hello",someone)

# greet("mani") ##arguments
# greet("mani vardhan") ##arguments




#write a funtion to add two numbers 

# def sum(a,b):
#     print(a,b)
#     print(a+b)

# sum(2,3)
# sum(2,30) 

#positional , default , *args , **kwargs
#scope



# 1 1
# 1 2 3
# 1 2 3 6
# 1 2 3 4 10
rows=5

for i in range(1,rows+1):#1
    s=""
    sum=0
    for j in range(1,i+1):#
        s+=str(j) +" "
        sum+=j
    print(s+ str(sum))