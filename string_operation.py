str_1 = "apple"
str_2 = "banana"

#Comparision
if len(str_1) == len(str_2):
    print("Strings are equal")
else:
    print("String are not equal")

#Concatanation
str_3 = str_1+str_2
print("Concatanate String is: "+ str_3)

#Resersing
str_4 = "Ashek-Al-Mahady"
reserve_str = str_4[::-1] #using slicing
print("Reversed String is: ", reserve_str)

#Slicing
sub_string = str_4[7:]
print("Sliced string is: ", sub_string)