even_num = []
odd_num = []

for num in range(1, 100):
    if(num%2 == 0):
        even_num.append(num)
    else:
        odd_num.append(num)
print("Even numbers between 10 to 100 are: ", even_num)
print("Odd numbers between 10 to 100 are: ", odd_num)
