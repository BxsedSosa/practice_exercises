#A pay rate calc that takes in account for Overtime pay @ 1.5x
def computepay():
    r = float(input('What is your pay rate?: '))
    h = float(input('How many hours did you work?: '))
    if h <= 40:
        return 'You made:',r*h
    else:
        h = h - 40
        ot = r * 1.5
        return 'You made:', (ot * h)+r*40

computepay()