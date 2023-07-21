#previous_num = 0

#for i in range(1, 11):
    #x_sum = previous_num + i
    #print('Current number', i,'Previous Number ', previous_num, 'Sum: ', x_sum)
    
    #previous_num = i

previous_num = 0

quantity = int(input('How many number do you want add?: '))
quantity = quantity + 1

for i in range(quantity):
    x_sum = previous_num + i
    print(previous_num, '+', i, '=', x_sum)

    previous_num = i