 # tuple = collection which is ordered and unchangeable used to group together related data


#student = ("Bob",19,"male")

#print(student.count("Bob"))
#print(student.index("male"))

#for x in student:
    #print(x)

#if "Bob" in student:
    #print("Bob is here!")


#-----------------------------------------------------------------------------------------------------------------------

#set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)    #adding dishes to utensils
#dinner_table = utensils.union(dishes)  #adding dishes to utensils

#print(utensils.difference((dishes)))    #Finding what utensils have that dishes don't
print(utensils.intersection(dishes))    #Finding what is in common between the two groups
#for x in dishes:
    #print(x)