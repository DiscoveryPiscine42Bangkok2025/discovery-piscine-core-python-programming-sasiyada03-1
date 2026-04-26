a = input()
text = list(a)
filter = [h for h in text if h not in {'"',"'"}]
output = ''.join(filter).upper()
print (output)