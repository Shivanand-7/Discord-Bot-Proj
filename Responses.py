from random import randint, choice

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Hey there, anyone around?'
    elif 'hello' in lowered:
        return "Hi there! How can I assist you today?"
    elif 'bye' in lowered:
        return 'Goodbye! Catch you later!'
    elif 'how are you' in lowered:
        return "I'm doing great, thanks for asking! How about you?"
    elif 'fine' in lowered:
        return "Glad to hear that! What can I do for you?"
    elif 'roll a dice' in lowered:
        return f'You got: {randint(1,6)}'
    elif 'toss a coin' in lowered:
        return f'It landed on: {choice(["heads", "tails"])}'
    else:
        return choice(["I'm not sure what you mean...", "Can you clarify that?", "Sorry, I didn't get that."])
