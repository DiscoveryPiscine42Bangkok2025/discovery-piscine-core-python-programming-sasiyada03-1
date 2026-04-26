a = input()
if not a :
    print ('none')
else :
    clean = a.strip('"')
    result = ""
    for char in clean :
        if char == 'z' :
            result += 'z'
    print (f'{result}')