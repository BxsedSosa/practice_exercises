#This is a True or False Trivia game. Using ChatGPT to generate questions for me

print('Welcome to the Ture or False Game!')
answer = str(input('Are you ready to play? Y/N: '))
score = 0
questions = 3

if answer.lower() == "y":
    answer = input('True or False: The Great Wall of China is visible from space: ')
    if answer.lower() == 'false':
        score += 1
        print('Correct!')
    else:
        print('Wrong! The Great Wall of China is not visible from space with the naked eye. This is a common myth, but astronauts have reported that it is difficult to see the wall from space without aid')

    answer = input('True or False: The Eiffel Tower is taller than the Empire State Building: ')
    if answer.lower() == 'false':
        score += 1
        print('Correct!')
    else:
        print('Wrong! The Empire State Building is taller than the Eiffel Tower. The Empire State Building, located in New York City, is approximately 1,454 feet (443 meters) tall, including its antenna. In comparison, the Eiffel Tower in Paris stands at a height of about 1,063 feet (324 meters)')
        
    answer = input('True or False: The Atlantic Ocean is the largest ocean in the world: ')
    if answer.lower() == 'false':
        score += 1
        print('Correct!')
    else:
        print('Wrong! The Pacific Ocean is the largest ocean in the world. It is significantly larger than the Atlantic Ocean, covering a vast area of approximately 63,800,000 square miles (165,250,000 square kilometers)')
else:
    quit()

total = int(score / questions * 100)
print('Thank you for playing!')
print('Your Score: ', total,'%')