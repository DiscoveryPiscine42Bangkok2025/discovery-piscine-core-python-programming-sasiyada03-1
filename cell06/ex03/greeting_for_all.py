def greetings (name = 'nobel stranger.') :
    if not isinstance(name ,str) :
        print ('Error, It was not a name.')
    else :
        print (f'Hello, {name}')
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)