import colorama as c
from random import randint
from generator import colors

c.init()
lister = []

##rep
def rainbow_text(text):
    for x in text:
        lister.append(colors[randint(1, 8)])
        lister.append(x)

    print(''.join(lister))
    return ''