import term as t
import termcolor as tc
def popup(text, title, x=0, y=0):
    t.pos(x, y)
    t.write('''┌─────────────────────────────┐
│                                  │
│                                  │
│                                  │
│                                  │
│                                  │
│                                  │
└─────────────────────────────┘''')
    t.pos(x, y)
    t.down()
    t.right()
    t.write(tc.colored(title, 'green'))
    t.pos(x, y)
    t.down()
    t.down()
    t.right()
    t.write(text)
    t.down()
    t.down()
    t.down()
    t.down()
    t.down()
    t.down()

def popupText(text, title, x=0, y=0):
    t.pos(x, y)
    t.write('''┌─────────────────────────────┐
│                                  │
│                                  │
│                                  │
│                                  │
│                                  │
│                                  │
└─────────────────────────────┘''')
    t.pos(x, y)
    t.down()
    t.right()
    t.write(tc.colored(title, 'green'))
    t.pos(x, y)
    t.down()
    t.down()
    t.right()
    t.write(text)
    t.pos(x, y)
    t.down()
    t.down()
    t.down()
    t.right()
    i = input()
    t.down()
    t.down()
    t.down()
    t.down()
    return i

def popupYesNo(text, title, x=0, y=0):
    t.pos(x, y)
    t.write('''┌─────────────────────────────┐
│                                  │
│                                  │
│                                  │
│                                  │
│                                  │
│                                  │
└─────────────────────────────┘''')
    t.pos(x, y)
    t.down()
    t.right()
    t.write(tc.colored(title, 'green'))
    t.pos(x, y)
    t.down()
    t.down()
    t.right()
    t.write(text)
    t.pos(x, y)
    t.down()
    t.down()
    t.down()
    t.right()
    t.write('Type "y" for yes, "n" for no')
    t.pos(x, y)
    t.down()
    t.down()
    t.down()
    t.down()
    t.right()
    i = input()
    t.down()
    t.down()
    t.down()
    if i.lower() == 'y':
        return True
    else:
        return False