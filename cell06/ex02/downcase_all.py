def lower_txt (a):
    a_split = a.split()
    for item in a_split :
        clean = item.strip('"').lower()
        print (clean)
a = input()
if not a :
    print ('none')
else :
    
    lower_txt(a)