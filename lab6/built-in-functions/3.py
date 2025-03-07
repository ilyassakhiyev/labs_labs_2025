s = input()
s = s.replace(' ', '') 
if s == s[::-1]:
    print("Oh yea")
else:
    print("nope")