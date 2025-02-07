def is_palindrome(string):
    cleaned = ''.join(filter(str.isalnum, string)).lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("madam"))
print(is_palindrome("programming"))