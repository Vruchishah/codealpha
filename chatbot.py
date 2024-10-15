# Install Required Libraries :- pip install nltk

from nltk import *
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Vruchi. You can call me Chandramukhi.",]
    ],
    [
        r"how are you?",
        ["I'm doing great, thanks for asking!", "I'm a chatbot, so I'm always good.",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no problem.", "No worries.",]
    ],
    [
        r"quit",
        ["Bye, take care! It was nice talking to you.",]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", "Can you tell me more?",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem, happy to help!"]
    ],
    [
        r"what can you do|what are your capabilities",
        ["I can converse with you"]
    ],
    [
        r"tell me a joke",
        ["Why was the math book sad? Because it had too many problems.", "Why did the computer go to the doctor? It had a virus!"]
    ],
    [
        r"how old are you|when were you created",
        ["I don't have a physical body, so I don't have an age.", "Idk ask my developer, but I'm constantly learning and improving!"]
    ],
    [
        r"do you have feelings|are you emotional",
        ["I don't have emotions like humans do, but I'm designed to be helpful and friendly.", "I'm a machine, so I don't have feelings or emotions."]
    ],
    [
        r"can you understand sarcasm|do you understand humor",
        ["I can try to understand sarcasm and humor, but I'm not perfect.", "I'm getting better at understanding sarcasm and humor, but it's still a work in progress!"]
    ]

]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

def chatbot():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
