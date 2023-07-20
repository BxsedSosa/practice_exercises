#A pay rate calc that takes in account for Overtime pay @ 1.5x

r = int(input('What is your pay rate?: '))
h = int(input('How many hours did you work?: '))

if h <= 40:
    print('You made:',r*h)
else:
    h = h - 40
    ot = r * 1.5
    print('You made:', (ot * h)+r*40 )