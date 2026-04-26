a = input()
if not a :
    print ('none')
else :
    raw_word = a.split()
    words = []
    for item in raw_word :
        clean = item.strip('"')
        words.append(clean)

    print (f'parameters : {len(words)}')
    for word in words :
        
        print (f'{word} : {len(word)}')