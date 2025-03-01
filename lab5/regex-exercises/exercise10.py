import re

def camel_to_snake(s):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', s).lower()

s = input()

snake = camel_to_snake(s)

print(snake)