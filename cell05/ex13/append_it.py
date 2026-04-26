a = input()
if not a :
    print ('none')
else :
    raw_word = a.split()
    words = [w.strip('"') for w in raw_word]

    for word in words :
        if not word.endswith('ism'):
            print (f'{word}ism')
        else :
            pass