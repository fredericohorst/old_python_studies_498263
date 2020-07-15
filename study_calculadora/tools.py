

import re

def testpricaract(x):
    return re.match('^[a-zA-Z]$', x)

def testop(x):
    return re.match('^[+*/-]$', x) # tá dando erro... rever expressoes regulares.

def testnum(x):
    return re.match('^[0-9]+$', x)

def teststring(x):
    return re.match('^[a-zA-Z]+$', x)

def testexpress(x):
    return re.match('^[0-9]+[+*/e]-[0-9]+$', x)



