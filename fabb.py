#Ans of question no 2

def fib(n, computed = {0:0,1:1}):
    if n not in computed:
        computed[n]=fib(n-1,computed)+fib(n-2, computed)
    return computed[n]

number= int(input("Enter a number:"))
for count in range(1,number):
    print(fib(count))





