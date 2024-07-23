fib = []

n = int(input("Enter the length of fibonacci series : "))

for i in range(0 , n):
    if i <= 1:
        fib.append(i)
    else:
        fib.append(fib[-1] + fib[-2])
        
print(fib)


