def generator(n):
    for i in range(1, n+1):
        yield i**2

makeSquares = generator(5)
for square in makeSquares:
    print(square)
