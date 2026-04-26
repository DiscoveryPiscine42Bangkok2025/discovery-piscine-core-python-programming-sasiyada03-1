a = input()
if not a :
    print ('none')
else :
    number = [int(n) for n in a.split()]
    start = number[0]
    end = number[1]
    result = list(range(start,end + 1))
    print (f'{result}')