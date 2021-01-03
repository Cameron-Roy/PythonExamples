

# Basically, to call a function from a switch statement, just say the name of the function.
def bruh():
    return 'Brochacho'

def cringe():
    return 'Cringe bro'

def gamer():
    return 'Game'

def indirect(i):
    # This is a dictionary, basically, you pass the switcher dictionary which ever
    # the first index / spot is, and then it will run the function you mention.
    switcher = {
            0:bruh,
            1:cringe,
            2:gamer
            }

    # This is the return part of it. the 'lambda: 'Invalid'' part of this is just
    # to pass a default incorrect input statement.
    func = switcher.get(i,lambda: 'Invalid')
    return func()

print(indirect(1))

# This works
'''
def cringe(x):
    switch = {
            "h": "Help",
            "l": "List",
            "c": "Cool"
        }
    return switch.get(x, "Invalid")

uInput = input("type either, h, l or c: ")
print(cringe(uInput))
'''
