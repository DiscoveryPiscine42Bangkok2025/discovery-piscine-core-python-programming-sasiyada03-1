filter = input().strip().replace('"','')
if not filter :
    print ('none')
else :
    input_user = input('What was the parameter? ').strip()
    if input_user == filter :
        print ("Good job!")
    else :
        print ("Nope, sorry...")