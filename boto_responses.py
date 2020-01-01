import random

greetings = [
    "Hello",
    "Hi",
    "Hey",
    "Howdy",
    "Peace",
    "Yea What?",
    "Greetings",
    "Oh hey hey !"]



subject = [
    " you ",
    " your Highness ",
    " ma people ",
    " Dawg ",
    " you Dude?! ",
    " you sweety "]

r_subject = random.choice(subject)

question_ask = [
    f"How are {r_subject} ?",
    f"How are {r_subject} doing?",
    f"What's up {r_subject} !?",
    "What's cookin good lookin!?",
    f"Heeey.. How {r_subject} doin?",
    "How's it hanging?",

]

responses = [
    "I'm okay",
    "I'm fine",

]

dont = [
    "huh ?",
    "sorry! My klingon is a bit rusty... you nerd! ",
    "wait! what? ",
    "mhmm ",
    "ha ha haha",
    "what what?",
    "what the...",
    "excuse me",
    
]

curses = [
    "fuck"
]

not_understand = " I did not understand what you said"


def resp(user_message):

    for message in greetings:
        if user_message.lower() == message.lower():
            r_greetings = random.choice(greetings)
            return (r_greetings)
        else:
            return (random.choice(dont) + not_understand)

    # for message in curses:
    #     if user_message.lower() == message.lower():
    #         random_curse_respond = random.choice(curse_response)
    #         return (random_curse_respond)
    #     else:
    #         return (random.choice(dont) + not_understand)

    for message in question:
        if user_message.lower() == message.lower():
            random_response = random.choice(responses)
            return (random_response)
        else:
            return (random.choice(dont) + not_understand)
