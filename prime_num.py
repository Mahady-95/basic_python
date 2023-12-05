prime_numbers = []
prime_sum = 0

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
        prime_sum += num

print("Prime numbers between 1 and 100:", prime_numbers)
print("Sum of prime numbers:", prime_sum)
# prime=0
# for i in range (2, 101):
#     for j in range(2,101):
#         if i%j==0:
#             break
#     if i == j:
#         #prime.append(i)
#         print(i, end=",")
#         #print(prime)
prime_sum = 0

for i in range(2, 101):
    for j in range(2, i):  # Changed the range to optimize the inner loop
        if i % j == 0:
            break
    else:
        print(i,end=",")
        prime_sum += i

print("\nSum of prime numbers between 2 and 100:", prime_sum)

