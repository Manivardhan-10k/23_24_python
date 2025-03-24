# list=[1,2,3,4,"",True]
#0 , len-1
# len(s)
# append 
# count 
# index 
# pop 
# insert 
# extend 
# remove 
# reverse 
# sort
# copy 
# clear 
# min 
# max 


#dictionary 
# hello : greeting
#Key:value
#key should always be a string
#key should always be unique
#mutable data type


# my_details["name"]="manivardhan"
# print(my_details)
# print(len(my_details)) 

# user_name=my_details["name"]

# print(user_name)

# print(my_details["nam"])
#get
# print(my_details.get("nam"))
# print("after the print")

#keys()
# print(my_details.keys())


#values()
# print(my_details.values())

#items()
# print(my_details.items())

#update
# (my_details.update({"dob":21}))
# (my_details.update({"city":"hyd"}))
# print(my_details)


#pop()
# my_details.pop(20)
# print(my_details)

#del 
# del my_details["ages"]
# del my_details

#clear
# my_details.clear()
# print(my_details)


# for key in my_details:
#     print(my_details[key])


# my_details["add"]["d_no"]=71

# my_details["add"]["landmark"]="bank"

# print(my_details)

# my_details={'name':"mani","age":20,"emp":True,"skills":["FE","BE","Devops"],"add":{"d_no":70,"street":"bank street"}}

# req="DB"
# exists=False
# for k in my_details:
#     if k=="skills":
#         for i in range(0,len(my_details[k]),1):
#             if my_details[k][i]==req:
#                 exists=True        
# if exists:
#     print("he has the skill")
# else:
#     print("nothing")



# person={
#     "name":"sai",
#     'age':19,
#     "count":"india"
# }

#check age and count 
#if valid add a eligible key with val True
# if person["age"]>18 and person["count"]=="india":
#     person["eligible"]=True
# else:
#     person["eligible"]=False

# print(person)







# details={
#     "name1":"chandu",
#     "name2":"sashi"
# }
# k_l=list(details.keys())
# v_l=list(details.values())
# details[k_l[0]]=v_l[1]
# details[k_l[1]]=v_l[0]
# print(details)