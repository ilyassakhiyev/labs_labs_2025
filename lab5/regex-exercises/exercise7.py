import re

def snake_camel(match):
    return match.group(1).upper()

def convert_to_camel_case(snake_str):
    camel_case_str = re.sub(r'_(\w)', snake_camel, snake_str)
    return camel_case_str

snake_str = input()

camel_case = convert_to_camel_case(snake_str)

print(camel_case)