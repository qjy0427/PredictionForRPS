from collections import Counter
from random import choice

# Times you play
times = 100

history = []
for i in range(times):
    history.append(input('Please input in this format: XX\n(e.g. PR means you played Paper, the AI played Rock, so on so forth):'))
print('Finished!')
print('Your playing history is:\n',history)
var = 1
while var == 1:
    find = input('Please input again:')
    win = []
    for index, item in enumerate(history):
        if item == find:
            win.append(index)
    print(win)
    # Next step
    plus = [i + 1 for i in win]
    print(plus)
    new = []
    for item in plus:
        if item < times:
            new.append(history[item])
    print(new)
    new2 = []
    for item in new:
        if item == 'RR' or item == 'PR' or item == 'SR':
            new2.append('R')
        elif item == 'RP' or item == 'PP' or item == 'SP':
            new2.append('P')
        elif item == 'RS' or item == 'PS' or item == 'SS':
            new2.append('S')
    print(new2)
    counts = Counter(new2)
    top = counts.most_common(1)
    PRS = ['P','R','S']
    AI = choice(PRS)
    print('test',AI)
    for tuple in top:
        for item in tuple:
            print(item)
            AI = item
            break
    if AI == 'P':
        print('You play scissors.')
    elif AI == 'R':
        print('You play paper.')
    elif AI == 'S':
        print('You play rock.')