def squares_inrange(a, b):
    for i in range(a, b+1):
        yield i * i

squares = squares_inrange(2, 10)

for square in squares:
    print(square)