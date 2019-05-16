import random

word_dict = dict()
with open('chat.csv', 'r') as reader:
    for line in reader:
        word_dict[line.split(',')[0]]=line.split(',')[1].strip()
    print(word_dict)

CONVERSING = True

print('Hello I am a chatbot. Type "stop" to exit from chat.')

while CONVERSING:
    lang = 'en-US'
    speed = .3

    userInput = input(">>>Me: ")
    if userInput.lower() in word_dict.keys():
        print (word_dict[userInput.lower()])
    elif userInput == 'stop':
        print('Thanks for having a chat!')
        break
        CONVERSING = False
    else:
        print("Sorry I didn't get you!")