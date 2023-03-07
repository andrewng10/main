# dictionary = A changeable, unordered collection of unique key: value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',            #Key is USA,India,China,Russia.... Will result in value (Washing DC and etc.)
            'China':'Beijing',
            'Russia':'Moscow'}

#print(capitals['Germany'])
#print(capitals.get('Germnay'))     #Checking if Germany is in the dictionary
#print(capitals.keys())             #Printing all keys
#print(capitals.values())           #Printing all values
#print(capitals.items())            #Printing both keys and values

#for key,value in capitals.items():     #Using "For Loop" to print both keys and values
    #print(key, value)

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'Las Vegas'})
#capitals.pop('China')   #Removing certain value & key
#capitals.clear()    #Clearing everything
#print(capitals)


#-----------------------------------------------------------------------------------------------------------------------
# index operator [] = gives access to a sequence's element (str,list,tuples)

#name = "andrew Ng!"

#if(name[0].islower()):      #checking if at value "0" is lowercase
    #name = name.capitalize()

#firstname = name[:6].upper()
#last_name = name[7:-1].lower()
#ast_character = name[-1]

#print(firstname)
#print(last_name)
#print(last_character)