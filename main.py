import time

x = input ("do you know how to use updog? ")

x = x.lower()  # Convert the whole thing to lower-case since comparing strings is case-sensitive
x = x.replace("'", "").replace("?", "")  # Essentially remove apostrophes and question marks
x = x.strip()  # Remove any leading or trailing white-spaces

good_answers = {  # Create a "set" of good answers
    "whats updog",
    "what is up dog",
    "what is updog"
}

if x in good_answers:  # This is called checking membership, if x is in our set
    print("not much dog whats up with you?")
else:
    print(  # This is called a f-string where you can use variables like this
        f"{x}?  hahahahahaa loser you dont even get my joke its a joke you should learn "
        f"how to joke better at joke school"  # Also it's standard to keep line length less than 120 characters
    )

time.sleep(1)



s = input ("okay lets do some backwards stuff now.  what text do ya want backwards homie")

def reverse_1(s):
    """
    This is called a doc-string that is used to communicate what your function does to the next person who
    is stuck reading your code.
    """
    str = ""
    for i in s:
        str = i + str
    return str


def reverse_2(s):
    """
    Returns the reverse of `s`

    Again, this is called slicing, but there are so many ways to use slicing.. It goes like this

    s[start:stop:step]

    so if we set the step to be `-1` then that means to step in reverse
    If we set the step to 2 it means to "step" 2 indexes at a time so it would only give you "every other" character
    If we set the step to -2 it means "every other" character in reverse
    """
    return s[::-1]


def reverse_3(s):
    """
    Returns the reverse of `s`

    reversed() is a python built-in function that will reverse things, but it doesn't return a string so we
    need to convert it back to a string.
    """
    return "".join(list(reversed(s)))


print("The original string is : ", end="")
print(s)

print("The reversed string is : ", end="")
print(reverse_1(s))
