a = input().split(maxsplit=1)
if len(a) >= 2 :
    s = a[0].strip('"')
    sen = a[1].strip('"')
    count = sen.count(s)
    print (f'{count}')
else :
    print ('none')