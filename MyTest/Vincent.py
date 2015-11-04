import sys

from utilities import prompt_for_input

print("Hello and welcome to the all new... Vincent quiz!!!")
error = 0
while True:
    name = prompt_for_input("Okay. To start off, what is Vincent's sisters first name?")
    if name.lower() == "jasmine":
        break
    else:
        print("Try again")
        error = error + 1

while True:
    family = prompt_for_input("Good work so far! Now... how many people are there in his family?")
    if family == '4':
        break
    else:
        print("You'll get it if you just keep trying.")
        error = error + 1

while True:
    Cont = prompt_for_input("Nice! Now, does Vincent want to be a construction worker?")
    if Cont.lower() == 'no':
        break
    else:
        print("What? Are you dumb?")
        error = error + 1

while True:
    print("You're right!")
    Anime = prompt_for_input("Alright, now what is Vincent's favotrite kind of show?")
    if Anime.lower() == "anime":
        break
    else:
        print("Nope, it's not {0}.".format(Anime))
        error = error + 1

while True:
    sport = prompt_for_input("Okay! You're good to get this far... now, what is Vincent's favorite sport?")
    if "ski" in sport.lower():
        break
    else:
        print("No, it's not {0} (hint down a snowy slope)".format(sport))
        error = error + 1

print("Congratulations! You made it through the Vincent quiz without going past a year!")
while True:
    ques = prompt_for_input("Now, be truthful, but how many errors have you made?")
    try:
        answer = int(ques)
        if abs(answer - error) < 8:
            print('Close enough, the actual number of error is {0}'.format(error))
            break

        print('Not even close, your number of error is really {0}'.format(error))
        break

    except:
        print('More error for you, type in a number buddy.')
        error = error + 1