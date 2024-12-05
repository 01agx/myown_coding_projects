import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses for the chat bot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me Chat Bot"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ]
]

# Create a chat bot instance
chatbot = Chat(pairs, reflections)

# Start the chat
chatbot.converse()
