import random
import string

def typeShakespeare(scriptRead):
    monkeyTyped = ''
    while monkeyTyped == '' or scriptRead.count(monkeyTyped) >= 1:
        monkeyTyped = monkeyTyped + (random.choice(string.ascii_lowercase + ' '))
            
    else:
        return (monkeyTyped[:-1])

script = open('Shakespeare.txt','r') # opens the files
scriptRead = script.read()
script.close()

keyPresses = 0
monkeyTyped = ''
while len(monkeyTyped) != len(scriptRead): ## infinite loop ... unless the monkey does it!

    monkeyTyped = typeShakespeare(scriptRead)
    keyPresses = keyPresses + len(monkeyTyped) + 1
    
    if len(monkeyTyped) >=5:
        monkeyTyped = "'"+monkeyTyped+"'"
        print monkeyTyped, keyPresses
    if keyPresses%10000==0:
        print keyPresses
