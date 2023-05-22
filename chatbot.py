chatbot_dictionary={
    "hi":"Hello!! How can I help you ?",
    "who is your creator ? ":"My creator is Yash Gokakkar"
}

def chatbot(message):
    message = message.lower()
    if message in chatbot_dictionary:
        return chatbot_dictionary[message]
    else:
        return chatbot_dictionary["default"]
    
while True:
    user_input = input("User => ")
    response = chatbot(user_input)
    print("Chatbot => ",response)
    
