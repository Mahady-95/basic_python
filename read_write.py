# Reading data from a file
import os
f=open("C:/Users/User/PycharmProjects/BasicProg/Basic/Data/read.txt", "rt")
# content = f.read(3)
# print(content)
# content = f.read(3)
# print(content)
#*********
# for line in f:
#     print(line, end="")
# f.close()
print(f.readlines(),end="")
f.close()
f=open("C:/Users/User/PycharmProjects/BasicProg/Basic/Data/write.txt", "w")
f.write("Sunday")
f.close()
f=open("C:/Users/User/PycharmProjects/BasicProg/Basic/Data/write.txt", "r")
print(f.readlines(),end="")
f.close()

f=open("C:/Users/User/PycharmProjects/BasicProg/Basic/Data/write_2.txt", "x")
a=f.write("Shunshine")
print(a)
# Writing data to a file
# with open('data.txt', 'w') as file:
#     text_to_write = "This is new data to be written to the file."
#     file.write(text_to_write)
#     print("Data has been written to the file.")
