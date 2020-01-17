
vowels = "aeiou"
user = input ("your words here")
blankstr = ""
index = 0
#index is a blank thing
while index < len(user):
    if user[index] == user[index] in vowels:
        blankstr += user[index] * 4
    else:
        blankstr += user[index]
    index += 1
print (blankstr)