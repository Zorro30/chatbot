import random
# from speech import *

CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['how are you?','how are you doing?']
responses = ['okay','i am fine']
validations = ['yes','yeah','yea','no','no','nah','nah']
verifications = ['are you sure?','you sure?','you sure?','sure?',"sure?"]

print('Hello I am a chatbot. Type "stop" to exit from chat.')

while CONVERSING:
    lang = 'en-US'
    speed = .3

    userInput = input(">>>Me: ")
    if userInput.lower() in greetings:
        random_greeting = random.choice(greetings)
        print (random_greeting)
    elif userInput.lower() in questions:
        random_response = random.choice(responses)
        print (random_response)
    elif userInput.lower() in verifications:
        random_response = random.choice(validations)
        print (random_response)
    elif 'sure' in userInput:
        response = "Sure about what?"
        print (response)
    elif userInput == 'stop':
        print('Thanks for having a chat!')
        break
        CONVERSING = False
    else:
        print("Sorry I didn't get you!")
		