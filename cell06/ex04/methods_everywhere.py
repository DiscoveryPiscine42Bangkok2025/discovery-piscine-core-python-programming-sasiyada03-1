import sys

def shrink (s) :
    print (s[:8])

def enlarge (s) :
    more_z = 8 - len(s)
    result = s + ('Z' * more_z)
    print (result)

def main() :
    user = input()
    argument = user.split()

    if len(argument) < 1 :
        print ('none')
        return
    else :
        for arg in argument :
            clean_arg = arg.strip("'")
            if len(clean_arg) > 8 :
                shrink(clean_arg)
            elif len(clean_arg) < 8 :
                enlarge(clean_arg)
            else :
                print (clean_arg)
main()