import time

x = input ("do you know how to use updog? ")
if x == ("what's updog?") or x == ("whats updog"):
    print("not much dog whats up with you?")
else:
    print(x + "?  hahahahahaa loser you dont even get my joke its a joke you should learn how to joke better at joke school")

time.sleep(1)



s = input ("okay lets do some backwards stuff now.  what text do ya want backwards homie")

def reverse(s):
    str = ""

    for i in s:
        str = i + str
        print(i)
        print (str)# damn jsut trying to see whats going on here.  omg i finally understand.  str starts at just "i", next passthru is the "previous i" (which is now "str") PLUS the new i.
    return str



print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse(s))
