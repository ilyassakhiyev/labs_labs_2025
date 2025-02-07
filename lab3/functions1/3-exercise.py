def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return "No solution found"

a,b = int(input("Enter number of heads: ")), int(input("Enter the number of legs: "))
print(solve(a,b))  