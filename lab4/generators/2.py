def evens(n):
    for i in range(0, n+1):
        if i%2==0:
            yield i

n=int(input())
my_nums=evens(n)
print(list(my_nums))